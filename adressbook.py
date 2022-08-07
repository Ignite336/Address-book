# Project: 'Address Book'
# Created by Ignite336

# People that are mainly added without a user interupt

John = {"Name: John", "Age: 26", "Phone: 135432453"}
Isabell = {"Name: Isabell", "Age: 19", "Phone: 16756487"}

people = [John, Isabell]

# Main Loop of the program

def main():

    user_input = input("Enter add to add another person or check to see all of people in it (add/check): ")

    if user_input == "check":
        print(people)
        main()
    if user_input == "add":
        name = input("Enter name: ")
        age = input("Enter age: ")
        phone = input("Enter phone")

        add = {name, age, phone}
        people.append(add)
        main()

main()