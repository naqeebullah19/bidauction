print("Welcome to the secret auction program.")

biddict={}
a=input("what is your name?")
a1=int(input("whats your bid?"))

biddict["a"]=a1

others=input("are there any other bidders?")
while others=='yes':
    print("\n"*100)
    b=input("what is your name?")
    b1=int(input("whats your bid?"))
