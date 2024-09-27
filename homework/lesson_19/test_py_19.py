import requests
import pytest


@pytest.fixture()
def new_post_id():
    body = {"name": "Apple MacBook Pro 16", "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9",
                                                     "Hard disk size": "1 TB"}}
    headers = {"content-type": "application/json"}
    req = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers,
    )
    postid = req.json()['id']
    print(postid)
    yield postid
    req = requests.delete(f'http://167.172.172.115:52353/object/{postid}')
    print('Удаление', req)


def test_delete_id(new_post_id):
    req = requests.delete(f'http://167.172.172.115:52353/object/{new_post_id}')
    assert req.status_code == 200, 'Метод удалить объект не отработал'


def test_create_post():
    body = {"name": "Zenit", "data": {"year": 2025, "price": 10000, "CPU model": "Zenit99",
                                                     "Hard disk size": "100 TB"}}
    headers = {"content-type": "application/json"}
    req = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers,
    )


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


@pytest.mark.regression
def test_put_id(new_post_id):
    body = {"name": "Apple MacBook Pro 16", "data": {"year": 2019, "price": 2049.99, "CPU model": "Intel Core i9",
                                                     "Hard disk size": "1 TB", "color": "silver"}}
    headers = {"content-type": "application/json"}
    r = requests.patch(f'http://167.172.172.115:52353/object/{new_post_id}', json=body, headers=headers).json()
    print(r)
