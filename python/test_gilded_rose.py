# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    """
    Unit tests for the GildedRose inventory management system.
    These tests cover various scenarios, edge cases for updating the quality and sell_in values of items.
    """

    def test_foo(self):
        """
        Test that an item with a generic name, its sell_in decreased by 1 and its quality remains unchanged at 0.
        """
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].name, "foo")
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 0)

    def test_aged_brie_increases_in_quality(self):
        """
        Test that "Aged Brie" increases in quality as its sell_in decreases.
        """
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 1)
        self.assertEqual(items[0].sell_in, 1)

    def test_aged_brie_quality_does_not_exceed_50(self):
        """
        Test that "Aged Brie" quality does not exceed the maximum value of 50.
        """
        items = [Item("Aged Brie", 2, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_aged_brie_sell_in_0(self):
        """
        Test that "Aged Brie" increases in quality by 2 when sell_in is 0 or less.
        """
        items = [Item("Aged Brie", 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 42)
        self.assertEqual(items[0].sell_in, -1)

    def test_aged_brie_sell_in_0_quality_49(self):
        """
        Test that "Aged Brie" quality does not exceed 50 even when sell_in is 0
        and the quality is close to the maximum.
        """
        items = [Item("Aged Brie", 0, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)
        self.assertEqual(items[0].sell_in, -1)

    def test_backstage_passes_single_increase_in_quality(self):
        """
        Test that "Backstage passes" increase in quality by 1 when there are more than 10 days left.
        """
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 21)

    def test_backstage_passes_increase_by_2_when_10_days_or_less(self):
        """
        Test that "Backstage passes" increase in quality by 2 when there are 10 days or less left.
        """
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 22)

    def test_backstage_passes_increase_by_3_when_5_days_or_less(self):
        """
        Test that "Backstage passes" increase in quality by 3 when there are 5 days or less left.
        """
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 23)

    def test_backstage_passes_quality_drops_to_0_after_concert(self):
        """
        Test that "Backstage passes" quality drops to 0 after the concert (sell_in <= 0).
        """
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_sulfuras_quality_and_sell_in_remain_constant(self):
        """
        Test that "Sulfuras, Hand of Ragnaros" does not change in quality or sell_in with different quality and sell on values
        """
        items = [
            Item("Sulfuras, Hand of Ragnaros", 0, 80),
            Item("Sulfuras, Hand of Ragnaros", 0, 40),
            Item("Sulfuras, Hand of Ragnaros", -1, 50),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[1].quality, 40)
        self.assertEqual(items[1].sell_in, 0)
        self.assertEqual(items[2].quality, 50)
        self.assertEqual(items[2].sell_in, -1)

    def test_regular_item_decreases_in_quality(self):
        """
        Test that a regular item decreases in quality by 1 as its sell_in decreases.
        """
        items = [Item("Regular Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 19)
        self.assertEqual(items[0].sell_in, 9)

    def test_regular_item_quality_decreases_twice_after_sell_in(self):
        """
        Test that a regular item decreases in quality by 2 when sell_in is 0 or less.
        """
        items = [Item("Regular Item", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 18)

    def test_quality_never_negative(self):
        """
        Test that the quality of an item never becomes negative.
        """
        items = [Item("Regular Item", 10, 0), Item("Regular Item", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[1].quality, 0)


if __name__ == "__main__":
    unittest.main()
