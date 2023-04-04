#required input values for gross income so as to calculate the tax
gross_income=float(input("Gross Income:"))
no_of_dependent=int(input("Number Of Dependents:"))
#given values in the question at which the tax depends
standard_deduction=10000
dependent_deduction=300
tax_rate=0.2 #20%=20/100=0.2

#calculating taxable income based off the equation using *,- operators
taxable_income= (gross_income)-(standard_deduction)-(no_of_dependent*dependent_deduction)
#calculating tax by the * operator
tax=taxable_income*tax_rate

print("tax to be payed:",tax)
