stock = []


def seeder():
  products = [
    {"name": "apple", "price": 0.5, "quantity_in_stock": 120},
    {"name": "banana", "price": 0.3, "quantity_in_stock": 200},
    {"name": "milk", "price": 2.5, "quantity_in_stock": 45},
    {"name": "bread", "price": 1.2, "quantity_in_stock": 60},
    {"name": "eggs", "price": 3.0, "quantity_in_stock": 30}
    ]
  for i in products:
    stock.append(i)
  return stock
seeder()

def show_products():
  for index, i in enumerate(stock):
    print(f"index: {index} - name: {i['name']} - price: {i['price']}")

def add():
  name = input("Write the name of the product: ").lower()
  price = float(input("Write the price of the product: "))
  quantity = int(input("Write the quantity of the products to add: "))
  stock.append({"name":name, "price": price, "quantity_in_stock": quantity})
  return

def search():
  exists = False
  show_products()
  product_name = input("write the name of the product you are looking for: \n")

  for i in stock:
    if i["name"] == product_name:
      print(i)
      exists = True
      return
  if exists == False:
    print("We do not have that product in our stocks")



def update():
  show_products()
  index = int(input("Give me the index of the product that you want to modify its price: "))
  new_price = float(input("Give us the new price: "))
  if new_price > 0:
    stock[index]["price"] = new_price
    show_products()
  else:
    print("A positive value is required")

def delete():
  show_products()
  delete_index = int(input("please give us the index of the item you want to delete: "))
  stock.remove(stock[delete_index])
  show_products()

def calculate_total():
  total = 0
  for i in stock:
    total += i["price"] * i["quantity_in_stock"]
  print( f"Total value of the stock: {total}")

def menu():
  closer = False
  print("Welcome to our Store! \n")
  while closer == False:
    option_selected = int(input("""What do you want to do? \n

          option 1: add a product
          option 2: Search a product
          option 3: Update a product price
          option 4: Delete a product
          option 5: Calculate the total stock value
          option 6: Exit
          """))

    if option_selected == 1:
      add()
    elif option_selected == 2:
      search()
    elif option_selected == 3:
      update()
    elif option_selected == 4:
      delete()
    elif option_selected == 5:
      calculate_total()
    elif option_selected == 6:
      closer = True
      print("\n \n BYEEEEEE")



menu()

