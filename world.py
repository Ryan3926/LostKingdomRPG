def create_world():
    return {
        "width": 5,
        "height": 5,
        "npc": (2, 2),
        "items": {
            (1, 3): {"name": "Moon Crystal", "type": "crystal"},
            (3, 3): {"name": "Moon Crystal", "type": "crystal"},
            (4, 1): {"name": "Moon Crystal", "type": "crystal"},
            (0, 2): {"name": "Health Potion", "type": "potion", "heal": 30},
            (3, 4): {"name": "Iron Sword", "type": "weapon", "bonus": 6},
            (4, 3): {"name": "Shield Charm", "type": "armor", "bonus": 2}
        },
        "monsters": {
            (1, 4): {"name": "Slime", "health": 22, "attack": 5, "reward": 5},
            (0, 1): {"name": "Forest Wolf", "health": 30, "attack": 7, "reward": 8},
            (3, 2): {"name": "Goblin Scout", "health": 35, "attack": 8, "reward": 10},
            (2, 1): {"name": "Skeleton", "health": 40, "attack": 9, "reward": 12},
            (4, 4): {"name": "Orc Brute", "health": 48, "attack": 10, "reward": 15}
        },
        "boss": {"name": "Shadow Dragon", "health": 85, "attack": 13, "reward": 100},
        "boss_position": (2, 0)
    }


def display_map(world, player):
    print("\n--- FOREST MAP ---")
    print("P = you | E = Elder | M = monster | I = item | B = boss | . = empty")
    for y in range(world["height"]):
        row = []
        for x in range(world["width"]):
            position = (x, y)
            if (player["x"], player["y"]) == position:
                symbol = "P"
            elif position == world["npc"]:
                symbol = "E"
            elif position == world["boss_position"]:
                symbol = "B"
            elif position in world["monsters"]:
                symbol = "M"
            elif position in world["items"]:
                symbol = "I"
            else:
                symbol = "."
            row.append(symbol)
        print(" ".join(row))
    print("Position:", (player["x"], player["y"]))


def move_player(world, player, command):
    new_x = player["x"]
    new_y = player["y"]

    if command == "w":
        new_y -= 1
    elif command == "s":
        new_y += 1
    elif command == "a":
        new_x -= 1
    elif command == "d":
        new_x += 1

    if 0 <= new_x < world["width"] and 0 <= new_y < world["height"]:
        player["x"] = new_x
        player["y"] = new_y
    else:
        print("You cannot move outside the map.")


def check_location(world, player):
    position = (player["x"], player["y"])
    if position == world["npc"]:
        return "npc"
    if position == world["boss_position"]:
        return "boss"
    if position in world["monsters"]:
        return "monster"
    if position in world["items"]:
        return "item"
    return "empty"
