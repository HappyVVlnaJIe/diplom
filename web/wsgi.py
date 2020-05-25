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

p = subprocess.Popen(["python", "./runscript.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()
if p.returncode == 0:
    application = get_wsgi_application()
else:
    raise Exception("{}, out={}".format(err,out))

application = get_wsgi_application()