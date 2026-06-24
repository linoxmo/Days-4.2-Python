import typing


def secure_archive(filename :str, action: str, content : str ="") -> typing.Tuple[bool, str]:
    try:
        if action == "r":
            with open(filename, 'r') as file:
                return (True, file.read())
            file.write("newtext")
        elif action == "w":
            with open(filename, 'w') as file:
                file.write(content)
                return (True, "Content succesfully written to file")
        else:
            raise Exception("Invalid Action")
    except Exception as e:
        return(False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")
    print(secure_archive("test.txt", "w", "hello"))
    
if __name__ == '__main__':
    main()