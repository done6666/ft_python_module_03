import sys


def main() -> None:
    arg_count: int = len(sys.argv)
    print("=== Command Quest ===")
    print("Program name: ft_command_quest.py")
    if arg_count == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {arg_count - 1}")
        arg_index: int = 1
        for arg in sys.argv[1:]:
            print(f"Argument {arg_index}: {arg}")
            arg_index += 1
    print(f"Total arguments: {arg_count}")


if __name__ == "__main__":
    main()
