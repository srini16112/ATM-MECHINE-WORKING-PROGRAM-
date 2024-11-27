n=int(input("Enter card number :"))
card =85
i=1000
a=i-de
b=i+cr
nex='y'
if(card!=n):
    print("--- Wrong Card number ----")
else:
    #print("yes")
    pin=8595
    p=int(input("Enter your pin number :"))
    if(p!=pin):
        print("------- Wrong Pin Number -------")
    while(p==pin):
            print("__________________________________")
            print("------------***MENU***------------")
            print("__________________________________")
            print("------------1. Debit--------------")
            print("------------2. Credit-------------")
            print("------------3. Check Balance -----")
            print("__________________________________")
            print("-----------***4.Exit***-----------")
            print("__________________________________")
            
            ch=int(input("Enter your Transation :"))
            
            match ch:
                case 1:
                    de=int(input("Enter your Amount :"))
                    if(i>=de):
                        print("Debited your Account :",de)
                        print("Current Balance your Amount :",i-de)
                        i=i-de
                        o=input("Enter your another option [Y/N] :")
                        if(nex==o):
                            #ch=int(input("Enter your transation :"))
                            continue
                        else:
                            print("--------------Thanks---------------")
                            break
                        
                    else:
                        print("Insuficient Your Balance")
                        if(de>i):
                            o=input("Enter your another option [Y/N] :")
                            if(nex==o):
                                continue
                            else:
                                print("--------------Thanks---------------")
                                break
                               
                case 2:
                    cr=int(input("Credit your Amount :"))
                    print("Current Balance your Amount :",i+cr)
                    i=i+cr
                    o=input("Enter your another option [Y/N] :")
                    if(nex==o):
                        continue
                    else:
                        print("--------------Thanks---------------")
                        break
                case 3:
                    
                    print("Avaliable Balance Your Account : ",i)
                    o=input("Enter your another option [Y/N] :")
                    if(nex==o):
                        continue
                    else:
                        print("--------------Thanks---------------")
                        break
                
                case 4:
                    if(ch==4):
                        print("--------------Thanks---------------")
                    else:
                        break
                case _:
                    print("--------Valid Transation---------")
                    break
                    
                     
                    
                   
                
           
                

        

