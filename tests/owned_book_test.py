from tests.base import TestBase


class TestOwnedBook(TestBase):

    def setUp(self):
        self.owned_book = self.client.owned_book('43018920')

    def test_owned_book(self):
        self.assertEqual(self.owned_book.gid, '43018920')
