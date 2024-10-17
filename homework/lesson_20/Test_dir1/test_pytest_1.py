import requests
import allure
import pytest


@allure.feature('удаление')
@allure.story("Метод удаления 1")
@allure.title('Удаление объекта методом 1')
def test_delete_id_1(new_post_id):
    with allure.step(f'Запрос методом Delete c ID = {new_post_id}'):
        req = requests.delete(f'http://167.172.172.115:52353/object/{new_post_id}')
    with allure.step('проверка на статус ответа 200'):
        assert req.status_code == 300, 'Метод удалить объект не отработал'

@allure.feature('удаление №2')
@allure.story("метод удаления 2")
def test_delete_id_2(new_post_id):
    req = requests.delete(f'http://167.172.172.115:52353/object/{new_post_id}')
    assert req.status_code == 200, 'Метод удалить объект не отработал'

@allure.feature("создание обеъкта")
@allure.story("Создание методом Post")
def test_create_post():
    body = {"name": "Zenit", "data": {"year": 2025, "price": 10000, "CPU model": "Zenit99",
                                      "Hard disk size": "100 TB"}}
    headers = {"content-type": "application/json"}
    req = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers).json()
    print(req)

@allure.feature('Изменения в объекте')
@allure.story("Метод PATCH")
@pytest.mark.smoke
def test_patch_id(new_post_id):
    body = {
        "data": {
            "Hard disk size": "11 TB"
        }
    }
    headers = {"content-type": "application/json"}
    r = requests.patch(f'http://167.172.172.115:52353/object/{new_post_id}', json=body, headers=headers).json()
    print(r)

@allure.feature("Изменение во всем объекте")
@allure.story("Метод PATCH")
@pytest.mark.regression
def test_put_id(new_post_id):
    body = {"name": "Apple MacBook Pro 16", "data": {"year": 2019, "price": 2049.99, "CPU model": "Intel Core i9",
                                                     "Hard disk size": "1 TB", "color": "silver"}}
    headers = {"content-type": "application/json"}
    r = requests.patch(f'http://167.172.172.115:52353/object/{new_post_id}', json=body, headers=headers).json()
    print(r)
