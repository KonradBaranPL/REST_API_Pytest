import requests
import pytest


# response = requests.get(f"{BASE_URL}/{ENDPOINT}").json()
# # r = response.json()
# # print(r)
# print(response)


# def test_create_and_delete_board():

endpoint = "boards/"
board_name = "python test board 1"
query_params_post = {
    "name": board_name,
    
}

create_board_response = requests.post(f"{BASE_URL}/{endpoint}")
print(create_board_response.status_code)
    