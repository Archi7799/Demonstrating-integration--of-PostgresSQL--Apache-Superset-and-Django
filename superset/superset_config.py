# PostgreSQL database connection URI
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:superset@postgres:5432/mydb'

# Set Superset's web server base URL
#SUPERSET_WEBSERVER_BASEURL = 'http://localhost:8088/'

#SESSION_COOKIE_SAMESITE = None
#SESSION_COOKIE_HTTPONLY = False
WTF_CSRF_ENABLED = True
TALISMAN_ENABLED=False
#OVERRIDE_HTTP_HEADERS = {'X-Frame-Options': 'ALLOWALL'}
#HTTP_HEADERS = {'X-Frame-Options': 'ALLOWALL'}
HTTP_HEADERS = {}
# Ensure public role behaves like Gamma
#GUEST_ROLE_NAME = "Gamma"
#PUBLIC_ROLE_LIKE = "Gamma"

# Enable the Embedded Superset feature flag
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    "EMBEDDABLE_CHARTS": True
}

CORS_OPTIONS = {
  'supports_credentials': True,
  'allow_headers': ['*'],
  'resources':['*'],
  'origins': ['http://localhost:8088', 'http://superset_container:8088']
}

#CONTENT_SECURITY_POLICY = {
#  'default-src': ['self', 'http://localhost:8000', 'http://django_container:8000'],
  # Add other directives as needed
#}

#ENABLE_JAVASCRIPT_CONTROLS = True

# Enable template processing
ENABLE_TEMPLATE_PROCESSING = True

# Enable proxy fix if Superset is behind a proxy
ENABLE_PROXY_FIX = True

# Enable CORS to accept requests from your Django application
#ENABLE_CORS = True
#CORS_ALLOW_ORIGIN = 'http://localhost:8000'

# Secret key for Superset
SECRET_KEY = "startwithyoursuperset"
