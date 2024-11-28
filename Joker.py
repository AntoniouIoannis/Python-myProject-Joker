import random

display_numbers45 = list(range(1,46))
display_numbers20 = list(range(1,21))
random_numbers5 = []
random_number1 = []

print("\n\nΣΗΜΕΡΙΝΗ ΚΛΗΡΩΣΗ JOKER\n")
print("Οι 45 αριθμοί επιλογής της τυχερής πεντάδας")
for i in range(9):
    for j in range(5):
        print(display_numbers45[i * 5 + j], end=" ")
    print()


    
print("\nΟι 20 αριθμοί επιλογής JOKER")
for i in range(4):
    for j in range(5):
        print(display_numbers20[i * 5 + j], end=" ")
    print()

print("\nΓίνεται η κλήρωση.......")

#******************random gia toys 5 ari8mous*****************
for _ in range(5):  # Loop runs 5 times
    num5 = display_numbers45.pop(random.randint(0, len(display_numbers45)-1)) #  45 στοιχεια [ 0-44 ]
    random_numbers5.append(num5) 
         

#Print the generated list of random numbers
print("Οι πέντε τυχεροί αριθμοί είναι οι: ", random_numbers5)

#************random gia to joker*****************

for _ in range(1):  # Loop runs 10 times
    num1 = random.randint(1, 20)  # Generate a random integer between 1 and 100
    random_number1.append(num1)  # Append the generated number to the list

# Print the generated list of random numbers
print("Ο αριθμός JOKER είναι ο: ", random_number1)

print("\n\nΕΥΧΑΡΙΣΤΟΥΜΕ ΠΟΥ ΣΥΜΜΕΤΕΙΧΑΤΕ ΜΑΖΙ ΜΑΣ\nΠΑΙΞΤΕ ΥΠΕΥΘΥΝΑ!")
    
        