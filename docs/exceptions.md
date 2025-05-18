# ⛔ Exceptions

### [`prohibit_negative_values`][utilsx.prohibit_negative_values]

Suppose you process a list of daily sales amounts
that must never contain negative values, as they represent revenue:

``` py title="manual.py" hl_lines="5-6"
# Daily sales data
sales = [1200.0, 1500.5, -300.0, 1100.0]

# Manual check for negatives
if any(sale < 0 for sale in sales):
    raise ValueError("Sales data contains negative values")
```

This check remains straightforward but forces you to repeat the same pattern
wherever you enforce non-negativity, cluttering your code.

Use UtilsX to make this validation clear and reusable:

``` py title="with_utilsx.py" hl_lines="1 6"
from utilsx import prohibit_negative_values

# Daily sales data
sales = [1200.0, 1500.5, -300.0, 1100.0]

prohibit_negative_values(sales)
```

With `prohibit_negative_values`, you express your intent directly,
improving readability and reducing boilerplate in data validation steps.
