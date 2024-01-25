# localstore

The `localstore` package is a collection of Python modules for managing data in a local store. It includes modules for converting CSV files to a JSON dataset, managing data in a local JSON store, and creating a local API for accessing data in the store.

## Installation

To install the `localstore` package, you can use pip:

```
pip install localstore
```

## Usage

### DatasetConverter

The `DatasetConverter` module provides a simple and intuitive API for converting CSV files to a JSON dataset. To use the `DatasetConverter` module, you can:

1. Import the `DatasetConverter` module:

```python
from localstore.DatasetConverter import Converter
```

2. Create an instance of the `Converter` class:

```python
converter = Converter()
```

3. Convert all the CSV files in a specified directory to a JSON dataset:

```python
converter.Dataset_From_Directory('path/to/directory')
```

4. Convert a single CSV file to a JSON dataset:

```python
converter.Dataset_From_File('path/to/file.csv')
```

5. Create a JSON dataset file and a text file containing the length of the dataset:

```python
converter.Create_Dataset()
```

### LocalStore

The `LocalStore` module provides a simple and intuitive API for managing data in a local JSON store. To use the `LocalStore` module, you can:

1. Import the `LocalStore` module:

```python
from localstore.LocalStore import LocalStore
```

2. Create an instance of the `LocalStore` class:

```python
local_store = LocalStore()
```

3. Add a new product to the local store:

```python
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
local_store.Add_New_Product(product_name='Apple', data=product)
```

4. Get a list of all the products in the local store:

```python
products = local_store.Show_product_List()
```

5. Print the list of products:

```python
for product in products:
    print(product)
```

### LocalAPI

The `LocalAPI` module provides a simple and intuitive API for creating a local API for accessing data in the store. To use the `LocalAPI` module, you can:

1. Import the `LocalAPI` module:

```python
from localstore.LocalAPI import LocalAPI
```

2. Create an instance of the `LocalAPI` class:

```python
local_api = LocalAPI()
```

3. Start the LocalAPI server:

```python
local_api.runServer()
```

4. Send API requests to the LocalAPI server to perform CRUD operations on data in the local store:

```python
import requests

# Get a list of all the products in the local store
products = requests.get('http://localhost:5000/products/show/')

# Print the list of products
for product in products.json():
    print(product)
```

## Conclusion

The `localstore` package is a powerful and easy-to-use Python package for managing data in a local store. It is a great choice for a variety of applications, including e-commerce websites, content management systems, data analysis applications, and any other application that needs to store data locally. 

## Contributing

Contributions to LocalStore are welcome! Please read the [contributing guidelines](https://github.com/colddsam/LocalStore/blob/main/CONTRIBUTING.md) before submitting a pull request.

## License

LocalStore is licensed under the [MIT License](https://github.com/colddsam/LocalStore/blob/b21bdae42f8a31a7ca5e9d954dace06d66c132f6/LICENSE)