
class ATM:

    def __init__(self, bank_name, balance):
        self.bank_name = bank_name
        self.balance = balance

    def withdraw(self, request) :

        print "welcome to %s bank" %self.bank_name
        print "your balance is %s" %self.balance
        if   request > self.balance:
            print("Can't give you all this money !!")
            return self.balance

        elif request < 0:
            print("More than zero plz!")
            return self.balance

        else:
            self.balance -= request
            while request > 0:

                if request >= 100:
                    request -= 100
                    print("give 100")

                elif request >= 50:
                    request -= 50
                    print("give 50")

                elif request >= 10:
                    request -= 10
                    print("give 10")

                elif request >= 5:
                    request -= 5
                    print("give 5")

                elif request < 5:
                    print("give " + str(request))
                    request = 0
            return self.balance

atm1 = ATM("BIAT", 500)
atm2 = ATM("Zitouna", 1450)

atm1.balance = atm1.withdraw(120)
atm1.balance = atm1.withdraw(78)
atm1.balance = atm1.withdraw(358)
atm1.balance = atm1.withdraw(123)
atm1.balance = atm1.withdraw(-54)
atm1.balance = atm1.withdraw(164)
atm2.balance = atm2.withdraw(320)
atm2.balance = atm2.withdraw(78)
atm2.balance = atm2.withdraw(358)
atm2.balance = atm2.withdraw(2000)
atm2.balance = atm2.withdraw(-54)
atm2.balance = atm2.withdraw(164)