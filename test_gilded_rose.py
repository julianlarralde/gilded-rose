# -*- coding: utf-8 -*-
import unittest

from gilded_rose import  GildedRose,Item,Brie,Concert,Sulfuras,Conjured

class GildedRoseTest(unittest.TestCase):
    
    # Default
    def test_default_sell_in(self):
        items = [Item("Default",10,20)]
        gilded_rose = GildedRose(items)
        gilded_rose.main_program_loop_days(4)

        self.assertEqual(6, items[0].sell_in)     
    def test_default_quality(self):
        items = [Item("Default",10,20)]
        gilded_rose = GildedRose(items)
        gilded_rose.main_program_loop_days(4)

        self.assertEqual(16, items[0].quality)

    # Aged Brie
    def test_brie_sell_in(self):
        items = [Brie("Aged Brie",2,0)]
        gilded_rose = GildedRose(items)
        gilded_rose.main_program_loop_days(4)

        self.assertEqual(-2, items[0].sell_in) 
    def test_brie_quality(self):
        items = [Brie("Aged Brie",2,0)]
        gilded_rose = GildedRose(items)
        gilded_rose.main_program_loop_days(4)

        self.assertEqual(6, items[0].quality)

    #   Concert Tickets
    def test_concert_sell_in_1(self):
        items = [Concert("Backstage passes to a TAFKAL80ETC concert",15,20)]
        gilded_rose = GildedRose(items)
        gilded_rose.main_program_loop_days(5)

        self.assertEqual(10, items[0].sell_in)
    def test_concert_quality_1(self):
        items = [Concert("Backstage passes to a TAFKAL80ETC concert",15,20)]
        gilded_rose = GildedRose(items)
        gilded_rose.main_program_loop_days(5)

        self.assertEqual(25, items[0].quality)
    def test_concert_sell_in_2(self):
        items = [Concert("Backstage passes to a TAFKAL80ETC concert",10,49)]
        gilded_rose = GildedRose(items)
        gilded_rose.main_program_loop_days(4)

        self.assertEqual(6, items[0].sell_in)
    def test_concert_quality_2(self):
        items = [Concert("Backstage passes to a TAFKAL80ETC concert",10,49)]
        gilded_rose = GildedRose(items)
        gilded_rose.main_program_loop_days(4)

        self.assertEqual(50, items[0].quality)
    def test_concert_sell_in_3(self):
        items = [Concert("Backstage passes to a TAFKAL80ETC concert",5,49)]
        gilded_rose = GildedRose(items)
        gilded_rose.main_program_loop_days(5)

        self.assertEqual(0, items[0].sell_in)
    def test_concert_quality_3(self):
        items = [Concert("Backstage passes to a TAFKAL80ETC concert",5,49)]
        gilded_rose = GildedRose(items)
        gilded_rose.main_program_loop_days(5)
        self.assertEqual(50, items[0].quality)

    #   Sulfuras
    def test_sulfuras_sell_in_1(self):
        items = [Sulfuras("Sulfuras, Hand of Ragnaros",0,80)]
        gilded_rose = GildedRose(items)
        gilded_rose.main_program_loop_days(4)

        self.assertEqual(0, items[0].sell_in)

    def test_sulfuras_quality_1(self):
        items = [Sulfuras("Sulfuras, Hand of Ragnaros",0,80)]
        gilded_rose = GildedRose(items)
        gilded_rose.main_program_loop_days(4)

        self.assertEqual(80, items[0].quality)

    def test_sulfuras_sell_in_2(self):
        items = [Sulfuras("Sulfuras, Hand of Ragnaros",-1,80)]
        gilded_rose = GildedRose(items)
        gilded_rose.main_program_loop_days(4)

        self.assertEqual(-1, items[0].sell_in)

    def test_sulfuras_quality_2(self):
        items = [Sulfuras("Sulfuras, Hand of Ragnaros",-1,80)]
        gilded_rose = GildedRose(items)
        gilded_rose.main_program_loop_days(4)

        self.assertEqual(80, items[0].quality)
    
    
    # Conjured
    def test_conjured_sell_in(self):
        items = [Conjured("Conjured Mana Cake",3,6)]
        gilded_rose = GildedRose(items)
        gilded_rose.main_program_loop_days(4)

        self.assertEqual(-1, items[0].sell_in)

    def test_conjured_quality(self):
        items = [Conjured("Conjured Mana Cake",3,6)]
        gilded_rose = GildedRose(items)
        gilded_rose.main_program_loop_days(4)

        self.assertEqual(0, items[0].quality)
    

if __name__ == '__main__':
    unittest.main()