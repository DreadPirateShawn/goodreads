from tests.base import TestBase
from goodreads.author import GoodreadsAuthor
from goodreads.book import GoodreadsBook


class TestAuthor(TestBase):

    def setUp(self):
        self.author = self.client.author('64941')

    def test_get_author(self):
        self.assertIsInstance(self.author, GoodreadsAuthor)
        self.assertEqual(self.author.gid, '64941')
        self.assertEqual(repr(self.author), 'Donald Ervin Knuth')

    def test_author_name(self):
        self.assertEqual(self.author.name, 'Donald Ervin Knuth')

    def test_author_about(self):
        self.assertStartsWith(self.author.about, 'Donald Ervin Knuth, born January 10th 1938,')

    def test_author_books(self):
        books = self.author.books
        self.assertGreater(len(books), 0)
        for book in books:
            self.assertIsInstance(book, GoodreadsBook)
        self.assertEqual(books[-1].title, 'Literate Programming')

    def test_born_at(self):
        self.assertEqual(self.author.born_at, '1938/01/10')

    def test_gender(self):
        self.assertEqual(self.author.gender, 'male')

    def test_hometown(self):
        self.assertEqual(self.author.hometown, 'Milwaukee')

    def test_link(self):
        self.assertEqual(self.author.link, 'https://www.goodreads.com/author/show/64941.Donald_Ervin_Knuth')

    def test_image_url(self):
        self.assertEquals(self.author.image_url, 'https://images.gr-assets.com/authors/1236845611p5/64941.jpg')

    def test_small_image_url(self):
        self.assertEquals(self.author.small_image_url, 'https://images.gr-assets.com/authors/1236845611p2/64941.jpg')

    def test_works_count(self):
        self.assertEqual(self.author.works_count, '72')
