import os, sys
 
from flup.server.fcgi import WSGIServer
from django.core.wsgi import get_wsgi_application
 
sys.path.insert(0, "/home2/hugong34/setup")
os.environ['DJANGO_SETTINGS_MODULE'] = "setup.settings"
 
WSGIServer(get_wsgi_application()).run()