principle = float(input("Enter the principle: "))
rate = float(input("Enter the rate in %: "))
time = float(input("Enter the time in years: "))
simple_interest = (principle*rate*time)/100
print(simple_interest,"Rs.")
print("Amount = ",simple_interest+principle,"Rs.")