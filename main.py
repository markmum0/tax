x = "the paye deductible"
print(x.upper())
basic_pay = int(input("How much do you earn? "))
relief = 2400

# adding the housing levy which was introduced on July 2023
housing_levy = basic_pay * 0.015

def Nssf():
    if basic_pay <= 18000:
        nssf = 360
    else:
        nssf = 1080
    return nssf


print('NSSF: ' + str(Nssf()))
income = basic_pay - Nssf()

print("Taxable Income: " + str(income))


def Insurance():
    if basic_pay == 0 or basic_pay <= 5999:
        insurance = 150
    elif basic_pay == 6000 or basic_pay <= 8000:
        insurance = 300
    elif basic_pay == 8000 or basic_pay <= 11999:
        insurance = 400
    elif basic_pay == 12000 or basic_pay <= 14999:
        insurance = 500
    elif basic_pay == 15000 or basic_pay <= 19998:
        insurance = 600
    elif basic_pay == 20000 or basic_pay <= 24999:
        insurance = 750
    elif basic_pay == 25000 or basic_pay <= 29999:
        insurance = 850
    elif basic_pay == 30000 or basic_pay <= 34999:
        insurance = 900
    elif basic_pay == 35000 or basic_pay <= 39000:
        insurance = 950
    elif basic_pay == 40000 or basic_pay <= 44999:
        insurance = 1000
    elif basic_pay == 45000 or basic_pay <= 49000:
        insurance = 1100
    elif basic_pay == 50000 or basic_pay <= 59999:
        insurance = 1200
    elif basic_pay == 60000 or basic_pay <= 69999:
        insurance = 1300
    elif basic_pay == 70000 or basic_pay <= 79999:
        insurance = 1400
    elif basic_pay == 80000 or basic_pay <= 89999:
        insurance = 1500
    elif basic_pay == 90000 or basic_pay <= 99999:
        insurance = 1600
    else:
        insurance = 1700
    return insurance


def Income_tax():
    global income_tax
    if income < 24000:
        income_tax = 0
    elif income <= 24000:
        income_tax = (income * 0.10)
    elif income == 24001 or income <= 32334:
        tier1 = (24000 * 0.10)
        tier2 = (income - 24000) * 0.25
        income_tax = tier1 + tier2
    elif income >= 32334:
        tier1 = (24000 * 0.10)
        tier2 = (32333 * 0.25)
        tier3 = (income - 32333) * 0.30
        income_tax = tier1 + tier2 + tier3
    return income_tax


print('Income Tax: ' + str(Income_tax()))
insurance_relief = Insurance() * 0.15
print('Insurance Relief (NHIF): ' + str(insurance_relief))
print('Personal Relief: ' + str(relief))

paye = Income_tax() - insurance_relief - relief
print('P.A.Y.E: ' + str(paye))

pay_after_tax = income - paye
print('PAY AFTER TAX: ' + str(pay_after_tax))
print('NHIF: ' + str(Insurance()))
# printing the housing levy
print('Housing Levy: '+ str(housing_levy))
net_pay = pay_after_tax - Insurance() - housing_levy
print('NET PAY: ' + str(net_pay))
