# DatasetConverter: A Python Tool for Effortless Data Conversion

## Overview

DatasetConverter is a versatile Python tool that simplifies the conversion of data from various formats to a standardized structure. This tool, found within the `localstore` package as `DatasetConverter.py`, is designed to handle data stored in directories or files, supporting common formats like CSV and Excel.

## Features of DatasetConverter

* **Support for multiple formats:** DatasetConverter supports both CSV and Excel formats, providing flexibility in handling different types of datasets.
* **Consistent data structure:** The tool ensures a consistent and standardized data structure for the converted datasets.
* **Data validation:** Built-in data validation helps maintain the accuracy and integrity of the converted data.
* **Efficient hashing:** Utilizes efficient hashing (SHA-256) to generate unique identifiers for each data entry.

## Benefits of Using DatasetConverter

DatasetConverter offers several advantages:

* **Format agnostic:** Handle datasets in different formats seamlessly, without worrying about the underlying file structure.
* **Automated conversion:** Easily convert entire directories or individual files with a few simple commands.
* **Structured output:** The converted datasets maintain a well-defined structure, making them easy to work with in subsequent processes.

## When and Where to Use DatasetConverter

Consider using DatasetConverter in the following scenarios:

* **Data integration:** When consolidating data from various sources into a standardized format.
* **Pre-processing:** For preparing datasets before analysis or machine learning tasks.
* **Data migration:** When transitioning between different data storage formats or structures.

## How to Use DatasetConverter

To utilize DatasetConverter, follow these steps:

1. **Installation:** Ensure that the `localstore` package, containing `DatasetConverter.py`, is accessible in your Python environment.

2. **Import the tool:** In your Python script, import the DatasetConverter class:

    ```python
    from localstore.DatasetConverter import Converter
    ```

3. **Create an instance:** Instantiate the DatasetConverter class:

    ```python
    converter = Converter()
    ```

4. **Convert data from a directory:** Use the `Dataset_From_Directory` method to convert data from a directory:

    ```python
    converter.Dataset_From_Directory(path='your_directory_path', format='csv')
    ```

5. **Convert data from a file:** Use the `Dataset_From_File` method to convert data from a file:

    ```python
    converter.Dataset_From_File(path='your_file_path', format='csv')
    ```

6. **Create the converted dataset:** Execute the `Create_Dataset` method to generate the converted dataset:

    ```python
    converter.Create_Dataset()
    ```

## Example

Here's a simple example demonstrating how to use DatasetConverter:

```python
from localstore.DatasetConverter import Converter

# Create an instance of the DatasetConverter class
converter = Converter()

# Convert data from a directory
converter.Dataset_From_Directory(path='your_directory_path', format='csv')

# Convert data from a file
converter.Dataset_From_File(path='your_file_path', format='csv')

# Create the converted dataset
converter.Create_Dataset()
```

## Conclusion

DatasetConverter is an indispensable tool for developers dealing with diverse datasets. Whether you're integrating data from different sources or preparing datasets for analysis, DatasetConverter ensures a seamless and structured conversion process. Its simplicity and flexibility make it a valuable asset in various data-related workflows.

## Table: DatasetConverter Methods

| Method | Description |
|---|---|
| `Dataset_From_Directory(path)` | Converts all the CSV or excel files in a specified directory to a JSON dataset. |
| `Dataset_From_File(path)` | Converts a single CSV or excel file to a JSON dataset. |
| `Create_Dataset()` | Creates a JSON dataset file and a text file containing the length of the dataset. | 