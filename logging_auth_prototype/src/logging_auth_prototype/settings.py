# Django settings for logging_auth_prototype project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '/home/jds/workspace/logging_auth_prototype/src/sqlite.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = ''
MEDIA_URL = ''
ADMIN_MEDIA_PREFIX = '/media/'
SECRET_KEY = 'cklk!dy&$tp3up16cu%t6b@uxpezu2-e^ns$8v*#h5rg&oa6*u'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'logging_auth_prototype.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'dblogging',
)

# To clear out login sessions....
# Session.objects.all().delete()
AUTHENTICATION_BACKENDS = ('dblogging.auth.ActiveDirectoryBackend',
                           'django.contrib.auth.backends.ModelBackend',)

# From Steve S.
# name and password: anonldap / atsadmin
# account is in the domain ultra-ats might need to be specified as ultra-ats\anonldap
# search root: cn=users, dc=ultra-ats, dc=com
# authentication type: simple

# Some links on the subject
# http://packages.python.org/django-auth-ldap/
# going to want to do this.
# https://docs.djangoproject.com/en/dev/topics/auth/#storing-additional-information-about-users
# trying this now.
# http://djangosnippets.org/snippets/501/
#AD_DNS_NAME = 'armstrong.ultra-ats.com'
AD_DNS_NAME = 'strongarm.ultra-ats.com'
AD_LDAP_PORT = 389
#AD_SEARCH_DN = 'CN=Users,dc=ultra-ats,dc=com'
AD_SEARCH_DN = 'dc=ultra-ats,dc=com'
AD_NT4_DOMAIN = 'EXAMPLE'
#AD_NT4_DOMAIN = 'ULTRA-ATS'
AD_SEARCH_FIELDS = ['mail','givenName','sn','sAMAccountName']
AD_LDAP_URL = 'ldap://%s:%s' % (AD_DNS_NAME,AD_LDAP_PORT)
