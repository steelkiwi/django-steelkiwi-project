PROJECT_NAME = "{{ project_name }}"
DB_NAME = "{{ project_name }}"

APPS = "common" "profiles"

default: mkvirtualenv _settings db end

_settings:
	@echo "Emitting local development settings module"
	@cp settings/local.py.example settings/local.py

requirements:
	@echo "Installing requirements"
	@pip install --exists-action=s -r requirements/local.txt

db: dropdb createdb syncdb migrate loaddata

createdb:
	@echo "Creating PostgreSQL database $(DB_NAME)"
	@make -i _createdb >> /dev/null

_createdb:
	@createdb $(DB_NAME)

dropdb:
	@echo "Destroying PostgreSQL database $(DB_NAME)"
	@make -i _dropdb >> /dev/null

_dropdb:
	@dropdb $(DB_NAME)

migrate:
	@echo "Running migrations"
	@python manage.py migrate -v 0

syncdb:
	@echo "Syncing database and loading initial fixtures"
	@python manage.py syncdb --noinput -v 0

loaddata:
	@echo "Loading additional data fixtures"
	@python manage.py filldb

run:
	@python manage.py runserver

runpub:
	@python manage.py runserver 0.0.0.0:8000

test:
	@python manage.py test $(APPS)

shell:
	@python manage.py shell

end:
	@echo "You can now run development server using 'make run' command"

clean:
	@echo "Cleaning *.pyc files"
	@find . -name "*.pyc" -exec rm -f {} \;

collect_static:
	python manage.py collectstatic -l --noinput

compilemessages:
	python manage.py compilemessages

makemessages:
	python manage.py makemessages -a

workon:
	@source ~/.bashrc && workon $(PROJECT_NAME)

mkvirtualenv:
	@source ~/.bashrc && mkvirtualenv $(PROJECT_NAME)
	@make workon && pip install -U pip setuptools && make requirements
