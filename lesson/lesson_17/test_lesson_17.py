from lesson.lesson_17.lesson_17_pet_api import create_pet, list_pet, rename_pet, delete_pet

def test_create_pet():
    response = create_pet()

    assert response.status_code == 200
    assert response.json()["name"] == "Tishka"


def test_list_pet():
    response = create_pet()
    pet_id = response.json()["id"]
    response = list_pet(pet_id)

    assert response.json()["id"] == pet_id

def test_rename_pet():
    response = create_pet()
    pet_name = response.json()["name"]
    response = rename_pet()

    assert response.json()["name"] != pet_name

def test_delete_pet():
    response = create_pet()
    pet_id = response.json()["id"]
    response = delete_pet(pet_id)
    response = list_pet(pet_id)

    assert response.status_code == 404


