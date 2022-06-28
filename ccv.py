print("Credit Card Validation")

while(1):
    print("enter a card number")
    creditCardNumber = int(input())
    workingCC = creditCardNumber
    suma = 0;
    count = 0;
    divisor = 10;
    while (workingCC > 0):
         lastDigit = int(workingCC % 10)
         suma = int(suma) + lastDigit
         workingCC = workingCC / 100

    workingCC = creditCardNumber / 10     
    while (workingCC > 0) :
        lastDigit =int(workingCC % 10)
        timesTwo = lastDigit * 2
        suma = int(suma) + (timesTwo % 10) + (timesTwo / 10)
        workingCC = workingCC / 100

    workingCC = creditCardNumber    
    while (workingCC != 0):
        workingCC = int(workingCC / 10)
        count=count+1
    for i in range(count - 2):
        divisor = divisor * 10
                
    firstDigit = creditCardNumber / divisor
    firstTwoDigits = creditCardNumber / (divisor // 10)
    
    if (int(suma % 10) == 0):
       if (int(firstDigit) == 4 and (int(count) == 13 or int(count) == 16)):
            print("VISA")
       elif ((int(firstTwoDigits) == 34 or int(firstTwoDigits) == 37) and int(count) == 15):
           print("AMEX")
       elif ((50 < int(firstTwoDigits) and int(firstTwoDigits) < 56) and int(count) == 16):
           print("MASTERCARD")
       else:
           print("INVALID")
    else :
        print("INVALID")
        
 


