# 🗄️ Collections

### [`check_equal_length`][utilsx.check_equal_length]

Consider a scenario where you receive synchronized lists of product information,
such as names, prices, and stock levels, and need to ensure the data is aligned
before further processing:

``` py title="manual.py" hl_lines="7"
# Raw product data
product_names = ["coffee", "cookie", "juice"]
product_prices = [3.5, 2.0]  # Missing price for "juice"
product_stock = [120, 85, 40]

# Manual length check
if not (len(product_names) == len(product_prices) == len(product_stock)):
    raise ValueError("Mismatched product data lengths")
```

Use UtilsX to perform that in a cleaner way:

``` py title="with_utilsx.py" hl_lines="1 9"
from utilsx import check_equal_length

# Raw product data
product_names = ["coffee", "cookie", "juice"]
product_prices = [3.5, 2.0]
product_stock = [120, 85, 40]

# Clean, readable validation
if not check_equal_length(product_names, product_prices, product_stock):
    raise ValueError("Mismatched product data lengths")
```
