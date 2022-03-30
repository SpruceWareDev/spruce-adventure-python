import time
import sys
import random

def print_logo():
    print("""
  _____                              ___      _                 _                  
/  ___|                            / _ \    | |               | |                 
\ `--. _ __  _ __ _   _  ___ ___  / /_\ \ __| |_   _____ _ __ | |_ _   _ _ __ ___ 
 `--. \ '_ \| '__| | | |/ __/ _ \ |  _  |/ _` \ \ / / _ \ '_ \| __| | | | '__/ _ \\
/\__/ / |_) | |  | |_| | (_|  __/ | | | | (_| |\ V /  __/ | | | |_| |_| | | |  __/
\____/| .__/|_|   \__,_|\___\___| \_| |_/\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|
      | |                                                                         
      |_|                                                                         
    """)

#handles menu and starting the game
def handle_menu():
    menu_items = ["[1]Play", "[2]Exit"]
    for item in menu_items:
        decoration = "*-*-"
        print((decoration * 9) + "* " + item + " " + (decoration * 9) + "*")

    option = input("Select an option: ")
    if option == "1":
        game_loop()
    elif option == "2":
        print("Exiting...")
        time.sleep(1)
        exit()

#cool typing effect i made :D
def typing_effect(text, delay):
    for char in text:
        time.sleep(delay)
        sys.stdout.write(char)
        sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.flush()

#main game loop
def game_loop():
    typing_effect("Starting game...", 0.05)

    typing_effect("Enter your players name: ", 0.05)
    playerName = input("> ")

    #inits player
    player = Player(playerName, 100)

    typing_effect("Welcome " + player.name + "!", 0.05)
    print()

    #tutorial
    typing_effect("Now the tutorial begins!", 0.05)
    tutorial(player)

#tutorial function
def tutorial(player):
    print()
    typing_effect("You have " + str(player.health) + " health.", 0.05)
    print()
    typing_effect("Try to preserve this health as best as you can while fighting enemies.", 0.05)
    typing_effect("...", 0.4)
    typing_effect("You will face enemies that you can attack, taunt or escape.", 0.05)
    typing_effect("...", 0.4)
    typing_effect("You can attack an enemy by typing 'attack'", 0.05)
    typing_effect("You can taunt an enemy by typing 'taunt'", 0.05)
    typing_effect("You can escape from an enemy by typing 'escape'", 0.05)
    typing_effect("...", 0.4)
    typing_effect("You will be given a random enemy to fight. Try and defeat it!", 0.05)
    typing_effect("...", 0.4)
    print()
    random_enemy_cutseen(player)
    
#random enemy generator
def random_enemy_cutseen(player):
    #random enemy generator
    enemy = Enemy("Tutorial enemy")
    enemy.set_enemy_type()

    typing_effect("You have encountered a " + enemy.enemyType + "!", 0.05)
    typing_effect("It has " + str(enemy.health) + " health.", 0.05)

    typing_effect("You can attack, taunt or escape.", 0.05)
    typing_effect("...", 0.4)

    fighting = True

    while fighting:
        playerOption = input("What do you want to do? [attack/taunt/escape]: ")
        if playerOption == "attack":
            damageDone = player.attack_enemy(enemy)
            print()
            typing_effect("You did " + str(damageDone) + " damage to the enemy.", 0.05)
            typing_effect("The enemy has " + str(enemy.health) + " health left.", 0.05)
            typing_effect("...", 0.4)
            if enemy.health <= 0:
                typing_effect("You have defeated the enemy!", 0.05)
                fighting = False
            else:
                fightBack = random.randint(0, 2)
                if fightBack == 0:
                    #enemy fights back
                    enemyDamageDone = enemy.attack_player(player)
                    typing_effect("The enemy has attacked you and did " + str(enemyDamageDone) + " damage!", 0.05)
                    typing_effect("You have " + str(player.health) + " health left.", 0.05)
                    typing_effect("...", 0.4)
                    if player.health <= 0:
                        player.death()
                elif fightBack == 1:
                    typing_effect("The enemy takes the hit!", 0.05)
                    typing_effect("...", 0.4)
                elif fightBack == 2:
                    typing_effect("The enemy has fled!", 0.05)
                    typing_effect("...", 0.4)
                    fighting = False
        elif playerOption == "taunt":
            typing_effect("You taunted the enemy!", 0.05)
            typing_effect("...", 0.4)
            print(enemy.get_random_taunt_response())
            typing_effect("...", 0.4)
        
        elif playerOption == "escape":
            typing_effect("You escaped from the enemy with " + str(player.health) + " health left!", 0.05)
            typing_effect("...", 0.4)
            fighting = False
    print()
    typing_effect("The battle has ended!", 0.05)


#player class
class Player():
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.inventory = []

    def attack_enemy(self, enemy):
        damage = random.randint(10,20)
        enemy.health -= damage
        return damage

    def death(self):
        print("You have died!")
        time.sleep(1)
        exit()    


#enemy class
class Enemy():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.enemyTypes = ["goblin", "orc", "troll", "dragon"]
        self.tauntResponses = ["The enemy rolls it eyes.", "The enemy looks at you angrily.", "The enemy ignores your taunt.", "'Oh really?'"]
        self.enemyType = None

    def set_enemy_type(self):
        self.enemyType = random.choice(self.enemyTypes)
        if self.enemyType == "goblin":
            self.health = random.randint(50, 100)
        elif self.enemyType == "orc":
            self.health = random.randint(100, 150)
        elif self.enemyType == "troll":
            self.health = random.randint(150, 200)
        elif self.enemyType == "dragon":
            self.health = random.randint(200, 250)

    def attack_player(self, player):
        damage = random.randint(10,20)
        player.health -= damage
        return damage

    def get_random_taunt_response(self):
        return random.choice(self.tauntResponses)    


#run code :3
print_logo()
handle_menu()