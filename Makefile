define USAGE

Commands:
	init	Install Python dependencies with pipenv
	serve 	Run app in dev environment.
endef

export USAGE
help:
	@echo "$$USAGE"

init:
	pip3 install pipenv
	pipenv install

serve:
	FLASK_APP=app.py pipenv run flask run