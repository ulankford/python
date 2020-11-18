h = 100
l = 0
num = (h-l)/2
c = str
ans = 'l'

print "Please think of a number between 0 and 100!"
while (ans != 'c'):
    #print "Sorry, I did not understand your input"
    print "Is your secret number: ", num
    ans=raw_input('Enter ''h'' to indicate the guess is too high. Enter ''l'' to indicate the guess is too low. Enter ''c'' to indicate I guessed correctly. ')
    if (ans == 'h'):
        h = num
        x=((h-l)/2)
        num = l+x
    elif (ans == 'l'):
        l = num
        x=((h-l)/2)
        num = l+x
    elif (ans == 'c'):
        break
    elif ((ans != 'c') or (ans != 'l') or (ans != 'h')):
         print "Sorry, I did not understand your input."
print "Game over. Your secret number was: ", num