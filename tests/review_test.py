from tests.base import TestBase
from goodreads.review import GoodreadsReview


class TestReview(TestBase):

    def test_recent_reviews(self):
        reviews = self.client.recent_reviews()
        self.assertGreater(len(reviews), 0)
        for r in reviews:
            self.assertIsInstance(r, GoodreadsReview)

    def test_review(self):
        review = self.client.review('2')
        self.assertEqual(review.gid, '2')
