import sys
import typing
import io


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    if (len(sys.argv) == 1):
        print("Plese enter a file")
        return
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")
    try:
        file : typing.IO[str]  = open(file_name, 'r')
    except FileNotFoundError as e:
        print(f"[STDERR] Error opening file '{file_name}' :" , e, file =sys.stderr)
        return
    except PermissionError as e:
        print(f"[STDERR] Permission error'{file_name}' :" , e, file =sys.stderr)
        return
    data = file.read()
    print(data) 
    data +=  "#"
    data.replace("\n", "#\n")
    file.close()
    print(f"The file {file_name} was closed correctly")
    print("Transorm data : \n---\n" , data)
    print("Veuillez ecrire quelque chose dans le terminal :")
    new_file = sys.stdin.readline()
    print(f"Saving data to '{new_file}'")
    try:
        new = open(new_file, "w")
    except PermissionError as e:
            print(f"[STDERR] Error opening file '{file_name}': "
                  f"{e}", file=sys.stderr)
            print("Data not saved")
            return
    
    new.close()
    print(f"Data saved in file '{new_file}'")

if __name__ == '__main__':
    main()
