import unittest
import requests

import validators as v
from config import Config


class TestPetstorePetEndPoint(unittest.TestCase):

    def setUp(self) -> None:
        requests.post(
            url=Config.URL,
            data=Config.DATA,
            headers=Config.HEADERS
        )

    def tearDown(self) -> None:
        requests.delete(
            url=Config.URL + str(Config.DATA["id"]),
            headers=Config.HEADERS
        )

    def test_can_post_new_pet(self):
        """New pet adds at the setUp function"""
        status, response = v.get_pet_by_id()
        self.assertEqual(status, 200)
        self.assertEqual(response["id"], 100200300)

    def test_find_pets_by_status(self):
        status, response = v.send_request_for_pets_with_status("sold")
        self.assertEqual(status, 200)
        for i in response['__root__']:
            self.assertEqual(i['status'], 'sold')

    def test_can_get_pet_by_id(self):
        status, response = v.get_pet_by_id()
        self.assertEqual(status, 200)
        self.assertEqual(response["id"], 100200300)
