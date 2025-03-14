from funcoes.contas import criar_conta, fazer_login
from funcoes.vender_produto import vender_prod
from main.funcoes.gerenciar_vendas import vendashist
from main.funcoes.menus import menusystem, menusystem2


print(f"{"\n"}{"\033[1;32m WELCOME TO THE SALES SYSTEM \033[m".center(54)}{"\n"}")
while True:
    print(f"{"\033[1;36m DO YOU HAVE AN ACCOUNT? ".center(52)}\n")
    resp = str(input(f"{" [1]YES   or   [2]NO ".center(45)}{"\n"}{"\n"}").replace(" ", "").lower())
    if resp == "1":
        fazer_login()
        while True:
            menusystem()
            resp2 = input(f"{" WHAT YOU WANT TO DO? ".center(42)}{"\n"}{"\n"}")
            match resp2:
                case "1":
                    break
                case "2":
                    fazer_login()
                case "3":
                    vendashist()
                case "4":
                    print(f"{"\n"}{"\033[1;32m SEE YOU SOON! \033[m".center(52)}{"\n"}")
                    exit()
                case _:
                    print(f"{"\n"}{"\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT! ".center(47)}")
                    print(f"\033[1;31mCHOOSE THE OPTION USING THE NUMBERS [1,2,3,4]".center(47))
        vender_prod()
        break
    elif resp == "2":
        criar_conta()
        while True:
            menusystem()
            resp3 = input(f"{" WHAT YOU WANT TO DO? ".center(42)}{"\n"}{"\n"}")
            match resp3:
                case "1":
                    break
                case "2":
                    fazer_login()
                case "3":
                    vendashist()
                case "4":
                    print(f"{"\n"}{"\033[1;32m SEE YOU SOON! \033[m".center(52)}{"\n"}")
                    exit()
                case _:
                    print("\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT! ".center(47))
        vender_prod()
    else:
        print(f"{"\n"}{"\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT \033[m".center(56)}")
        print(f"{"\033[1;31mCHOOSE THE OPTION USING THE NUMBERS [1,2]".center(54)}{"\n"}")
while True:
    menusystem2()
    resp4 = input("").strip().lower()
    if resp4 == "1":
        vender_prod()
    elif resp4 == "2":
        fazer_login()
    elif resp4 == "3":
        while True:
            menusystem()
            resp6 = input(f"{" WHAT YOU WANT TO DO? ".center(42)}{"\n"}{"\n"}")
            match resp6:
                case "1":
                    break
                case "2":
                    fazer_login()
                case "3":
                    vendashist()
                case "4":
                    print(f"{"\n"}{"\033[1;32m SEE YOU SOON! \033[m".center(52)}{"\n"}")
                    exit()
                case _:
                    print("\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT! ".center(47))
                    print(f"\033[1;31mCHOOSE THE OPTION USING THE NUMBERS [1,2,3,4]".center(47))
        vender_prod()
    elif resp4 == "4":
        print(f"{"\n"}{"\033[1;32m SEE YOU SOON! \033[m".center(48)}{"\n"}")
        exit()   
    else:
        print(f"{"\n"}{"\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT \033[m".center(54)}{"\n"}")
        print(f"\033[1;31mCHOOSE THE OPTION USING THE NUMBERS [1,2,3,4]".center(47))
