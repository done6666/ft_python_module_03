import random


class Player:
    def __init__(self, name: str = "Unknown Player"):
        self._name: str = name
        self._achievements: set[str] = set()

    def __str__(self) -> str:
        return self._name

    def get_name(self) -> str:
        return self._name

    def get_achievements(self) -> set[str]:
        return self._achievements

    def set_name(self, name: str = "Unknown Player") -> None:
        self._name = name

    def set_achievements(self, achievements: set[str]) -> None:
        self._achievements = achievements


ACHIEVEMENTS: list[str] = [
    "First Steps",
    "Speed Runner",
    "Boss Slayer",
    "Treasure Hunter",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Survivor",
    "Strategist",
    "Crafting Genius",
    "World Savior",
    "Unstoppable",
    "Sharp Mind",
    "Hidden Path Finder",
    "Night Owl",
    "Perfect Aim",
    "Combo Master",
    "Dungeon Cleaner",
    "Lucky Roll",
    "Legend Born",
    "Silent Blade",
    "Beast Tamer",
    "Sky Diver",
    "Puzzle Breaker",
    "Shield Wall",
    "Potion Brewer",
    "Map Maker",
    "Gold Hoarder",
    "Quest Finisher",
    "Arena Champion",
    "Ghost Walker",
    "Storm Caller",
    "Iron Will",
    "Loot Goblin",
    "Trap Disarmer",
    "Rune Scholar",
    "Dragon Rider",
    "Camp Builder",
    "Echo Listener",
    "Final Blow",
]
PLAYERS: list[Player] = [
    Player("Alice"),
    Player("Bob"),
    Player("Charlie"),
    Player("Dylan"),
]
MIN_ACHIEVEMENTS: int = 16


def gen_player_achievements() -> set[str]:
    return set(
        random.sample(
            ACHIEVEMENTS,
            random.randint(MIN_ACHIEVEMENTS, len(ACHIEVEMENTS)),
        )
    )


def union_of_others(players: list[Player], skipped: int) -> set[str]:
    others: set[str] = set()
    after: int = skipped + 1
    for player in players[:skipped] + players[after:]:
        others = others.union(player.get_achievements())
    return others


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()
    unions: set[str] = set()
    common: set[str] = set()
    for player in PLAYERS:
        player.set_achievements(gen_player_achievements())
        unions = unions.union(player.get_achievements())
        common = common.intersection(player.get_achievements())
        print(f"Player {player}: {player.get_achievements()}")
    print()
    print(f"All distinct achievements: {unions}")
    print()
    print(f"Common achievements: {common}")
    print()
    index: int = 0
    for player in PLAYERS:
        others: set[str] = union_of_others(PLAYERS, index)
        only: set[str] = player.get_achievements().difference(others)
        print(f"Only {player} has: {only}")
        index += 1
    print()
    catalogue: set[str] = set(ACHIEVEMENTS)
    for player in PLAYERS:
        missing: set[str] = catalogue.difference(player.get_achievements())
        print(f"{player} is missing: {missing}")


if __name__ == "__main__":
    main()
