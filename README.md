# LocalStore

## Introduction

LocalStore is a Python library that provides various operations on a local database of products, which can be used to store and manage information about items in a local store inventory.

## Features

* **View Items**: Get a list of all items in the database.
* **View Product List**: Get a list of all products in the database along with their details.
* **View Random Product**: Get a random product from the database.
* **Add New Product**: Add a new product to the database.
* **Add New Item**: Add a new item to a product in the database.
* **Show Data**: Get the data of a specific item in the database.
* **Delete Data**: Delete a specific item from the database.
* **Write JSON**: Save the database to a JSON file and a text file containing the length of the database.

## Installation

To install LocalStore, run the following command in your terminal:

```
pip install localstore
```

## Usage

### Initialization

To use LocalStore, you need to create an instance of the `LocalStore` class. You can pass the path to a JSON file containing the database and a text file containing the length of the database as arguments to the constructor. If you do not pass these arguments, the default dataset will be loaded.

```
from localstore import LocalStore

# Initialize the LocalStore class with default dataset
store = LocalStore()

# Initialize the LocalStore class with custom dataset and length file
store = LocalStore(data="path/to/dataset.json", length="path/to/length.txt")
```

### Show Items

To get a list of all items in the database, use the `Show_Items` method.

```
response = store.Show_Items()

if response["status"]:
    print(response["response"])  # List of items
else:
    print(response["response"])  # Error message
```

### Show Product List

To get a list of all products in the database along with their details, use the `Show_product_List` method.

```
response = store.Show_product_List(product_name="product_name")

if response["status"]:
    print(response["response"])  # List of products
else:
    print(response["response"])  # Error message
```

### Show Random Product

To get a random product from the database, use the `Show_Random_Product` method.

```
response = store.Show_Random_Product()

if response["status"]:
    print(response["response"])  # Random product
else:
    print(response["response"])  # Error message
```

### Add New Product

To add a new product to the database, use the `Add_New_Product` method. You need to pass the product name and a dictionary containing the product details as arguments to the method.

```
product_name = "product_name"
product_details = {"key1": "value1", "key2": "value2"}

response = store.Add_New_Product(product_name, product_details)

if response["status"]:
    print(response["response"])  # Newly added product
else:
    print(response["response"])  # Error message
```

### Add New Item

To add a new item to a product in the database, use the `Add_New_Item` method. You need to pass the product name as an argument to the method.

```
product_name = "product_name"

response = store.Add_New_Item(product_name)

if response["status"]:
    print(response["response"])  # New item added message
else:
    print(response["response"])  # Error message
```

### Show Data

To get the data of a specific item in the database, use the `Show_Data` method. You need to pass the item index as an argument to the method.

```
item_index = "item_index"

response = store.Show_Data(item_index)

if response["status"]:
    print(response["response"])  # Item data
else:
    print(response["response"])  # Error message
```

### Delete Data

To delete a specific item from the database, use the `Delete_Data` method. You need to pass the item index as an argument to the method.

```
item_index = "item_index"

response = store.Delete_Data(item_index)

if response["status"]:
    print(response["response"])  # Deleted item data
else:
    print(response["response"])  # Error message
```

### Write JSON

To save the database to a JSON file and a text file containing the length of the database, use the `Write_Json` method. You can pass the paths to the JSON file and the text file as arguments to the method.

```
json_path = "path/to/dataset.json"
text_path = "path/to/length.txt"

response = store.Write_Json(json_path, text_path)

if response["status"]:
    print(response["response"])  # File saved message
else:
    print(response["response"])  # Error message
```

## Contributing

Contributions to LocalStore are welcome! Please read the [contributing guidelines](https://github.com/colddsam/LocalStore/blob/main/CONTRIBUTING.md) before submitting a pull request.

## License

LocalStore is licensed under the MIT License