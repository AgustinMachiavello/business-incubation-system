""" Dictionaries used across all the site """

# Models
from ..models import *
from ...accounts.models import *

# Forms
from ..forms import modelForms
from ..forms import modelFieldsForms
from ..forms import modelSearchForms

# Serializers
from ..serializers import modelViewSerializers

# Django
from django.urls import reverse


FORM_FIELDS_DICT = {
    'activities': modelFieldsForms.ActivitiesFieldsForm,
    'businessareas': modelFieldsForms.BusinessAreaFieldsForm,
    'broadcasts': modelFieldsForms.BroadcastAreaFieldsForm,
    'entrepreneurs': modelFieldsForms.EntrepreneurFieldsForm,
    'files': modelFieldsForms.FilesFieldsForm,
    'interviews': modelFieldsForms.InterviewFieldsForm,
    'postulations': modelFieldsForms.PostulationFieldsForm,
    'projects': modelFieldsForms.ProjectFieldsForm,
    'stages': modelFieldsForms.StageFieldsForm,
    'technicians': modelFieldsForms.TechnicianFieldsForm,
    'cities': modelFieldsForms.CityFieldsForm,
    'provinces': modelFieldsForms.ProvinceFieldsForm,
    'financings': modelFieldsForms.FinancingsFieldsForm,
    'inscriptions': modelFieldsForms.InscriptionFieldsForm,
    'technicianspecialities': modelFieldsForms.TechnicianSpecialityFieldsForm,
    'users': modelFieldsForms.UserFieldsForm,
}

FORM_DICT = {
    'activities': modelForms.ActivitiesForm,
    'businessareas': modelForms.BusinessAreaForm,
    'broadcasts': modelForms.BroadcastAreaForm,
    'entrepreneurs': modelForms.EntrepreneurForm,
    'files': modelForms.FilesForm,
    'interviews': modelForms.InterviewForm,
    'postulations': modelForms.PostulationForm,
    'projects': modelForms.ProjectForm,
    'stages': modelForms.StageForm,
    'technicians': modelForms.TechnicianForm,
    'cities': modelForms.CityForm,
    'provinces': modelForms.ProvinceForm,
    'financings': modelForms.FinancingForm,
    'inscriptions': modelForms.InscriptionForm,
    'technicianspecialities': modelForms.TechnicianSpecialityForm,
    'users': modelForms.UserForm,
    'sitesettings': modelForms.SiteSettingsForm,
}

GENERAL_SEARCH_FORM_DICT = {
    'entrepreneurs': modelSearchForms.EntrepreneurGeneralSearchForm,
    'projects': modelSearchForms.ProjectGeneralSearchForm,
    'inscriptions': modelSearchForms.InscriptionGeneralSearchForm,
    'stages': modelSearchForms.StageGeneralSearchForm,
    'postulations': modelSearchForms.PostulationGeneralSearchForm,
    'activities': modelSearchForms.ActivityGeneralSearchForm,
    'financings': modelSearchForms.FinancingGeneralSearchForm,
    'broadcasts': modelSearchForms.BroadcastGeneralSearchForm,
    'provinces': modelSearchForms.ProvinceGeneralSearchForm,
    'cities': modelSearchForms.CityGeneralSearchForm,
    'technicians': modelSearchForms.TechnicianGeneralSearchForm,
    'technicianspecialities': modelSearchForms.TechnicianSpecialityGeneralSearchForm,
    'businessareas': modelSearchForms.BusinessAreaGeneralSearchForm,
    'files': modelSearchForms.FileGeneralSearchForm,
    'interviews': modelSearchForms.InterviewGeneralSearchForm,
}

MODEL_DICT = {
    'activities': Activity,
    'businessareas': BusinessArea,
    'broadcasts': Broadcast,
    'entrepreneurs': Entrepreneur,
    'files': File,
    'interviews': Interview,
    'postulations': Postulation,
    'projects': Project,
    'stages': Stage,
    'technicians': Technician,
    'cities': City,
    'provinces': Province,
    'financings': Financing,
    'inscriptions': Inscription,
    'technicianspecialities': TechnicianSpeciality,
    'users': User,
    'sitesettings': SiteSettings,
}

MODEL_NAME_DICT = {
    'activities': 'actividad',
    'businessareas': 'rubro',
    'broadcasts': 'difusión',
    'entrepreneurs': 'emprendedor',
    'files': 'archivo',
    'interviews': 'entrevista',
    'postulations': 'postulación',
    'projects': 'proyecto',
    'stages': 'etapa',
    'technicians': 'técnico',
    'cities': 'ciudad',
    'provinces': 'departamento',
    'financings': 'finanza',
    'inscriptions': 'inscripción',
    'technicianspecialities': 'especialidad de técnico',
    'users': 'usuario',
    'sitesettings': 'configuración del sitio',
}

MODEL_NAME_PLURAL_DICT = {
    'activities': 'actividades',
    'businessareas': 'rubros',
    'broadcasts': 'difusiones',
    'entrepreneurs': 'emprendedores',
    'files': 'archivos',
    'interviews': 'entrevistas',
    'postulations': 'postulaciones',
    'projects': 'proyectos',
    'stages': 'etapas',
    'technicians': 'técnicos',
    'cities': 'ciudades',
    'provinces': 'departamentos',
    'financings': 'finanzas',
    'inscriptions': 'inscripciones',
    'technicianspecialities': 'especialidades de técnicos',
    'users': 'usuarios',
    'sitesettings': 'configuración del sitio',
}

MODEL_FILTER_DICT = {
    'projects': {
        'status|estado': {
            'en progeso': 'P',
            'graduado': 'G',
            'egresado': 'E',
        },
        'order_by|ordenar': {
            'recientes': '-created_at', 
            'antiguos': 'created_at',
        }
    },
    'entrepreneurs': {
        'sex|sexo': {
            'femenino': 'F',
            'masculino': 'M',
            'no aplica': 'N/A',
        },
        'order_by|ordenar': {
            'recientes': '-created_at', 
            'antiguos': 'created_at',
        }
    },
    'postulations': {
        'status|estado': {
            'sin atender': '-',
            'pre-seleccionado': 'P',
            'derivado': 'D',
        },
        'order_by|ordenar': {
            'recientes': '-created_at', 
            'antiguos': 'created_at',
        }
    },
    'activities': {
        'activity_type|tipo': {
            'Sensibilización': 'SE',
            'Pre-Incubación': 'PE',
            'Incubación': 'IN',
            'Post-Incubación': 'PO',
        },
        'order_by|ordenar': {
            'recientes': '-created_at', 
            'antiguos': 'created_at',
        }
    },
    'financings': {
        'code_type|tipo': {
            'ANDE': 'AE',
            'ANII': 'A1',
            'ANII Segundo Financiamiento': 'A2',
            'Otros': '-',
        },
        'order_by|ordenar': {
            'recientes': '-created_at', 
            'antiguos': 'created_at',
        }
    },
    'inscriptions': {
        'assisted|asistencia': {
            'Si': True,
            'No': False,
        },
        'order_by|ordenar': {
            'recientes': '-created_at', 
            'antiguos': 'created_at',
        }
    },
    'stages': {
        'stage_type|etapa': {
            'En Postulación': 'EP',
            'Evaluación Incubadora/Capital Semilla': 'EV',
            'Pre-Incubación': 'PI',
            'Incubación': 'IN',
            'Post-Incubación': 'PO',
        },
        'order_by|ordenar': {
            'recientes': '-created_at', 
            'antiguos': 'created_at',
        }
    },
    'technicians': {
        'technician_type|tipo': {
            'Coordinador': 'CO',
            'Consultor': 'C',
            'Mentor': 'M',
            'Otro': '-',
        },
        'order_by|ordenar': {
            'recientes': '-created_at', 
            'antiguos': 'created_at',
        }
    }, 
}

MODEL_ANALYTICS_DICT = {
    # TODO: Documentation of all this dictionaries and make this editable in the admin page
    'entrepreneurs': [
        {
            'analytic_handle': 'entrepreneurs_incubated',
            'show_graph': True,
            'graph_type': 'bar',
            'graph_size': None,
            'title': 'emprendedores incubados',
            'link_url': 'entrepreneurs_incubated', # Add the analytic handle to make this link generate a report
            'link_label': 'exportar',
            'logo': None,
        },
        {
            'analytic_handle': 'entrepreneurs_sex',
            'show_graph': True,
            'graph_type': None,
            'graph_size': None,
            'title': 'sexo de emprendedores',
            'link_url': None,
            'link_label': 'exportar',
            'logo': None,
        },
        {
            'analytic_handle': 'entrepreneurs_ages',
            'show_graph': True,
            'graph_type': None,
            'graph_size': None,
            'title': 'edad de emprendedores',
            'link_url': None,
            'link_label': 'exportar',
            'logo': None,
        },
        {
            'analytic_handle': 'entrepreneurs__count',
            'show_graph': True,
            'graph_type': 'line',
            'graph_size': None,
            'title': 'total de emprendedores',
            'link_url': None,
            'link_label': 'exportar',
            'logo': None,
        },
    ],
    'projects': [
        {
            'analytic_handle': 'projects_incubated',
            'show_graph': True,
            'graph_type': 'bar',
            'graph_size': None,
            'title': 'proyectos incubados',
            'link_url': 'projects_incubated',
            'link_label': 'exportar',
            'logo': None,
        },
        {
            'analytic_handle': 'projects_preincubated',
            'show_graph': True,
            'graph_type': 'bar',
            'graph_size': None,
            'title': 'proyectos pre-incubados',
            'link_url': 'projects_preincubated',
            'link_label': 'exportar',
            'logo': None,
        },
        {
            'analytic_handle': 'projects__status__G',
            'show_graph': True,
            'graph_type': 'bar',
            'graph_size': None,
            'title': 'proyectos graduados',
            'link_url': 'projects__status__G',
            'link_label': 'exportar',
            'logo': None,
        },
        {
            'analytic_handle': 'projects_second_seed',
            'show_graph': True,
            'graph_type': 'bar',
            'graph_size': None,
            'title': 'proyectos 2da etapa capital semilla',
            'link_url': 'projects_second_seed',
            'link_label': 'exportar',
            'logo': None,
        },
        {
            'analytic_handle': 'projects__count',
            'show_graph': True,
            'graph_type': 'line',
            'graph_size': 'large',
            'title': 'total de proyectos',
            'link_url': 'projects__count',
            'link_label': 'exportar',
            'logo': None,
        },
    ],
    'activities': [
        {
            'analytic_handle': 'activities__count',
            'show_graph': True,
            'graph_type': 'bar',
            'graph_size': None,
            'title': 'total de actividades',
            'link_url': 'activities__count',
            'link_label': 'exportar',
            'logo': None,
        },
        {
            'analytic_handle': 'inscriptions__assisted__1',
            'show_graph': True,
            'graph_type': 'bar',
            'graph_size': None,
            'title': 'personas sensibilizadas',
            'link_url': 'inscriptions__assisted__1',
            'link_label': 'exportar',
            'logo': None,
        },
    ],
    'postulations': [
        {
            'analytic_handle': 'postulations__count',
            'show_graph': True,
            'graph_type': 'line',
            'graph_size': None,
            'title': 'total de postulaciones recibidas',
            'link_url': 'postulations__count',
            'link_label': 'exportar',
            'logo': None,
        },
        {
            'analytic_handle': 'postulations__status__P',
            'show_graph': True,
            'graph_type': 'line',
            'graph_size': None,
            'title': 'postulaciones pre-seleccionadas',
            'link_url': 'postulations__status__P',
            'link_label': 'exportar',
            'logo': None,
        },
    ],
    'inscriptions': [
        {
            'analytic_handle': 'inscriptions__count',
            'show_graph': True,
            'graph_type': 'line',
            'graph_size': None,
            'title': 'total de inscripciones recibidas',
            'link_url': 'inscriptions__count',
            'link_label': 'exportar',
            'logo': None,
        },
        {
            'analytic_handle': 'inscriptions_sex',
            'show_graph': True,
            'graph_type': 'bar',
            'graph_size': None,
            'title': 'inscripciones por sexo',
            'link_url': None,
            'link_label': 'exportar',
            'logo': None,
        },
        {
            'analytic_handle': 'inscriptions_provinces',
            'show_graph': True,
            'graph_type': 'bar',
            'graph_size': 'large',
            'title': 'inscripciones por departemento',
            'link_url': None,
            'link_label': 'exportar',
            'logo': None,
        },
    ],
}

REPORTS_INDEX_ANALYTICS_DICT = {
    'projects_incubated': {
        'analytic_handle': 'projects_incubated',
        'show_graph': True,
        'graph_type': 'bar',
        'graph_size': None,
        'title': 'proyectos incubados',
        'link_url': 'projects',
        'link_label': '↗ reportes de proyectos',
        'logo': None,
    },
    'entrepreneurs_incubated': {
        'analytic_handle': 'entrepreneurs_incubated',
        'show_graph': True,
        'graph_type': 'bar',
        'graph_size': None,
        'title': 'emprendedores incubados',
        'link_url': 'entrepreneurs',
        'link_label': '↗ reportes de emprendedores',
        'logo': None,
    },
    'activities__count': {
        'analytic_handle': 'activities__count',
        'show_graph': True,
        'graph_type': 'bar',
        'graph_size': None,
        'title': 'actividades',
        'link_url': 'activities',
        'link_label': '↗ reportes de actividades',
        'logo': None,
    },
    'postulations__count': {
        'analytic_handle': 'postulations__count',
        'show_graph': True,
        'graph_type': 'bar',
        'graph_size': None,
        'title': 'postulaciones',
        'link_url': 'postulations',
        'link_label': '↗ reportes de postulaciones',
        'logo': None,
    },
}

HOME_INDEX_ANALYTICS_DICT = {
    'entrepreneurs__count': {
        'analytic_handle': 'entrepreneurs__count',
        'show_graph': True,
        'graph_type': 'line',
        'graph_size': None,
        'title': 'nuevos emprendedores',
        'link_url': 'entrepreneurs',
        'link_label': '↗ emprendedores',
        'logo': 'bi-person',
    },
    'projects__count': {
        'analytic_handle': 'projects__count',
        'show_graph': True,
        'graph_type': 'line',
        'graph_size': None,
        'title': 'nuevos proyectos',
        'link_url': 'projects',
        'link_label': '↗ proyectos',
        'logo': 'bi-bar-chart-steps',
    },
    'postulations__count': {
        'analytic_handle': 'postulations__count',
        'show_graph': True,
        'graph_type': 'bar',
        'graph_size': None,
        'title': 'nuevas postulaciones',
        'link_url': 'postulations',
        'link_label': '↗ postulaciones',
        'logo': 'bi-clipboard',
    },
    'activities__count': {
        'analytic_handle': 'activities__count',
        'show_graph': True,
        'graph_type': 'bar',
        'graph_size': None,
        'title': 'nuevas actividades',
        'link_url': 'activities',
        'link_label': '↗ actividades',
        'logo': 'bi-calendar-week',
    },
}

MODEL_REPORT_FIELDS = {
    'entrepreneurs': {
        'id': 'ID',
        'identification_number': 'C.I',
        'first_name': 'nombre',
        'last_name': 'apellido',
        'phone_number': 'número de teléfono',
        'username': 'usuario',
        'email': 'correo',
        'sex': 'sexo',
        #'date_of_birth',
        'city': 'ciudad (ID)',
        #'business_area': 'rubro',
        #'created_at',
    },
    'projects': {
        'id': 'ID',
        'name': 'nombre',
        'description': 'descripción',
        'social_reason': 'razón social',
        'status': 'estado',
        'general_stage': 'etapa general',
        'time_spent': 'tiempo empleado (horas)',
        'business_area': 'rubro (ID)',
        'postulation': 'postulación (ID)',
        'registered_by': 'registrado por (ID)',
        'entrepreneurs': 'emprendedores (ID)',
    },
    'activities': {
        'id': 'ID',
        'title': 'nombre',
        #'date': 'fecha',
        'activity_type': 'tipo',
        'description': 'descripción',
        'inscription_deadline': 'fecha límite de inscripción',
        'inscription_time_message': 'mensaje de inscripción',
        'attendance_limit': 'máximo número de participantes',
        'start_time': 'hora de inicio',
        'end_time': 'hora de finalización',
        'inscription_link': 'código de inscripción',
        'created_by': 'creado por (ID)',
        'inscriptions': 'inscripciones (ID)',
        #'created_at',
    },
    'postulations': {
        'id': 'ID',
        'name': 'nombre',
        'description': 'descripción',
        'postulant': 'postulante (ID)',
        'business_area': 'rubro (ID)',
        #'created_at',
    },
    'inscriptions': {
        'id': 'ID',
        'email': 'correo',
        'first_name': 'nombre',
        'last_name': 'apellido',
        'sex': 'sexo',
        'province': 'departamento (ID)',
        'city': 'ciudad (ID)',
        'assisted': 'asistencia',
    }
}

DISPLAY_NAMES = {
    'entrepreneurs': {
        'M': 'Masculino',
        'F': 'Femenino',
        'N/A': 'No aplica',
    },
    'projects': {
        '-': 'En progreso',
        'P': 'En progreso',
        'G': 'Graduado',
        'E': 'Egresado',
        'DE': 'Desarrollo del Producto o Servicio / Puesta en Marcha',
        'CO': 'Comercialización Temprana',
        'CN': 'Consolidación Comercial e Internacionalización',
    },
    'stages': {
        'EP': 'En Postulación',
        'EV': 'Evaluación Incubadora/Capital Semilla',
        'PI': 'Pre-Incubación',
        'IN': 'Incubación',
        'PO': 'Post-Incubación',
        None: 'Sin inicio'
    },
    'technicians': {
        'CO': 'Coordinador',
        'C': 'Consultor',
        'M': 'Mentor',
    },
    'postulations': {
        '-': 'Sin atender',
        'P': 'Pre-Seleccionado',
        'D': 'Derivado'
    },
    'interviews': {
        'EP': 'Entrevista de Postulación',
        'SG': 'Seguimiento',
        'CA': 'Capacitación',
        'SN': 'Taller de Sensibilización',
        'CO': 'Consultoría',
        'ME': 'Mentoría',
        'P': 'Presencial',
        'O': 'Online',
    },
    'activities': {
        'SE': 'Sensibilización',
        'PI': 'Pre-Incubación',
        'IN': 'Incubación',
        'PO': 'Post-Incubación',
    },
    'financings': {
        'AE': 'ANDE',
        'A1': 'ANII',
        'A2': 'ANII Segundo Financiamiento',
        '-': 'Otros',
    },
    'broadcasts': {
        None: 'Sin asunto',
        True: 'Si',
        False: 'No',
    },
    'cities': {
        'province_id': 'Sin asignar',
    },
    'inscriptions': {
        False: 'No',
        True: 'Si',
    },
}


MODEL_QUICK_VIEW_SERIALIZERS_DICT = {
    'activities': modelViewSerializers.ActivitiesModelSerializer,
    'businessareas': modelViewSerializers.BusinessAreaModelSerializer,
    'broadcasts': modelViewSerializers.BroadcastAreaModelSerializer,
    'entrepreneurs': modelViewSerializers.EntrepreneurModelSerializer,
    'files': modelViewSerializers.FilesModelSerializer,
    'interviews': modelViewSerializers.InterviewModelSerializer,
    'postulations': modelViewSerializers.PostulationModelSerializer,
    'projects': modelViewSerializers.ProjectModelSerializer,
    'stages': modelViewSerializers.StageModelSerializer,
    'technicians': modelViewSerializers.TechnicianModelSerializer,
    'cities': modelViewSerializers.CityModelSerializer,
    'provinces': modelViewSerializers.ProvinceModelSerializer,
    'financings': modelViewSerializers.FinancingModelSerializer,
    'inscriptions': modelViewSerializers.InscriptionModelSerializer,
    'technicianspecialities': modelViewSerializers.TechnicianSpecialityModelSerializer,
    'users': modelViewSerializers.UserModelSerializer,
}

MODEL_FIELDS_LABELS_DICT = {
    'activities': {
            'title': 'nombre',
            'date': 'fecha',
            'start_time': 'hora de comienzo',
            'end_time': 'hora de finalización',
            'description': 'descripción',
            'activity_type': 'tipo de actividad',
            'inscription_deadline': 'cierre de inscripciones', 
            'attendance_limit': 'cupos',
            'inscription_link': 'código de inscripción (autogenerado)',
            'created_at': 'creado',
        },
    'businessareas': {
            'name': 'nombre',
            'created_at': 'creado',   
        },
    'broadcasts': {
            'addressee': 'recipientes',
            'subject': 'asunto',
            'message': 'mensaje',
            'files': 'archivos',
            'activity': 'actividad',
            'send_to_activity_inscriptions': 'inscritos',
            'send_to_entrepreneurs': 'emprendedores',
            'send_to_massive': 'masivo',
            'created_at': 'creado',
        },
    'entrepreneurs': {
            'identification_number': 'cédula de identidad',
            'email': 'correo electrónico',
            'first_name': 'nombre',
            'last_name': 'apellido',
            'date_of_birth': 'fecha de nacimiento',
            'sex': 'sexo',
            'phone_number': 'número de teléfono',
            'city': 'ciudad',
            'created_at': 'creado',
        },
    'files': {},
    'interviews': {
            'date': 'fecha',
            'interview_type': 'tipo de entrevista',
            'start_time': 'hora de inicio',
            'end_time': 'hora de fin',
            'modality': 'modalidad',
            'stage': 'etapa',
            'comments': 'comentarios',
            'technicians': 'técnicos',
            'get_time_spent': 'Tiempo empleado (Horas)',
            'created_at': 'creado',
        },
    'postulations': {
            'name': 'nombre',
            'postulant': 'postulante',
            'business_area': 'rubro',
            'description': 'descripción',
            'status': 'estado',
            'created_at': 'creado',
        },
    'projects': {            
            'name': 'nombre',
            'social_reason': 'razón social',
            'rut': 'RUT',
            'description': 'descripción',
            'business_area': 'sector de negocios',
            'status': 'estado',
            'general_stage': 'etapa general',
            'entrepreneurs': 'emprendedores',
            'postulation': 'postulación',
            'get_time_spent': 'Tiempo empleado (Horas)',
            'registered_by': 'Registrado por usuario (ID)',
            'created_at': 'creado',
        },
    'stages': {
            'stage_type': 'tipo',
            'project': 'proyecto',
            'description': 'descripción',
            'start_date': 'fecha de inicio',
            'end_date': 'fecha de finalización',
            'created_at': 'creado',
            'get_time_spent': 'Tiempo empleado (Horas)',
        },
    'technicians': {
            'identification_number': 'cédula de identidad',
            'email': 'correo',
            'first_name': 'nombre',
            'last_name': 'apellido',
            'phone_number': 'número de teléfono',
            'technician_speciality': 'especialidad',
            'technician_type': 'tipo',
            'company': 'empresa',
            'created_at': 'creado',       
        },
    'cities': {
            'name': 'nombre',
            'province': 'departamento',
            'created_at': 'creado',
        },
    'provinces': {
            'name': 'Nombre', 
            'created_at': 'creado',   
        },
    'financings': {
            'project': 'proyecto',
            'code': 'código de financiamiento',
            'code_type': 'tipo de financiamiento',
            'started_on_date': 'comenzado',
            'finished_on_date': 'finalizado',
            'created_at': 'creado',
        },
    'inscriptions': {
            'email': 'correo electrónico',
            'first_name': 'nombre',
            'last_name': 'apellido',
            'assisted': 'asistencia',
            'created_at': 'creado',
        },
    'files': {
            'name': 'nombre',
            'file_link': 'link',
            'project': 'proyecto',
            'interview': 'entrevista',
            'stage': 'etapa',
            'entrepreneur': 'emprendedor',
            'created_at': 'creado',
        },
    'technicianspecialities': {
        'name': 'nombre',
        'created_at': 'creado',
    },
    'users': {
        'identification_number': 'cédula de identidad',
        'first_name': 'nombre',
        'last_name': 'apellido',
        'username': 'nombre de usuario',
        'phone_number': 'teléfono',
        'email': 'correo',
        'password': 'contraseña',
        'last_login': 'último login',
        'created_at': 'creado',
    }
}

ADMINISTRATION_INDEX_MENUS = {
    'provinces': {
        'label': 'Departamentos',
        'logo': 'bi-geo-alt',
    },
    'cities': {
        'label': 'Ciudades',
        'logo': 'bi-geo',
    }, 
    'technicians': {
        'label': 'Técnicos',
        'logo': 'bi-person-check',
    },
    'technicianspecialities': {
        'label': 'Especialidades de técnicos',
        'logo': 'bi-award',
    }, 
    'businessareas': {
        'label': 'Rubros',
        'logo': 'bi-grid-1x2',
    },
    'files': {
        'label': 'Archivos',
        'logo': 'bi-folder2-open',
    },
    'users': {
        'label': 'Usuarios',
        'logo': 'bi-people',
    },
    'sitesettings': {
        'label': 'Sitio',
        'logo': 'bi-globe2',
    },
}

REPORTS_INDEX_MENUS = {
    'entrepreneurs': {
        'label': 'Emprendedores',
        'logo': 'bi-person',
    },
    'projects': {
        'label': 'Proyectos',
        'logo': 'bi-journal',
    },
    'activities': {
        'label': 'Actividades',
        'logo': 'bi-calendar-date',
    },
    'postulations': {
        'label': 'Postulaciones',
        'logo': 'bi-clipboard',
    },
    'inscriptions': {
        'label': 'Inscripciones',
        'logo': 'bi-card-checklist',
    },
}

AVAILABLE_FILTERS_LIST = [
    'status', 
    'sex', 
    'activity_type', 
    'code_type', 
    'assisted', 
    'stage_type', 
    'technician_type', 
    'activity_inscriptions',
]


def getModel(modelHandle):
    return MODEL_DICT.get(modelHandle, None)

def getModelName(modelHandle):
    return MODEL_NAME_DICT.get(modelHandle, None)

def getModelPluralName(modelHandle):
    return MODEL_NAME_PLURAL_DICT.get(modelHandle, None)

def getModelForm(modelHandle):
    return FORM_DICT.get(modelHandle, None)

def getModelFieldsForm(modelHandle):
    return FORM_FIELDS_DICT.get(modelHandle, None)

def getModelFilters(modelHandle):
    return MODEL_FILTER_DICT.get(modelHandle, None)

def getAvailableFilters():
    # This function does not contemplate sorting
    return AVAILABLE_FILTERS_LIST # do not inlude order_by as it has a separarate logic

def getModelAnalytics(modelHandle):
    return MODEL_ANALYTICS_DICT.get(modelHandle, None)

def getModelReportFields(modelHandle):
    return MODEL_REPORT_FIELDS.get(modelHandle, None)

def getDisplayName(field_name, model_handle):
    display_name = DISPLAY_NAMES.get(model_handle, None)
    if not display_name:
        return field_name
    display_name = display_name.get(field_name, None)
    if not display_name:
        return field_name
    return display_name

def getObject(model_handle, pk):
    try:
        return getModel(model_handle).objects.get(id=pk)
    except Exception as e:
        print('Exception:', e, model_handle, pk)
        return None

def getModelQuickViewSerializer(modelHandle):
    return MODEL_QUICK_VIEW_SERIALIZERS_DICT.get(modelHandle, None)

def getModelQuickViewSerializerLabel(field_name, model_handle):
    display_name = MODEL_FIELDS_LABELS_DICT.get(model_handle, None)
    if not display_name:
        return field_name
    display_name = display_name.get(field_name, None)
    if not display_name:
        return field_name
    return display_name

def getAdministrationIndexMenus():
    return ADMINISTRATION_INDEX_MENUS

def getReportsIndexMenus():
    return REPORTS_INDEX_MENUS

def getReportIndexAnalytics():
    return REPORTS_INDEX_ANALYTICS_DICT

def getHomeIndexAnalytics():
     return HOME_INDEX_ANALYTICS_DICT

def getModelGeneralSearchForm(modelHandle):
    return GENERAL_SEARCH_FORM_DICT.get(modelHandle, None)