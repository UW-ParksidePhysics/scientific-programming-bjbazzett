nest_egg = 1000
years = 3
interest_rate  = 4.31
interest = nest_egg * (1+ (interest_rate/100)) ** years - nest_egg

print("initial amount $", nest_egg)
print("interest rate", interest_rate)
print("growth amount $", interest)