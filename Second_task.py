def get_cats_info(path):
    cats = []  
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()  
            for line in lines:
                cat_data = line.strip().split(',')  
                cat_dict = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": cat_data[2]
                }
                
                cats.append(cat_dict)

    except FileNotFoundError:
        print(f"Error: The file at path '{path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    
    return cats


