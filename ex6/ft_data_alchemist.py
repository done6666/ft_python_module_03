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
    capitalized: list[str] = []
    capitalized_only: list[str] = []
    scores: dict[str, int] = {}
    average: float = 0.0
    high_scores: dict[str, int] = {}
    print("=== Game Data Alchemist ===")
    print()
    print(f"Initial list of players: {PLAYERS}")
    for name in PLAYERS:
        capitalized.append(name.capitalize())
    print(f"New list with all names capitalized: {capitalized}")
    for name in PLAYERS:
        if name[0].isupper():
            capitalized_only.append(name)
    print(f"New list of capitalized names only: {capitalized_only}")
    print()
    for name in capitalized:
        scores.update({name: random.randint(1, 1000)})
    print(f"Score dict: {scores}")
    average = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {average}")
    for name in scores:
        if scores[name] > average:
            high_scores.update({name: scores[name]})
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
