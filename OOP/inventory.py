from tabulate import tabulate

class Shoes():
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost
    
    def get_quantity(self):
        return self.quantity

    def get_country(self):
        return self.country

    def get_code(self):
        return self.code
    
    def get_product(self):
        return self.product

    #This function allocates the new quantity that the user enters for a product.
    def set_quantity(self, new_quant):
        self.quantity = new_quant

    
    def __str__(self) :
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}\n".upper()

#--------------functions---------------
# The empty list of shoe objects
shoe_obj_list = []
# print(shoe_obj_list)

def read_shoes_data():
    
    infile = None
    try:
        with open('inventory.txt', 'r+', encoding='utf-8') as infile:
            next(infile) #skip the first line
            inventory_info = infile.read()
            inventory_lines = inventory_info.split("\n")

            for line in inventory_lines:
                shoe_details = line.strip().split(",") # Split on the space, and store the results in a list of two strings
                #creating a shoes object
                # shoe_obj = Shoes(shoe_details[0], shoe_details[1],shoe_details[2], shoe_details[3], shoe_details[4])
                if len(shoe_details) == 5:
                    shoe_obj = Shoes(*shoe_details)
                    shoe_obj_list.append(shoe_obj)

    except FileNotFoundError:
            print("file {} does not exist".format('inventory.txt'))

    finally:
        if infile is not None:
            infile.close()

    
def capture_shoes():
    
    user_coutry = str(input("Enter the country of the shoe: "))
    user_code = int(input("Enter the code if the shoes: "))
    user_product = str(input("Enter the product: "))
    user_cost = float(input("Enter the cost of the shoe:"))
    user_quanty = int(input("Enter the quantity: "))

    user_shoe = Shoes(user_coutry, user_code, user_product, user_cost, user_quanty)

    shoe_obj_list.append(user_shoe)

def view_all():
    country = []
    code = []
    product = []
    cost = []
    table  = []
    quantity = []

    for lines in shoe_obj_list:
        country.append(lines.get_country())
        code.append(lines.get_code())
        product.append(lines.get_product())
        cost.append(lines.get_cost())
        quantity.append(lines.get_quantity())

    table = zip(country, code, product, cost, quantity)

    print(tabulate(table, headers = ('Country','Code', 'Product', 'Cost', 'Quantity'), tablefmt='fancy_grid'))


def restock():

    # restock_list = []
    # country = []
    # code = []
    # product = []
    # cost = []
    # quantity = []
    # table = []

    #Finding the shoe with the lowest quantity 
    # shoe_obj_list.sort(key=lambda x:x.quantity)
    min_quantity_shoe = min(shoe_obj_list, key=lambda x:x.quantity)
    print(f"{min_quantity_shoe.product} has the lowest quantity.")
    restock_choice = input("Would you like to restock this shoes? (y/n)").lower()

    if restock_choice == 'y':
        quantity = int(input(f"Enter the quantity you want to add: "))
        min_quantity_shoe.quantity = quantity
        with open('inventory.txt', 'r+') as outfile:
            next(outfile)  #skip the first line in the file
            lines = outfile.readlines()
            outfile.seek(0)
            outfile.write(lines[0])
            for line in lines[1:]:
                data = line.strip().split(',')
                if data[1] == min_quantity_shoe.code:
                    data[4] = str(min_quantity_shoe.quantity)
                    line = ','.join(data) + '\n'
                outfile.write(line)
                outfile.close
        print("\nThe product has been updated!")
    else:
        pass

    
    # output = ''
    # for item in shoe_obj_list:
    #     output += (f'{item.get_country()},{item.get_code()},{item.get_product()},{item.get_cost()},{item.get_quantity()}\n')

    # user_output = open("inventory2.txt", "w")
    # user_output.write(output)
    # user_output.close()


def search_shoe():
    code = input("Enter shoe code you would like to search: ")
    for shoe in shoe_obj_list:
        if shoe.code == code:
            print(shoe)
            break
    else:
        print(f"No shoe with code {code} found.")

 
def value_per_item():
    table = []
    print('{:20s} {:>20s} {:>20s}'.format('Code', 'Product', 'Total Value'))
    for shoe in shoe_obj_list:
        value = round(int(shoe.cost) * int(shoe.quantity), 2)
        print('{:20s} {:>20s} {:>20f}'.format(shoe.code, shoe.product, value))


def highest_qty():
    shoe = max(shoe_obj_list, key=lambda x: x.quantity)
    print(f"The shoe with the highest quantity is: {shoe}")

#------------------Main Code--------------------------------
read_shoes_data()
while True:

    try:
        menu = int(input('''\n

            Please select from the menu below:

            1. Capture Shoes
            2. View All
            3. Restock
            4. Search
            5. View Item Values
            6. View Highest Quantity
            7. Exit
            \n'''))

        if menu == 1:
            capture_shoes()

        elif menu == 2:
            view_all()

        elif menu == 3:
            restock()

        elif menu == 4:
            search_shoe()

        elif menu == 5:
            value_per_item()

        elif menu == 6:
            highest_qty()

        elif menu == 7:
            break


        elif menu > 7:
            print("\nYou have selected an invalid option. Please try again by choosing from the menu below.\n")

    except ValueError:
        print("\nYou have selected an invalid option. Please try again by entering a number.\n")
        




