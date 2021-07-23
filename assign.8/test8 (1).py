""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from Frozen_Item import Frozen_Item
Vanill_ice_cream = Frozen_Item(-20, "20/20/2020", "D7735i", "B&J Vanill", 16.00, 3)
Frozen_peas = Frozen_Item(-20, "15/1/2019", "DA1212", "Green Peas", 10.00, 2)
Salmon_fish = Frozen_Item(-20, "30/1/2019", "DDc55i8", "Salmon", 14.00, 4)

print(Frozen_peas.item_id == "DA1212")
print(Salmon_fish.qty == 4)
print(Vanill_ice_cream.max_temp == -20)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from Dry_Item import Dry_Item
granola = Dry_Item("Mr. Awesome", 150, 400, "1/3/2020", "1023", "best granola ever", 84.90, 2)
cereal = Dry_Item("C&C inc", 750, 2565 , "20/12/2020", "idid8909", "coco coffe cereal", 23.99 , 5)
Doritos = Dry_Item("Doritos", 250, 1190 , "14/5/2020", "id88gg0", "BBQ Doritos", 14.99 , 7)

print(granola.calories_in_100g() == 266.66666666666663)
print(cereal.calories_in_100g() == 342)
print(Doritos.calories_in_100g() == 476)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from Meat_Item import Meat_Item
chiken_breast = Meat_Item("the clowns", "22/1/2018", 100.0 , "301", "chicken breast", 25, 3)
chicken = Meat_Item("The Pines", "20/1/2019", 257.00 , "idff567", "chiken", 92.50, 3)
steak = Meat_Item("SCP", "23/1/2023", 500.00 , "430jhk", "Juciy Steak", 60.5, 4, "Party Size")

print(chiken_breast.__repr__() == "id: 301, name: chicken breast, price: 25 nis" + "\n" + "qty: 3, request: None" + "\n" + "butcher: the clowns, exp: 22/1/2018, 100.0g")
print(chicken.__repr__() == "id: idff567, name: chiken, price: 92.5 nis" + "\n" + "qty: 3, request: None" + "\n" + "butcher: The Pines, exp: 20/1/2019, 257.0g")
print(steak.__repr__() == "id: 430jhk, name: Juciy Steak, price: 60.5 nis" + "\n" + "qty: 4, request: Party Size" + "\n" + "butcher: SCP, exp: 23/1/2023, 500.0g")
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from Fruit_Veggie_Item import Fruit_Veggie_Item
orange = Fruit_Veggie_Item("uncle moses", True, ["a","c"], "203", "orange", 5.0, 3, "big ones")
cucmber = Fruit_Veggie_Item("Moses and Jesus", False, [], "cc880", "cucmber", 4.8, 7)
watermelon = Fruit_Veggie_Item("Sister's garden", True, ["a","b","c"], "99d0", "watermelon", 12.0, 1)

print(orange.__repr__() == "id: 203, name: orange, price: 5.0 nis" + "\n" + "qty: 3, request: big ones" + "\n" + "farm: uncle moses, fruit, 2 vitamins")
print(cucmber.__repr__() == "id: cc880, name: cucmber, price: 4.8 nis" + "\n" + "qty: 7, request: None" + "\n" + "farm: Moses and Jesus, vegetable, 0 vitamins")
print(watermelon.__repr__() == "id: 99d0, name: watermelon, price: 12.0 nis" + "\n" + "qty: 1, request: None" + "\n" + "farm: Sister's garden, fruit, 3 vitamins")
print(orange.number_vitamins() == 2)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
orange.update_quantity(3)
print(orange.qty == 3)

cucmber.update_quantity(1)
print(cucmber.qty == 1)

chiken_breast.update_quantity(3)
print(chiken_breast.qty == 3)

print(chiken_breast.get_request() == "")
print(steak.get_request() == "Party Size")
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from Shopping_List import Shopping_List
my_shopping_list = Shopping_List("1", "nir")
my_shopping_list + orange
my_shopping_list + [chiken_breast, granola]

print(my_shopping_list.item_summary() == [('orange', 3), ('chicken breast', 3), ('best granola ever', 2)])
print(my_shopping_list.total_price() == 259.8)
print(my_shopping_list.__repr__() == "*"*30 + "\n" + "List id: 1" + "\n" + "Number of Products: 3" + "\n" + "Number of Items: 8" + "\n" + "Total Price: 259.8"  + "\n" + "*"*30 )

chiken_breast.update_quantity(1)

print(my_shopping_list.item_summary() == [('orange', 3), ('chicken breast', 1), ('best granola ever', 2)])
print(my_shopping_list.total_price() == 209.8)
print(my_shopping_list.__repr__() == "*"*30 + "\n" + "List id: 1" + "\n" + "Number of Products: 3" + "\n" + "Number of Items: 6" + "\n" + "Total Price: 209.8"  + "\n" + "*"*30 )

my_shopping_list2 = Shopping_List("2", "sagi")
my_shopping_list2 + [granola, orange]

print(my_shopping_list2.__repr__() == "*"*30 + "\n" + "List id: 2" + "\n" + "Number of Products: 2" + "\n" + "Number of Items: 5" + "\n" + "Total Price: 184.8"  + "\n" + "*"*30 )
print((my_shopping_list > my_shopping_list2) == True)

print(my_shopping_list.get_customer_name() == "nir")
print(my_shopping_list2.get_customer_name() == "sagi")

my_shopping_list3 = Shopping_List("3", "noa")
print(my_shopping_list3.is_empty() == True)

print(my_shopping_list3.item_summary() == [])
print(my_shopping_list3.total_price() == 0)
print(my_shopping_list3.__repr__() == "*"*30 + "\n" + "List id: 3" + "\n" + "Number of Products: 0" + "\n" + "Number of Items: 0" + "\n" + "Total Price: 0"  + "\n" + "*"*30 )
print((my_shopping_list3 > my_shopping_list) == False)

#check gt money== items num== 
orange.update_quantity(20)
my_shopping_list3 + orange
my_shopping_list4 = Shopping_List("4", "10 frozen peas")
Frozen_peas.update_quantity(10)
my_shopping_list4 + Frozen_peas

print((my_shopping_list3 > my_shopping_list4) == True)

emty_product = Dry_Item("Mr. Awesome", 150, 400, "1/3/2020", "6666", "best granola ever", 0, 10)
my_shopping_list4 + emty_product

print((my_shopping_list3 > my_shopping_list4) == False)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""