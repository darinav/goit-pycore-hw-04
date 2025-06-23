def get_cats_info(path: str) -> list[dict]:
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = [p.strip() for p in line.split(',')]
                if len(parts) == 3 and all(parts) and parts[-1].isdigit():
                    cats.append({'id': parts[0],
                                 'name': parts[1],
                                 'age': int(parts[2])})
                else:
                    print(f'Невірні дані для "{line.strip()}"')
    except IOError:
            print('Помилка обробки файлу')
    return cats

cats_info = get_cats_info("cats.txt")
for cat in cats_info:
    print(cat)