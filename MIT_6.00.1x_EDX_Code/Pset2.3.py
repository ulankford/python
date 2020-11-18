balance = 320000
annualInterestRate = 0.2

monthlyrate = annualInterestRate/12
originalbalance = balance
startmin = 0
startmax = 0
unpaidbalance = 0
paymentrate = 0
epsilon=0.0001

startmin = balance/12
#print "Startmin", startmin
startmax = (balance*(1+monthlyrate)**12)/12
#print "Startmax", startmax

while (balance > 0  or balance < 0):
    paymentrate = (startmax-startmin)/2+startmin
    #print "paymentrate", paymentrate
    for month in range(12):
            unpaidbalance = balance - paymentrate
            #print "unpaidbalance" , unpaidbalance
            interest = (annualInterestRate*unpaidbalance)/12
            balance = unpaidbalance + interest
            #print "Month: ", month+1
            round(balance,2) 
            #print "Balance", balance
    round(balance,2)   
    
    if (balance <= 0.01 and balance >= 0 ):
        break
    elif (balance < epsilon):
        startmax = paymentrate
        balance = originalbalance
    elif (balance > epsilon):
        startmin = paymentrate
        balance = originalbalance
        
#print "paymentrate", paymentrate
#print "Balance", balance
paymentrate=round(paymentrate, 2)
print "Lowest Payment: ", paymentrate
        
    
