"""
this file is obsolete. the input differs depending on the numer of line items hence a class is not suitable for the
task.
"""


class InvoiceData(CData):

    def __init__(self, invoice_inf: list, InvoiceData: list):
        super().__init__(InvoiceData)
        self.description = invoice_inf[0]
        self.price = invoice_inf[1]
        self.amount = invoice_inf[2]
        self.VAT_rate = invoice_inf[3]

    def TotalWithoutVAT(self, amount, price):
        total_without_VAT = amount * price
        return total_without_VAT

    def VAT(self,amount, price, VAT_rate):
        total_VAT = (amount * price) * VAT_rate
        return total_VAT

    def TotalWithVAT(self, amount, price, VAT_rate):
        total_with_VAT = (amount * price) * (1 + VAT_rate)
        return total_with_VAT

    def __str__(self):
        return_string = ""

        company = "{}\n{}\n{}\n{}\n{}\n\n"\
            .format("Leuw & Co", "Europapark 9", "3829741", "3747287", "NL28INGB0665801589",)

        invoice = "Concerning: Invoice\n\nInvoice ID: {}\nInvoice data: {}\n\n"\
            .format(0, date.today())

        customer = "To:\n{}\n{}\n{}\n{}\n\n"\
            .format(self.firm_name, self.firm_street, self.firm_postal_code, self.firm_country)

        items_top_rule = "Items:\n{:8}\t | {:8}\t | {:8}\t | {:8}\t  | {:8}\t | {:8}\t | {:8}\t"\
            .format("Description", "Units", "Price", "ex VAT", "VAT %", "VAT", "Total")

        # for loop if X elements also do this for the input function --> while loop?
        items = "\n{:8}\t | {:8}\t | {:8}\t | {:8}\t  | {:8}\t | {:8}\t | {:8}\t "\
            .format(self.description, self.amount, self.price,
                    self.TotalWithoutVAT(self.amount, self.price),
                    self.VAT_rate,
                    self.VAT(self.amount, self.price, self.VAT_rate),
                    self.TotalWithVAT(self.amount, self.price, self.VAT_rate))

        # loop again for each VAT
        totals = "\n\n\n Totals:\n total excluding VAT\t {}\n total VAT ({})\t {}\n total VAT ({})\t {}\n total\t {}"

        return_string += company + invoice + customer + items_top_rule + items + totals

        return return_string


if __name__ == '__main__':
    invoice = InvoiceData(['Studying', 300, 1, 3], ['Arjan', 'Brugstraat 10', '5045ZS Tilburg', 'Nederland', 234234, 23423432, 'NL90INGB23423423'])
    print(invoice)
