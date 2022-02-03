from CustomerData import CData
import CustumerDatabase as CDatabase
import InvoiceData2 as IData
import InvoiceDatabase as IDatabase

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


def main():
    """
    combines the CustomerData.py and CustomerDatabase.py:
    """

    # 1. produce input:
    customer_database = 'customer_database.txt'
    invoice_database = 'invoice_database.txt'
    company_name = input('What is the company name?\n')

    # 2. check whether input already exists:
    checker, input_customer_db = CDatabase.main(customer_database, company_name)
    if checker == 'FALSE':
        comp_information = input("Supply the Street, postal code and city, country, KVK, BTW-ID and Bank account "
                                 "of the company seperated by comma's\n").split(',')
        # Check if the supplied data is of sufficient size
        list_len = list_size_checker(comp_information, 6)
        while list_len != 'TRUE':
            comp_information = input("Supply the Street, postal code and city, country, KVK, BTW-ID and Bank account "
                                     "of the company seperated by comma's\n").split(',')
            list_len = list_size_checker(comp_information, 6)

        # 3. add company information to the customer database and write to a file
        comp_information.insert(0,company_name)
        input_customer_db = \
            str(CData(comp_information)).split(',')
        CDatabase.main(customer_database, input_customer_db)

    """
    Combines InvoiceData.py and InvoiceDataApp.py, and using information from customer: 
    """

    # 4. produce invoice and ask for line items:
    invoice_inf = []
    checker = 'no'
    while checker != 'yes':
        input_invoice = \
            input("supply the invoice information description, price, amount and VAT-rate seperated by comma's.\n")\
                .split(',')
        # Check if the information is of sufficient size.
        list_len = list_size_checker(input_invoice, 4)
        while list_len != 'TRUE':
            input_invoice = \
                input("supply the invoice information description, amount, price and VAT seperated by comma's.\n") \
                    .split(',')
            list_len = list_size_checker(input_invoice, 4)
        # continue appending line items until checker = 'yes'
        input_invoice[1:] = [int(n) for n in input_invoice[1:]]
        invoice_inf.append(input_invoice)
        checker = input('Was that everything (yes/no)?\n')
    # 5. Construct the invoice and write to a database
    invoice = IData.invoiceGenerator(invoice_inf, input_customer_db)
    IDatabase.main(invoice_database, invoice.splitlines(True))
    print(invoice)


if __name__ == '__main__':
    main()