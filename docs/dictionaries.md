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
