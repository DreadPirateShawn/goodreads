import collections
from tests.base import TestBase
from goodreads.book import GoodreadsBook
from goodreads.author import GoodreadsAuthor
from goodreads.shelf import GoodreadsShelf


class TestBook(TestBase):

    def setUp(self):
        self.book = self.client.book('17118893')

    def test_get_book(self):
        self.assertIsInstance(self.book, GoodreadsBook)
        self.assertEqual(self.book.gid, '17118893')
        self.assertEqual(repr(self.book), 'The Fault in Our Stars')

    def test_title(self):
        self.assertEqual(self.book.title, 'The Fault in Our Stars')

    def test_authors(self):
        self.assertEqual(len(self.book.authors), 1)
        self.assertIsInstance(self.book.authors[0], GoodreadsAuthor)

    def test_description(self):
        self.assertStartsWith(self.book.description, "Despite the tumor-shrinking medical miracle")

    def test_average_rating(self):
        rating = float(self.book.average_rating)
        self.assertGreaterEqual(rating, 1.0)
        self.assertLessEqual(rating, 5.0)

    def test_rating_dist(self):
        self.assertStartsWith(self.book.rating_dist, '5:')

    def test_ratings_count(self):
        self.assertIsDigit(self.book.ratings_count)

    def test_text_reviews_count(self):
        self.assertIsDigit(self.book.text_reviews_count)

    def test_num_pages(self):
        self.assertIsDigit(self.book.num_pages)

    def test_popular_shelves(self):
        self.assertGreater(len(self.book.popular_shelves), 0)
        self.assertTrue('to-read' in self.book.popular_shelves)
        for shelf in self.book.popular_shelves:
            self.assertIsInstance(shelf, str)

    def test_work(self):
        self.assertEqual(type(self.book.work), collections.OrderedDict)
        self.assertEqual(self.book.work['id']['#text'], '16827462')

    def test_series_works(self):
        self.assertIsNone(self.book.series_works)

    def test_publication_date(self):
        self.assertEqual(self.book.publication_date, ('1', '3', '2013'))

    def test_publisher(self):
        self.assertEqual(self.book.publisher, 'Penguin Books')

    def test_language_code(self):
        self.assertEqual(self.book.language_code, 'eng')

    def test_edition_information(self):
        self.assertIsNone(self.book.edition_information)

    def test_image_url(self):
        self.assertEquals(self.book.image_url, 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1356100942i/17118893._SX98_.jpg')

    def test_small_image_url(self):
        self.assertEquals(self.book.small_image_url, 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1356100942i/17118893._SY75_.jpg')

    def test_is_ebook(self):
        self.assertEqual(self.book.is_ebook, 'false')

    def test_format(self):
        self.assertEqual(self.book.format, 'Paperback')

    def test_isbn(self):
        self.assertEqual(self.book.isbn, '0141345659')

    def test_isbn13(self):
        self.assertEqual(self.book.isbn13, '9780141345659')

    def test_link(self):
        self.assertEqual(self.book.link, 'https://www.goodreads.com/book/show/17118893-the-fault-in-our-stars')

    def test_reviews_widget(self):
        self.assertStartsWith(self.book.reviews_widget, '<style>')
        self.assertEndsWith(self.book.reviews_widget, '</div>')

    def test_similar_books(self):
        self.assertGreater(len(self.book.similar_books), 0)
        for b in self.book.similar_books:
            self.assertIsInstance(b, GoodreadsBook)
