install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirement.txt

test:
	python3 -m pytest -vv test_hello.py

format:
	black *.py


lint:
	pylint --disable=R,C hello.py

all: install lint test