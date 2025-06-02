print("Welcome to the secret auction program.")

biddict={}
a=input("what is your name?")
a1=int(input("whats your bid?"))

biddict[a]=a1
values=biddict.values()
counter=1
others=input("are there any other bidders?")
while others=='yes':
    if others=='yes':
        
        print("\n"*100)
        b=input("what is your name?")
        b1=int(input("whats your bid?"))
        biddict[b]=b1
        others=input("are there any other bidders?")
        counter+=1
    else:
        break
    
sorted_dict = dict(sorted(biddict.items()))
first_key = next(iter(sorted_dict))
print(f"{first_key} is the winner of the auction with a bid of {sorted_dict[first_key]}")
    
