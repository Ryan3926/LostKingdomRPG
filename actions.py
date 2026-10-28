def fight(player, monster):
    print("\nA battle begins against", monster["name"] + "!")
    print("Type A to attack, P to use a potion, or R to run.")

    while monster["health"] > 0 and player["health"] > 0:
        print("\nYour health:", player["health"], "|", monster["name"], "health:", monster["health"])
        action = input("(A/P/R) > ").strip().lower()

        if action == "a":
            damage = player["attack"] + player["weapon_bonus"]
            monster["health"] -= damage
            print("You deal", damage, "damage.")
            if monster["health"] <= 0:
                print("You defeated", monster["name"] + "!")
                print("You earned", monster["reward"], "gold.")
                player["gold"] += monster["reward"]
                return True
        elif action == "p":
            used = False
            for index, item in enumerate(player["inventory"]):
                if item["type"] == "potion":
                    old_health = player["health"]
                    player["health"] = min(player["max_health"], player["health"] + item["heal"])
                    print("You healed", player["health"] - old_health, "health.")
                    player["inventory"].pop(index)
                    used = True
                    break
            if not used:
                print("You have no potions.")
                continue
        elif action == "r":
            print("You escaped. The monster remains where it was.")
            return True
        else:
            print("Please enter A, P, or R.")
            continue

        if monster["health"] > 0:
            player["health"] -= monster["attack"]
            print(monster["name"], "hits you for", monster["attack"], "damage.")

    return player["health"] > 0


def talk_to_npc(player):
    print("\nElder: The Shadow Dragon threatens our kingdom.")
    if player["quest"]["completed"]:
        print("Elder: You have saved us. Your name will be remembered!")
    elif not player["quest"]["accepted"]:
        answer = input("Will you collect 3 moon crystals and defeat the dragon? (y/n) ").strip().lower()
        if answer == "y":
            player["quest"]["accepted"] = True
            print("Quest accepted!")
        else:
            print("Elder: Return when you are ready.")
    else:
        print("Elder: You have", player["quest"]["crystals"], "of 3 moon crystals.")
        if player["quest"]["crystals"] >= 3:
            print("The ruins are open. Defeat the Shadow Dragon!")
        else:
            print("Search the forest for the remaining moon crystals.")


def update_quest(player, item):
    if item["type"] == "crystal":
        player["quest"]["crystals"] += 1
        if player["quest"]["accepted"]:
            print("Quest progress:", player["quest"]["crystals"], "of 3 moon crystals.")
        else:
            print("Moon crystal collected. Talk to the Elder to accept the quest.")


def show_quest(player):
    print("\n--- QUEST ---")
    if player["quest"]["completed"]:
        print("Completed: The Shadow Dragon has been defeated!")
    elif player["quest"]["accepted"]:
        print("Collect 3 moon crystals and defeat the Shadow Dragon.")
        print("Moon crystals:", str(player["quest"]["crystals"]) + "/3")
    else:
        print("No active quest. Find the Elder (E) and press T to talk.")
