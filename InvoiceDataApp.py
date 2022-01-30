import os
from sys import argv

def read_csv(in_file):
    """This functions reads a file

    Keyword arguments:
        in_file: path to a file
    Return:
        lines: a list of all lines in the file
    """
    lines = []
    #First check if the file exists before trying to read it.
    if os.path.exists(in_file):
        with open(in_file) as f:
            for line in f:
                lines.append(line)
    return lines

def line_parser(lines):
    """
    This function takes a list and makes a list of lists where each list contains one line.

    Keyword arguments:
        lines: a list containing all the text in a file
    Return:
        list_lines: list of lists where each list contains one line
    """
    list_lines = []
    for line in lines:
        list_elements = line.split(',')
        list_lines.append(list_elements)
    return list_lines

def list_checker(in_lines, comp_name):
    """
    This function checks if the company name is allready in the database

    Keyword arguments:
        in_lines: list of lists where each list is a line in the file
        comp_name: string containing the company name
    Return:
        checker: TRUE if the company name is allready in the database and FALSE if the customer is not in the database
    """
    checker = 'FALSE'
    for line in in_lines[1:]:
        if line[0] == comp_name:
            checker = 'TRUE'
            break
        else:
            continue
    return checker

def list_size_checker(in_list, size):
    """
    This function checks if the size of a list is sufficient

    Keyword arguments:
        in_list: a list of which the size should be checked
        size: integer representing the required size of the in_list
    Return:
        size_checker: boolean value short if the length of the list is shorter than the supplied size,
        long if the length of the list is longer than the supplied size
        or TRUE if the list is of sufficient size
    """
    if len(in_list) < size:
        print("Too little information is supplied or it is not seperated by comma's.")
        size_checker = 'short'
    elif len(in_list) > size:
        print("Too much information is supplied or too many comma's are used.")
        size_checker = 'long'
    elif len(in_list) == size:
        size_checker = 'TRUE'
    return size_checker

def list_to_str(in_lines):
    """
    This function takes a list of lists and puts all elements into one string.

    Keyword arguments:
        in_lines: a list of lists where each list is one line
    Return:
        out_str: a string containing all the elements from the in_lines variable
    """

    out_str = ''
    for list_line in in_lines:
        for element in list_line:
            if element.endswith('\n'):
                out_str += element
            else:
                out_str += element
                out_str += ','
    return out_str

def file_writer(lines, out_file):
    """
    Write one string to a file.

    Keyword arguments:
        lines: a single string containing all the lines from a file
        out_file: the path to where the file needs to be written to
    Return:
        out_file: the path to where the file is written to
    """
    with open(out_file, 'w') as f:
            f.write(lines)
    return out_file

def main():
    """
    This function combines the previous functions

    argv[1]: file path to customer database
    """
    company_name = input('What is the company name?\n')
    argv = 'input.txt'
    customer_database_lines = read_csv(argv[1])
    customer_database_list = line_parser(customer_database_lines)
    comp_name_existance = list_checker(customer_database_list, company_name)
    #Check if the company name allready exists in the database
    if comp_name_existance == 'FALSE':
        comp_information = input("Supply the Address, KVK, BTW-ID and Bank account "
                                 "of the company seperated by comma's\n").split(',')
        #Check if the supplied data is of sufficient size
        list_len = list_size_checker(comp_information, 4)
        while list_len != 'TRUE':
            comp_information = input("Supply the Address, KVK, BTW-ID and Bank account "
                                     "of the company seperated by comma's\n").split(',')
            list_len = list_size_checker(comp_information, 4)
        #add space to first element to make it look better in the output file and add an enter to the last element
        comp_information[0] = ' ' + comp_information[0]
        comp_information[-1] = comp_information[-1] + '\n'
        #add company information to the customer database and write it to a file
        comp_information.insert(0, company_name)
        customer_database_list.append(comp_information)
        customer_database_str = list_to_str(customer_database)
        file_writer(customer_database_str, argv[1])
    #Get the invoice information
    invoice_inf = []
    checker = 'no'
    while checker != 'yes':
        input_invoice = \
            input("supply the invoice information description, amount, price and VAT seperated by comma's.\n").split(',')
        #Check if the information is of sufficient size.
        list_len = list_size_checker(input_invoice, 4)
        while list_len != 'TRUE':
            input_invoice = \
                input("supply the invoice information description, amount, price and VAT seperated by comma's.\n")\
                    .split(',')
            list_len = list_size_checker(input_invoice, 4)
        invoice_inf.append(input_invoice)
        checker = input('Was that everything (yes/no)?')

if __name__ == '__main__':
    main()