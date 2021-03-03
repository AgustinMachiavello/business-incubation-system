"""
Model quick view serialziers
"""


# Serializers
from rest_framework import serializers

# Models
from ..models import *
from ...accounts.models import User
   

class EntrepreneurModelSerializer(serializers.ModelSerializer):
    city = serializers.ReadOnlyField(source='entrepreneur.city.name')
    date_of_birth = serializers.DateField(format='%d/%m/%Y')
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M')

    class Meta:
        model = Entrepreneur
        fields = ('identification_number', 'first_name', 'last_name', 'email', 'date_of_birth', 
                  'sex', 'phone_number', 'city', 'created_at')

class ProjectModelSerializer(serializers.ModelSerializer):
    business_area = serializers.ReadOnlyField()
    postulation = serializers.ReadOnlyField()
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M')

    class Meta:
        model = Project
        fields = ('name', 'social_reason', 'rut', 'description', 'business_area', 'status', 'general_stage', 'postulation', 'get_time_spent', 'registered_by', 'created_at')

class ActivitiesModelSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format='%d/%m/%Y')
    inscription_deadline = serializers.DateField(format='%d/%m/%Y')
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M')
    class Meta:
        model = Activity
        fields = ('title', 'description', 'date', 'start_time', 'end_time', 'activity_type',
                  'inscription_deadline', 'attendance_limit', 'inscription_link', 'created_at')
        
class BusinessAreaModelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M')
    class Meta:
        model = BusinessArea
        fields = ('name', 'created_at')

class BroadcastAreaModelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M')
    class Meta:
        model = Broadcast
        fields = ('send_to_massive', 'send_to_entrepreneurs', 'activity', 'send_to_activity_inscriptions', 'subject', 'message', 'created_at')

class FilesModelSerializer(serializers.ModelSerializer):
    project = serializers.ReadOnlyField()
    interview = serializers.ReadOnlyField()
    stage = serializers.ReadOnlyField()
    entrepreneur = serializers.ReadOnlyField()
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M')
    class Meta:
        model = File
        fields = ('name', 'file_link', 'project', 'interview', 'stage', 'entrepreneur', 'created_at')

class InterviewModelSerializer(serializers.ModelSerializer):
    stage = serializers.ReadOnlyField()
    date = serializers.DateField(format='%d/%m/%Y')
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M')

    class Meta:
        model = Interview
        fields = ('date', 'interview_type', 'start_time', 'end_time', 'modality', 'stage', 'comments', 'get_time_spent', 'created_at')

class PostulationModelSerializer(serializers.ModelSerializer):
    postulant = serializers.ReadOnlyField()
    business_area = serializers.ReadOnlyField()
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M')
    class Meta:
        model = Postulation
        fields = ('name', 'postulant', 'business_area', 'description', 'status', 'created_at')

class StageModelSerializer(serializers.ModelSerializer):
    project = serializers.ReadOnlyField()
    start_date = serializers.DateField(format='%d/%m/%Y')
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M')
    class Meta:
        model = Stage
        fields = ('stage_type', 'project', 'description', 'start_date', 'get_time_spent', 'created_at')

class TechnicianModelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M')
    class Meta:
        model = Technician
        fields = ('identification_number', 'first_name', 'last_name', 'email', 'phone_number',
                  'technician_speciality', 'technician_type', 'company', 'created_at')

class CityModelSerializer(serializers.ModelSerializer):
    province = serializers.ReadOnlyField()
    class Meta:
        model = City
        fields = ('name', 'province',)

class ProvinceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ('name',)

class FinancingModelSerializer(serializers.ModelSerializer):
    project = serializers.ReadOnlyField()
    started_on_date = serializers.DateField(format='%d/%m/%Y')
    finished_on_date = serializers.DateField(format='%d/%m/%Y')
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M')
    class Meta:
        model = Financing
        fields = ('project', 'code', 'code_type', 'started_on_date', 'finished_on_date', 'created_at',)

class InscriptionModelSerializer(serializers.ModelSerializer):
    activity_inscriptions = serializers.ReadOnlyField()
    class Meta:
        model = Inscription
        fields = ('email', 'first_name', 'last_name', 'assisted', 'activity_inscriptions')

class TechnicianSpecialityModelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M')
    class Meta:
        model = TechnicianSpeciality
        fields = ('name', 'created_at')


class UserModelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M')
    class Meta:
        model = User
        fields =  ('identification_number', 'first_name', 'last_name', 'username', 'phone_number', 'email', 'created_at')