#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
import random

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
    def alive(self):
        alive = True
        if self.health <= 0:
            alive = False
        return alive


class Hero(Character):
    def attack(self, goblin):
        randomNum = random.randrange(10)
        if randomNum < 2:
            goblin.health -= self.power * 2
            print(f"You do {self.power * 2} damage to the {goblin.name}.")
        else:
            goblin.health -= self.power
            print(f"You do {self.power} damage to the {goblin.name}.")
        if goblin.health <= 0:
            print(f"The {goblin.name} is dead.")


    def print_status(self):
        print(f"You have {self.health} health and {self.power} power.")


class Goblin(Character):
    def attack(self, hero):
        hero.health -= self.power
        print(f"The {self.name} does {self.power} damage to you.")
        if hero.health <= 0:
            print("You are dead.")
    def print_status(self):
        print(f"The {self.name} has {self.health} health and {self.power} power.")

class Medic(Goblin):
    def heal(self):
        randomNum = random.randrange(10)
        if randomNum < 2:
            self.health += 2


def main():
    hero = Hero('hero',10, 5)
    goblin = Goblin('goblin', 6, 2)
    medic = Medic('medic', 6, 1)

    while goblin.alive() and hero.alive():
        goblin.print_status()
        hero.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.alive():
            # Goblin attacks hero
            goblin.attack(hero)

    while medic.alive() and hero.alive():
        medic.print_status()
        hero.print_status()
        print()
        print("What do you want to do?")
        print("1. fight medic")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(medic)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if medic.alive():
            # Goblin attacks hero
            goblin.attack(hero)


main()
