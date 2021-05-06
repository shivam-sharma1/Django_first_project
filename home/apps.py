from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

# register app in admin.py and copy name from apps.py and save it in installed apps setting.