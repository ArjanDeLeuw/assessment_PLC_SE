# assessment_PLC_SE
The assesment of the Python Learning Community advanced track.

https://github.com/ArjanDeLeuw/assessment_PLC_SE

To do's:

* De code is niet volledig geoptimaliseerd, sommige functies kunnen achter gezien veel efficiënter;
* In de plaats van dat InvoiceDatabase de input voor de invoice naar een .csv schrijft, schrijft de script nu een .txt bestand met daarin de volledige invoice in de format zoals gegeven in het voorbeeld. Dit had ik achteraf gezien anders aangepakt.
* Ik heb in de eerste instantie CustomerData en InvoiceData (zie bijlage) in een class geschreven, maar InvoiceData neemt een verschillend aantal items en VAT-rate totals als input en is daarmee ongeschikt voor een class.
* Het was achteraf gezien misschien mogelijk geweest om ook de CustomerDatabase in een class te schrijven aangezien de input altijd dezelfde format heeft.

Scripts: 
* **CustomerData:** Class taking a list of customer information as input and returning a csv compatible format.
* **CustomerDatabase:** Read a csv with customer information, check whether the firm already exists, and write to a csv.
* **InvoiceData:** Class taking customer and invoice information and returning an invoice. Can only take 1 line item.
* **InvoiceData2:** customer and invoice information and returning an invoice. Can take multiple line items and VAT rates.
* **InvoiceDatabase:** Read a csv with invoice information, produce a dictionairy based on Invoice ID, and write to a csv.
* **InvoiceDataApp** 
  * combines all the aforementioned scripts
  * will ask for a firm name, 
  * check whether it already exists, 
    * if not, asks for company information, 
    * writes this to a database, 
  * asks for invoice information, 
  * produces the invoice 
  * writes to an invoice database 


