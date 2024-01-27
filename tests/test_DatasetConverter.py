import pytest
import os
import json
from localstore.DatasetConverter import Converter


@pytest.fixture
def converter_instance():
    return Converter()


def test_dataset_from_directory(converter_instance):
    test_path = '../DATASET'
    test_format = 'csv'
    converter_instance.Dataset_From_Directory(test_path, test_format)
    assert converter_instance.dataset is not None


def test_dataset_from_file(converter_instance):
    test_path = '../products.csv'
    test_format = 'csv'
    converter_instance.Dataset_From_File(test_path, test_format)
    assert converter_instance.dataset is not None


def test_create_dataset(converter_instance, tmpdir):
    test_path = '../products.csv'
    test_format = 'csv'
    converter_instance.Dataset_From_File(test_path, test_format)

    assert converter_instance.dataset is not None

    converter_instance.Create_Dataset()

    assert os.path.exists('CONVERTED_DATASET/DATASET.json')
    assert os.path.exists('CONVERTED_DATASET/LENGTH.txt')

    with open('CONVERTED_DATASET/DATASET.json', 'r') as f:
        saved_data = json.load(f)
        assert saved_data == converter_instance.dataset

    with open('CONVERTED_DATASET/LENGTH.txt', 'r') as o:
        saved_length = int(o.read())
        assert saved_length == converter_instance.dataset["length"]
