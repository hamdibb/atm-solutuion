def atm(request):
    request = int(request)
    allowed_paper = [200, 100, 50, 10, 5]
    for i in range(len(allowed_paper)):
        while request >= allowed_paper[i]:
            request -= allowed_paper[i]
            print "give " + str(allowed_paper[i]) + "$"
        if request < allowed_paper[-1]:
            print "give " + str(request) + "$"


atm(raw_input("enter the amount you want to withdraw: "))
