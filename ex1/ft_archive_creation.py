import sys
import typing


def main() -> None:
    if ((len(sys.argv)) != 2):
        print("Usage: ft_ancient_text.py <file>")
        return
    
    file = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file}'")

    try:
        O_file: typing.IO[str] = open(file, 'r')
    except FileNotFoundError as e:
        print(f"Error opening file '{file}': {e}")
        return
    except PermissionError as e:
        print(f"Error opening file '{file}': {e}")
        return

    data = O_file.read()
    O_file.close()
    print("---\n")
    print(data)
    data = data + "#"
    print("---")
    print(f"File '{file}' closed.\n")

    print('Transform data:\n---\n')
    print(data.replace("\n", "#\n"))
    print('---')

    new_file = input("Enter new file name (or empty): ")
    if new_file:
        new = open(new_file, "w")
        data = data.replace("\n", "#\n")
        new.write(data)
        print(f"Saving data to '{new_file}'")
        new.close()
        print(f"Data saved in file '{new_file}'")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()
