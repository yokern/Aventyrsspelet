import random

class Player():
    def __init__(self, lvl, hp, strength, inv):
        self.lvl = lvl
        self.hp =  hp
        self.strength = strength
        self.inv = inv
    
    def print_inventory(self):
        for item in self.inv:
            print(item.name)
   
class Item():
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

def door(player):
    door_type = random.choice(["Treasure", "Trap", "Monster"]) 
    if door_type == "Treasure":
        random_treasure = random.choice(list_of_items)
        print(f"You received a {random_treasure.name}.") 
        print(f"This item has a strength of {random_treasure.strength}.\n")
        if len(player.inv) < 5:
            player.inv.append(random_treasure)
            player.strength = player.strength + random_treasure.strength
        elif len(player.inv) >= 5:
            print("Your inventory is full, would you like to exchange it for one of your weakest sword?)")
            print()
            print("Your inventory right now:")
            player.print_inventory()
            print()
            while True:
                exchange = input("Type: Y/N (Y for Yes, N for No) ")
                print()
                if exchange == "Y": 
                    item_exchange(player)
                    player.inv.append(random_treasure)
                    player.strength = player.strength + random_treasure.strength
                    break
                elif exchange == "N":  
                    print("You left the treasure and countinued your journey")
                    break
                else:
                    print("You need to type Y or N (Y for Yes, N for No)")
                    print()

    elif door_type == "Trap":
        trap_damage = random.randint(66666,66666666)
        player.hp = player.hp - trap_damage
        print("You encountered a trap")
        print(f"The trap dealt {trap_damage} damage\n")
    elif door_type == "Monster":
        monster_strength = random.randint(1, 80)
        print(f"The monster has a strength of {monster_strength}")
        if monster_strength > player.strength:
            player.hp = player.hp - 1
            print("The monster won the battle and you lost 1 hp\n")
        elif monster_strength < player.strength:
            player.lvl = player.lvl + 1
            print("You won the battle against the monster")
            print("Your level went up by one point")
            print()

diamond_sword = Item("Diamond sword", 25)
iron_sword = Item("Iron sword", 20)
gold_sword = Item("Gold sword", 15)
stone_sword = Item("Stone sword", 10)
wooden_sword = Item("Wooden sword", 5)

list_of_items = [diamond_sword, iron_sword, gold_sword, stone_sword, wooden_sword]

def item_exchange(player):
    worst = Item("", 100)
    for item in player.inv:
        if worst.strength > item.strength:
            worst = item
    player.inv.remove(worst)
              
def start_game():
    player = Player(1,25,0,[])
    while player.lvl < 10: #Checka om man så man inte vunnit
        if player.hp <= 0: #Checka om man är död
            print("You died")
            while True:
                play_again = input("DO YOU WANT TO PLAY AGAIN? Y/N: ")
                print()
                if play_again == "Y":
                    start_game()
                elif play_again == "N":
                    print ("See you next time!")
                    exit()
                else:
                    print("You need to type Y or N (Y for Yes, N for No):")  
                    print()
        choice = input("What would you like to do?\nA: Check your stats\nB: Pick your door\nC: Check your inventory\n\nYOUR CHOICE: ")
        if choice == "A":
            print()
            print("YOUR STATS:")  
            print(f"\nCurrent Level: {player.lvl}\nYour HP: {player.hp}\nStrength: {player.strength}\n")
        elif choice == "B":
            print()
            door(player)
        elif choice == "C":
            print()
            print("YOUR INVENTORY:\n--------------")  
            player.print_inventory()
            print()
        else:
            print()
            print("Please type either A, B or C\n")
    else:
        print("Congratulations, you won!")
        while True:
            play_again = input("DO YOU WANT TO PLAY AGAIN? Y/N: ")
            print()
            if play_again == "Y":
                start_game()
            elif play_again == "N":
                print ("See you next time!")
                exit()
            else:
                print("You need to type Y or N (Y for Yes, N for No):")
                print()

start_game() 