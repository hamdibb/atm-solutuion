# allowed papers: 100, 50, 10, 5, and cents
balance = 500

def withdraw(balance, request) :
    original_request = request

    print "your balance is %s" %balance
    if   request > balance:
        print("Can't give you all this money !!")
        return balance

    elif request < 0:
        print("More than zero plz!")
        return balance

    else:
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
        return balance - original_request

balance = withdraw(balance, 120)
balance = withdraw(balance, 78)
balance = withdraw(balance, 358)
balance = withdraw(balance, 123)
balance = withdraw(balance, -54)
balance = withdraw(balance,164)
