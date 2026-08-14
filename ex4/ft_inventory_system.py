import sys


def parse_args() -> dict[str, int]:
    items: dict[str, int] = {}
    for arg in sys.argv[1:]:
        try:
            name, quantity = arg.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{arg}'")
            continue
        if len(name) == 0:
            print(f"Error - invalid parameter '{arg}'")
            continue
        if name in items:
            print(f"Redundant item '{name}'- discarding")
            continue
        try:
            items[name] = int(quantity)
        except ValueError as err:
            print(f"Quantity error for '{name}': {err}")
    return items


def main() -> None:
    print("=== Inventory System Analysis ===")
    items: dict[str, int] = parse_args()
    total: int = sum(items.values())
    item_length: int = len(items)
    print(f"Got inventory: {items}")
    print(f"Item list: {list(items.keys())}")
    print(f"Total quantity of the {item_length} items: {total}")
    if total > 0:
        for item in items:
            percentage: float = round(items[item] / total * 100, 1)
            print(f"Item {item} represents {percentage}%")
    if item_length > 0:
        most_abundant: str = list(items.keys())[0]
        least_abundant: str = most_abundant
        for item in items:
            if items[item] > items[most_abundant]:
                most_abundant = item
            if items[item] < items[least_abundant]:
                least_abundant = item
        print(
            f"Item most abundant: {most_abundant} with"
            f" quantity {items[most_abundant]}"
        )
        print(
            f"Item least abundant: {least_abundant} with"
            f" quantity {items[least_abundant]}"
        )
    items.update({"magic_item": 1})
    print(f"Updated inventory: {items}")


if __name__ == "__main__":
    main()
