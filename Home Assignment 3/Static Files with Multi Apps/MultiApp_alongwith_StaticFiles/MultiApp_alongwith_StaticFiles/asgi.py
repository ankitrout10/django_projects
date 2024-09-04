"""
ASGI config for MultiApp_alongwith_StaticFiles project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MultiApp_alongwith_StaticFiles.settings')

application = get_asgi_application()
