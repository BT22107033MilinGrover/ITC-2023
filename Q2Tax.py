gross_income=float(input("Gross Income:"))
no_of_dependent=int(input("Number Of Dependents:"))

standard_deduction=10000
dependent_deduction=300
tax_rate=0.2


taxable_income= (gross_income)-(standard_deduction)-(no_of_dependent*dependent_deduction)

tax=taxable_income*tax_rate

print("tax to be payed:",tax)