# Check for typos in texts across the codebase
check-spelling:
	codespell

# Run a linter and a code formatter
lint:
	ruff check --fix
	ruff format

# Run a static type checker
type-checking:
	mypy .

# Run all unit tests
unit-tests:
	pytest .

# Run all continuous integration checks, including absolutely all unit tests
all-checks:
	make check-spelling
	pre-commit run --all-files
	make type-checking
	make unit-tests
