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

## Division

### [`safe_divide`][utilsx.safe_divide]

Helps you avoid the `try` / `except ZeroDivisionError` clause when a divisor can potentially be zero.

```py title="return_on_equity.py" hl_lines="1 6"
from utilsx import safe_divide

profit = 12
equity = 0

roe = safe_divide(profit, equity)
print(f"Return on equity: {roe:.0%}")
# Return on equity: 0%
```

## Downscaling

### [`convert_number_to_units`][utilsx.convert_number_to_units]

Convert numbers to thousands / millions.

``` py title="downscaling.py" hl_lines="1 4"
from utilsx import convert_number_to_units

revenue_usd = 132890200
revenue_musd = convert_number_to_units(revenue_usd, "million")
print(revenue_musd)
# 132.8902
```
