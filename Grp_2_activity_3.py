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
    c=average(lst)
    d=empty(lst)
    for i in d:
        lst[i]=c
    return lst


def replace_min(lst):
    """Replaces an empty cell with minimum value of the list and returns the replaced list."""
    c=min(lst)
    d=empty(lst)
    for i in d:
        lst[i]=c
    return lst


def replace_max(lst):
    """Replaces an empty cell with maximum value of the list and returns the replaced list."""
    c=max(lst)
    d=empty(lst)
    for i in d:
        lst[i]=c
    return lst


def sort_ascending(lst):
    """Sorts the values of a list in ascending order."""
    for i in range(0,len(lst)):
        j=i
        while j>0 and float(lst[j-1]) > float(lst[j]):
            lst[j-1],lst[j] = lst[j],lst[j-1]
            j-=1
    return lst


def sort_descending(lst):
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

