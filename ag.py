   print("i have tow friends and i am gonna take one large pizza for us .")
large_pizza_price = 40 
my_money = 20
print("ooh ! i have just 20 dollars ,the large pizza price here is 40 dollars and i don't have all that !")
print("OK , i have an idea , i will collect my money with my friends money and then i will be able to buy the large pizza !")
friend_1_money = int(input("please enter your first friend's money :"))
friend_2_money = int(input("please enter your sconde friend's money :"))

total = friend_1_money + friend_2_money + my_money
if total == large_pizza_price :
    print("enjoy the pizza with your friends !")
elif total < large_pizza_price :
        print("sorry , you need more money.")
elif total > large_pizza_price :
            print("take your change bro ! , and enjoy the pizza with your friends !")
else :
            print("sorry bro i can't accept that !")
           
