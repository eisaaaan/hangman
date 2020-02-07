"""class Apple():
    def __init__(self,color,weight,stem_length,circumference):
        self.color=color
        self.weight=weight
        self.stem__length=stem_length
        self.circumference
        


import math

class Circle():
    def __init__(self,radius):
        self.radius=radius

    def calculate_area(self):
        return self.radius ** 2 * math.pi

a_circle = Circle(4)
print(a_circle.calculate_area())

class Hexagon():
    def __init__(self,s1,s2,s3,s4,s5,s6):
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.s4=s4
        self.s5=s5
        self.s6=s6

    def calclate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

a_hexagon =Hexagon(1,2,3,4,5,6)
print(a_hexagon.calclate_perimeter())


class Rectangle:
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

class Data:
    def __init__(self):
        self.nums = [1,2,3,4,5]

    def change_data(self,index,n):
        self.nums[index] = n

data_one = Data()
data_one.nums[0] =100
print(data_one.nums)

data_two = Data()
data_two.change_data(0,100)
print(data_two.nums)
        
"""


"""
class PublicPrivateExample:
    def __init__(self):
        self.public ="self"
        self._unisafe ="unisafe"

    def public_method(self):
        pass
    def _unisafe_methd(self):
        pass

#    print("HW")
#    print(200)
#    print(299.1)
    
type("HW")
type(222)
type(299.0)
"""




"""
shapes =[tr1,sq1,cr1]
for a_shape in shapes:
    if isinstance(a_shape,Traiangle):
        a_shape.draw_triangle()
    if isinstance(a_shape,Square):
         a_shape.draw_Square()
    if isinstance(a_shape,Circle):         
         a_shape.draw_Circle()

Shapes =[tr1,sw1,cr1]
for a_shape in shapes:
    a_shape.draw()
"""

"""
class Shape:
    def __init__(self,w,l):
        self.width =w
        self.len=l

    def print_size(self):
        print("{}by{}".format(self.width,self.len))

my_shape = Shape(20,25)
my_shape.print_size()
"""
"""
class Shape:
    def __init__(self,w,l):
        self.width =w
        self.len=l

    def print_size(self):
        print("{}by{}".format(self.width,self.len))

class Square(Shape):
    pass

a_square = Square(20,20)
a_square.print_size()

"""
"""
class Shape:
    def __init__(self,w,l):
        self.width =w
        self.len=l

    def print_size(self):
        print("{}by{}".format(self.width,self.len))

class Square(Shape):
    def area(self):
        return self.width*self.len

a_square=Square(20,20)
print(a_square.area())
"""
"""
class Shape:
    def __init__(self,w,l):
        self.width =w
        self.len=l

    def print_size(self):
        print("{}by{}".format(self.width,self.len))

class Square(Shape):
    def area(self):
        return self.width*self.len

    def print_size(self):
        print("I am {}by{}".format(self.width,self.len))

a_square = Square(20,20)
a_square.print_size() 
    
"""
"""
class Dog:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self,name):
        self.name = name

mick =Person("Mick Jagger")
stan =Dog("Stanley","bulldog","mick")
print(stan.owner.name)


#古いPyhon対応上記
"""

"""

class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(25, 50)
a_square = Square(20)

print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())


class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 += new_size

a_square = Square(100)
print(a_square.s1)

a_square.change_size(200)
print(a_square.s1)


class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(20, 50)
a_square = Square(29)

a_rectangle.what_am_i()
a_square.what_am_i()

class Horse():
    def __init__(self, name):
        self.name = name


class Rider():
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

harry_the_horse = Horse("Harry")
the_rider = Rider("Sally", harry_the_horse)

print(the_rider.horse.name)

"""
"""
class Square:
    pass

print(Square)

class Rectangle:
    def __init__(self,w,l):
        self.width =w
        self.len=l

    def print_size(self):
        print("{}by{}".format(self.width,self.len))



my_rectangle =Rectangle(20,34)
my_rectangle.print_size()
"""
from random import shuffle


class Card:
    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"]

    values = [None, None,"2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] +\
            " of " + \
            self.suits[self.suit]
        return v


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards\
                    .append(Card(i,
                                 j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("p1 name ")
        name2 = input("p2 name ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n,
                     p1c,
                     p2n,
                     p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("beginning War!")
        while len(cards) >= 2:
            m = "q to quit. Any " + \
                "key to play:"
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,
                      p1c,
                      p2n,
                      p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1,
                         self.p2)
        print("War is over.{} wins"
              .format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"

game = Game()
game.play_game()
