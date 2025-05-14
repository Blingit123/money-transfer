"""f_name= input("enter your name: ")
age= input("enter your age: ")
print( f"your name is {f_name} and your age is {age}")
"""
#Note: anything from input is considered a string 
#write a program that 2 number from user and display the sum of both numbers

#num1 = input( "enter your first number: ")
#num2 = input( "enter your second number: ")

#sum = int(num1)  + int(num2)
#print(sum)


#write a code to help your client with money transfer
# it should ask for user total amount to send in usd
# then it shoud tell how much the receiver will get in cameroon ==> CFA 
# sending fee should be 0.02 added to the total amount 
# exchange rate should be 655

sending_fees =0.02
exchange_rate = 655

user_amount = int(input( "enter the amount: "))
fee_amount = sending_fees * user_amount 
amount_plus_fees = user_amount + fee_amount
receiving_amount = exchange_rate * user_amount 
print(F"the total amount plus sending fees is: ${amount_plus_fees:,} and your family will receive {receiving_amount:,} CFA")

user_answer = input("do you want to proceed (yes/no)?")

if user_answer == 'yes':
    print("proceed with the payment")
else:
    print("Thank you for stopping by")

