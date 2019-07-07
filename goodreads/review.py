"""Class implementation for Goodreads reviews"""
from .book import GoodreadsBook
from datetime import datetime


class GoodreadsReview():
    def __init__(self, review_dict, client):
        self._review_dict = review_dict
        self.client = client

    def __repr__(self):
        return "review [%s]" % self.gid

    @property
    def gid(self):
        """Goodreads id for the review"""
        return self._review_dict['id']

    @property
    def book(self):
        """Book that the review belongs to"""
        return GoodreadsBook(self._review_dict['book'], self.client)

    @property
    def rating(self):
        """Rating of the book"""
        return self._review_dict['rating']

    @property
    def shelves(self):
        """Shelves for the book"""
        try:
            return [shelf['@name']
                    for shelf in self._review_dict['shelves']['shelf']]
        # In some cases it appears the Goodreads API returns a response
        # where 'shelf' object is not a list but rather a single shelf.
        # In this case the Exception "TypeError: string indices must be
        # integers" is raised.
        except TypeError:
            return [self._review_dict['shelves']['shelf']['@name']]

    @property
    def recommended_for(self):
        """Book recommended for"""
        return self._review_dict['recommended_for']

    @property
    def recommended_by(self):
        """Book recommended by"""
        return self._review_dict['recommended_by']

    @property
    def started_at(self):
        """Book started at"""
        return self._review_dict['started_at']

    @property
    def read_at(self):
        """Book read at"""
        return self._review_dict['read_at']

    @property
    def date_added(self):
        """Book added to shelf at"""
        val = self._review_dict['date_added']
        try:
            return datetime.strptime(val, "%a %b %d %H:%M:%S %z %Y")
        except ValueError:
            print("Can't parse date_added value: %s" % val)
            return None

    @property
    def body(self):
        """Body for the review"""
        return self._review_dict['body']

    @property
    def comments_count(self):
        """Number of comments to this review"""
        return self._review_dict['comments_count']

    @property
    def url(self):
        """URL for this comment"""
        return self._review_dict['url']

    @property
    def owned(self):
        """Is the book owned by this user?"""
        return self._review_dict['owned']
