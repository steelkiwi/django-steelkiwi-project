from dotenv import read_dotenv
from django.core.wsgi import get_wsgi_application

read_dotenv()
application = get_wsgi_application()
