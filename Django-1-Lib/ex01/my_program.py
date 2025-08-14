import path

if __name__ == "__main__":
    content = f'''   Outstanding\n        
        .
       ,O,
      ,OOO,
'oooooOOOOOooooo'
  `OOOOOOOOOOO`
    `OOOOOOO`
    OOOO'OOOO
   OOO'   'OOO
  O'         'O\n'''


    directory  = path.Path("outstanding")
    if not directory.exists():
        directory.makedirs()

    file_path = directory / "outstanding.txt"
    file_path.write_text(content)

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            print(file.read())
    except Exception as e:
        print(e)