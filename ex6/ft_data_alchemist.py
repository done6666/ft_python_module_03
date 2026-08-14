import random

PLAYERS: list[str] = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam",
]


def main() -> None:
    print("=== Game Data Alchemist ===")
    print()
    print(f"Initial list of players: {PLAYERS}")
    capitalized: list[str] = [name.capitalize() for name in PLAYERS]
    print(f"New list with all names capitalized: {capitalized}")
    capitalized_only: list[str] = [
        name for name in PLAYERS if name[0].isupper()
    ]
    print(f"New list of capitalized names only: {capitalized_only}")
    print()
    scores: dict[str, int] = {
        name: random.randint(1, 1000) for name in capitalized
    }
    print(f"Score dict: {scores}")
    average: float = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {average}")
    high_scores: dict[str, int] = {
        name: score for name, score in scores.items() if score > average
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
