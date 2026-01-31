from celery import Celery

app = Celery('tasks', broker='amqp://guest:guest@rabbitmq:5672', backend='rpc://')
app.config_from_object('my_celery.celery_config')

@app.task
def add(x, y):
    return x + y
