from random import randint

numbers = []

# generating single number


def generate_number(number_code):
    phone_number = number_code
    step = 0
    while step < 8:
        random_number = randint(0, 9)
        phone_number = phone_number+str(random_number)
        step = step + 1
    print(phone_number)
    return phone_number

# generate numbers as many as user want


def generate_numbers(amount, number_code):
    step = 0
    while step < amount:
        number = generate_number(number_code)
        numbers.append(number)
        step = step + 1


amount = int(input("How much number you want to generate: "))
choice = int(input("""
1. GP with old -> 017
2. GP with new -> 013
3. Airtel -> 016
4. Banglalink -> 019
5. Banglalink -> 014
6. Robi -> 018
7. Teletalk -> 015
8. All Numbers
Which number you want to generate: """))

if choice == 1:
    generate_numbers(amount, "017")
elif choice == 2:
    generate_numbers(amount, "013")
elif choice == 3:
    generate_numbers(amount, "016")
elif choice == 4:
    generate_numbers(amount, "019")
elif choice == 5:
    generate_numbers(amount, "014")
elif choice == 6:
    generate_numbers(amount, "018")
elif choice == 7:
    generate_numbers(amount, "015")
elif choice == 8:
    generate_numbers(amount, "017")
    generate_numbers(amount, "013")
    generate_numbers(amount, "019")
    generate_numbers(amount, "014")
    generate_numbers(amount, "016")
    generate_numbers(amount, "018")
    generate_numbers(amount, "015")
else:
    print("Something work!! Please choose option correctly")
    exit(0)

with open("phone_numbers.txt", "a") as numberfile:
    for number in numbers:
        numberfile.write(number + "\n")
    print("Genarated numbers saved on phone_numbers.txt file")
