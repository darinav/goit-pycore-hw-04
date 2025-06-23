
def total_salary(path: str) -> tuple[int, int]:
    salary_sum = 0
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    parts = line.strip().split(',')
                    salary_sum += int(parts[-1])
                    count += 1
                except (ValueError, IndexError):
                    print(f'Невірні дані для "{line.strip()}"')
                    continue
    except IOError:
            print('Помилка обробки файлу')
    salary_avg = int(salary_sum / count) if count else 0
    print(salary_sum, salary_avg)
    return salary_sum, salary_avg


total, average = total_salary('salaries.txt')
print(f'Загальна сума заробітної плати: {total}, '
      f'Середня заробітна плата: {average}')