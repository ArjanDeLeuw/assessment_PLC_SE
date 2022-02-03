from datetime import date
"""
this is the replacement for InvoiceData. We have 3 helper functions to calculate totals and the invoicegenerator
"""


def TotalWithoutVAT(amount, price):
    total_without_VAT = amount * price
    return total_without_VAT


def VAT(amount, price, VAT_rate):
    total_VAT = (amount * price) * (VAT_rate/100)
    return total_VAT


def TotalWithVAT(amount, price, VAT_rate):
    total_with_VAT = (amount * price) * (1 + VAT_rate/100)
    return total_with_VAT


def invoiceGenerator(items, customer_data):
    return_string = ""

    # standard information:
    company = "{}\n{}\n{}\n{}\n{}\n\n"\
        .format("Leuw & Co", "Europapark 9", "3829741", "3747287", "NL28INGB0665801589",)

    # 0 will be replaced by an invoice number in InvoiceDatabase:
    invoice = "Concerning: Invoice\n\nInvoice ID: {}\nInvoice data: {}\n\n"\
        .format(0, date.today())

    # use customer data:
    customer = "To:\n{}\n{}\n{}\n{}\n\n"\
        .format(customer_data[0].strip(), customer_data[1].strip(), customer_data[2].strip(), customer_data[3].strip())

    # standard top rule:
    items_top_rule = "Items:\n{:8}\t | {:8}\t | {:8}\t | {:8}\t  | {:8}\t | {:8}\t | {:8}\t"\
        .format("Description", "Units", "Price", "ex VAT", "VAT %", "VAT", "Total")

    # retrieve each line item:
    item_lines = ''
    total_ex_VAT = 0
    total_in_VAT = {}
    for item in items:
        description = item[0]
        amount = item[1]
        price = item[2]
        VAT_rate = float(item[3])

        # format line itmes
        line = "\n{:8}\t | {:8}\t | {:8}\t | {:8}\t  | {:8}\t | {:8}\t | {:8}\t "\
            .format(description, amount, price,
                    round(TotalWithoutVAT(amount, price), 2),
                    VAT_rate,
                    round(VAT(amount, price, VAT_rate), 2),
                    round(TotalWithVAT(amount, price, VAT_rate), 2))
        item_lines += line

        # Calculate total values
        total_ex_VAT += TotalWithoutVAT(amount, price)
        if VAT_rate not in total_in_VAT.keys():
            total_in_VAT[VAT_rate] = VAT(amount, price, VAT_rate)
        elif VAT_rate in total_in_VAT.keys():
            VAT_price = total_in_VAT.get(VAT_rate)
            total_in_VAT[VAT_rate] = VAT_price + VAT(amount, price, VAT_rate)

    # format totals
    total_ex_VAT = "\n\n\nTotals:\ntotal excluding VAT\t\t{}\n"\
        .format(total_ex_VAT)
    totals_in_VAT = ''
    total_VAT = 0

    # retrieve totals depending on the supplied vat rates
    for key, value in total_in_VAT.items():
        totals_in_VAT += 'total VAT ({:4}%)\t\t{}\n'.format(key, round(value, 2))
        total_VAT += value
    totals = 'total\t\t\t\t{}'.format(total_VAT)

    # produce invoice:
    return_string += company + invoice + customer + items_top_rule + item_lines + total_ex_VAT + totals_in_VAT + totals
    return return_string


if __name__ == '__main__':
    invoiceGenerator()
