from models.atm import Atm
from models.user import User
from models.atm_machine import AtmMachine

def main():
    user1 = User('amit')
    user2 = User('sumit')
    user3 = User('mika')
    user4 = User('sunita')

    a1 = Atm(user1, 1000, '1234')
    a2 = Atm(user2, 2000, '2314')
    a3 = Atm(user3, 3000, '2341')
    a4 = Atm(user4, 4000, '3214')



    #   start the atm machine
    atm_machine = AtmMachine()
    atm_machine.start_atm()





if __name__ == "__main__":
    main()