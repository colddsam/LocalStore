# How to Use LocalAPI as an API

LocalAPI can be used as an API to allow other applications to access and manipulate data in a local store. To use LocalAPI as an API, you need to:

1. **Create a LocalAPI instance:**
```python
from localstore.LocalAPI import LocalAPI
local_api = LocalAPI()
```

2. **Start the LocalAPI server:**
```python
local_api.runServer()
```

3. **Send API requests to the LocalAPI server:**
You can use any HTTP client to send API requests to the LocalAPI server. For example, you can use the `requests` library:
```python
import requests

# Get a list of all the products in the local store
products = requests.get('http://localhost:5000/products/show/')

# Print the list of products
for product in products.json():
    print(product)
```

The following table provides a summary of the available LocalAPI endpoints:

| Endpoint | Method | Description |
|---|---|---|
| `/products/show/` | GET | Returns a list of all the products in the local store. |
| `/products/random/` | GET | Returns a random product from the local store. |
| `/products/insert/{product_name}` | POST | Adds a new product to the local store. |
| `/data/show/` | GET | Returns the data stored at the specified index in the local store. |
| `/data/delete/{index}` | DELETE | Deletes the data stored at the specified index in the local store. |
| `/items/insert/{product_name}` | POST | Adds a new item to the local store. |
| `/items/show/` | GET | Returns a list of all the items in the local store. |

## Example

The following example shows how to use LocalAPI as an API to manage product data on an e-commerce website:

1. **Create a LocalAPI instance:**
```python
from localstore.LocalAPI import LocalAPI
local_api = LocalAPI()
```

2. **Start the LocalAPI server:**
```python
local_api.runServer()
```

3. **Send API requests to the LocalAPI server to perform CRUD operations on product data:**
```python
import requests

# Add a new product to the local store
product = {
    'name': 'iPhone 13 Pro',
    'main_category': 'Electronics',
    'sub_category': 'Smartphones',
    'image': 'https://example.com/iphone-13-pro.jpg',
    'link': 'https://example.com/iphone-13-pro',
    'ratings': '4.5',
    'no_of_ratings': '100',
    'discount_price': '999.00',
    'actual_price': '1099.00'
}
requests.post('http://localhost:5000/products/insert/Apple', json=product)

# Get a list of all the products in the local store
products = requests.get('http://localhost:5000/products/show/')

# Print the list of products
for product in products.json():
    print(product)
```

## Conclusion

LocalAPI is a powerful and easy-to-use Python package that can be used as an API to allow other applications to access and manipulate data in a local store. This makes it a great choice for building a variety of applications, including e-commerce websites, content management systems, data analysis applications, and any other application that needs to store data locally. 