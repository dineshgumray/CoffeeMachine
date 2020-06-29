# print("Starting to make a coffee")
# print("Grinding coffee beans")
# print("Boiling water")
# print("Mixing boiled water with crushed coffee beans")
# print("Pouring coffee into the cup")
# print("Pouring some milk into the cup")
# print("Coffee is ready!")

# print("Write how many cups of coffee you will need: ")
# number = int(input().strip())
# print("For {} cups of coffee you will need: ".format(number))
# print(str(200 * number) + " ml of water")
# print(str(50 * number) + " ml of milk")
# print(str(15 * number) + " g of coffee beans")

# print("Write how many ml of water the coffee machine has: ")
# water = int(input()) // 200
#
# print("Write how many ml of milk the coffee machine has: ")
# milk = int(input()) // 50
#
# print("Write how many grams of coffee beans the coffee machine has: ")
# coffee_beans = int(input()) // 15
#
# print("Write how many cups of coffee you will need: ")
# cups = int(input())
#
# if water < milk:
#     if water < coffee_beans:
#         totalCups = water
#     else:
#         totalCups = coffee_beans
# else:
#     if milk < coffee_beans:
#         totalCups = milk
#     else:
#         totalCups = coffee_beans
#
# if totalCups == 1 and cups > 0:
#     print("Yes, I can make that amount of coffee")
# elif totalCups >= cups:
#     print("Yes, I can make that amount of coffee (and even {} more than that)".format(totalCups - cups))
# else:
#     print("No, I can make only {} cups of coffee".format(totalCups))

# water = 400
# milk = 540
# coffee_beans = 120
# cups = 9
# money = 550
#
# print("The coffee machine has: ")
# print("{} of water".format(water))
# print("{} of milk".format(milk))
# print("{} of coffee beans".format(coffee_beans))
# print("{} of disposable cups".format(cups))
# print("{} of money".format(money))
#
# print("Write action (buy, fill, take): ")
# option = input()
#
# if option == "buy":
#     print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
#     buy_option = input()
#
#     if buy_option == "1":
#         water -= 250
#         coffee_beans -= 16
#         money += 4
#     elif buy_option == "2":
#         water -= 350
#         milk -= 75
#         coffee_beans -= 20
#         money += 7
#     else:
#         water -= 200
#         milk -= 100
#         coffee_beans -= 12
#         money += 6
#
#     cups -= 1
#
# elif option == "fill":
#     print("Write how many ml of water do you want to add: ")
#     water += int(input())
#
#     print("Write how many ml of milk do you want to add: ")
#     milk += int(input())
#
#     print("Write how many grams of coffee beans do you want to add: ")
#     coffee_beans += int(input())
#
#     print("Write how many disposable cups of coffee do you want to add: ")
#     cups += int(input())
#
# else:
#     print("I gave you ${}".format(money))
#     money = 0
#
# print("The coffee machine has: ")
# print("{} of water".format(water))
# print("{} of milk".format(milk))
# print("{} of coffee beans".format(coffee_beans))
# print("{} of disposable cups".format(cups))
# print("{} of money".format(money))

# water = 400
# milk = 540
# coffee_beans = 120
# cups = 9
# money = 550

# print("The coffee machine has: ")
# print("{} of water".format(water))
# print("{} of milk".format(milk))
# print("{} of coffee beans".format(coffee_beans))
# print("{} of disposable cups".format(cups))
# print("{} of money".format(money))

# while True:
#     print("Write action (buy, fill, take, remaining, exit): ")
#     option = input()
#     print()
#
#     if option == "buy":
#         print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
#         buy_option = input()
#         print()
#         if buy_option == "1":
#             if water >= 250 and coffee_beans >= 16 and cups >= 0:
#                 print("I have enough resources, making you a coffee!\n")
#                 water -= 250
#                 coffee_beans -= 16
#                 cups -= 1
#                 money += 4
#             else:
#                 if water < 250:
#                     print("Sorry, not enough water!\n")
#                 elif coffee_beans < 16:
#                     print("Sorry, not enough coffee beans!\n")
#                 else:
#                     print("Sorry, not enough disposable cups!\n")
#
#         elif buy_option == "2":
#             if water >= 350 and milk >= 75 and coffee_beans >= 20 and cups >= 0:
#                 print("I have enough resources, making you a coffee!\n")
#                 water -= 350
#                 milk -= 75
#                 coffee_beans -= 20
#                 cups -= 1
#                 money += 7
#             else:
#                 if water < 350:
#                     print("Sorry, not enough water!\n")
#                 elif milk < 75:
#                     print("Sorry, not enough milk!\n")
#                 elif coffee_beans < 20:
#                     print("Sorry, not enough coffee beans!\n")
#                 else:
#                     print("Sorry, not enough disposable cups!\n")
#
#         elif buy_option == "3":
#             if water >= 200 and milk >= 100 and coffee_beans >= 12 and cups >= 0:
#                 print("I have enough resources, making you a coffee!\n")
#                 water -= 200
#                 milk -= 100
#                 coffee_beans -= 12
#                 cups -= 1
#                 money += 6
#             else:
#                 if water < 200:
#                     print("Sorry, not enough water!\n")
#                 elif milk < 100:
#                     print("Sorry, not enough milk!\n")
#                 elif coffee_beans < 12:
#                     print("Sorry, not enough coffee beans!\n")
#                 else:
#                     print("Sorry, not enough disposable cups!\n")
#
#         else:
#             continue
#
#     elif option == "fill":
#         print("Write how many ml of water do you want to add: ")
#         water += int(input())
#
#         print("Write how many ml of milk do you want to add: ")
#         milk += int(input())
#
#         print("Write how many grams of coffee beans do you want to add: ")
#         coffee_beans += int(input())
#
#         print("Write how many disposable cups of coffee do you want to add: ")
#         cups += int(input())
#
#     elif option == "take":
#         print("I gave you ${}".format(money))
#         money = 0
#
#     elif option == "remaining":
#         print("The coffee machine has: ")
#         print("{} of water".format(water))
#         print("{} of milk".format(milk))
#         print("{} of coffee beans".format(coffee_beans))
#         print("{} of disposable cups".format(cups))
#         print("{} of money".format(money))
#         print()
#
#     else:
#         break


class CoffeeMachine:

    water = 400
    milk = 540
    coffee_beans = 120
    cups = 9
    money = 550

    def __init__(self):
        self.start()

    def buy(self, buy_option):
        if buy_option == "1":
            if self.water >= 250 and self.coffee_beans >= 16 and self.cups >= 0:
                self.water -= 250
                self.coffee_beans -= 16
                self.cups -= 1
                self.money += 4
                return "done"
            else:
                if self.water < 250:
                    return "water"
                elif self.coffee_beans < 16:
                    return "coffee beans"
                else:
                    return "cups"

        elif buy_option == "2":
            if self.water >= 350 and self.milk >= 75 and self.coffee_beans >= 20 and self.cups >= 0:
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.cups -= 1
                self.money += 7
                return "done"
            else:
                if self.water < 350:
                    return "water"
                elif self.milk < 75:
                    return "milk"
                elif self.coffee_beans < 20:
                    return "coffee beans"
                else:
                    return "cups"

        elif buy_option == "3":
            if self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 12 and self.cups >= 0:
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.cups -= 1
                self.money += 6
                return "done"
            else:
                if self.water < 200:
                    return "water"
                elif self.milk < 100:
                    return "milk"
                elif self.coffee_beans < 12:
                    return "coffee beans"
                else:
                    return "cups"

    def fill(self, water, milk, coffee_beans, cups):
        self.water += water
        self.milk += milk
        self.coffee_beans += coffee_beans
        self.cups += cups

    def take(self):
        return self.money

    def remaining(self):
        print("The coffee machine has: ")
        print("{} of water".format(self.water))
        print("{} of milk".format(self.milk))
        print("{} of coffee beans".format(self.coffee_beans))
        print("{} of disposable cups".format(self.cups))
        print("{} of money".format(self.money))
        print()

    def action(self, action_option):
        if action_option == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
            buy_option = input().strip()

            if buy_option != "back":
                status = self.buy(buy_option)
                if status != "done":
                    print(f"Sorry, not enough disposable {status}!\n")
                else:
                    print("I have enough resources, making you a coffee!\n")

        elif action_option == "fill":
            print("Write how many ml of water do you want to add: ")
            water = int(input().strip())

            print("Write how many ml of milk do you want to add: ")
            milk = int(input().strip())

            print("Write how many grams of coffee beans do you want to add: ")
            coffee_beans = int(input().strip())

            print("Write how many disposable cups of coffee do you want to add: ")
            cups = int(input().strip())

            self.fill(water, milk, coffee_beans, cups)

        elif action_option == "take":
            money = self.take()
            print("I gave you ${}".format(money))
            self.money = 0

        else:
            self.remaining()

    def start(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit): ")
            option = input().strip()
            print()
            if option == "exit":
                break
            else:
                self.action(option)


make_coffee = CoffeeMachine()
