"""Positive tests for 'boards/' endpoint of Trello API, covering basic CRUD operations."""


def test_create_and_delete_board(boards_client):
    """User can create a new board and delete it"""
    name = boards_client.unique_board_name()
    response = boards_client.create_board(name)
    assert response.status_code == 200, (
        f"Expected response status code 200 when creating a board, got {response.status_code}"
    )
    response_body = response.json()
    assert response_body["name"] == name, (
        f"Expected board name to be {name}, got {response_body["name"]}"
    )
    board_id = response_body["id"]
    delete_response = boards_client.delete_board(board_id)
    assert delete_response.status_code == 200, (
        f"Expected response status code 200 when deleting a board, got {delete_response.status_code}"
    )


def test_delete_board(boards_client, board_to_delete):
    """User can delete existing board"""
    board_id = board_to_delete
    response = boards_client.delete_board(board_id)
    assert response.status_code == 200, (
        f"Expected response status code 200 when deleting a board, got {response.status_code}"
    )
    response_get = boards_client.get_board(board_id)
    assert response_get.status_code == 404, (
        f"Expected response status code 404 when trying to get deleted board, got {response_get.status_code}"
    )


def test_update_board_name(boards_client, temp_board):
    """User can update an existing board by id"""
    board_id = temp_board
    new_name = f"updated_{boards_client.unique_board_name()}"
    response = boards_client.update_board(board_id, name=new_name)
    assert response.status_code == 200, (
        f"Expected status code 200 when updating the board, got {response.status_code}"
    )
    response_body = response.json()
    assert response_body["name"] == new_name, (
        f"Expected board name after update to be {new_name}, got {response_body["name"]}"
    )
