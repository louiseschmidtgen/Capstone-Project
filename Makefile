
.PHONY: 

all:
	@echo "make install-deps"
	@echo "make mysql"
	@echo "make upgrade-mysqlconnector"
	@echo "make start-app"

install-deps:
	pipenv --python 3.7
	pipenv install
	pipenv shell

install-pyqt5-mac-m1:
	pipenv shell
	pip install pyqt5 --config-settings --confirm-license= --verbose

mysql:
	docker pull mysql:latest
	docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=my-secret-pw -d -p 3306:3306 mysql:latest

upgrade-mysqlconnector:
	pipenv shell
	pip install --upgrade mysql-connector-python

start-app:
	pipenv shell
	python main.py

mysql-stop:
	docker stop mysql-container
	docker rm mysql-container
