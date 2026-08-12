import math


def get_player_pos() -> tuple[float, float, float]:
    position_input: str = input(
        "Enter new coordinates as floats in format 'x,y,z': "
    )
    try:
        x_value, y_value, z_value = position_input.split(",")
    except ValueError:
        print("Invalid syntax")
        return get_player_pos()
    try:
        x: float = float(x_value)
    except ValueError as err:
        print(f"Error on parameter '{x_value.strip()}': {err}")
        return get_player_pos()
    try:
        y: float = float(y_value)
    except ValueError as err:
        print(f"Error on parameter '{y_value.strip()}': {err}")
        return get_player_pos()
    try:
        z: float = float(z_value)
    except ValueError as err:
        print(f"Error on parameter '{z_value.strip()}': {err}")
        return get_player_pos()
    return (x, y, z)


def get_distance(
    start: tuple[float, float, float],
    end: tuple[float, float, float],
) -> float:
    return math.sqrt(
        (end[0] - start[0]) ** 2
        + (end[1] - start[1]) ** 2
        + (end[2] - start[2]) ** 2
    )


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first_position: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {first_position}")
    print(
        f"It includes: X={first_position[0]}, Y={first_position[1]}"
        f", Z={first_position[2]}"
        )
    center: tuple[float, float, float] = (0.0, 0.0, 0.0)
    print(
        f"Distance to center: {round(get_distance(center, first_position), 4)}"
        )
    print("Get a second set of coordinates")
    second: tuple[float, float, float] = get_player_pos()
    between: float = round(get_distance(first_position, second), 4)
    print(f"Distance between the 2 sets of coordinates: {between}")


if __name__ == "__main__":
    main()
