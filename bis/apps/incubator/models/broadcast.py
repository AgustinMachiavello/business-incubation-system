"""
Broadcast model
"""

# Models
from django.db import models
from .timeStampMixin import TimeStampMixin
from ...accounts.models.users import User
from ..models.files import File
from ..models.activities import Activity

from ..models.entrepreneurs import Entrepreneur # temprary email recipents

# Date and time
from django.utils import timezone

# Emails
from ..views.emails import startSendEmails, generateBroadcastMessage

# Threading
import threading

# Ck Editor
from ckeditor.fields import RichTextField

# Signals
from django.db.models.signals import post_save
from django.dispatch import receiver


class Broadcast(TimeStampMixin, models.Model):
    # choices
    # senders = models.ManyToManyField() should be default Gapian email address
    addressee = models.TextField(null=True, blank=True, help_text='Ej: correo@gmail.com, ejemplo@gmail.com ...')
    subject = models.CharField(null=True, blank=True, max_length=50)
    message = RichTextField(null=False, blank=False)
    files = models.ManyToManyField(File, null=True, blank=True, related_name='broadcast_files')
    activity = models.ForeignKey(Activity, null=True, blank=True, related_name='broadcast_activity', on_delete=models.SET_NULL)
    send_to_entrepreneurs = models.BooleanField(null=False, blank=False, default=False)
    send_to_massive = models.BooleanField(null=False, blank=False, default=False)
    send_to_activity_inscriptions = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return '#{0} · {1}'.format(self.id, self.subject or 'sin asunto')

    class Meta:
        verbose_name = 'Broadcast'
        ordering = ['-created_at', '-id']


@receiver(post_save, sender=Broadcast)
def handle_send_emails(sender, **kwargs):
    broadcast = kwargs['instance']
    email_list = set() # Set prevents duplicated
    if broadcast.message:
        if broadcast.addressee:
            addressee_list = broadcast.addressee.split(',')[:-1]
            for email in addressee_list:
                email_list.add(email)
        if broadcast.send_to_entrepreneurs:
            entrepreneurs_list = Entrepreneur.objects.filter(is_active=True).values_list('email', flat=True)
            for email in entrepreneurs_list:
                email_list.add(email)
        if broadcast.send_to_massive:
            users_list = User.objects.filter(is_active=True).values_list('email', flat=True)
            for email in users_list:
                email_list.add(email)
        if broadcast.send_to_activity_inscriptions and broadcast.activity:
            inscriptions_list = broadcast.activity.inscriptions.all().values_list('email', flat=True)
            for email in inscriptions_list:
                email_list.add(email)
        if len(email_list) > 0:
            message = generateBroadcastMessage(broadcast)
            startSendEmails(addressee_list=email_list, message=message, subject=broadcast.subject)
    return