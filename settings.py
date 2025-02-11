from pathlib import Path

# List of fields, the value of which will be saved
# to the excel file when exporting tasks.
TASK_COLUMNS = ["creation_date", "name", "closing_date", "lead_time", "id"]

# ✅ Celery Settings
CELERY_BROKER_URL = "redis://localhost:6379/0"  # Using Redis as a message broker
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"

# ✅ Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ Static Files Configuration
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

# ✅ Security Settings
SECRET_KEY = "django-insecure-fxirp6s-em6dx=j$#ti$a!^7d3p(1$67g=%9=-j4-6m_4ad-ly"
DEBUG = True

# ✅ Allowed Hosts
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# ✅ Installed Apps
INSTALLED_APPS = [
    "recruitment.apps.RecruitmentConfig",  # ✅ Ensure this is correct
    "tasks.apps.TasksConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# ✅ Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ✅ URL Configuration
ROOT_URLCONF = "mycrm.urls"

# ✅ Fixed TEMPLATES Section (Proper Indentation)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "recruitment" / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

# ✅ WSGI Application
WSGI_APPLICATION = "mycrm.wsgi.application"

# ✅ Database Configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ✅ Authentication Settings
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ✅ Login & Redirect Settings
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "/dashboard/"
LOGOUT_REDIRECT_URL = "/login/"

# ✅ Internationalization
LANGUAGE_CODE = "en-uk"
TIME_ZONE = "GMT"
USE_I18N = True
USE_TZ = True

# ✅ Default Primary Key Field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
