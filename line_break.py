def copy_line():
    while True:
        nf1 = int(input('Введите номер файла из которого копируем строчку (1 или 2): '))
        nf2 = int(input('Введите номер файла в который копируем строчку (1 или 2): '))
        
        if nf1 not in [1, 2] or nf2 not in [1, 2]:
            print('Вы ввели неверный номер файла. Введите 1 или 2.')
        else:
            break
    
    line_numb = int(input('Введите номер копируемой строки: '))
    
    with open(f'db/data_{nf1}.txt', 'r', encoding='utf-8') as file1:
        lines = file1.readlines()
    if line_numb < 1 or line_numb > len(lines):
        print('Неверный номер строки')
        return

    with open(f'db/data_{nf2}.txt', 'a', encoding='utf-8') as file2:
        file2.write(lines[line_numb - 1])
        print('Строка скопирована')

