from django.apps import AppConfig


class ModelBasedFormAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Model_Based_Form_App'
