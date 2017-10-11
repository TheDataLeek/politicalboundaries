import politicalboundaries
import pytest
import numpy as np


class TestMask(object):
    @pytest.fixture
    def mask(self):
        return politicalboundaries.Mask()

    def test_parse(self, mask):
        mask.parse_list([[1, 0, 0],
                         [1, 0, 0],
                         [0, 0, 0]])
        mask.parse_list([[1, 0, 0],
                         [0, 0, 0]])

    def test_valid(self, mask):
        mask.parse_list([[1, 0, 0],
                         [1, 0, 0],
                         [0, 0, 0]])
        assert mask.is_valid is True
        mask.parse_list([[1, 0, 0],
                         [0, 0, 0]])
        assert mask.is_valid is True
        mask.parse_list([[1, 0, 0],
                         [1, 0, 0],
                         [0, 0, 1]])
        assert mask.is_valid is False
        mask.parse_list([[1, 0, 0],
                         [1, 0, 1],
                         [0, 0, 1]])
        assert mask.is_valid is False
        mask.parse_list([[1, 0, 0],
                         [1, 1, 1],
                         [0, 0, 1]])
        assert mask.is_valid is True
        mask.parse_list([[1, 1, 0],
                         [0, 1, 1]])
        assert mask.is_valid is True

    def test_overlap(self, mask):
        mask.parse_list([[1, 0, 0],
                         [1, 1, 1],
                         [0, 0, 1]])
        mask0 = politicalboundaries.Mask()
        mask0.parse_list([[0, 0, 0],
                          [0, 1, 1],
                          [0, 0, 0]])
        assert mask.overlap(mask0) is True
        mask0.parse_list([[0, 0, 0],
                          [0, 0, 0],
                          [1, 1, 0]])
        assert mask.overlap(mask0) is False

    def test_parse_locations(self, mask):
        mask.parse_locations(3, 3, [[0, 0], [1, 1], [1, 0]])
        mask0 = politicalboundaries.Mask()
        mask0.parse_list([[1, 0, 0],
                          [1, 1, 0],
                          [0, 0, 0]])
        assert mask.overlap(mask0) is True

    def test_make_valid(self, mask):
        mask.parse_list([[1, 0, 0],
                         [1, 0, 1],
                         [1, 0, 1]])
        mask.make_valid()
        mask0 = politicalboundaries.Mask()
        mask0.parse_list([[0, 0, 0],
                          [0, 0, 1],
                          [0, 0, 1]])
        mask1 = politicalboundaries.Mask()
        mask1.parse_list([[1, 0, 0],
                          [1, 0, 0],
                          [1, 0, 0]])
        assert mask.overlap(mask0) or mask.overlap(mask1)

        mask.parse_list([[1, 0, 1],
                         [0, 0, 0],
                         [1, 0, 1]])
        mask.make_valid()
        mask0 = politicalboundaries.Mask()
        mask0.parse_list([[0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 1]])
        mask1 = politicalboundaries.Mask()
        mask1.parse_list([[1, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]])
        mask2 = politicalboundaries.Mask()
        mask2.parse_list([[0, 0, 0],
                          [0, 0, 0],
                          [1, 0, 0]])
        mask3 = politicalboundaries.Mask()
        mask3.parse_list([[0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 1]])
        assert (mask.overlap(mask0) or mask.overlap(mask1)
                or mask.overlap(mask2) or mask.overlap(mask3))
