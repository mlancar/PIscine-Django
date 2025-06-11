def format_file():
    try:
        file = open("numbers.txt")
        content = file.read()
        formatted_content = content.replace(",", "\n")
        return formatted_content
    except Exception as err:
        print(f"Unexpected {err}")

if __name__ == '__main__':
    print(format_file())