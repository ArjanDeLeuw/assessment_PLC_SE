from CustomerData import CD

class InvoiceData(CD):

    def __init__(self, Invoice_ID, description, price, amount, VAT_rate, firm_name, firm_address, firm_kvk,
                 firm_btw_id, firm_bank_account):
        super().__init__(firm_name, firm_address, firm_kvk, firm_btw_id, firm_bank_account)
        self.Invoice_ID = Invoice_ID
        self.description = description
        self.price = price
        self.amount = amount
        self.VAT_rate = VAT_rate

    def TotalWithoutVAT(self, amount_per_unit, number_of_units):
        total_without_VAT = amount_per_unit * number_of_units
        return total_without_VAT

    def VAT(self,amount_per_unit, number_of_units, VAT_rate):
        total_VAT = (amount_per_unit * number_of_units) * VAT_rate
        return total_VAT

    def TotalWithVAT(self, amount_per_unit, number_of_units, VAT_rate):
        total_with_VAT = (amount_per_unit * number_of_units) * (1 + VAT_rate)
        return total_with_VAT

    def InvoiceTemplate(self, firm_address, firm_kvk, firm_btw_id, firm_bank_account,
                        description, amount_per_unit, number_of_units, VAT_rate):
        ...
        return template

    def Date(self):
        ...

    def __str__(self):
        return_string = ""

        company = "{}\n {}\n {}\n {}\n {}\n\n "\
            .format("Leuw & Co", "Europapark 9", "3829741", "3747287", "NL28INGB0665801589",)

        invoice = "{}\n\n " "{}\n {}\n\n"\
            .format( "Concerning: Invoice", self.Invoice_ID, date.today())

        customer = " To: {}\n {}\n {}\n {}\n"\
            .format(self.firm_name, self.firm_address, self.firm_address, self.firm_address, self.firm_address)

        items_top_rule = "Items:\n {}\t | {}\t | {}\t | {}\t  | {}\t | {}\t | {}\t"\
            .format("Description", "Units", "Price", "ex VAT", "VAT %", "VAT", "Total")

        # for loop if X elements also do this for the input function --> while loop?
        items = "\n {}\t | {}\t | {}\t | {}\t  | {}\t | {}\t"\
            .format(self.description, self.amount, self.price,
                    self.TotalWithoutVAT(amount_per_unit, number_of_units),
                    self.VAT_rate,
                    self.VAT(self,amount_per_unit, number_of_units, VAT_rate),
                    self.TotalWithVAT(amount_per_unit, number_of_units, VAT_rate)) # description, units, price should be derived from input

        # loop again for each VAT
        totals = "\n\n\n Totals:\n total excluding VAT\t {}\n total VAT ({})\t {}\n total VAT ({})\t {}\n total\t {}"

        return_string += company + invoice + customer + items_top_rule + items + totals

        return return_string


if __name__ == '__main__':
    main()
