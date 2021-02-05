from django.test import TestCase
from http import HTTPStatus

class AddUserFormTests(TestCase):
    def test_username(self):
        response = self.client.post(
            "/users/registers/", data={"username": "username"}
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(
            response, "Should start with an uppercase letter", html=True
        )

    # def test_title_ending_full_stop(self):
    #     response = self.client.post(
    #         "/books/add/", data={"title": "A stopped title."}
    #     )

    #     self.assertEqual(response.status_code, HTTPStatus.OK)
    #     self.assertContains(
    #         response, "Should not end with a full stop", html=True
    #     )

    # def test_title_with_ampersand(self):
    #     response = self.client.post(
    #         "/books/add/", data={"title": "Dombey & Son"}
    #     )

    #     self.assertEqual(response.status_code, HTTPStatus.OK)
    #     self.assertContains(response, "Use 'and' instead of '&'", html=True)
