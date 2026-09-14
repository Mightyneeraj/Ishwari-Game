import random

# -------------------------------
# Welcome
# -------------------------------

name = input('''
        Hello and welcome to your very own epic RPG game!!
        To start, please enter your name below

:- ''')

# -------------------------------
# Choose Class
# -------------------------------

while True:
    try:
        clas = int(input(f'''
        Alright {name}, now it's time to pick your class!

You have 3 options:

1) Warrior   (balanced character)
2) Mage      (high damage, low health)
3) Tank      (low damage, high health)

To choose a character, enter its number below!

==> '''))

        if clas in [1, 2, 3]:
            break
        else:
            print("Please enter 1, 2, or 3.")

    except ValueError:
        print("Please enter a valid number.")


# -------------------------------
# Character Setup
# -------------------------------

if clas == 1:
    player_class = "Warrior"
    max_health = 100
    damage = 25

elif clas == 2:
    player_class = "Mage"
    max_health = 70
    damage = 40

else:
    player_class = "Tank"
    max_health = 150
    damage = 15


print(f'''
Alright {name}, you have chosen the {player_class} class!
''')

a = input("Are you ready to go on your amazing journey? (yes/no)\n==> ")

if a.lower() != "yes":
    print("Bye, hope to see you soon!")
    exit()

print("\nAlright then, let's start!")

# -------------------------------
# Player
# -------------------------------

player = {
    "name": name,
    "class": player_class,
    "health": max_health,
    "max health": max_health,
    "damage": damage,
    "health potions": 3,
    "damage potions": 1,
    "money": 0
}

print("\nHere's a breakdown of your current inventory:\n")

for x, y in player.items():
    print(f"{x}: {y}")


# -------------------------------
# Main Game Loop
# -------------------------------

while True:

    # Game over
    if player["health"] <= 0:
        print("\n💀 You have died!")
        print(f"You collected ${player['money']} before dying.")
        print("GAME OVER!")
        break

    try:
        b = int(input(f'''
        
Now, {name}, here's a few things you can do:

1) Fight a zombie (earn money)
2) Use a health potion
3) Use a damage potion
4) Open the shop
5) View inventory
6) Quit

==> '''))

    except ValueError:
        print("Please enter a number from 1 to 6.")
        continue


    # -------------------------------
    # Fight Zombie
    # -------------------------------

    if b == 1:

        zombie_health = random.randint(30, 70)
        zombie_damage = random.randint(5, 20)

        print("\n🧟 A zombie appeared!")
        print(f"Zombie HP: {zombie_health}")
        print(f"Your HP: {player['health']}")

        while zombie_health > 0 and player["health"] > 0:

            action = input("""
What do you want to do?

1) Attack
2) Run

==> """)

            if action == "1":

                # Player attacks
                player_damage = random.randint(
                    player["damage"] - 5,
                    player["damage"] + 5
                )

                zombie_health -= player_damage

                print(
                    f"\n⚔️ You attacked the zombie "
                    f"and dealt {player_damage} damage!"
                )

                if zombie_health <= 0:
                    reward = random.randint(20, 50)
                    player["money"] += reward

                    print("\n🎉 You defeated the zombie!")
                    print(f"You earned ${reward}!")
                    print(f"Your money: ${player['money']}")
                    break

                print(f"Zombie HP: {zombie_health}")

                # Zombie attacks
                damage_taken = random.randint(
                    max(1, zombie_damage - 5),
                    zombie_damage + 5
                )

                player["health"] -= damage_taken

                print(
                    f"🧟 The zombie attacked you "
                    f"and dealt {damage_taken} damage!"
                )

                print(f"Your HP: {max(0, player['health'])}")

            elif action == "2":

                print("\n🏃 You ran away from the zombie!")
                break

            else:
                print("Invalid choice!")

    # -------------------------------
    # Health Potion
    # -------------------------------

    elif b == 2:

        if player["health potions"] > 0:

            if player["health"] == player["max health"]:
                print("\nYour health is already full!")
            else:
                player["health"] = player["max health"]
                player["health potions"] -= 1

                print("\n❤️ You used a health potion!")
                print(f"Your health is now {player['health']}.")
                print(
                    f"Health potions remaining: "
                    f"{player['health potions']}"
                )

        else:
            print("\n❌ You don't have any health potions!")

    # -------------------------------
    # Damage Potion
    # -------------------------------

    elif b == 3:

        if player["damage potions"] > 0:

            boost = int(player["damage"] * 0.25)

            player["damage"] += boost
            player["damage potions"] -= 1

            print("\n🔥 You used a damage potion!")
            print(f"Your damage increased by {boost}!")
            print(f"Your new damage: {player['damage']}")
            print(
                f"Damage potions remaining: "
                f"{player['damage potions']}"
            )

        else:
            print("\n❌ You don't have any damage potions!")

    # -------------------------------
    # Shop
    # -------------------------------

    elif b == 4:

        while True:

            print(f'''
            
=============================
          🏪 SHOP
=============================

Your money: ${player["money"]}

1) Health Potion - $30
2) Damage Potion - $50
3) Leave Shop
=============================
''')

            try:
                shop_choice = int(input("==> "))
            except ValueError:
                print("Please enter a number.")
                continue

            # Health potion
            if shop_choice == 1:

                if player["money"] >= 30:

                    player["money"] -= 30
                    player["health potions"] += 1

                    print("\n❤️ You bought a health potion!")

                else:
                    print("\n❌ You don't have enough money!")

            # Damage potion
            elif shop_choice == 2:

                if player["money"] >= 50:

                    player["money"] -= 50
                    player["damage potions"] += 1

                    print("\n🔥 You bought a damage potion!")

                else:
                    print("\n❌ You don't have enough money!")

            # Leave
            elif shop_choice == 3:

                print("\nYou left the shop.")
                break

            else:
                print("\nInvalid choice!")

    # -------------------------------
    # Inventory
    # -------------------------------

    elif b == 5:

        print("\n=============================")
        print("        📦 INVENTORY")
        print("=============================")

        for x, y in player.items():
            print(f"{x}: {y}")

        print("=============================")

    # -------------------------------
    # Quit
    # -------------------------------

    elif b == 6:

        print(f'''
        
Thanks for playing, {name}!

You finished with:
💰 Money: ${player["money"]}
❤️ Health: {max(0, player["health"])}
⚔️ Damage: {player["damage"]}

See you next time! 👋
''')

        break

    else:
        print("\n❌ Invalid option. Please choose a number from 1 to 6.")