pyenv-setup:
	pyenv install 3.10.6
	pyenv virtualenv 3.10.6 ds_demo_package
	pyenv local ds_demo_package

env-setup:
	cp .env.template .env

activate:
	pyenv activate ds_demo_package

install:
	make activate
	pip install -e .

dev-install:
	make activate
	pip install -e ".[dev]"

test-install:
	make activate
	pip install -e ".[test]"

all-install:
	make install
	make dev-install
	make test-install

code-clean:
	black .
	flake8

tests:
	pytest

new-model:
	@mkdir -p apps/models/$(MODEL_NAME)
	@cp assets/templates/model_template.py apps/models/$(MODEL_NAME)/main.py
	@touch apps/models/$(MODEL_NAME)/README.md
