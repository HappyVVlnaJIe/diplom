"""
WSGI config for testproject project.

It exposes the WSGI callable as a module-level variable named   ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import subprocess

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
migrate_retcode = subprocess.run(["python", "../runscript.py"], capture_output=True).returncode
if migrate_retcode == 0:
    application = get_wsgi_application()
else:
    raise Exception("failed to generate")