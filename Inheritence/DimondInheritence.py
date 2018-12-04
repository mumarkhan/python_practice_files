class First(object):
    def __init__(self):
        super(First, self).__init__()
        print "first"

class Second(First):
    def __init__(self):
        super(Second, self).__init__()
        print "second"

class Third(First):
    def __init__(self):
        super(Third, self).__init__()
        print "third"

class Fourth(Second, Third):
    def __init__(self):
        super(Fourth, self).__init__()
        print "that's it"
        

obj = Fourth()
