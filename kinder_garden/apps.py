from django.apps import AppConfig

class KinderGardenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kinder_garden'

    def ready(self):
        import kinder_garden.translation
