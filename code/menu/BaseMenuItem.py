class BaseMenuItem():
    def signal(self, code):
        print str(self.__class__) + " received Code " + str(code)