venv:
	python3 -m venv venv

install:
	venv/bin/pip install -r libs.txt -c extra.txt