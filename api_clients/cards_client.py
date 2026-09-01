"""Module for interaction with "cards/" endpoint of Trello API."""

from api_clients.base_client import BaseClient


class CardClient(BaseClient):
    """Class for interaction with "cards/" endpoint of Trello API."""

    def __init__(self):
        """Initialize CardsClient and set the endpoint to 'boards/'."""
        super().__init__()
        self.endpoint = "cards/"


    def create_card(self):
        """Create a new card on a list"""
        pass

    def get_card(self):
        """Get details about a specific single card"""
        pass

    def update_card(self):
        pass

    def delete_card(self):
        pass

    def get_list(self):
        pass

    def add_comment(self):
        pass

    def delete_comment(self):
        pass

    def create_label(self):
        pass

    def remove_label(self):
        pass