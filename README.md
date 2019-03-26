# PyAgain
PyAgain makes it easy to try again (theoretically). In development.

## Usage
Decorate your function with @pyagain(maximum_number_of_retries,allowed_exceptions,verbose)

Retries are quiet by default. Set verbose to True to see what's going on.
If the number of retries exceeds the maximum, the last exception is re-raised.
If you don't define allowed exceptions, only a pyagain.IntendedException will be caught. 

## Example usage
```python
from random import random
@pyagain(10, allowed_exceptions=(ValueError), verbose=True)
def example():
    if random()>0.2:
        raise ValueError
    else:
        print("Success")
```

## The pyagain.IntendedException
It might come handy if you want to re-run your function depending on a stochastic outcome. A nice example is scraping an unreliable page, where backend fetch fails sometimes. Example:
```python
import requests
@pyagain(10, verbose=True)
def scrape_page(url):
    page = requests.get(url)
    if page.status_code!=200:
        raise IntendedException
    else:
        return page
```


