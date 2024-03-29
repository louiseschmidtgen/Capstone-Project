.PHONY: build install-deps install-pyqt5-mac-m1 mysql upgrade-mysqlconnector start-app mysql-stop

# Default target to display available commands
help:
	@echo "Available commands:"
	@echo "make install-deps      # Install Python dependencies and create a virtual environment"
	@echo "make install-pyqt5-mac-m1  # Install PyQt5 on macOS (M1), comment out its line in the pipfile" 
	@echo "make mysql-start       # Start a MySQL Docker container"
	@echo "make upgrade-mysqlconnector  # Upgrade the MySQL Connector/Python library"
	@echo "make start-app         # Start the application"
	@echo "make mysql-stop        # Stop and remove the MySQL Docker container"

build: mysql-start install-deps  start-app

build-m1: mysql-start install-deps install-pyqt5-mac-m1  start-app

install-deps: upgrade-mysqlconnector
	pipenv --python 3.7
	pipenv install
	pipenv run pip install --upgrade mysql-connector-python

install-pyqt5-mac-m1:
	pipenv run pip install pyqt5 --config-settings --confirm-license= --verbose

mysql-start:
	docker pull mysql:latest
	docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=my-secret-pw -d -p 3306:3306 mysql:latest --default-authentication-plugin=mysql_native_password

upgrade-mysqlconnector:
	pipenv run pip install --upgrade mysql-connector-python

start-app:
	cd ./app && \
	pipenv run python main.py && \
	cd ..

mysql-stop:
	docker stop mysql-container
	docker rm mysql-container
