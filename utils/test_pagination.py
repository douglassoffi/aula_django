from unittest import TestCase
from pagination import make_pagination_range

class PaginationTest(TestCase):
    def test_pagination_range_returns_pagination_tes(self):
        pagination = make_pagination_range(
            page_range=list(range(1,21)),
            qty_pages=5,
            current_page=1
            )
        self.assertEqual([0, 1, 2, 3, 4], pagination) 