```bash
docker-compose -f docker-compose.yml up -d rabbitmq flask_app
```
```bash
virtualenv -p python3.8 ENV
source ENV/bin/activate
./ENV/bin/pip install -r requirements.txt
```




Management UI: http://localhost:15672
Homebrew-specific docs: https://rabbitmq.com/install-homebrew.html

To start rabbitmq now and restart at login:
```bash
  brew services start rabbitmq
```
Or, if you don't want/need a background service you can just run:
```bash
  CONF_ENV_FILE="/opt/homebrew/etc/rabbitmq/rabbitmq-env.conf" /opt/homebrew/opt/rabbitmq/sbin/rabbitmq-server
```


```bash
celery -A my_celery.celery_tasks worker --loglevel=info
celery -A my_celery.celery_tasks beat --loglevel=info

python my_celery.celery_app.py
```
