print ('Welcome !\nwelcome to MEIY-BANK \n\nEnter your password for get money')

#VARIABLE
password = 671383
choice = 0
balance = 0


pin = int(input('\n\nPASSWORD 6 PINS  : '))


if pin == password :

    while choice != 4:  
        
        print('\n\n    ---- MENU ----')
        print('1  ---  Balance  ---')
        print('2  ---  Deposit  ---')
        print('3  --- Withdraws ---')
        print('4  ---   Cancel   ---\n')

        choice = int(input('\nOPTION : '))

        if choice == 1:
            print('\n==> Balance = ', balance,'THB')

        elif choice == 2 :
            dep = int(input('\nEnter your Deposit : '))
            balance += dep
            print('\n==> Deposited amout : ', dep ,'THB')
            print('Total - > Balance =',balance,'THB')

        elif choice == 3:
            wit = int(input('\nEnter amount to withdraw :'))
            balance -= wit
            print('\nwithdraw amount : ', wit ,'THB')
            print('Total - > balance = ', balance ,'THB')

        elif choice == 4:
            print('\nSession Ended!! Good Bye Thank you :)')
        
        else :
            print('\nUnvalid Please Entry !!')


else :
        print('Your Pin Incorrect !! please try again :)')
        



