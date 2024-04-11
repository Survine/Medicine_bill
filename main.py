from medicine import Medicine
from user import User
from bill import Bill

def main():
    user_name = input("Enter User Name: ")
    num_medicines = int(input("Enter the types of medicines to purchase: "))

    medicines = []
    for i in range(num_medicines):
        name = input(f"Enter medicine name #{i+1}: ")
        quantity = int(input(f"Enter quantity of {name}: "))
        medicines.append(Medicine(name, quantity))

    user = User(user_name)
    bill = Bill(user, medicines)

    bill.print_bill()

if __name__ == "__main__":
    main()
