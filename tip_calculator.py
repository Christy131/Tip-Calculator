
def tip_calculator():
    print('Hi Welcome to Tip & Split!')
    parties = num_of_people()
    bill = meal_amount()
    meal_tax = amt_sales_tax(bill)
    bill_tip = add_tip(bill)
    bonus_tip = add_tip_amt()
    total_bill = round(bill + meal_tax + bill_tip + bonus_tip, 2)
    print (f'The total bill is ${total_bill}')
    split_per_person = round((total_bill/parties), 2)
    if parties == 1:
        print (f'Amount per person is ${total_bill}')
    else:
        print (f'Amount per person is ${split_per_person}')
    redo_calc()


#input information from user for number if people in party, 
# user try and except to find ValueErrors.
def num_of_people():
    try:
        parties = int(input('How may people are in you party?' ))
        print (f'OK so this bill will be split by {parties}.')
        return parties
    except ValueError:
        print('Please enter valid number')
        return num_of_people()  
    


#get user input for the amount of bill, uses if, elif, else statments to comment, 
# uses try and except to find ValueErrors

def meal_amount ():
    try:
        bill = float(input('What is the amount of the bill? '))
        if bill <=50:
            print ('early night?')
        elif bill <=100:
            print ('Looks like you had a good time.')
        else:
            print ('Whoa, Big Spender!')
        return bill
    except ValueError:
        print('Please enter valid number')
        return meal_amount()  

#figure sales tax amount

def amt_sales_tax(meal_amount):   
    tax_amt = meal_amount * 0.10
    return tax_amt


#get user input for the amount of tip, uses if, elif, else statments to comment, 
# uses try and except to find ValueErrors and calculates the amount of tip.

def add_tip(meal_amount):
    tip = float(input('How much would you Like to tip to be in percentage?' ))   
    if tip ==0:
        print ('Cheapskate')
    elif tip <=5:
        print ('Was it really that bad?!')
    elif tip <=10:
        print ('OK, your an average joe')
    elif tip <=15:
        print ('That is a decent tip')
    else:
        print ('ROCKSTAR')
    try:
        tip_percentage = round(meal_amount * (0.01 * tip), 2)
        print (f' your tip amount is {tip_percentage}')
        return tip_percentage
    except ValueError:
        print('Please enter a number in percentage %')
        return add_tip()
    

#ask user if the wish to add an additional tip, uses try and except to check ValueErrors, 
#and prints a statement showing the amount of additional tip.
                
def add_tip_amt ():
    try:
        more_tip = float(input('Would you like to leave an additional tip in $, please enter 0 for none?' ))
        print (f'the additional tip amount is ${more_tip}')
        return more_tip 
    except ValueError:
        print('Please enter valid number')
        return add_tip_amt()     
     
#ask user if they want to try agian and uses a loop using if, elif and else to start over

def redo_calc():
    do_over = input('Would you like to rerun the calculator? Please enter y for Yes, n for No' ).strip()
    if do_over.lower() =='y':
        tip_calculator()
    elif do_over.lower() =='n':
        print ('Thank you for using Tip & Split')
    else:
        print('Please neter y for yes n for no.' )
        redo_calc()

tip_calculator()