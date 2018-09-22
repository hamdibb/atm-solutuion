
class ATM:

    def __init__(self, bank_name, balance):
        self.bank_name = bank_name
        self.balance = balance

    def withdraw(self, request) :

        print "welcome to %s bank" %self.bank_name
        print "your balance is %s" %self.balance
        if   request > self.balance:
            print("Can't give you all this money !!")

        elif request < 0:
            print("More than zero plz!")

        else:
            allowed_paper = [200, 100, 50, 10, 5]
            self.balance -= request
            for i in range(len(allowed_paper)):
                while request >= allowed_paper[i]:
                    request -= allowed_paper[i]
                    print "give %s$" %allowed_paper[i]
                if request < allowed_paper[-1] and request > 0:
                    print "give %s$ " %request
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