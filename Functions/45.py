# Name: Kartik Vanjani
# Email: KARTIK.VANJANI21@myhunter.cuny.edu
# 4/25/23
# Program #45: Correct the errors in the program to output the correct results.

""" printNames(nameList) prints out ONCE Five most popular female names in the USA, then print every name on the list of nameList, one per line """
def printNames(nameList):
    for name in nameList:
        print("Five most popular female names in USA: ")
        print(name)
    
  
""" inList(nameList, nameToSearch) checks if name is a name on the nameList and prints out a message accordingly """     
def inList(nameList, nameToSearch):
    found = False    
    for name in nameList:
        if name == nameToSearch:
            found = True
    if not found:
        print(nameToSearch + " is not in the list of names.")
        
""" numNames(nameList) return a number of names in the list"""                
def numNames(nameList):
    num = len(nameList)
    return "There are " + num + " names in the list."

def main():
    # A list of five most popular female names in the USA 
    nameList = ["Olivia", "Emma" "Charlotte", "Amelia", "Ava"]
    
    printNames(nameList)

    inList(nameList, "Olivia")
    inList(nameList, "Emma")          
    inList(nameList, "Mary")
    inList(nameList, "Helen")
    
    print(len(nameList))

    
if __name__ == "__main__":
    main()
