import csv
import datetime
import Pizza
import Menu
import Decorator


# It takes the information from the customer and saves it to the Excel file with the order information.
def Payment():
    print("-----------------------------------")
    print("Please Enter Customer Information.")
    Name = input("Enter your name: ")
    Surname = input("Enter your surname: ")
    ID_No = input("Enter your ID number: ")
    Card_No = input("Enter your credit card number: ")
    Card_Password = input("Enter the card password: ")
    Order_Date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    Data = [Name, Surname, ID_No, Card_No, Card_Password, Order_Date]

    with open('Orders_Database.csv', mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        if file.tell() == 0:
            writer.writerow(["Name", "Surname", "ID_No", "Card_No", "Card_Password", "Order_Date"])
        writer.writerow(Data)
    file.close()

    print("Your Payment Was Successful.")


# Creates an extra material menu and makes multiple selections.
def component():
    listMeterials = []
    componentCost = 0
    sumComponent = ""
    while True:
        menu.choice_the_compenent()
        componentChoice = input("Select the Materials You Want to Add and Press 0 Key To Proceed To Payment Section: ")
        if componentChoice.isnumeric():
            compChoice = int(componentChoice)
            if compChoice == 1:
                if 'Olive' not in sumComponent:
                    sumComponent = sumComponent + str(Decorator.Olive.OliveDesc()) + " "
                componentCost = componentCost + int(Decorator.Olive.OliveCost())
            elif compChoice == 2:
                if 'Mushroom' not in sumComponent:
                    sumComponent = sumComponent + str(Decorator.Mushroom.MushroomDesc()) + " "
                componentCost = componentCost + int(Decorator.Mushroom.MushroomCost())
            elif compChoice == 3:
                if 'Cheese' not in sumComponent:
                    sumComponent = sumComponent + str(Decorator.Cheese.CheeseDesc()) + " "
                componentCost = componentCost + int(Decorator.Cheese.CheeseCost())
            elif compChoice == 4:
                if 'Sausage' not in sumComponent:
                    sumComponent = sumComponent + str(Decorator.Sausage.SausageDesc()) + " "
                componentCost = componentCost + int(Decorator.Sausage.SausageCost())
            elif compChoice == 5:
                if 'Onion' not in sumComponent:
                    sumComponent = sumComponent + str(Decorator.Onion.OnionDesc()) + " "
                componentCost = componentCost + int(Decorator.Onion.OnionCost())
            elif compChoice == 6:
                if 'Sweetcorn' not in sumComponent:
                    sumComponent = sumComponent + str(Decorator.Sweetcorn.SweetcornDesc()) + " "
                componentCost = componentCost + int(Decorator.Sweetcorn.SweetcornCost())
            elif compChoice == 7:
                if 'nothing' not in sumComponent:
                    sumComponent = sumComponent + str(Decorator.Nothing.NothingDesc()) + "Nothing"
                componentCost = componentCost + int(Decorator.Nothing.NothingCost())
            elif compChoice == 0:
                listMeterials.append(sumComponent)
                listMeterials.append(componentCost)
                break
            else:
                print("\nMAKE THE RIGHT CHOICE!")
        else:
            print("\nPLEASE ENTER THE NUMBER!")
    return listMeterials


# Creates a menu and makes a selection.
while True:
    menu = Menu.Menu()
    menu.choice_menu()
    choice = int(input("Please Choose a Pizza Base: "))
    if choice == 1:
        Classic_Pizza = Pizza.Classic()
        result = component()
        print("\nDescription-> " + Classic_Pizza.get_description("Classic Pizza") + "\n" +
              "Materials-> " + result[0])
        print("Cost-> " + str(Classic_Pizza.get_cost(30) + result[1]))

    elif choice == 2:
        Margharita_Pizza = Pizza.Margherita()
        result = component()
        print("\nDescription-> " + Margharita_Pizza.get_description("Margharita Pizza") + "\n" +
              "Materials-> " + result[0])
        print("Cost-> " + str(Margharita_Pizza.get_cost(35) + result[1]))

    elif choice == 3:
        BBQChicken_Pizza = Pizza.BBQ()
        result = component()
        print("\nDescription-> " + BBQChicken_Pizza.get_description("BBQ Chicken Pizza") + "\n" +
              "Materials-> " + result[0])
        print("Cost-> " + str(BBQChicken_Pizza.get_cost(40) + result[1]))

    elif choice == 4:
        FourCheese_Pizza = Pizza.FourCheese()
        result = component()
        print("\nDescription-> " + FourCheese_Pizza.get_description("Four Cheese Pizza") + "\n" +
              "Materials-> " + result[0])
        print("Cost-> " + str(FourCheese_Pizza.get_cost(45) + result[1]))

    else:
        print("\nMAKE THE RIGHT CHOICE!")
    Payment()
    break
