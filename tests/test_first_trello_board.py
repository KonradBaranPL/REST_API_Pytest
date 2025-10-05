import requests
import pytest

API_KEY = "18a796421b243fda27700d4e49bbccde"

TOKEN = "ATTAf82e8f88f07b695c04c41009be80d41ccf80a8080cb60844eb6842158b4e054bC85AF46E"

BASE_URL = "https://api.trello.com/1/"



response = requests.get(f"{BASE_URL}/{ENDPOINT}").json()
# r = response.json()
# print(r)
print(response)

def test_create_and_delete_board():

    board_name = "python test board 1"
    pass