from tests.base import TestBase
from goodreads.book import GoodreadsBook
from goodreads.review import GoodreadsReview


class TestReview(TestBase):

    def setUp(self):
        self.review = self.client.review('5365046')

    def test_recent_reviews(self):
        reviews = self.client.recent_reviews()
        self.assertGreater(len(reviews), 0)
        for r in reviews:
            self.assertIsInstance(r, GoodreadsReview)

    def test_review(self):
        self.assertEqual(self.review.gid, '5365046')

    def test_url(self):
        self.assertEqual(self.review.url, 'https://www.goodreads.com/review/show/5365046')

    def test_book(self):
        keys = [
            'id',
            'isbn',
            'isbn13',
            'text_reviews_count',
            'uri',
            'title',
            'title_without_series',
            'image_url',
            'small_image_url',
            'large_image_url',
            'link',
            'num_pages',
            'format',
            'edition_information',
            'publisher',
            'publication_day',
            'publication_year',
            'publication_month',
            'average_rating',
            'ratings_count',
            'description',
            'authors',
            'published',
            'work'
        ]
        self.assertIsInstance(self.review.book, GoodreadsBook)
        self.assertCountEqual(self.review.book._book_dict.keys(), keys)
        self.assertEqual(self.review.book.isbn, '0345453743')
        self.assertEqual(self.review.book.title, "The Ultimate Hitchhiker's Guide to the Galaxy (Hitchhiker's Guide to the Galaxy, #1-5)")

    def test_rating(self):
        self.assertEqual(self.review.rating, '4')

    def test_shelves(self):
        shelves = [
            'read',
            'humor',
            'scifi',
            'fiction',
            'own',
            'fantasy',
            'recced',
            '2008'
        ]
        self.assertCountEqual(self.review.shelves, shelves)

    def test_recommended_for(self):
        self.assertIsNone(self.review.recommended_for)

    def test_recommended_by(self):
        self.assertEqual(self.review.recommended_by, 'Haley')

    def test_started_at(self):
        self.assertIsNone(self.review.started_at)

    def test_read_at(self):
        self.assertEqual(self.review.read_at, 'Mon Jul 07 00:00:00 -0700 2008')

    def test_body(self):
        self.assertStartsWith(self.review.body, 'Just as funny as advertised,')

    def test_comments_count(self):
        self.assertGreaterEqual(self.review.comments_count, '18')

    def test_owned(self):
        self.assertEqual(self.review.owned, '0')
