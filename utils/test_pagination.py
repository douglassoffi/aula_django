from unittest import TestCase
from pagination import make_pagination_range

class PaginationTest(TestCase):
    def test_pagination_range_returns_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1,21)),
            qty_pages=4,
            current_page=1
            )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination) 

    def test_change_range_when_current_page_is_greater_than_middle_page(self):
        pagination = make_pagination_range(
            page_range=list(range(1,21)),
            qty_pages=4,
            current_page=5
            )['pagination']
        self.assertEqual([4, 5, 6, 7], pagination)

    def test_change_range_when_last_page_is_equal_or_greater_than_total_pages(self):
        pagination = make_pagination_range(
            page_range=list(range(1,21)),
            qty_pages=4,
            current_page=20
            )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)
