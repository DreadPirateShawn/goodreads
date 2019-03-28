from tests.base import TestBase
from goodreads import apikey
from goodreads.book import GoodreadsBook


class TestClient(TestBase):

    def test_client_setup(self):
        self.assertEqual(self.client.client_key, apikey.key)
        self.assertEqual(self.client.client_secret, apikey.secret)

    def test_auth_user(self):
        user = self.client.auth_user()
        self.assertEqual(user.user_name, 'DreadPirateShawn')

    def test_user_info(self):
        user = self.client.user(1)
        self.assertEqual(user.user_name, 'otis')

    def test_author_by_id(self):
        author_id = '8566992'
        author = self.client.author(author_id)
        self.assertEqual(author.gid, author_id)

    def test_author_by_name(self):
        author_name = 'Richard Dawkins'
        author = self.client.find_author(author_name)
        self.assertEqual(author.name, author_name)

    def test_book_by_id(self):
        book_id = '11870085'
        book = self.client.book(book_id)
        self.assertEqual(book.gid, book_id)

    def test_search_books(self):
        books = self.client.search_books("The selfish gene")
        self.assertGreater(len(books), 0)
        for book in books:
            self.assertIsInstance(book, GoodreadsBook)

    def test_group_by_id(self):
        group_id = '1'
        group = self.client.group(group_id)
        self.assertEqual(group.gid, group_id)
