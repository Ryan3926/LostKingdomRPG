def create_player():
    """Create and return the player's starting information."""
    return {
        "name": input("Enter your hero's name: ").strip() or "Hero",
        "health": 100,
        "max_health": 100,
        "attack": 12,
        "x": 0,
        "y": 4,
        "inventory": [
            {"name": "Small Potion", "type": "potion", "heal": 25},
            {"name": "Rusty Sword", "type": "weapon", "bonus": 3}
        ],
        "weapon_bonus": 0,
        "gold": 0,
        "quest": {"accepted": False, "crystals": 0, "completed": False}
    }


def show_status(player):
    print("\n--- HERO STATUS ---")
    print("Name:", player["name"])
    print("Health:", str(player["health"]) + "/" + str(player["max_health"]))
    print("Base attack:", player["attack"])
    print("Weapon bonus:", player["weapon_bonus"])
    print("Total attack:", player["attack"] + player["weapon_bonus"])
    print("Gold:", player["gold"])


def show_inventory(player):
    print("\n--- INVENTORY ---")
    if len(player["inventory"]) == 0:
        print("Your inventory is empty.")
    else:
        for number, item in enumerate(player["inventory"], start=1):
            print(str(number) + ".", item["name"], "-", item["type"])


def use_potion(player):
    for index, item in enumerate(player["inventory"]):
        if item["type"] == "potion":
            old_health = player["health"]
            player["health"] = min(player["max_health"], player["health"] + item["heal"])
            healed = player["health"] - old_health
            player["inventory"].pop(index)
            print("You used", item["name"], "and restored", healed, "health.")
            print("Health:", str(player["health"]) + "/" + str(player["max_health"]))
            return
    print("You do not have any potions.")


def equip_item(player):
    weapons = []
    for item in player["inventory"]:
        if item["type"] == "weapon":
            weapons.append(item)

    if len(weapons) == 0:
        print("You have no weapons to equip.")
        return

    print("\nWeapons you own:")
    for number, item in enumerate(weapons, start=1):
        print(str(number) + ".", item["name"], "(+" + str(item["bonus"]) + " attack)")

    choice = input("Enter weapon number, or press Enter to cancel: ").strip()
    if choice == "":
        return
    if choice.isdigit() and 1 <= int(choice) <= len(weapons):
        selected = weapons[int(choice) - 1]
        player["weapon_bonus"] = selected["bonus"]
        print("Equipped", selected["name"] + ".")
    else:
        print("That is not a valid weapon number.")
