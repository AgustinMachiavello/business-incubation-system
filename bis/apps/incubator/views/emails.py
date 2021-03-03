"""
Email module
"""

# Threading
import threading

from django.core.mail import message

# Email
from ....settings.base import EMAIL_HOST_USER
from django.core.mail.message import (
    EmailMultiAlternatives,
)
from django.utils.module_loading import import_string

# Templates
from django.core.mail import send_mail, send_mass_mail
from django.template.loader import get_template


# Settings
from ....settings import base as settings

# Site
from django.contrib.sites.models import Site

SINGLE_EMAIL_LIMIT = 2

# Message generation
def generateInscriptionAlertMessage(name, activity, inscription):
    context = {
        'name': name,
        'activity_title': activity.title,
        'activity': activity,
        'inscription': inscription,
        'domain': Site.objects.get_current().domain,
    }
    template = get_template('emails/inscriptionAlert.html')
    content = template.render(context)
    return content

def generateBroadcastMessage(broadcast):
    context = {
        'broadcast': broadcast,
        'domain': Site.objects.get_current().domain,
    }
    template = get_template('emails/broadcast.html')
    content = template.render(context)
    return content

def generateStatusReportMessage(messages_dict):
    context = {
        'messages': messages_dict,
    }
    template = get_template('emails/statusreport.html')
    content = template.render(context)
    return content


# Backend
def generateDatatuple(recipent_list, subject, message):
    # for sending massive emails
    # format: subject, message, sender, reciever list
    datatuple = (subject, message, settings.EMAIL_HOST_USER, recipent_list)
    return datatuple

def get_connection(backend=None, fail_silently=False, **kwds):
    """Load an email backend and return an instance of it.
    If backend is None (default) settings.EMAIL_BACKEND is used.
    Both fail_silently and other keyword arguments are used in the
    constructor of the backend.
    """
    klass = import_string(backend or settings.EMAIL_BACKEND)
    return klass(fail_silently=fail_silently, **kwds)

def sendMassiveHtmlEmails(datatuple, fail_silently=False, auth_user=None,
                        auth_password=None, connection=None):
    """
    Given a datatuple of (subject, message, html_message, from_email,
    recipient_list), send each message to each recipient list.
    Return the number of emails sent.
    If from_email is None, use the DEFAULT_FROM_EMAIL setting.
    If auth_user and auth_password are set, use them to log in.
    If auth_user is None, use the EMAIL_HOST_USER setting.
    If auth_password is None, use the EMAIL_HOST_PASSWORD setting.
    """
    connection = connection or get_connection(
        username=auth_user,
        password=auth_password,
        fail_silently=fail_silently,
    )
    plain_text_message = ''
    messages = []
    step = 100
    email_list_length = len(datatuple[3])
    for j in range(0, email_list_length, step):
        if j + step > email_list_length:
            bcc_recipents = datatuple[3][j:]
        else:
            bcc_recipents = datatuple[3][j:j + step]
        message = EmailMultiAlternatives(datatuple[0], plain_text_message, datatuple[2],
                                alternatives=[(datatuple[1], 'text/html')],
                                connection=connection,
                                bcc=bcc_recipents)
        messages.append(message)
    connection.send_messages(messages)
    return

def sendMassiveEmails(addressee_list, subject, message): # Do not use this function directly
    data = (subject, message, EMAIL_HOST_USER, addressee_list)
    """send_mass_mail(
        (data,),
        fail_silently=False,
    )"""
    for email in addressee_list:
        send_mail(
            data[0],
            data[1],
            data[2],
            [email],
            fail_silently=False,
            html_message=message
        )
    return True

def startSendEmails(addressee_list, message, subject='Información Gepian'):
    print('---- Threads before sending:', threading.active_count())
    if len(addressee_list) > SINGLE_EMAIL_LIMIT:
        datatuple = generateDatatuple(addressee_list, subject, message)
        email_thread = threading.Thread(target=sendMassiveHtmlEmails, args=(datatuple,))
    else:
        email_thread = threading.Thread(target=sendMassiveEmails, args=(addressee_list, subject, message))
    email_thread.start()
    #email_thread.join()
    # sendMassiveEmails(addressee_list, message)
    print('---- Sending {0} emails...'.format(len(addressee_list)))
    return True