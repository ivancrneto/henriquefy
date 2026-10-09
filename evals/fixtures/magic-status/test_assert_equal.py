from unittest import TestCase


class HomeTest(TestCase):
    def test_get(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        self.assertNotEqual(404, resp.status_code)
        self.assertEqual(len(resp.content), 200)
