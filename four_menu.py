import os

print("Please choose your options")
print("[1]Show your IP")
print("[2]Control Pannel")
print("[3]Firewall Config")
print("[0]Exit")

cmd1 = "ipconfig"
cmd2 = "control"
cmd3 = "firewall.cpl"

option = input("Input:")

if option == "1":
    returned_value = os.system(cmd1)

elif option == "2":
    returned_value = os.system(cmd2)

elif option == "3":
    returned_value = os.system(cmd3)

elif option =="0":
    print("Bye")
