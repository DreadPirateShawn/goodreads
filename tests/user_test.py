from tests.base import TestBase
from goodreads.user import GoodreadsUser
from goodreads.group import GoodreadsGroup
from goodreads.owned_book import GoodreadsOwnedBook
from goodreads.review import GoodreadsReview
from goodreads.shelf import GoodreadsShelf


class TestUser(TestBase):

    def setUp(self):
        self.user = self.client.user('1')

    def test_get_user(self):
        self.assertIsInstance(self.user, GoodreadsUser)
        self.assertEqual(self.user.gid, '1')

    def test_user_name(self):
        self.assertEqual(self.user.user_name, 'otis')

    def test_name(self):
        self.assertEqual(self.user.name, 'Otis Chandler')

    def test_link(self):
        self.assertEqual(self.user.link, 'https://www.goodreads.com/user/show/1-otis-chandler')

    def test_image_url(self):
        self.assertEqual(self.user.image_url, 'https://images.gr-assets.com/users/1506617226p3/1.jpg')

    def test_small_image_url(self):
        self.assertEqual(self.user.small_image_url, 'https://images.gr-assets.com/users/1506617226p2/1.jpg')

    def test_user_in_groups(self):
        groups = self.user.list_groups()
        self.assertGreater(len(groups), 0)
        for group in groups:
            self.assertIsInstance(group, GoodreadsGroup)

    def test_user_not_in_any_group(self):
        user = self.client.user('25044452')  # A user with no joined groups
        self.assertEqual(user.list_groups(), [])

    def test_user_own_books(self):
        owned_books = self.user.owned_books()
        self.assertGreater(len(owned_books), 0)
        for book in owned_books:
            self.assertIsInstance(book, GoodreadsOwnedBook)

    def test_reviews(self):
        reviews = self.user.reviews()
        self.assertGreater(len(reviews), 0)
        for review in reviews:
            self.assertIsInstance(review, GoodreadsReview)

    def test_shelves(self):
        shelves = self.user.shelves()
        self.assertGreater(len(shelves), 0)
        for shelf in shelves:
            self.assertIsInstance(shelf, GoodreadsShelf)
