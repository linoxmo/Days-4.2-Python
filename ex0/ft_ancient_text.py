import sys
import typing


def main() -> None:
    if (len(sys.argv) != 2):
        print("Usage: ft_ancient_text.py <file>")
        return
    file = sys.argv[1]
    print("=== Cyber Archive Recovery ===")
    print(f"Accessing file '{file}'")
    try:
        O_file: typing.IO[str] = open(file, 'r')
    except FileNotFoundError as e:
        print(f"Error opening file {file}: ", e)
        return
    except PermissionError as e:
        print(f"Error opening file {file}: ", e)
        return
    
    print(O_file.read())
    O_file.close()
    print(f"File {file} closed.")


if __name__ == '__main__':
    main()