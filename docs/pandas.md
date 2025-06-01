# 🐻‍❄️ Pandas

Utilities for working with Pandas.

### [`count_na`][utilsx.pandas.count_na]

Pandas `DataFrame` doesn't provide a property with the total number of missing values
in the entire dataframe, so we made it a utility function here.

```py hl_lines="2 5"
import pandas as pd
from utilsx.pandas import count_na

df = pd.DataFrame(...)
if count_na(df):
    print("Dataframe has missing values!")
```

This can be useful in unit testing your data cleaning functions,
when you need to assure that some missing values are preserved.
