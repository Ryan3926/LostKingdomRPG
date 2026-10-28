from player import create_player, show_status, show_inventory, use_potion, equip_item
from world import create_world, display_map, move_player, check_location
from actions import fight, talk_to_npc, update_quest, show_quest


def main():
    player = create_player()
    world = create_world()
    game_over = False

    print("=" * 44)
    print("        THE LOST KINGDOM: FOREST QUEST")
    print("=" * 44)
    print("Collect 3 moon crystals and defeat the Shadow Dragon.")
    print("Controls: W/A/S/D move | I inventory | P potion | E equip")
    print("T talk | Q quest | H status | X quit")
    input("\nPress Enter to begin...")

    while not game_over:
        display_map(world, player)
        command = input("\nWhat would you like to do? > ").strip().lower()

        if command in ["w", "a", "s", "d"]:
            move_player(world, player, command)
            result = check_location(world, player)

            if result == "npc":
                print("\nYou found the Elder. Press T to speak.")
            elif result == "item":
                item = world["items"].pop((player["x"], player["y"]), None)
                if item:
                    player["inventory"].append(item)
                    print("\nYou collected:", item["name"])
                    if item["type"] == "crystal":
                        update_quest(player, item)
            elif result == "monster":
                monster = world["monsters"].pop((player["x"], player["y"]), None)
                if monster and not fight(player, monster):
                    game_over = True
            elif result == "boss":
                if not player["quest"]["accepted"]:
                    print("\nA magical barrier blocks the ruins. Talk to the Elder first.")
                elif player["quest"]["crystals"] < 3:
                    print("\nThe lair is sealed. You need 3 moon crystals.")
                else:
                    if fight(player, world["boss"]):
                        player["quest"]["completed"] = True
                        print("\nYou defeated the Shadow Dragon and saved the kingdom!")
                        print("YOU WIN!")
                    game_over = True

        elif command == "i":
            show_inventory(player)
        elif command == "p":
            use_potion(player)
        elif command == "e":
            equip_item(player)
        elif command == "t":
            if (player["x"], player["y"]) == world["npc"]:
                talk_to_npc(player)
            else:
                print("There is no one here to talk to.")
        elif command == "q":
            show_quest(player)
        elif command == "h":
            show_status(player)
        elif command == "x":
            print("You leave the forest. Thanks for playing!")
            game_over = True
        else:
            print("Unknown command. Use W/A/S/D, I, P, E, T, Q, H, or X.")

        if player["health"] <= 0:
            print("\nYou have fallen in battle. GAME OVER.")
            game_over = True

    print("\nFinal status:")
    show_status(player)


if __name__ == "__main__":
    main()
