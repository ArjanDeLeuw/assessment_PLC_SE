class CData:
    """
    a class that:
        1. takes the customer information as input
        2. returns a string with a \n
    """

    def __init__(self, customer_data: list):
        self.firm_name = customer_data[0]
        self.firm_street = customer_data[1]
        self.firm_postal_code = customer_data[2]
        self.firm_country = customer_data[3]
        self.firm_kvk = customer_data[4]
        self.firm_btw_id = customer_data[5]
        self.firm_bank_account = customer_data[6]

    def __str__(self):
        return_string = ""
        customer_db_format = "{},{},{},{},{},{},{}\n"

        firm_string = customer_db_format.format(self.firm_name,
                                                self.firm_street,
                                                self.firm_postal_code,
                                                self.firm_country,
                                                self.firm_kvk,
                                                self.firm_btw_id,
                                                self.firm_bank_account)
        return_string += firm_string

        return return_string

