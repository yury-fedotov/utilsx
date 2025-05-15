# 🪨 Constants

A module with common real-world constants.

## Numbers

Commonly used literal numbers:

- `THOUSAND`
- `MILLION`
- `BILLION`
- `TRILLION`

Besides helping avoid duplication of
[magic numbers](https://code-basics.com/languages/python/lessons/magic-numbers) in your code,
using these constants protects from typos involving missing / extra `0` in magic numbers.

Example:

``` py title="bad_practice.py"
revenue = 2819920021

# The number below has a missing zero - how long would it take for you to spot?
revenue_billions = revenue / 100000000
```

Do instead:

``` py title="good_practice.py"
from utilsx import BILLION

revenue = 2819920021
revenue_trillions = revenue / BILLION
```

!!! tip "Constants like `pi`, `e` are available in built-in `math` module"

    See full list [here](https://docs.python.org/3/library/math.html#constants).
    UtilsX does not re-define them, and encourages you to import them from `math`.

## Physics

## Time
