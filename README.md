# UtilsX

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![mypy](https://img.shields.io/badge/mypy-checked-brightgreen)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)

A collection of useful constants and generic functions for Python.

**Available utilities:**

* 🪨 **Constants**: `MINUTES_IN_HOUR`, `GRAMS_IN_LBS`...
* 📋 **Dictionary operations**: filtering, sorting, summation...
* 🧮 **Math operations**: safe division, scaling, normalization...
* 📊 **Visual utilities**: how many bins to plot?
* 🗄️ **Collections utils**: get duplicates, check all elements are equal...
* ⛔ **Common exceptions**: raise if any negative values, `KeyError` with fix suggestions...
* 📝 **Text**: add suffix with a delimiter...
* 🇹 [**Type variables**](https://docs.python.org/3/library/typing.html#typing.TypeVar) for you to use in custom generic functions.

**Great developer experience:**

* 🐍 Installable via `pip`
* 🤝 Supports all Python versions >= 3.10
* ⛓️ Compatible with type checkers (`mypy`, ...)
* 🪶 Lightweight: has no dependencies

UtilsX aims to provide convenient machinery for generic operations,
so you can focus on the domain logic of your projects.

## Getting started

### Installation

UtilsX is available as `utilsx` on PyPI:

```shell
# With uv's pip interface
uv pip install utilsx

# With uv's project management interface
uv add utilsx

# With plain pip
pip install utilsx
```

### Usage

Import components of UtilsX into your Python files and use just like any other library:

```python
from utilsx import safe_divide

profit = 12
capital = 0

roe = safe_divide(profit, capital)
print(f"Return on equity: {roe:.0%}")
# Output: Return on equity: 0%
```
