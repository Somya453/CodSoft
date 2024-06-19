names=[]
phone_numbers=[]

num=int(input("Enter the Contacts that you want to add:"))

for i in range(num):
    name=input("Enter Name:")
    phone_number=input("Enter Phone Number:")


    names.append(name)
    phone_numbers.append(phone_number)

print("\tName\t\t\tPhone number")

for i in range(num):
    print(f"\t{names[i]}\t\t\t{phone_numbers[i]}")

n=input('Enter the name to search:')

if n in names:
    index=names.index(n)
    name=name[index]
    phone_number=phone_numbers[index]

    print(f"Name:{name}, Phone Number:{phone_number}")
else:
    print("Name not found..")
