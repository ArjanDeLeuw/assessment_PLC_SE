class CD:
    """
    a class that:
        1. takes the customer information as input
        2. checks whether the customer already exists in a .csv database
            a. if true, do nothing or print 'already exists'
            b. if false, append the customer information

    so we have a .csv input file containing all customers
    we have to check whether the customer already exists
    and we have to generate an output file (overwrite input) with the new customer, if there is one

    finally, i do not think that a class is needed to do this properly

    """

    def __init__(self, firm_name, firm_address, firm_kvk, firm_btw_id, firm_bank_account):
        self.firm_name = firm_name
        self.firm_address = firm_address
        self.firm_kvk = firm_kvk
        self.firm_btw_id = firm_btw_id
        self.firm_bank_account = firm_bank_account

    def __str__(self):
        return_string = ""
        customer_db_format = "{},{},{},{},{}\n"
        # return_string += customer_db_format.format("Firm name", "Address", "KVK", "BTW-ID", "Bank account")

        firm_string = customer_db_format.format(self.firm_name,
                                                self.firm_address,
                                                self.firm_kvk,
                                                self.firm_kvk,
                                                self.firm_btw_id,
                                                self.firm_bank_account)
        return_string += firm_string

        return return_string


if __name__ == '__main__':
    customer = CD("CBL", "Brugstraat 8", "3728473", "748472", "NL28INGB0665801599")
    print(customer)
