DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'db',  # Docker service name for PostgreSQL
        'PORT': '5432',
    }
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'logstash': {
            'level': 'DEBUG',
            'class': 'logstash.LogstashHandler',
            'host': 'logstash',
            'port': 5044,
        },
    },
    'root': {
        'handlers': ['logstash'],
        'level': 'DEBUG',
    },
}