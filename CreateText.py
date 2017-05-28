import random
import csv

a = "abcdefghijklmnopqrstuvwxyz"
digit = "1234567890"
specialSymbols = '!@#$%^&*(){}[]'
Alphabets = a.upper() + a.lower() + digit + specialSymbols

with open('trainingData.txt', 'w') as txtfile:
    for i in range(1000):
        write = []
        temp = ''.join(random.sample(Alphabets,random.randint(5,8)))
        if len(temp) == 5:
            write.extend([temp,str(0)])
            txtfile.write(write[0] + "," + write[1] + "\n")
        if len(temp) == 6:
            write.extend([temp,str(1)])
            txtfile.write(write[0] + "," + write[1] + "\n")
        if len(temp) == 7:
            write.extend([temp,str(2)])
            txtfile.write(write[0] + "," + write[1] + "\n")
        if len(temp) == 8:
            write.extend([temp,str(3)])
            txtfile.write(write[0] + "," + write[1] + "\n")

print("File created Succesfully")
