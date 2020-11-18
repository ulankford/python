balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

#months = 12
minpayment = 10
unpaidbalance = 0
interest = 0
totalpaid = 0

for m in range(12) :
    minpayment = balance * monthlyPaymentRate
    unpaidbalance = balance - minpayment
    interest = (annualInterestRate*unpaidbalance)/12
    balance = unpaidbalance + interest
    totalpaid = totalpaid + minpayment
    print "Month: ", m+1
    print "Minimum monthly payment: ", round(minpayment,2)
    #print "unpaidbalance", unpaidbalance
    #print "interest", interest
    print "Remaining balance: ", round(balance,2)
print "Total paid: " , round(totalpaid,2)
print "Remaining balance: ", round(balance,2)
    
    
    