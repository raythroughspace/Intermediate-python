# =============================================================================
# """OOP BASICS"""
#class Point:
#     """Point class represents and manipulates x,y coords."""
#     
#     def __init__(self, x=0, y=0):
#         """Point(x,y) -> None
#         initializes point with coords x,y"""
#         self.x = x
#         self.y = y
#     
#     def distance_from_origin(self):
#         """Point.distance_from_origin() -> int
#         returns this points distance from origin"""
#         return (self.x**2 + self.y**2)**0.5
#     
#     def __str__(self):
#         """str(Point) -> str
#         returns the string representation of point"""
#         return "(" + str(self.x) + "," +  str(self.y) +")"
#     
#     def halfway(self, target):
#         """Point.halfway(target) -> Point
#         returns a point halfway in between Point and target"""
#         return Point((self.x + target.x)/2, (self.y + target.y) /2)
#     
# print(Point(3,4).halfway(Point(5,12)))
# 
# =============================================================================
# =============================================================================
# class Date:
#     '''class to represent a date'''
# 
#     def __init__(self,month,day,year):
#         '''Date(month,day,year) -> Date'''
#         self.month = month
#         self.day = day
#         self.year = year
# 
#     def __str__(self):
#         '''str(Date) -> str
#         returns date in readable format'''
#         # list of strings for the months
#         months = ['','Jan','Feb','Mar','Apr','May','Jun','Jul',
#                   'Aug','Sep','Oct','Nov','Dec']
#         output = months[self.month] + ' ' # month
#         output += str(self.day) + ', '  # day
#         output += str(self.year)
#         return output
# 
#     def go_to_next_day(self):
#         '''Date.go_to_next_day()
#         advances the date to the next day'''
#         # list with the days in the month
#         daysInMonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]
#         # check for leap year
#         isLeapYear = self.year%4 == 0 and \
#                      (self.year%100 != 0 or self.year%400 == 0)
#         # you have to write the rest!
#         if (isLeapYear):
#             daysInMonth[2] = 29
#         if (self.day == daysInMonth[self.month]): #new month
#             self.day = 1
#             if (self.month == 12): #new year
#                 self.year +=1
#                 self.month = 1
#             else:
#                 self.month += 1
#         else:
#             self.day += 1
# # test cases
# d1 = Date(6,11,2014)
# print(d1)
# d1.go_to_next_day()
# print(d1)
# # new month
# d2 = Date(9,30,2005)
# print(d2)
# d2.go_to_next_day()
# print(d2)
# # leap year tests
# d3 = Date(2,28,2011) # not a leap year
# print(d3)
# d3.go_to_next_day()
# print(d3)
# d4 = Date(2,28,2016) # is a leap year
# print(d4)
# d4.go_to_next_day()
# print(d4)
# # happy new year!
# d5 = Date(12,31,2014)
# print(d5)
# d5.go_to_next_day()
# print(d5)
# =============================================================================
# =============================================================================
# class Point:
#     """ Point class represents and manipulates x,y coords. """
# 
#     def __init__(self, x=0, y=0):
#         """ Create a new point """
#         self.x = x
#         self.y = y
# 
#     def distance_from_origin(self):
#         """ Compute my distance from the origin """
#         return ((self.x ** 2) + (self.y ** 2)) ** 0.5
# 
#     def __str__(self):
#         return "("+str(self.x)+","+str(self.y)+")"
# 
#     def halfway(self, target):
#         """ Return the halfway point between myself and the target """
#         mx = (self.x + target.x)/2
#         my = (self.y + target.y)/2
#         return Point(mx, my)
#     
#     def slope(self, other):
#         """Point.slope(other) -> float
#         returns the slope of the line joining Point and other"""
#         if (self.x == other.x):
#             return "undefined"
#         else:
#             return (self.y - other.y)/(self.x - other.x)
#     
#     def is_on(self, p, q):
#         """Point.is_on(p, q) -> bool
#         returns True if Point is on line joining p,q otherwise False"""
#         return self.slope(p) == self.slope(q)
#         
# # test cases
# p = Point(1,-2)
# q = Point(3,5)
# r = Point(3,7)
# print(p.slope(q))  # should be 3.5
# print(q.slope(p))  # should be 3.5
# print(q.slope(r))  # should print "undefined"
# # test cases
# p = Point(0,0)
# q = Point(3,6)
# r = Point(1,2)
# s = Point(2,3)
# print(r.is_on(p,q))   # should be True
# print(s.is_on(p,q))   # should be False
# =============================================================================
# =============================================================================
# class Elevator:
#     '''Represents a simple elevator'''
# 
#     def __init__(self, startFloor, startDoorsOpen):
#         '''Elevator(startFloor, startDoorsOpen) -> Elevator
#         Constructs an Elevator
#         startFloor: int giving the starting floor
#         startDoorsOpen: bool giving the starting doors 
#                     (True = 'open')'''
#         self.floor = startFloor  # store floor attribute
#         self.doorsOpen = startDoorsOpen  # store doors attribute
#         self.passengers = []
#     def __str__(self):
#         '''str(Elevator) -> str
#         Returns a string giving the floor and state of the doors.'''
#         answer = 'doors '         # will contain string to return
#         if self.doorsOpen:        # if doors open
#             answer += 'open'      # say so
#         else:                     # if doors closed
#             answer += 'closed'    # say that too
#         answer += ', floor '      # this is in every answer
#         answer += str(self.floor) # add floor number
#         answer += ', passengers ' + str(self.passengers)
#         return answer
# 
#     def open_doors(self):
#         '''Elevator.open_doors()
#         Opens the doors by setting doors attribute to True.'''
#         self.doorsOpen = True # set doors to open
# 
#     def close_doors(self):
#         '''Elevator.close_doors()
#         Closes the doors by setting doors attribute to False.'''
#         self.doorsOpen = False # set doors to closed
# 
#     def go_up(self):
#         '''Elevator.go_up()
#         Goes up by one floor if doors are not open.'''
#         if self.doorsOpen:               # if doors are open
#             print('Please close doors!') # print warning
#         else:                            # if doors are closed
#             self.floor += 1              # increase floor by 1
# 
#     def go_down(self):
#         '''Elevator.go_down()
#         Goes down by one floor if doors are not open.'''
#         if self.doorsOpen:               # if doors are open
#             print('Please close doors!') # print warning
#         else:                            # if doors are closed
#             self.floor -= 1              # decrease floor by 1
# 
#     def go_to_floor(self, destination):
#         '''Elevator.go_to_floor(int)
#         Closes doors, moves to destination, and opens doors.'''
#         if self.doorsOpen:               # if doors are open
#             self.close_doors()           # close 'em
#         while self.floor != destination: # if not at destination
#             if self.floor < destination: # if below
#                 self.go_up()             # go up 1 floor
#             else:                        # if above
#                 self.go_down()           # go down 1 floor
#         self.open_doors()                # open doors
#     
#     def get_on(self, passenger):
#         """Elevator.go_on(passenger) -> None
#         Let passengers on the elevator"""
#         if (self.doorsOpen):
#             self.passengers.append(passenger)
#         else:
#             print("Please open doors to let passengers in!")
#     
#     def get_off(self, passenger):
#         """Elevator.go_off(passengers) -> None
#         Let passengers off the elevator"""
#         if (self.doorsOpen):
#             if (passenger not in self.passengers):
#                 print("Passenger " + passenger + " is not on the elevator!")
#             else:
#                 self.passengers.remove(passenger)
#         else:
#             print("Please open doors to let passengers off the elevator!")
#             
# # test cases
# myElevator = Elevator(1,True)
# myElevator.get_on('John')
# print(myElevator)
# myElevator.go_to_floor(3)
# myElevator.get_on('Mary')
# print(myElevator)
# myElevator.close_doors()
# myElevator.get_on('Steve')   # doors are closed
# print(myElevator)
# myElevator.go_to_floor(6)
# myElevator.get_off('Susan')  # not on the elevator
# myElevator.get_off('John')
# print(myElevator)
# =============================================================================
class Jar:
    """Represents a jar"""
    
    def __init__(self, capacity):
        """Jar(capacity) -> None
        initializes a jar with capacity"""
        self.capacity = capacity
        self.filled = 0
    
    def __str__(self):
        """str(Jar) -> str
        returns a string representation of Jar"""
        return "Jar with capacity: " + str(self.capacity) + " and filled water: " + str(self.filled)
    
    def fill(self):
        """Jar.fill() -> None
        fill this Jar with water"""
        self.filled = self.capacity
    
    def pour(self, other):
        """Jar.pour(other) -> None
        pour water from Jar into other"""
        toPour = min(self.filled, other.capacity - other.filled)
        self.filled -= toPour
        other.filled += toPour
        
    def empty(self):
        """Jar.empty() -> None
        empty Jar completely"""
        self.filled = 0
        
a = Jar(3)
b = Jar(5)
a.fill()
print(a)
print(b)
a.pour(b)
a.fill()
print(a)
print(b)
a.pour(b)
b.empty()
print(a)
print(b)
a.pour(b)
a.fill()
a.pour(b)
print(a)
print(b)
        