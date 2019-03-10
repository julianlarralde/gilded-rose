# -*- coding: utf-8 -*-

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def main_program_loop_days(self,days):
        for day in range(days):
            self.main_program()
        print("-------- day %s --------" % (day + 1) )
        print("name, sellIn, quality")
        print(self.items)

    def main_program(self):
        for item in self.items:
            item.process_sell_in()
            item.process_quality()


@property
def x(self):
    print("getter of x called")
    return self._x

class Item:

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

        self.QUALITY_MULTIPLIER_SIGN = -1
        self.QUALITY_MULTIPLIER_VALUE = 1


    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def process_sell_in(self):
        self.sell_in -= 1
        
        if self.sell_in < 0:
                self.process_quality()
    
    def process_quality(self):
        if self.sell_in < 0:
            self.QUALITY_MULTIPLIER_VALUE = 2
            
        if (self.quality > 0 and self.quality < 50):
            self.quality += self.QUALITY_MULTIPLIER_SIGN * self.QUALITY_MULTIPLIER_VALUE

class Brie(Item):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.QUALITY_MULTIPLIER_SIGN = 1
        self.QUALITY_MULTIPLIER_VALUE = 1
    
    def process_quality(self):
        self.quality += self.QUALITY_MULTIPLIER_SIGN * self.QUALITY_MULTIPLIER_VALUE

class Sulfuras(Item):
    def process_quality(self):
        pass
    def process_sell_in(self):
        pass

class Conjured(Item,object):
    def process_quality(self):
        self.QUALITY_MULTIPLIER_VALUE = 2
        super(Conjured, self).process_quality()


class Concert(Item):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.QUALITY_MULTIPLIER_SIGN = 1
        self.QUALITY_MULTIPLIER_VALUE = 1

    def process_quality(self):
                
        if (self.sell_in < 10 and self.sell_in > 5):
            self.QUALITY_MULTIPLIER_VALUE = 2
        elif (self.sell_in <= 5 and self.sell_in > 0):
            self.QUALITY_MULTIPLIER_VALUE = 3
        elif (self.sell_in == 0):
            self.QUALITY_MULTIPLIER_VALUE = 0
        
        if (self.quality >= 0 and self.quality + self.QUALITY_MULTIPLIER_VALUE <= 50):
            self.quality += self.QUALITY_MULTIPLIER_SIGN * self.QUALITY_MULTIPLIER_VALUE
        else:
            self.quality = 50
        
            