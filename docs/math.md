# 🧮 Math

## Collections

### [`check_values_add_up_to_one`][utilsx.check_values_add_up_to_one]

Useful in data validation to assure that values in a collection add up to 1 or 100.

Imagine a cooking recipe defined as proportions:

```py title="recipe.py" hl_lines="1 10"
from utilsx import check_values_add_up_to_one

recipe = {
    "water": 0.5,
    "sauce": 0.1,
    "potatoes": 0.25,
    "fish": 0.15,
}

check_values_add_up_to_one(recipe.values())
# > True
```

By default, it returns `True` if values add up either to 1 or 100.
You can control this behavior using the `mode` argument.

### [`normalize`][utilsx.normalize]

Helps you scale a sequence of numbers to add up to one, while keeping original relations.

```py title="portfolio.py" hl_lines="1 5"
from utilsx import normalize

holdings_usd = [300, 50, 120]

holdings_proportions = normalize(holdings_usd)
print(holdings_proportions)
# [0.6383, 0.1064, 0.2553]
```
