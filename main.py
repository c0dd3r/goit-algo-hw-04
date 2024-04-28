def total_salary(path):
    try:
        # Initialize variables to hold total salary and number of developers
        total_salary = 0
        num_developers = 0

        # Open the file with context manager to read salaries
        with open("file.txt", 'r', encoding='utf-8') as file:
            # Iterate through each line in the file
            for line in file:
                # Strip any newline characters and split into name and salary
                data = line.strip().split(',')
                if len(data) == 2:  # Ensure we have both name and salary
                    # Extract salary and convert to integer
                    salary = int(data[1])
                    # Increment total salary and count of developers
                    total_salary += salary
                    num_developers += 1

        # Calculate average salary if there are any developers
        if num_developers > 0:
            average_salary = total_salary / num_developers
        else:
            average_salary = 0

        # Return the total and average salary
        return total_salary, average_salary
        
    except FileNotFoundError:
        # Handle the case where the file does not exist
        return "File not found", None
    except Exception as e:
        # Handle other exceptions
        return f"Error: {e}", None


# Call the function to calculate total and average salary
total_salary("file.txt")  # Expected output: (6000, 2000.0)

