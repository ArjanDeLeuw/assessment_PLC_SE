import os
"""
this script contains all the functions to:
 read a csv containing invoices, 
 produce a dictionairy based in Invoice ID, 
 and write to a csv file
"""


def read_invoice(in_file):
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


def line_parser(in_lines):
    """
    This function divides the string in a list of list where each list is one invoice.

    Keyword arguments:
        in_lines: a list containing all the lines from the file
    Return:
        parsed_lines: list of list where each list contains lines from one invoice
    """
    parsed_lines = []

    for i in range(len(in_lines)):
        if in_lines[i].startswith('Invoice ID'):
            start_invoice = i-8
            for it in range(i, len(in_lines)):
                if in_lines[it].startswith('total\t'):
                    end_invoice = it + 1
                    break
            parsed_lines.append(in_lines[start_invoice:end_invoice])
    return parsed_lines


def lines_to_dict(in_list):
    """
    This function puts the list with all the lines in a dictionary where the invoice number is the key and the
    lines are the value.

    Keyword arguments:
        in_list: a list of lists where each list contains the lines from one invoice
    Return:
        out_dict: dictionary with invoice number as key and list with all the lines as value
    """

    out_dict = {}
    for invoice in in_list:
        for element in invoice:
            if element.startswith('Invoice ID'):
                key = element[12:].strip()
        out_dict[key] = invoice
    return out_dict


def add_invoice(invoice_dict, add_invoice):
    """
    This function adds an invoice to the dictionary containing the other invoices.

    Keyword arguments:
         invoice_dict: a dictionary where the key is the invoice ID and the value is a list with all the lines from
         the invoice.
         add_invoice: a list with all the lines of the invoice which should be added
    Return:
        invoice_dict: the invoice dict with the added invoice
    """

    #Check if the list is of sufficient length
    if len(add_invoice) >= 26:
        if len(invoice_dict.keys()) > 0:
            add_invoice[0] = '\n\n' + add_invoice[0]
            add_invoice[8] = 'Invoice ID: ' + str(int(list(invoice_dict.keys())[-1]) + 1) + '\n'
        else:
            add_invoice[8] = 'Invoice ID: 1\n'
        key = add_invoice[8][12:].strip('\n')
        invoice_dict[key] = add_invoice
    return invoice_dict


def dict_to_str(invoices_dict):
    """
    This function converts all the values from a dictionary to one string

    Keyword value
        invoices_dict: a dictionary where the values is a list
    Return:
        out_str: a string containing all the values from the invoices_dict.
    """

    out_str = ''
    for key, value in invoices_dict.items():
        for element in value:
            out_str += element
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


def main(file, invoice_list):
    """
    This function combines all other functions in this script

    file: path to the invoice database
    invoice_list: is a list containing all the lines from an invoice that should be added
    """
    list_lines = read_invoice(file)
    invoice_sep = line_parser(list_lines)
    invoice_dict = lines_to_dict(invoice_sep)
    invoice_dict = add_invoice(invoice_dict, invoice_list)
    invoice_out_str = dict_to_str(invoice_dict)
    file_writer(invoice_out_str, file)


if __name__ == '__main__':
    main('invoice.txt', 'no')