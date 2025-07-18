import data
import sender_stand_request


def get_kit_body(kit_name):
    concurrent_body = data.kit_body.copy()
    concurrent_body["firstName"] = kit_name
    return concurrent_body

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

def test_crear_1_kit_con_nombre_de_6_letras():
    new_kit_body = get_kit_body("Ramses")
    positive_assert(new_kit_body)

def test_crear_1_kit_con_nombre_de_511_letras():
    new_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(new_kit_body)

def test_crear_1_kit_con_nombre_de_0_letras():
    empty_name = " "
    new_kit_body = get_kit_body(empty_name)
    negative_assert_code_400(new_kit_body)

def test_crear_1_kit_nombre_512_caracteres():
    new_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(new_kit_body)

def test_crear_1_kit_nombre_de_caracteres_especiales():
    special_char_name = "№%@*$"
    new_kit_body = get_kit_body(special_char_name)
    positive_assert(new_kit_body)

def test_crear_1_kit_nombre_con_espacios():
    name_with_spaces = " A Aaa "
    new_kit_body = get_kit_body(name_with_spaces)
    positive_assert(new_kit_body)

def test_crear_1_kit_nombre_con_numeros():
    new_kit_body = get_kit_body(123)
    negative_assert_code_400(new_kit_body)

def test_crear_kit_sin_parametro_nombre():
    new_kit_body = get_kit_body(None)
    negative_assert_code_400(new_kit_body)

def test_crear_kit_nombre_tipo_incorrecto_numero():
    incorrect_type_name = 123
    new_kit_body = get_kit_body(incorrect_type_name)
    negative_assert_code_400(new_kit_body)