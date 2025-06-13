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
  O'         'O'''


    directory  = path.Path("outstanding")
    if not directory.exists():
        directory.makedirs()

    file = directory / "outstanding.txt"
    file.write_text(content)