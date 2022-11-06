
grocery_menu = {
	"products" : ["Apples","Banana","Grapes","Orange"],
	"cost"	   : [28,15,18,200],
	"stock"    : [20,40,30,10]
}

Receipt = {
	"Cart" : [],
	"cart_quan" : [],
	"single_cost" : []
}

_total_cost = int(0) 

_exit = True
while(_exit):

	_exit = False
	print ("-------------------------> Welcome to Ramy's Groceries shop <-------------------------")
	print ("customer mode Enter 1")
	print ("Owner mode Enter 2")
	print ("Exit 0")
	print ("-------------------------")
	main_mode = int( input("enter your choice ") )

	if main_mode == 1 and _exit == False :

		print ("To list Available items press 1")
		print ("For Order page press 2 ")
		#print ("Print your bill Press 3")
		print ("Exit 0")
		print ("-------------------------")
		customer_mode = int( input("enter your choice ") )

		if customer_mode == 1 or customer_mode == 2  : 
			print("#"+3 * " "+"ITEMS"+ 6 *" "+"PRICE")
			for i in range(4):
				print(i+1,"-",grocery_menu["products"][i],6 * " ",grocery_menu["cost"][i],"\n")
			if 	customer_mode == 1 :
				_buy = int(input("For buy page press 1\nTo Exit press 0\n"))
				if _buy == 0 : _exit = True
			if customer_mode == 2 or _buy == 1 :
				_add = True
				while (_add) :
					_add = False
					num_index= int(input("please write the index of the item "))
					quantity= int(input("please write the quantity in Kg "))
					Receipt["Cart"].append(grocery_menu["products"][num_index-1])
					Receipt["cart_quan"].append(quantity)
					grocery_menu["stock"][num_index-1] -= quantity
					_single_cost = (quantity * grocery_menu["cost"][num_index-1])
					Receipt["single_cost"].append(_single_cost )
					_add = int (input(" To add more press 1 , to Print Receipt press 0\n"))
					if _add == 0 : 
						print("#"+3 * " "+"ITEMS"+ 6 *" "+"quantities"+ 6 *" "+"Cost")
						for i in range(len(Receipt["single_cost"])):
							print(i+1,"-",Receipt["Cart"][i],6 * " ",Receipt["cart_quan"][i],10 * " ",Receipt["single_cost"][i],"\n")
						_total_cost = sum(Receipt["single_cost"])
						print ( "Total cost= ", _total_cost )
						
		elif customer_mode == 0 : 
			print(" Have a nice day")


	elif main_mode == 2 and _exit == False :
		pass_status = True
		while (pass_status):
			_pass=input("Please enter the password\n")
			if _pass == "1234" :
				print ("-------------------------")
				print("Welcome Back Mr.Ramy")
				print ("-------------------------")
				pass_status = False
					
			else :
				print ("Wrong Please try again")
				
		print ("Add New Product Press 1 ")
		print ("Show list of products Press 2 ")
		print ("Change cost of a product Press 3")
		print ("Exit 0")
		owner_mode = int( input("enter your choice ") )
		
		if owner_mode == 1 or owner_mode == 2:
			_exit = True
			print("#"+3 * " "+"ITEMS"+ 6 *" "+"PRICE" + 6 *" "+"Stock"  )
			for i in range(len(grocery_menu["products"])):
				print(i+1,"-",grocery_menu["products"][i],6 * " ",grocery_menu["cost"][i],6 * " ",grocery_menu["stock"][i],"\n")
			if owner_mode == 2 :
				_dis = int(input(" To add a new product Press 1 or To Exit 0 "))
				if _dis == 0 : 
					_exit = True
			if owner_mode == 1 or _dis == 1 :
				_add_2 = True
				while(_add_2) :
					_add_2 = False
					_new_pro = str(input("Please enter the new product name "))
					_new_cost = int(input("Please enter the cost of the product "))
					_new_stock = int(input("Please enter the stock level of the product "))
					grocery_menu["products"].append(_new_pro)
					grocery_menu["cost"].append(_new_cost)
					grocery_menu["stock"].append(_new_stock)
					_add_2 = int (input(" To add more press 1 , to Exit press 0\n"))
				if _add_2 == 0 :
						print("#"+3 * " "+"ITEMS"+ 6 *" "+"PRICE" + 6 *" "+"Stock"  )
				for i in range(len(grocery_menu["products"])):
					print(i+1,"-",grocery_menu["products"][i],6 * " ",grocery_menu["cost"][i],6 * " ",grocery_menu["stock"][i],"\n")
		if owner_mode == 3 :
			_add_3 = True
			_exit = True
			while(_add_3) :
				_add_3 = False
				print("#"+3 * " "+"ITEMS"+ 6 *" "+"PRICE" + 6 *" "+"Stock"  )
				for i in range(len(grocery_menu["products"])):
					print(i+1,"-",grocery_menu["products"][i],6 * " ",grocery_menu["cost"][i],6 * " ",grocery_menu["stock"][i],"\n")
				_index_cost = int ( input("Please enter the index of the product "))
				_update_cost = int ( input("Please enter updated cost "))
				grocery_menu["cost"][_index_cost-1]=_update_cost
				_add_3 = int (input(" To add more press 1 , to Exit press 0\n"))
			if _add_3 == 0 :	
				print("#"+3 * " "+"ITEMS"+ 6 *" "+"PRICE" + 6 *" "+"Stock"  )
				for i in range(len(grocery_menu["products"])):
					print(i+1,"-",grocery_menu["products"][i],6 * " ",grocery_menu["cost"][i],6 * " ",grocery_menu["stock"][i],"\n")
					
				

	elif main_mode == 0 and _exit == False : 
	
		print(" Have a nice day")




