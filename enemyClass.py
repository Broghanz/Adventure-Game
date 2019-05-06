import random
import time

player_health = 5

class Enemy:

    def __init__(self, name, strength, defense, health):
        self.name = name
        self.strength = strength
        self.defense = defense
        self.health = health

    def attack_enemy(self):
        time.sleep(1)
        print ("what move would you like to make? (Stab or Smack?")
        print("")
        answer = input.lower()
        if answer == "stab":
            if Sword == True:
                self.health = self.health -     (random.randint(1,3)/(random.uniform(0,1)*     self.defense))
                self.health = int(self.health)
            else:
                print("You cannot stab with a sword you do not have..")
        elif answer == "smack":
            self.health = self.health -   (random.randint(1,3)/(random.uniform(0,1)* self.defense))
            self.health = int(self.health)

        else:
            print("you stumble...")

        time.sleep(1)

        print (self.name + "'s health is now: " + str(int(self.health)))
        print("")

        return int(self.health)

    def enemy_attack(self):
        global player_health
        time.sleep(1)
        print ("The enemy " + self.name + " " + "attacks...")
        print("")
        player_health = player_health - (self.strength * random.uniform(0.1, 1.4))1:41 PM 5/1/2019
        player_health = int(player_health)
        time.sleep(1)
        print ("Your health is now " + str(int(player_health)))
        print ("")
        return int(player_health)

    def battle_script(self):
        global player_health
        print ("An enemy " + self.name + " appears...")
        print ("")
        time.sleep(1)
        while player_health > 0 and self.health > 0:
            self.attack_enemy()
            if self.health <=0:
               break
            self.enemy_attack()
            if player_health <=0:
                break
        if self.health <= 0:
            time.sleep(1)
            print ("You have killed the " + self.name)

        if player_health <= 0:
            time.sleep(1)
            print ("Sorry, you died")


enemies = [Enemy("Boss", 5, 5, 5), Enemy("Tiger", 3, 3, 3), Enemy("Lion", 3, 3, 3)]
random_enemy = random.choice(enemies)
random_enemy.battle_script()
