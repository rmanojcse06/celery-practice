```bash
docker pull quay.io/arubadevops/rabbitmq-base-jenkins:rabbitmq-3.12.3-management
docker stop rabbitmq_celery
docker rm rabbitmq_celery
docker run -d --name rabbitmq_celery --platform linux/amd64 -p 5672:5672 -p 15672:15672 -v rabbitmq_data:/var/lib/rabbitmq quay.io/arubadevops/rabbitmq-base-jenkins:rabbitmq-3.12.3-management
docker start rabbitmq_celery
pip install -r requirements.txt
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
celery -A tasks worker --loglevel=info
celery -A tasks beat --loglevel=info

python app.py
```
