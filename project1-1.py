"""
This function loads data from a specified file into a dictionary
it takes the argument file_path, a string which gives the path to Data.txt
it returns a dictionary containing the loaded data, where keys are column names,
and values are lists of corresponding data values.
"""
def load_data_as_dict(file_path):

    data_dict = {} # intialize empty dictionary
    current_column = None # initialize the current  position

    with open(file_path, 'r') as file: # access the data file with read 'r' permissions
        for line in file: # iterates through lines in the data file
            line = line.strip() # lines are striped of leading and trailing whitespace

            if line.startswith('COLUMN'): # Check if the line indicates a new column
                current_column = line[6:].strip()  # Extract column name an strips off whitespace after
                data_dict[current_column] = []  # Initialize a new list for the column
            
            elif line == 'END': # Checks if the end of the data is reached
                break
            
            else: # Otherwise, append the line to the current column's list
                if current_column:
                    data_dict[current_column].append(line)

    # Print the dictionary in correct format
    for column, values in data_dict.items(): # iterates through the dictionary
        print(f"\"{column}\": [") #prints column name in quotes; "Names"
        for value in values:
            print(f" \"{value}\",") #prints value in quotes; "Joseph"
        print("]")

    return data_dict  # Return the populated dictionary


"""
This function loads data from data.txt a list of tuples.
it takes the argument file_path, a string which is the path to the data file.
it returns a list of tuples, where each tuple contains a column name and a list of corresponding data values.
"""
def load_data_as_list(file_path):

    data_list = [] #initializes empty list of data items
    current_column = None #initializes current column position
    current_values = [] # initializes a list of current values in the data file

    with open(file_path, 'r') as file: # access the data file with read 'r' permissions
        for line in file: # iterates through lines in the data file
            line = line.strip() # lines are striped of leading and trailing whitespace

            if line.startswith('COLUMN'): # Check if the line indicates a new column
                # If there's a previous column, add it to the list
                if current_column:
                    data_list.append((current_column, current_values)) # appends the current value in the data file to the list
                current_column = line[6:].strip()  # extract column name and strip whitespace 
                current_values = []  # initialize a new list for the column
            
            elif line == 'END': # Check if the end of the data is reached
                
                if current_column: # Add the last column and its values to the list
                    data_list.append((current_column, current_values))
                break
            
            else: # Otherwise, append the line to the current column's values
                current_values.append(line)

    # Print the list in the correct format
    for column, values in data_list: # iterates through the list
        print(f"({column}, [{', '.join(values)}])")

    return data_list  # Return the populated list


"""
This function returns a list of values for a given column name from the provided data.
it takes data from either dictionary or list form which it extracts the sublist.
and col_name which is a string of the name of the column to extract.
it returns a list of values for the specified column, or None if the column
does not exist or the data format is invalid.
"""
def return_sublist(data, col_name):

    if isinstance(data, dict): #checks if the data received is a dictionary
        if col_name in data: #checks if column name is in the data
            return data[col_name] #returns data list with column name inside
    elif isinstance(data, list): #checks if the data received is a list
        for column, values in data: #iterates through values the list
            if column == col_name: #returns values if column name is correct
                return values
    return None


"""
This function calculates the sum of values in a specified column.
it takes data either a dictionary or a list the data to extract the sublist from.
and col_name, a string of the name of the column to sum up.
it returns a float, The sum of values in the specified column, 
or None if the column does not exist, the data format is invalid, 
or the values cannot be converted to floats.
"""
def return_sublist_total(data, col_name):

    sublist = return_sublist(data, col_name)
    if sublist is None: # based on the return sublist value, so if it doesn't work this won't
        return None
    try:
        return sum(float(value) for value in sublist) # convert each value to a float and calculate the sum
    except ValueError: #if there's a value error return none
        return None


"""
This function calculates the mean of values in a specified column.
it takes the arguments data, a dictionary  or a list the data to extract the sublist from.
and col_name, a string the name of the column to calculate the mean.
it returns a float which The mean of values in the specified column, or None if the columndoes not exist, 
the data format is invalid, or the values cannot be converted to floats.
"""
def return_sublist_mean(data, col_name):

    sublist = return_sublist(data, col_name)
    sublist_total = return_sublist_total(data, col_name)
    if sublist_total is None: #uses the sublist_total funtion to check if it's invalid
        return None
    try:
        return sublist_total / len(sublist)  # calculates mean, by dividing the sublist total by lengthof sublist
    except ValueError:
        return None

"""
THIS IS THE PART WHERE THE FUNCTIONS ARE IMPLEMENTED
"""
file_path = "Data.txt"

# Runs and prints the function load_data_as_dict
print("THE DICTIONARY; \n")
data_dict = load_data_as_dict(file_path)
print(" ")
# Runs and prints the function load_data_as_dict
print("THE LIST; \n")
data_list = load_data_as_list(file_path)
print(" ")

# Runs and prints the return sublist function from dictionary
print("The sublist values from dictionary;")
from_dict = return_sublist(data_dict, "Addresses")
print(from_dict)
print(" ")
# Runs and prints the return sublist function from a list
print("The sublist values from list;")
from_list = return_sublist(data_list, "Addresses")
print(from_list)
print(" ")

# Runs and prints the total values from dictionary
print("The total sum of values from dictionary;")
total_dict = return_sublist_total(data_dict, "Prices")
print(total_dict)
print(" ")
# Runs and prints the total vales from list
print("The total sum of values from list;")
total_list = return_sublist_total(data_list, "Prices")
print(total_list)
print(" ")

# Runs and prints the mean values from dictionary
print("The average of values from dictonary;")
mean_dict = return_sublist_mean(data_dict, "Prices")
print(mean_dict)
print(" ")
# Runs and prints the mean values from list
print("The average of values from list;")
mean_list = return_sublist_mean(data_list, "Prices")
print(mean_list)