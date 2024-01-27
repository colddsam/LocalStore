import pytest
from localstore.LocalStore import LocalStore


@pytest.fixture
def localstore_instance():
    return LocalStore()


def test_show_items(localstore_instance):
    result = localstore_instance.Show_Items()
    assert result["status"] is True
    assert isinstance(result["response"], list)


def test_show_product_list(localstore_instance):
    result = localstore_instance.Show_product_List('existing_product')
    assert result["status"] is False


def test_show_random_product(localstore_instance):
    result = localstore_instance.Show_Random_Product()
    assert result["status"] is True
    assert isinstance(result["response"], dict)


def test_add_new_product(localstore_instance):
    data = {"param1": "value1", "param2": "value2"}
    result = localstore_instance.Add_New_Product('new_product', data)
    assert result["status"] is False


def test_add_new_item(localstore_instance):
    result = localstore_instance.Add_New_Item('new_item')
    assert result["status"] is True


def test_show_data(localstore_instance):
    result = localstore_instance.Show_Data('existing_index')
    assert result["status"] is False


def test_delete_data(localstore_instance):
    result = localstore_instance.Delete_Data('index_to_delete')
    assert result["status"] is False


def test_write_json(localstore_instance):
    result = localstore_instance.Write_Json()
    assert result["status"] is True

