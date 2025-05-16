# 📋 Dictionaries

## Combination

### `sum_dicts`

Consider an example with two coffee shop locations,
each reporting sales as a dictionary, with the goal of
producing a dictionary of total sales:

``` py title="before.py" hl_lines="1 8-11"
from collections import defaultdict

# Sales from two locations
north_sales = {"coffee": 120, "cookie": 5, "juice": 40}
south_sales = {"coffee": 80, "cookie": 45, "banana": 10}

# Manual summation using defaultdict
combined_sales = defaultdict(int)
for location_sales in (north_sales, south_sales):
    for product, quantity in location_sales.items():
        combined_sales[product] += quantity

print(combined_sales)
# {"coffee": 200, "cookie": 50, "juice": 40, "banana": 10}
```
!!! question "Why avoid this approach?"

    Note that the dictionary summation logic takes more than half of the code: 5 lines out of 8.
    But nothing in it relates specifically to business logic - combining sales.

Use UtilsX to drastically simplify the preceding code:

``` py title="after.py" hl_lines="1 8"
from utilsx import sum_dicts

# Sales from two locations
north_sales = {"coffee": 120, "cookie": 5, "juice": 40}
south_sales = {"coffee": 80, "cookie": 45, "banana": 10}

# Summation using UtilsX function
combined_sales = sum_dicts(north_sales, south_sales)

print(combined_sales)
# {"coffee": 200, "cookie": 50, "juice": 40, "banana": 10}
```

## Filtering

### `remove_items_with_zero_values`

Consider a case where a coffee shop tracks product sales, but some items haven’t sold at all.
The sales report includes all items, even those with zero sales - which clutters the output
and may cause confusion in downstream reporting.

``` py title="before.py" hl_lines="11"
# Sales including items with zero quantity
sales_report = {
    "coffee": 200,
    "cookie": 0,
    "juice": 40,
    "banana": 0,
    "sandwich": 25,
}

# Filtering using a dictionary comprehension
cleaned_report = {item: qty for item, qty in sales_report.items() if qty}

print(cleaned_report)
# {"coffee": 200, "juice": 40, "sandwich": 25}
```

!!! question "Why avoid this approach?"

    The filtering logic still mixes with business logic — it obscures the intent to simply "clean up the report."
    Repeating this pattern across different places increases maintenance cost.

Use UtilsX to cleanly filter the sales report:

``` py title="after.py" hl_lines="1 13"
from utilsx import remove_items_with_zero_values

# Sales including items with zero quantity
sales_report = {
    "coffee": 200,
    "cookie": 0,
    "juice": 40,
    "banana": 0,
    "sandwich": 25,
}

# Remove zero-value entries using UtilsX
cleaned_report = remove_items_with_zero_values(sales_report)

print(cleaned_report)
# {"coffee": 200, "juice": 40, "sandwich": 25}
```
