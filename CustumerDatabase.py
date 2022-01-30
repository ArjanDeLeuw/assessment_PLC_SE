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

def csv_checker(lines, add_line):
    """Check if the line you want to add is allready in the database.

    Keyword arguments
        lines: a list of lists containing all the lines in a file
        add_line: a list that should be added to the file
    Return:
        checker: Boolean value which indicates if the line is allready in the file
    """
    checker = 'TRUE'

    # Check if the line allready exists
    for line in lines:
        if add_line == line:
            checker = 'FALSE'
            break
    return checker

def enter_editor(in_lines):
    """
    This function appends an enter to the last element of a line if this is not present

    Keyword arguments:
        in_lines: a list of lists where one list is a line
    Return:
        out_list: same list of lists as in_lines but with an added enter
    """

    for line in in_lines:
        if line[-1].endswith('\n'):
            break
        else:
            line[-1] = line[-1] + '\n'
    return in_lines

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
        in_lines = ["Firm name", "Address", "KVK", "BTW-ID", "Bank account\n"]
        in_lines.append(add_line)
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

def main():
    """
    This function combines all previous functions

    argv[1]: the input/output file containing the contact information
    argv[2]: a list containing a line of contact information
    """
    added_line = argv[2]
    added_line[-1] = added_line[-1] + '\n'
    file_lines = read_csv(argv[1])
    list_lines = line_parser(file_lines)
    custemor_exists = csv_checker(list_lines, added_line)
    if custemor_exists == 'FALSE':
        print('already exists')
    else:
        list_lines = enter_editor(list_lines)
        out_lines = line_editor(list_lines, added_line)
        out_line_str = list_to_str(out_lines)
        file_writer(out_line_str, argv[1])

if __name__ == '__main__':
    main()


