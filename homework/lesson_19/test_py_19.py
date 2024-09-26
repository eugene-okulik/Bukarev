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
    assert req.status_code == 200, 'Метод удалить объект не отработал'
    print('Удаление', req)
    r = requests.get(f'https://api.restful-api.dev/objects/{postid}')
    assert r.status_code == 404, 'Объект не удален'
    print('dddd', r)


# @pytest.fixture()
# def get_obj_id():
#     r = requests.get(f'http://167.172.172.115:52353/object/64')
#     print('dddddddddddddd', r.status_code)


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
