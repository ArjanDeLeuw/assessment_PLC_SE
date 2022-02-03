import os

"""
this script contains all the functions to:
 read a csv containing customers, 
 check whether the customer already exists, 
 and write to a csv 
"""


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


def csv_checker(in_lines, comp_name):
    """
    This function checks if the company name is allready in the database

    Keyword arguments:
        in_lines: list of lists where each list is a line in the file
        comp_name: string containing the company name
    Return:
        checker: TRUE if the company name is allready in the database and FALSE if the customer is not in the database
        out_line: if the company exists get the line
    """
    checker = 'FALSE'
    out_line = None
    #If only a string with the company name is supplied:
    if isinstance(comp_name, str):
        for line in in_lines[1:]:
            if line[0] == comp_name:
                checker = 'TRUE'
                out_line = line
                break
            else:
                continue
    return checker, out_line


def line_editor(in_lines, add_line):
    """
    This function appends a given line to the list of lists.

    Keyword arguments:
        in_lines: list of lists where each list contains one line.
        add_line: a list containing the line that should be added.
    return:
        in_lines: a list of lists containing all the supplied lines.
    """
    #If the file does not exist then the length of lines will be 0.
    if len(in_lines) > 0:
        in_lines.append(add_line)
    else:
        in_lines = []
        in_lines.append(["Firm name", "Street", "postal code and city", "Country", "KVK", "BTW-ID", "Bank account\n"])
        #remove spaces if present
        new_line = [data.strip() for data in add_line]
        new_line[-1] = new_line[-1] + '\n'
        in_lines.append(new_line)
    return in_lines


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


def main(file, new_customer):
    """
    This function combines all previous functions

    file: the input/output file containing the contact information
    new_customer: a list containing a line of contact information OR a string containing only the company name
    """
    file_lines = read_csv(file)
    list_lines = line_parser(file_lines)
    custemor_exists, custemor_line = csv_checker(list_lines, new_customer)
    if custemor_exists == 'TRUE':
        print('Existing customer')
    else:
        #Only proceed when the full line is given
        if isinstance(new_customer, list):
            out_lines = line_editor(list_lines, new_customer)
            out_line_str = list_to_str(out_lines)
            file_writer(out_line_str, file)
    return custemor_exists, custemor_line


if __name__ == '__main__':
    main()


