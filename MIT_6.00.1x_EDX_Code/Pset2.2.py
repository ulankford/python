balance = 3926
originalbalance = balance
annualInterestRate = 0.2


months = 12
minpayment = 10
unpaidbalance = 0
interest = 0
originalbalance = balance

while (balance >= 0):
    for m in range(12) :
        unpaidbalance = balance - minpayment
        interest = (annualInterestRate*unpaidbalance)/12
        balance = unpaidbalance + interest
        if (balance <= 0):
            break
    if (balance <= 0):
            break
    balance = originalbalance
    minpayment = minpayment + 10
print "Lowest Payment: ", minpayment
    
    