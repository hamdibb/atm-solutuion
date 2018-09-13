def atm(request) :
	while request >= 100:
		request -=100
		print "give 100$"
	while request >= 50:
		request -=50
		print "give 50$"
	while request >= 10:
		request -=10
		print "give 10$"
	while request >= 5:
		request -=5
		print "give 5$"
	if request != 0 :
		print "give " + str(request) + "$"