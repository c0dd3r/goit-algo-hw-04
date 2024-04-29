def total_salary(path):
    
    try:
        with open(path, encoding='utf-8') as file:
            
            data = file.readlines()

        total_salary = 0
        number_of_developers = 0

        for row in data:
           
            name, salary_str = row.strip().split(',')

            salary = int(salary_str)

            total_salary += salary

            number_of_developers += 1

        if number_of_developers > 0:
            average_salary = total_salary / number_of_developers
        else:
            average_salary = 0

        return total_salary, average_salary

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return 0, 0

    except Exception as e:
        print(f"Помилка при роботі з файлом: {e}")
        return 0, 0
