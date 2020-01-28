#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
import random

class Character:
    def __init__(self, name, health, power, coins, armor):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins
        self.armor = armor
    
    def alive(self):
        alive = True
        if self.health <= 0 and self.name != 'zombie':
            alive = False
        return alive


class Hero(Character):

    def attack(self, enemy):
        randomNum = random.randrange(10)
        if randomNum < 2:
            enemy.health -= self.power * 2
            print(f"You do {self.power * 2} damage to the {enemy.name}.")
        else:
            enemy.health -= self.power
            print(f"You do {self.power} damage to the {enemy.name}.")
        if enemy.name != 'zombie':
            if enemy.health <= 0:
                print(f"The {enemy.name} is dead.")
                self.coins += enemy.coins


    def print_status(self):
        print(f"You have {self.health} health and {self.power} power.")


    def shadow(self, enemy):
        randomNum = random.randrange(10)
        if randomNum < 1:
            self.attack(enemy)

    def buy(self, item):
        self.coins -= item.cost

class Enemy(Character):
    def attack(self, hero):
        hero.health -= (self.power - hero.armor)
        print(f"The {self.name} does {self.power} damage to you.")
        if hero.health <= 0:
            print("You are dead.")
    def print_status(self):
        print(f"The {self.name} has {self.health} health and {self.power} power.")

    def heal(self):
        if self.name == 'medic':
            randomNum = random.randrange(10)
            if randomNum < 2:
                self.health += 2
                print(f'The medic healed and now has {self.health} health.')

class Tonic():
    def __init__(self, cost):
        self.cost = cost
        self.name = "Tonic"

    def bought(self, hero):
        hero.health = 10
        print("You have been restored to 10 health")

class Armor():
    def __init__(self, cost):
        self.cost = cost
        self.name = 'Armor'

    def bought(self, hero):
        hero.armor += 2
        print(f"Your armor is now {hero.armor}")


class Store(object):

    # If you define a variable in the scope of a class:

    # This is a class variable and you can access it like

    # Store.items => [Tonic, Sword]
    tonic = Tonic(3)
    armor = Armor(3)

    items = [tonic, armor]

    def do_shopping(self, hero):

        while True:

            print("=====================")

            print("Welcome to the store!")

            print("=====================")

            print(f"You have {hero.coins} coins.")

            print("What do you want to do?")

            for i in range(len(self.items)):

                item = self.items[i]

                print(f"{i + 1}. buy {item.name} ({item.cost})")

            print("10. leave")

            response = int(input("> "))

            if response == 10:

                break

            else:

                itemBought = self.items[response - 1]

                itemBought.bought(hero)

                hero.buy(self.items[response-1])


def main():
    hero = Hero('hero',10, 5, 0, 0)
    goblin = Enemy('goblin', 6, 2, 5, 0)
    medic = Enemy('medic', 6, 1, 3, 0)
    zombie = Enemy('zombie', 4, 1, 10, 0)
    shadow = Enemy('shadow', 1, 1, 15, 0)
    store = Store()

    def fighting(hero, enemy):
        while enemy.alive() and hero.alive():
            enemy.print_status()
            hero.print_status()
            print()
            print("What do you want to do?")
            print(f"1. fight {enemy.name}")
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')
            raw_input = input()
            if raw_input == "1":
                # Hero attacks enemy
                if enemy.name == 'shadow':
                    hero.shadow(enemy)
                else:
                    hero.attack(enemy)
            elif raw_input == "2":
                pass
            elif raw_input == "3":
                print("Goodbye.")
                break
            else:
                print("Invalid input {}".format(raw_input))

            if enemy.alive():
                # enemy attacks hero
                enemy.attack(hero)
                enemy.heal()

    fighting(hero, goblin)
    store.do_shopping(hero)
    fighting(hero, medic)
    store.do_shopping(hero)
    fighting(hero, zombie)
    store.do_shopping(hero)
    fighting(hero, shadow)


main()
