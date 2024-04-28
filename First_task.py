def total_salary(path):
    try:
        total_salary = 0
        num_developers = 0

       
        with open("file.txt", 'r', encoding='utf-8') as file:
           
            for line in file:
                
                data = line.strip().split(',')
                if len(data) == 2:  
                    salary = int(data[1])
                    total_salary += salary
                    num_developers += 1

        
        if num_developers > 0:
            average_salary = total_salary / num_developers
        else:
            average_salary = 0

        
        return total_salary, average_salary
        
    except FileNotFoundError:
        
        return "File not found", None
    except Exception as e:
       
        return f"Error: {e}", None



