def compoundintrest(amount, rateofintrest, time):
    rateofintrest = float(rateofintrest)
    totalamount = amount * (1 + (rateofintrest / 100))** time
    countintest = totalamount - amount
    return countintest, totalamount

principle = float(input("enter the princeiplal amount "))
rate = float(input("enter the rate of intrest "))
numberofyears = int(input("enter the number of years "))

countintest, totalamount = compoundintrest(15000, 5, 5)
print("intest", round(countintest), 'total amount is',  round(totalamount))

countintest, totalamount = compoundintrest(principle, rate, numberofyears)
print("intest", round(countintest), 'total amount is', round(totalamount))
