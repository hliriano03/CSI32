# 3/3

class Date:
     
    def __init__(self):
        # By default: January 1, 2000
        self._month = 1
        self._day = 1
        self._year = 2000
        self.monthNames = ('January', 'February', 'March', 'April', 'May',
                           'June', 'July', 'August', 'September', 'October',
                           'November', 'December')
 
    def getDay(self):
 
        return self._day
 
    def setYear(self, year):
 
        self._year = year
 
    def __str__(self):
 
        return "{} {}, {}".format(self.monthNames[self._month - 1], self._day, \
                                  self._year)
