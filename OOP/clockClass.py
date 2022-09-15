
class Clock:
    """Creates a Clock Class"""
    def __init__(self, hours=0, minutes=0, seconds=0):

        self.setTime(hours, minutes, seconds)
        
    def setTime(self, hours, minutes, seconds):

        if type(hours) is int and hours >= 0 and hours <= 23:
            self._hours = hours
        else:
            raise ValueError("Hours must be between 0 and 23")

        if type(minutes) is int and minutes >= 0 and minutes <= 59:
            self.__minutes = minutes
        else:
            raise ValueError("Minutes must be between 0 and 59")

        if type(seconds) is int and seconds >= 0 and seconds <= 59:
            self.__seconds = seconds
        else:
            raise ValueError("Seconds must be between 0 and 59")

    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self._hours,
                                                self.__minutes,
                                                self.__seconds)

    def tick(self):
        if self.__seconds == 59:
            self.__seconds = 0
            if self.__minutes == 59:
                self.__minutes = 0
                if self._hours == 23:
                    self._hours = 0
                else:
                    self._hours +=1
            else:
                self.__minutes +=1
        else:
            self.__seconds +=1


class Calendar:
    months = (31,28,31,30,31,30,31,31,30,31,30,31)
    date_style = "British"

    @staticmethod
    def leapyear(year):
        if not year % 4 == 0:
            return False
        elif not year % 100 == 0:
            return True
        elif not year % 400 == 0:
            return False
        else:
            return True

    def __init__(self, day, month, year):

        self.setCalendar(day,month,year)

    def setCalendar(self, day, month, year):

        if type(day) == int and type(month) == int and type(year) == int:
            self.__days = day
            self.__months = month
            self.__years = year
        else:
            raise TypeError("day, month, year have to be integers!")

    def __str__(self):
        if Calendar.date_style == "British":
            return "{0:02d}/{1:02d}/{2:4d}".format(self.__days,
                                                self.__months,
                                                self.__years)
        else: 
            # assuming American style
            return "{0:02d}/{1:02d}/{2:4d}".format(self.__months,
                                                self.__days,
                                                self.__years)

    def advance(self):

        max_days = Calendar.months[self.__months-1]
        if self.__months == 2 and Calendar.leapyear(self.__years):
            max_days += 1
        if self.__days == max_days:
            self.__days= 1
            if self.__months == 12:
                self.__months = 1
                self.__years += 1
            else:
                self.__months += 1
        else:
            self.__days += 1

class CalendarClock(Clock, Calendar):

    def __init__(self, day, month, year, hour, minute, seconds):
        Clock.__init__(self, hour, minute, seconds)
        Calendar.__init__(self, day, month, year)

    def update(self):

        previous_hour = self._hours
        Clock.tick(self)
        if (self._hours < previous_hour):
            self.advance()

    def __str__(self):
        return Calendar.__str__(self) + "," + Clock.__str__(self)

x = CalendarClock(31, 12, 2013, 23, 59, 59)
print(x)
x.update()
print(x)