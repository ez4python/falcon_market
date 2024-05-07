mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

admin:
	python3 manage.py createsuperuser

run:
	sudo chmod 666 /var/run/docker.sock
	docker start pg_messenger minio_tg redis_db

lan:
	python3 manage.py makemessages -l en -l ru -l uz
	python3 manage.py compilemessages --ignore=.venv