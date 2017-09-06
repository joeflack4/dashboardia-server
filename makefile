PYTHON=python3
SERVER_DIR=./server/
CLIENT_DIR=./client/
SRC=${SERVER_DIR}dashboardia/
TEST=${SERVER_DIR}test/

PYLINT=${PYTHON} -m pylint --output-format=colorized --reports=n
PYCODESTYLE=${PYTHON} -m pycodestyle
PYDOCSTYLE=${PYTHON} -m pydocstyle

LINT_SRC=${PYLINT} ${SRC}
LINT_TEST=${PYLINT} ${TEST}

CODE_SRC=${PYCODESTYLE} ${SRC}
CODE_TEST=${PYCODESTYLE} ${TEST}

DOC_SRC=${PYDECSTYLE} ${SRC}
DOC_TEST=${PYDOCSTYLE} ${TEST}

MANAGE=${PYTHON} ${SERVER_DIR}manage.py


.PHONY: lint linttest lintall pylint pylinttest pylintall code codetest codeall doc doctest docall test testdoc serve shell db

# ALL LINTING
lint:
	${LINT_SRC} && ${CODE_SRC} && ${DOC_SRC}
linttest:
	${LINT_TEST} && ${CODE_TEST} && ${DOC_TEST}
lintall: lint linttest

# PYLINT
pylint:
	${LINT_SRC}
pylinttest:
	${LINT_TEST}
pylintall: pylint pylinttest

# PYCODESTYLE
code:
	${CODE_SRC}
codetest:
	${CODE_TEST}
codeall: code codetest

# PYDOCSTYLE
doc:
	${DOC_SRC}
doctest:
	${DOC_TEST}
docall: doc doctest

# TESTING
test:
	${PYTHON} -m unittest discover -v
testdoc:
	${PYTHON} -m test --doctests-only

# SERVER MANAGEMENT
serve:
	${MANAGE} runserver
#	flask run
shell:
	${MANAGE} shell
db:
# TODO: Add DB option to manager.
	${MANAGE} initdb --overwrite
gunicorn:
	gunicorn server.dashboardia:app
