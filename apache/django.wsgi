import os, sys

PROJECT = os.path.dirname(os.path.dirname(__file__))
WORKSPACE = os.path.dirname(PROJECT)

if WORKSPACE not in sys.path:
    sys.path.append(PROJECT)
    sys.path.append(WORKSPACE)

os.environ['DJANGO_SETTINGS_MODULE'] = '%s.settings' % os.path.basename(PROJECT)

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()