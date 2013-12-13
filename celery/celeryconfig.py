from celery.schedules import crontab

BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "myuser"
BROKER_PASSWORD = "mypassword"
BROKER_VHOST = "/"

CELERY_RESULT_BACKEND = "amqp"
CELERY_IMPORTS = ("tasks",)

CELERY_DISABLE_RATE_LIMITS = True  #expensive submodule (disable if not in use)

CELERYBEAT_SCHEDULE = {
    "tasks.DateTimeTask_every-minute": {
        "task": "tasks.DateTimeTask",   
        "schedule": crontab(minute="*/2"),
    },
}
