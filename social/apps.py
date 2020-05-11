from django.apps import AppConfig

# Este Verbose cambia el nombre que aparece en el admin
class SocialConfig(AppConfig):
    name = 'social'
    verbose_name = "Redes Sociales"
