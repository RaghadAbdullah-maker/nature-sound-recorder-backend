"""
WSGI config for nature_sound_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nature_sound_project.settings')

django.setup()
call_command('migrate', interactive=False)  # هنا نشغل المايجريشن تلقائي

application = get_wsgi_application()
