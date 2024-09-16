import requests


'''Создать объект'''


def post_object():
    body = {
            "name": "Apple MacBook Pro 21",
            "data": {
                "year": 2024,
                "price": 4000.95,
                "CPU model": "Intel Core i9",
                "Hard disk size": "10 TB"
            }
    }
    headers = {"content-type": "application/json"}
    req = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers,
    ).json()
    print(req)


'''удалить объект по ID'''


def clear(post_id):
    req = requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
    assert req.status_code == 200, 'Метод удалить объект не отработал'


def get_id(post_id):
    req = requests.get(f'https://api.restful-api.dev/objects/{post_id}')
    assert req.json() == {'error': f'Oject with id={post_id} was not found.'}, 'Запись не удалена'


'''Изменить обхект по ID и удалить после создания'''


def put_object_id():
    post_id = new_post_object()
    body = {
            "name": "Apple MacBook Pro 21",
            "data": {
                "year": 2024,
                "price": 4000.95,
                "CPU model": "Intel Core i9",
                "Hard disk size": "10 TB",
                "color": "red"
            }
    }
    headers = {"content-type": "application/json"}
    req = requests.put(
        f'https://api.restful-api.dev/objects/{post_id}',
        json=body,
        headers=headers,
    ).json()
    print(req)
    clear(post_id)
    get_id(post_id)


'''создать обхект и изменить часть объекта и удалить после выполнения'''


def patch_object_id():
    post_id = new_post_object()
    body = {
        "name": "Жили были"

    }
    headers = {"content-type": "application/json"}
    req = requests.patch(
        f'https://api.restful-api.dev/objects/{post_id}',
        json=body,
        headers=headers,
    ).json()
    print(req)
    clear(post_id)
    get_id(post_id)


'''пред условия для тестирования (функция)'''


def new_post_object():
    body = {
            "name": "Apple MacBook Pro 21",
            "data": {
                "year": 2024,
                "price": 4000.95,
                "CPU model": "Intel Core i9",
                "Hard disk size": "10 TB"
            }
    }
    headers = {"content-type": "application/json"}
    req = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers,
    ).json()
    return req['id']


put_object_id()
patch_object_id()
