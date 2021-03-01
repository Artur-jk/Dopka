from random import random, randrange


class Family:

    def __init__(self, name, satiety, happyness):
        self.name = name
        self.satiety = satiety
        self.happyness = happyness

    def eat(self):
        count_products = 0
        a = randrange(1, 30)
        self.satiety += a
        hous.products -= a
        count_products += a


class Husband(Family):

    def play_wot(self):
        self.satiety -= 10
        husband.happyness += 20

    def work(self):
        self.satiety -= 10
        hous.money += 150


class Wife(Family):

    def buy_products(self):
        self.satiety -= 10
        a = randrange(1, hous.money)
        hous.money -= a
        hous.products += a

    def buy_coat(self):
        self.satiety -= 10
        hous.money -= 350
        wife.happyness += 60

    def clean_hous(self):
        self.satiety -= 10
        a = int(input())
        hous.mud -= a


class Hous:

    def __init__(self, money, products, mud):
        self.money = money
        self.products = products
        self.mud = mud


hous = Hous(100, 50, 0)
husband = Husband('John', 30, 100)
wife = Wife('Andy', 30, 100)

print('Hello in Real-life simulator! Choice your hero: Husband or Wife')
player1 = input()
player2 = input()

if player1 == 'Husband'.lower() and player2 == 'Wife'.lower():
    print('Player1 is a Husband', ' Name:', husband.name, ' Satiety:', husband.satiety, 'Happyness: ',
          husband.happyness, )
    print('Player2 is a Wife', ' Name:', wife.name, ' Satiety:', wife.satiety, ' Happyness: ', wife.happyness)
else:
    print('Player1 is a Wife', ' Name:', wife.name, ' Satiety:', wife.satiety, ' Happyness: ', wife.happyness)
    print('Player2 is a Husband', ' Name:', husband.name, ' Satiety:', husband.satiety, 'Happyness: ',
          husband.happyness, )

count_money = 0
count_products = 0
count_coats = 0

day = 1
while day <= 365:
    hous.mud += 5
    if hous.mud >= 90:
        husband.happyness -= 10
        wife.happyness -= 10

    print('Hous resources:', 'Money: ', hous.money, 'Products: ', hous.products, 'Hous mud: ', hous.mud)
    print(husband.name, 'Satiety: ', husband.satiety, 'Happyness: ', husband.happyness)
    print(wife.name, 'Satiety: ', wife.satiety, 'Happyness: ', wife.happyness)
    player1 = input('Husbands turn: eat, work, play: '.lower())
    player2 = input('Wifes turn: eat, buy products, buy coat, clean:  '.lower())
    if player1 == 'eat'.lower():
        husband.eat()
    if player1 == 'work'.lower():
        husband.work()
    if player1 == 'play'.lower():
        husband.play_wot()

    if player2 == 'eat'.lower():
        wife.eat()
    if player2 == 'buy products'.lower():
        wife.buy_products()
    if player2 == 'buy coat'.lower():
        wife.buy_coat()
    if player2 == 'clean'.lower():
        wife.clean_hous()

    if husband.satiety or wife.satiety <= 10:
        print('You are very hungry! You should eat or you can die!')

    if husband.happyness or wife.happyness <= 10:
        print('You are so unhappy! You should care about this, or you can die!')

    if wife.buy_coat():
        count_coats += 1

    if husband.work():
        count_money += 150

print('Statistics: eaten products: ', count_products, 'bought coats: ', count_coats, 'earned money: ', count_money)
