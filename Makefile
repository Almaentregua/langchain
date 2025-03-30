create-env:
	python3 -m venv llm-env
	
install:
	. llm-env/bin/activate && pip install -r requirement.txt
