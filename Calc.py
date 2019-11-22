def soma(x,y):
    return x + y

def sub(x,y):
    return x - y

def div(x,y): 
    return x/y

def mult(x,y):
    return x*y


while (1):

    expression = input("")

    SuportList = (list(expression))

    StringA = ""
    StringB = ""

    for i in SuportList:
        if( i == "+" or i == "*" or i == "-" or i == "/"):
            break
        elif(i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i =="."):
            StringA = StringA + i
        else: 
            break


    for j in SuportList[len(StringA)+1:]: 
        if(j == "0" or j == "1" or j == "2" or j == "3" or j == "4" or j == "5" or j == "6" or j == "7" or j == "8" or j == "9" or j == "."):
             StringB = StringB + j
    
    if(StringA == ""):
        x = 0
    else:
        x = float(StringA)

    if(StringB == ""):
        y = 0
    else:
        y = float(StringB)

    if(i == "+"):
        print("\nResult: ", soma(x,y))
    elif(i == "-"):
        print("\nResut: ", sub(x,y))
    elif(i == "*"):
        print("\nResult: ", mult(x,y))
    elif(i == "/"):
        print("\nResult: ", div(x,y))
    elif(StringB == ""):
        print("\nResult:", x)
    else:
        print("\nIncorret Operation!")

    sair = input("\n1 - Exit\n2 - To another Operation\nChose: ")
    print("")
    if(sair == "1"):
        break