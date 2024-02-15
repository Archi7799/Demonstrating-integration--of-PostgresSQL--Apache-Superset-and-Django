import os

# PostgreSQL database connection URI
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:superset@postgres:5432/mydb')

# Set Superset's web server base URL
SUPERSET_WEBSERVER_BASEURL = 'http://django_container:8000/'

SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_HTTPONLY = False
WTF_CSRF_ENABLED = False

# Ensure public role behaves like Gamma
GUEST_ROLE_NAME = "Gamma"
PUBLIC_ROLE_LIKE = "Gamma"

# Enable the Embedded Superset feature flag
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    "EMBEDDABLE_CHARTS": True
}

# Enable template processing
ENABLE_TEMPLATE_PROCESSING = True

# Enable proxy fix if Superset is behind a proxy
ENABLE_PROXY_FIX = True

# Enable CORS to accept requests from your Django application
ENABLE_CORS = True
CORS_ALLOW_ORIGIN = 'http://localhost:8000'

# Secret key for Superset
SECRET_KEY = "startwithyoursuperset"
