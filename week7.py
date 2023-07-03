# Python Class 3478
# Lesson 7 Problem 5 Part (b)
# Author: RayThroughSpace (328031)

import turtle

class SuperAwesomeTurtle(turtle.Turtle):
    '''a super awesome turtle!'''
    def __init__(self):
        """SuperAwesomeTurtle() 
        creates a super awesome turtle"""
        turtle.Turtle.__init__(self)
        self.speed = 0
        
        self.getscreen().onkey(self.speed_up, "Up")
        self.getscreen().onkey(self.slow_down, "Down")
        self.getscreen().onkey(self.left_turn, "Left")
        self.getscreen().onkey(self.right_turn, "Right")
        self.getscreen().onkey(self.stop, "s")
        self.getscreen().onkey(self.close, "q")
        
        self.goforward()
    
    def goforward(self):
        """SuperAwesomeTurtle.goforward() -> None
        goes forward at self.speed every 10 ms"""
        self.forward(self.speed)
        self.getscreen().ontimer(self.goforward, 10)
        
    def speed_up(self):
        """SuperAwesomeTurtle.speed_up() -> None
        increases speed by 25units/s"""
        self.speed += 0.025
    
    def slow_down(self):
        """SuperAwesomeTurtle.slow_down() -> None
        decreases speed by 25 units/s"""
        self.speed -= 0.025
        
    def left_turn(self):
        """SuperAwesomeTurtle.left_turn() -> None
        turns left by 90 degrees"""
        self.left(90)
    
    def right_turn(self):
        """SuperAwesomeTurtle.right_turn() -> None
        turns right by 90 degrees"""
        self.right(90)
        
    def stop(self):
        """SuperAwesomeTurtle.stop() -> None
        stops this turtle"""
        self.speed = 0
    
    def close(self):
        """SuperAwesomeTurtle.close() -> None
        closes the window and program"""
        self.getscreen().bye()

wn = turtle.Screen()
pete = SuperAwesomeTurtle()
wn.listen()
wn.mainloop()