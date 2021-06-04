from django.apps import AppConfig


class ProjectUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project_user'

    def ready(self):
        from . import signals
