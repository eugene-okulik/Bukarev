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
