
restart = ('Y') 
chances = 3
balance = int(999.32)

while chances >=0 :    
    pin = int(input('Please Enter You 4 Digit Pin: '))
    if pin ==(1234):
        
        print('You entered you pin Corectly ')
        print('Please Press 1 For Your Balance')
        print('Please Press 2 To Make a Withdrawl')
        print('Please Press 3 To Pay in')
        print('Please Press 4 Return Card\n')
        while restart not in ('n','NO','no','N*'):
            print('Please Press 1 For Your Balance')
            print('Please Press 2 To Make a Withdrawl')
            print('Please Press 3 To Pay in')
            print('Please Press 4 Return Card')
            option = int(input('what would you like to choose?: '))
            if option == 1:
                print(' Your Balance is $',balance)
                restart = input('Would you like to go back? Y or N:  ')
                if restart in ('n','NO','no','N*') :
                    print('Thank you')
                    break
            elif option == 2:
                withdrawl = int(input('How much would you like to withdrawl? 100 200 500 1000 2000 or press 1 to other : ')) 
                if withdrawl in [100,200,500,1000,2000,3000]:
                    balance = balance - withdrawl
                    print ('\n Your Balance is now $: ',balance)
                    restart = input('Would you like to go back? Y or N: ') 
                    if restart in ('n','NO','no','N*') :
                        print('Thank you')
                    break
                elif withdrawl != [100,200,500,1000,2000,3000] :
                    print('Invalid Amount , Please Re-try\n')
                    restart = ('y')
            elif option == 3 :
                Pay_in = int(input('How much would you like to pay in: '))
                balance = (balance + Pay_in)
                print('\n Your Balance is now $: ',balance)
                restart = input('would you like to go back? Y or N')
                if restart in ('n','NO','no','N*'):
                    print('thank you')
                break
            elif option == 4:
                print(' Please wait whilst your card is Returned ...\n')
                print(' Thank you for you service')
                break
            else:
                print('Please Enter a correct number. \n')   
                restart = ('y')
        break    
    else :
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('No more tries')
            break

        




