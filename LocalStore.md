 # LocalStore: A Python Package for Managing Local Store Data

## Overview

LocalStore is a Python package that provides a simple and intuitive API for managing data in a local store. It is a submodule of the `localstore` package, and it makes it easy to perform CRUD (Create, Read, Update, Delete) operations on data stored in a local JSON file.

## Features of LocalStore

* **Simple and intuitive API:** LocalStore's API is designed to be easy to use and understand. It uses a straightforward syntax, and all methods are clearly documented.
* **CRUD operations:** LocalStore supports all four CRUD operations (Create, Read, Update, Delete). This makes it easy to manage data in a local store.
* **Extensible:** LocalStore is extensible, allowing you to add your own custom methods and functionality.
* **Data validation:** LocalStore includes built-in data validation, which helps to ensure that the data you store is accurate and consistent.

## Benefits of Using LocalStore

There are many benefits to using LocalStore, including:

* **Improved performance:** LocalStore can significantly improve the performance of your application by reducing the number of times it needs to access the database.
* **Increased security:** LocalStore can help to improve the security of your application by reducing the risk of data breaches.
* **Simplified development:** LocalStore can simplify the development process by making it easier to manage data.
* **Portability:** LocalStore is a portable package, which means it can be used on any platform that supports Python.

## When and Where to Use LocalStore

LocalStore can be used in a variety of applications, including:

* **E-commerce websites:** LocalStore can be used to manage product data on an e-commerce website.
* **Content management systems:** LocalStore can be used to manage content on a content management system.
* **Data analysis:** LocalStore can be used to manage data for data analysis purposes.
* **Any other application that needs to store data locally:** LocalStore can be used in any application that needs to store data locally.

## How to Use LocalStore

To use LocalStore, you first need to install it using pip:

```
pip install localstore
```

Once you have installed LocalStore, you can import it into your Python script:

```python
from localstore.LocalStore import LocalStore
```

You can then create an instance of the LocalStore class:

```python
local_store = LocalStore()
```

The LocalStore class has a number of methods that you can use to manage data in a local store. These methods include:

* **Show_Items:** This method returns a list of all the items in the local store.
* **Show_product_List:** This method returns a list of all the products in the local store.
* **Show_Random_Product:** This method returns a random product from the local store.
* **Add_New_Product:** This method adds a new product to the local store.
* **Add_New_Item:** This method adds a new item to the local store.
* **Show_Data:** This method returns the data stored at the specified index in the local store.
* **Delete_Data:** This method deletes the data stored at the specified index in the local store.
* **Write_Json:** This method writes the data in the local store to a JSON file and a text file.

## Example

The following example shows how to use LocalStore to manage product data on an e-commerce website:

```python
from localstore.LocalStore import LocalStore

# Create an instance of the LocalStore class
local_store = LocalStore()

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
local_store.Add_New_Product(product_name='Apple', data=product)

# Get a list of all the products in the local store
products = local_store.Show_product_List()

# Print the list of products
for product in products:
    print(product)
```

## Table: LocalStore Methods

| Method | Description |
|---|---|
| `Show_Items()` | Returns a list of all the items in the local store. |
| `Show_product_List()` | Returns a list of all the products in the local store. |
| `Show_Random_Product()` | Returns a random product from the local store. |
| `Add_New_Product(product_name, data)` | Adds a new product to the local store. |
| `Add_New_Item(product_name)` | Adds a new item to the local store. |
| `Show_Data(index)` | Returns the data stored at the specified index in the local store. |
| `Delete_Data(index)` | Deletes the data stored at the specified index in the local store. |
| `Write_Json(textpath, jsonpath)` | Writes the data in the local store to a JSON file and a text file. | 

## Conclusion

LocalStore is a powerful and easy-to-use Python package for managing data in a local store. It is a great choice for a variety of applications, including e-commerce websites, content management systems, data analysis applications, and any other application that needs to store data locally.
