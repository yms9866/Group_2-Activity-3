"""
GROUP 2
Authors:

        1. 


        2.Dona Pal:
            Contributed in the functions: min(), max(), average(), replace_avg(), replace_max(), replace_min(), 
            visualizeData(), sort_ascending(), sort_descending()

        
GIT Repository: https://github.com/yms9866/Group_2-Activity-3.git

Manifesto :This Program is written to facilitate a Command Line Interface Tool for Data Analysis.
        The program guides the user with a step-by-step instruction, from choosing desired CSV file for loading 
        the data into the program, to preparing the data, analyzing the data to the final visualization of the 
        processed data. 


"""


import csv

def longest_word(file_path):
    """ Returns the length of the longest word. We use this value to determine the maximum gap 
        between two columns of the data while loading the data in the consol."""
    with open(file_path) as file:
        csv_r = csv.reader(file)
        len_longest_word=0
        for i in csv_r:
            for j in i:
                length = len(j)
                if length > len_longest_word:
                    len_longest_word=length
        return len_longest_word
    

def load_data(file_path,start,end_col):
    """ start: starting column
        end_col: end column
    The function loads the data in a row-colomn format. """
    with open(file_path,'r') as file:
            csv_r = csv.reader(file)
            rows=1
            for row in csv_r:
                for j in range(start-1,end_col):
                    striped = row[j].strip()
                    length=len(row[j]) # length of words
                    maximum_gap = longest_word(file_path) # maximum gap between two columns
                    whitespace_leng = maximum_gap -length # number of spaces 
                    white = whitespace_leng*' '  #the white space printed after printing the word to make the table look good.
                    
                    if start-1 <= j < end_col-1: # for all columns except the last column
                        if striped == '':
                            print(' -',white+'|',end='')
                        else:
                            print(row[j],white+'|',end ='' )
                    elif j == end_col-1: #  for the last column
                        if striped == '':
                            print(' -')
                        else:
                            print(row[j])    
                rows+=1

def one_column_load(file_path,column): 
        """This function loads a data of one column only."""
        with open(file_path,'r') as file:
            csv_r = csv.reader(file)
            empty_cells = []
            row=1
            for i in csv_r:
                striped=i[column-1].strip()
                if striped == '':
                    print(str(row)+'.',' -')
                    empty_cells.append('row-'+str(row))
                else:
                    print(str(row)+'. '+striped)
                row+=1
            return empty_cells 

def checking(path,column):
    with open(path,'r') as file:
        csv_r = csv.reader(file)
        next(csv_r)
        list = []
        for data in csv_r:
            list.append(data[int(column)-1].strip())
        result = 'Numeric'
        for value in list:
            if value != '':
                try:
                    int(value)
                except ValueError:
                    result = 'Non-numeric'
            elif value == '':
                continue    
        return result
    
def number_of_column(file_path):
    """Returns the number of columns that the csv file has."""
    with open(file_path,'r') as file:
        csv_r = csv.reader(file)
        for i in csv_r:
            return len(i)


def name_of_column(file_path):
        """Returns a list of the names of columns in the csv file."""
        with open(file_path,'r') as file:
            csv_r = csv.reader(file)
            for i in csv_r:
                return i

def return_list(file_name,column):
    """Returns a list of the values under a specified column."""
    with open(file_name,'r') as file:
        csv_r = csv.reader(file)
        next(csv_r)
        lst=[]
        for i in csv_r:
            try:
                lst.append(float(i[column-1].strip()))
            except ValueError:
                lst.append(i[column-1].strip())
        return lst
    

def empty(lst):
    """Returns a list of indices whereby there is no value associated with the indices. """
    j=0
    empty_cell=[]
    for i in lst:
        if lst[j] == '':
            empty_cell.append(j)
        j+=1
    return empty_cell



def min(lst):
    """Returns the minimum value of a list."""
    min=max(lst)
    for i in lst:
        try:
            if float(i) < min:
                min = float(i)
        except ValueError:
            continue
        return min
    
def max(lst):
    """Returns the maximum value of a list."""
    max=0
    for i in lst:
        try:
            if float(i) > max:
                max = float(i)
        except ValueError:
            continue
        return max
    
def average(lst):
    """Returns the average value of a list."""
    n=len(lst)
    sum = 0
    for i in lst:
        try:
            sum = sum + float(i)
        except ValueError:
            continue
    avg = sum/n
    return avg



def replace_avg(lst):
    """Replaces an empty cell with average value of the list and returns the replaced list."""
    avg=average(lst)
    empty_indices=empty(lst)
    for i in empty_indices:
        lst[i]=avg
    return lst


def replace_min(lst):
    """Replaces an empty cell with minimum value of the list and returns the replaced list."""
    minimum=min(lst)
    empty_indices=empty(lst)
    for i in empty_indices:
        lst[i]=minimum
    return lst


def replace_max(lst):
    """Replaces an empty cell with maximum value of the list and returns the replaced list."""
    maximum_value=max(lst)
    empty_indices=empty(lst)
    for i in empty_indices:
        lst[i]=maximum_value
    return lst


def insertion_sort_ascending(lst):
    """Sorts the values of a list in ascending order."""
    for i in range(0,len(lst)):
        j=i
        while j>0 and float(lst[j-1]) > float(lst[j]):
            lst[j-1],lst[j] = lst[j],lst[j-1]
            j-=1
    return lst


def insertion_sort_descending(lst):
    """Sorts the values of a list in descending order."""
    for i in range(0,len(lst)):
        j=i
        while j>0 and float(lst[j-1]) < float(lst[j]):
            lst[j-1],lst[j] = lst[j],lst[j-1]
            j-=1
    return lst

def visualizeData(lst):
    """It gives a visual/graphical representation for a given list."""
    for i in lst:
        if int(i)<100:
            value= int(i)//5+1
        elif int(i)>=100:
            value=20
        strg="*"*value
        
        print(strg)

def main():
        print("""=========================================================================
Welcome to Data Analysis CLI
=========================================================================
Program stages:
1. Load Data 
2. Clean and prepare data
3. Analyse Data
4. Visualize Data"""
) 
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        print('STAGE 1: LOAD DATA ')
        print()
        while True:
            try:
                file = input("Enter your csv file path: ")
                number_of_columns=number_of_column(file)
                name = name_of_column(file)
                print('File Loading...')
                load_data(file,1,number_of_columns)
                input('Your file is loaded successfully. Press ENTER to continue ')
                print('Your file contains',number_of_columns,'columns named as: ')

                column_choices='' # gives choices of names of columns as separated by /
                for i in name:
                    column_choices+=i+'/'
                while True:    
                    n=1
                    for i in range(number_of_columns):
                        print(str(n)+'.',name[i].strip())
                        n+=1

                    column=input('Which column do you want to analyse? \nChoose '+column_choices+' :').capitalize()
                    
                    column_number = 0  # changing the name of column given by the user to number to know which column number is the given name.
                    for i in name:
                        column_number+=1
                        if column == i.strip():
                            break
                    check = checking(file,column_number)
                    if check == 'Numeric':
                        print('Here is your chosen column: ')
                        empty_rows = one_column_load(file,column_number)
                        lst=return_list(file,column_number)
                        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                        input("Press ENTER to move to the next stage...")
                        print('STAGE 2: CLEANING AND PREPARING DATA')
                        print()
                        print('\nHere the data of your chosen column\n',lst,'\n')
                        if empty_rows!=[]:
                            print('You have empty cell at: ')
                            for i in empty_rows:
                                print('\t',i)
                            while True:
                                if len(empty_rows) == 1:
                                    replace=input("""What do you want to do about this cell? Do you want to replace it with
        ************************************************************************
        1. Average of the list.
        2. Minimum value of the list 
        3. Maximum value of the list
        ************************************************************************
        Choose [1/2/3]:  """)
                                else:
                                    replace=input("""What do you want to do about these cells? Do you want to replace them with
        ************************************************************************
        1. Average of the list.
        2. Minimum value of the list 
        3. Maximum value of the list
        ************************************************************************
        Choose [1/2/3]:  """)
                                if replace == '1':
                                        avg = average(lst)
                                        print('All empty values replaced with average value which is',avg)
                                        lst2=replace_avg(lst)
                                elif replace == '2':
                                        mini = min(lst)
                                        print('All empty values replaced with minimum value which is',mini)
                                        lst2=replace_min(lst)
                                elif replace == '3':
                                        maxi = average(lst)
                                        print('All empty values replaced with minimum value which is',maxi)
                                        lst2=replace_max(lst)
                                else:
                                    print('Input Error. Please try again!')
                                    continue
                                break
                            
                            print('\nHere is the replaced list\n',lst2,'\n')
                            print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                            input("Press ENTER to move to the next stage...")
                            print('STAGE 3: ANALYSING DATA')
                            print()

                            while True:
                                sort_choice = input("""Do you want to sort the list in: 
        1. Ascending order
        2. Decending order
        Choose [1/2]: """)
                                if sort_choice == '1':
                                    sorted=insertion_sort_ascending(lst2)
                                elif sort_choice == '2':
                                    sorted=insertion_sort_descending(lst2)
                                else:
                                    print('Input Error. Please try again!')
                                    continue
                                break
                            print('\nHere is your sorted list \n',sorted,'\n')
                            print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                            input("Press ENTER to move to the next stage...")
                            print('STAGE 4: VISUALIZING DATA')
                            print()
                            print('Column:',column)
                            print('Legend: each * represents 5 units')
                            visualizeData(sorted)
                            print('Visualization Completed.')
                            print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                    elif check == 'Non-numeric':
                            print('You have chosen a non-numeric column. Please try again!')
                            continue
                    else:
                            print('Input Error. Please try again!')
                            continue
                    repeat = input('Do you want to continue analyzing the other numerical columns? [yes/no]: ').lower()
                    if repeat=='yes':
                        continue
                    elif repeat == 'no':
                        break
                    break
                restart=input('Press 1 to go back to the first stage or 0 to exit: ')
                if restart == '1':
                    continue
                elif restart == '0':
                    print('The program is closed.')
                    print('Thank you and Goodbye!')
                    break
                else:
                    print('Input Error. Please try again!')
                    continue  
            except FileNotFoundError:
                print('File does not exist.')
            except Exception:
                print('Something went wrong. Please try again!')


            
if __name__ == "__main__": 
    main()
