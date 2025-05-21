# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            if item.name == "Aged Brie":
                self._update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._update_backstage_passes(item)
            elif item.name == "Conjured":
                self._update_conjured_item(item)
            else:
                self._update_regular_item(item)

    def _update_aged_brie(self, item):
        if item.quality < 50:
            item.quality += 1

        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1

    def _update_backstage_passes(self, item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in <= 5 and item.quality < 50:
                item.quality += 2
            elif item.sell_in <= 10 and item.quality < 50:
                item.quality += 1

        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0

    def _update_conjured_item(self, item):
        if item.quality > 0:
            item.quality -= 2

        item.sell_in -= 1
        if item.sell_in < 0 < item.quality:
            item.quality -= 2

    def _update_regular_item(self, item):
        if item.quality > 0:
            item.quality -= 1

        item.sell_in -= 1
        if item.sell_in < 0 < item.quality:
            item.quality -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
