#asking the user to enter the temperature
temprature=float(input("enter the temperature "))
farenhiet=(temprature*1.8)+32
print("the temperature in farenhiet is ",farenhiet)
if farenhiet>104:
 print("the temperature is hot")
elif farenhiet<40:
    print("the temperature is cold")
else:
    print("the temperature is normal")    