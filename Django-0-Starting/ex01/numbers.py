def display_file():
    try:
        file = open("numbers.txt")
        print(file.read())
    except Exception as err:
        print(f"Unexpected {err}")

if __name__ == '__main__':
    display_file()