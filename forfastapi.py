from pydantic import BaseModel, validator, Field
from datetime import date


class Author(BaseModel):
    first_name: str = Field(..., max_length=25)
    last_name: str
    age: int = Field(..., gt=15, lt=90, description='Age 15 <> 90')

    #@validator('age')
    #def check_age(cls, v):
     #   if v < 15 > 90:
      #      raise ValueError('author age must be more than 15')
       # return v


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: str = None


class BookOut(Book):
    id: int



############FOR OOP


class Car:
    PURCHASE_TYPES = ('LEASE', 'CASH')

    __sales_list = None

    @classmethod
    def get_purchase(cls):
        return cls.PURCHASE_TYPES

    @staticmethod
    def get_sales_list():
        if Car.__sales_list == None:
            Car.__sales_list = []
        return Car.__sales_list

    def __init__(self, maker, model, color, price, purchase_type):
        self.maker = maker
        self.model = model
        self.color = color
        self.price = price
        if (not purchase_type in Car.PURCHASE_TYPES):
            raise ValueError(f'{purchase_type} is not a valid purchase type')
        else:
            self.purchase = purchase_type

    def get_price(self):
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def set_discount(self, amount):
        self._discount = amount


class Boat:
    def __init__(self, name):
        self.name = name

car1 = Car('BMW', 'e1312', 'Black', 10806, 'CASH')
car2 = Car('Merz', 'M8', 'Blue', 108000, 'LEASE')

sales_month = Car.get_sales_list()
sales_month.append(car1)
sales_month.append(car2)

print(sales_month)
















class MusicBand():
    def __init__(self, title, label, musican=None):
        self.title = title
        self.label = label

        self.musican = musican

        self.album = []


    def write_album(self, album):
        self.album.append((album))

class Musican():
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f'{self.name} {self.instrument}'


class Album:
    def __init__(self, song, genre):
        self.song = song
        self.genre = genre


band1 = MusicBand('The beats prod', 'Palaroid', 'Palagen')
band1.write_album('CryptoWorld')
band1.write_album('Paranoia')
band1.write_album('Reborn')

print(band1.title, band1.label, band1.musican, band1.album)
