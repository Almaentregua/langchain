# Variables
SRC = src

create-env:
	python3 -m venv llm-env
	
install:
	. llm-env/bin/activate && pip install -r requirement.txt

format:
	black $(SRC)

sort:
	isort $(SRC)

check-format:
	black --check $(SRC)

check-sort:
	isort --check-only $(SRC)

lint:
	make format
	make sort

check:
	make check-format
	make check-sort
