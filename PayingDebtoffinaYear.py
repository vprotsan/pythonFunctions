########################################################################
# Test Case 1:
# balance = 42
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04

# Result Your Code Should Generate Below:
# Remaining balance: 31.38
########################################################################

########################################################################
#Test Case 2:
# balance = 484
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04

# Result Your Code Should Generate Below:
# Remaining balance: 361.61
########################################################################



########################################################################
# month = 1
# while month <= 12:
#     monthlyInterestRate= annualInterestRate / 12.0
#     minimumMonthlyPayment = monthlyPaymentRate * balance
#     monthlyUnpaidBalance = balance - minimumMonthlyPayment
#     balance = round(monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance, 2)
#     # print("Month " + str(month) + " Remaining balance: " + str(balance))
#     month += 1
#
# print("Remaining balance: " + str(balance))
########################################################################



#with fixed minimum payment
########################################################################
# Test Case 1:
# balance = 3329
# annualInterestRate = 0.2
# minimumFixedMonthlyPayment = 10
# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 310

#Test Case 2:
# balance = 4773
# annualInterestRate = 0.2
# minimumFixedMonthlyPayment = 10

# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 440

#Test Case 3
balance = 19;
annualInterestRate = 0.18
########################################################################


########################################################################
minimumFixedMonthlyPayment = 10
total = balance
if minimumFixedMonthlyPayment * 12 > balance:
    print("Lowest Payment: " + str(minimumFixedMonthlyPayment))

while balance > 0:
    balance = total
    minimumFixedMonthlyPayment += 10
    for el in range(12):
        monthlyInterestRate = annualInterestRate / 12.0
        monthlyUnpaidBalance = balance - minimumFixedMonthlyPayment
        balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
print("Lowest Payment: " + str(minimumFixedMonthlyPayment))
########################################################################
