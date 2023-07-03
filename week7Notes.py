"""KEY PRESSES"""
# =============================================================================
# import turtle
# 
# turtle.setup(400,500)                # Determine the window size
# wn = turtle.Screen()                 # Get a reference to the window
# wn.title("Handling keypresses!")     # Change the window title
# wn.bgcolor("lightgreen")             # Set the background color
# tess = turtle.Turtle()               # Create our favorite turtle
# 
# # The next four functions are our "event handlers".
# def h1():
#     tess.forward(30)
# 
# def h2():
#     tess.left(45)
# 
# def h3():
#     tess.right(45)
# 
# def h4():
#     wn.bye()                        # Close down the turtle window
# 
# # These lines "wire up" keypresses to the handlers we've defined.
# wn.onkey(h1, "Up")
# wn.onkey(h2, "Left")
# wn.onkey(h3, "Right")
# wn.onkey(h4, "q")
# # Now we need to tell the window to start listening for events,
# # If any of the keys that we're monitoring is pressed, its
# # handler will be called.
# wn.listen()
# wn.mainloop()
# 
# =============================================================================
"""MOUSE EVENTS"""
# =============================================================================
# import turtle
# 
# turtle.setup(400,500)
# wn = turtle.Screen()
# wn.title("How to handle mouse clicks on the window!")
# wn.bgcolor("lightgreen")
# 
# tess = turtle.Turtle()
# tess.color("purple")
# tess.pensize(3)
# tess.shape("circle")
# 
# def h1(x, y):
#     tess.goto(x, y)
# 
# wn.onclick(h1)  # Wire up a click on the window.
# wn.mainloop()
# =============================================================================
# =============================================================================
# import turtle
# 
# turtle.setup(400,500)              # Determine the window size
# wn = turtle.Screen()               # Get a reference to the window
# wn.title("Handling mouse clicks!") # Change the window title
# wn.bgcolor("lightgreen")           # Set the background color
# tess = turtle.Turtle()             # Create two turtles
# tess.color("purple")
# alex = turtle.Turtle()             # Move them apart
# alex.color("blue")
# alex.forward(100)
# 
# def handler_for_tess(x, y):
#     wn.title("Tess clicked at "+str(x)+","+str(y))
#     tess.left(42)
#     tess.forward(30)
# 
# def handler_for_alex(x, y):
#     wn.title("Alex clicked at "+str(x)+","+str(y))
#     alex.right(84)
#     alex.forward(50)
# 
# tess.onclick(handler_for_tess)
# alex.onclick(handler_for_alex)
# 
# wn.mainloop()
# =============================================================================
"""TIMER EVENTS"""
# =============================================================================
# import turtle
# 
# turtle.setup(400,500)
# wn = turtle.Screen()
# wn.title("Using a timer to get events!")
# wn.bgcolor("lightgreen")
# 
# tess = turtle.Turtle()
# tess.color("purple")
# 
# def h1():
#     tess.forward(100)
#     tess.left(56)
#     wn.ontimer(h1, 60)
# 
# h1()
# wn.mainloop()
# =============================================================================
# =============================================================================
"""STATE MACHINES"""
# import turtle         # Tess becomes a traffic light.
# 
# turtle.setup(400,500)
# wn = turtle.Screen()
# wn.title("Tess becomes a traffic light!")
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle()
# 
# def draw_housing():
#     """ Draw a nice housing to hold the traffic lights """
#     tess.pensize(3)
#     tess.color("black", "darkgrey")
#     tess.begin_fill()
#     tess.forward(80)
#     tess.left(90)
#     tess.forward(200)
#     tess.circle(40, 180)
#     tess.forward(200)
#     tess.left(90)
#     tess.end_fill()
# 
# draw_housing()
# tess.penup()
# # Position tess onto the place where the green light should be
# tess.forward(40)
# tess.left(90)
# tess.forward(50)
# # Turn tess into a big green circle
# tess.shape("circle")
# tess.shapesize(3)
# tess.fillcolor("green")
# 
# # A traffic light is a kind of state machine with three states,
# # Green, Yellow, Red.  We number these states  0, 1, 2
# # When the machine changes state, we change tess' position and
# # her fillcolor.
# 
# stateNum = 0
# 
# def state_machine():
#     global stateNum
#     if (stateNum ==0):
#         tess.forward(70)
#         tess.fillcolor("yellow")
#         stateNum = 1
#     elif(stateNum == 1):
#         tess.forward(70)
#         tess.fillcolor("red")
#         stateNum = 2
#     else:
#         tess.back(140)
#         tess.fillcolor("green")
#         stateNum = 0
# wn.onkey(state_machine, "space")
# wn.listen()                 # Listen for events
# wn.mainloop()
# =============================================================================
"""TKINTER"""
# =============================================================================
# from tkinter import *
# 
# class HelloWorldFrame(Frame):
#     '''creates a hello world window'''
# 
#     def __init__(self, master):
#         '''HelloWorldFrame()
#         creates a new HelloWorldFrame'''
#         Frame.__init__(self, master)  # set up as a Tk frame
#         self.grid()  # place the frame in the root window
#         # create a button
#         self.hwButton = Button(self, text='Click me!', command=self.print_message)
#         self.hwButton.grid(row=0, column=0)
#         # create a text display
#         self.hwMessageBox = Label(self, text="I'm waiting...")
#         self.hwMessageBox.grid(row=1, column=0)
# 
#     def print_message(self):
#         '''prints hello world message'''
#         self.hwMessageBox['text'] = 'Hello, World!'
# 
# root = Tk()
# hwf = HelloWorldFrame(root)
# hwf.mainloop()
# =============================================================================
"""PROBLEMS"""
# =============================================================================
# import turtle
# import random
# 
# # you should add handlers
# def h1():
#     for t in turtles:
#         amt = random.randint(1,50)
#         t.forward(amt)
# 
# def h2():
#     tRed.left(15)
#     tBlue.left(30)
#     tGreen.left(45)
# 
# 
# def h3():
#     tRed.right(15)
#     tBlue.right(30)
#     tGreen.right(45)
#             
# # set up window and turtles
# wn = turtle.Screen()
# tRed = turtle.Turtle()
# tRed.color('red')
# tBlue = turtle.Turtle()
# tBlue.color('blue')
# tGreen = turtle.Turtle()
# tGreen.color('green')
# turtles = [tRed, tGreen, tBlue]
# # listeners
# # you should add
# wn.onkey(h1, "Up")
# wn.onkey(h2, "Left")
# wn.onkey(h3, "Right")
# 
# # listen and run
# wn.listen()
# wn.mainloop()
# =============================================================================
# =============================================================================
# import turtle
# 
# # you'll need to add more code
# def teleport_and_draw(x,y):
#     carol.pendown()
#     carol.goto(x,y)
# 
# def teleport_and_no_draw(x,y):
#     carol.penup()
#     carol.goto(x,y)
#     
# # set up window and TT
# wn = turtle.Screen()
# carol = turtle.Turtle()
# 
# # listeners to teleport
# wn.onclick(teleport_and_draw,1)    # left click
# wn.onclick(teleport_and_no_draw,2) # right click
# 
# # turn on the listeners and run
# wn.listen()
# wn.mainloop()
# =============================================================================
# =============================================================================
# from tkinter import *
# 
# class ClickFrame(Frame):
#     
#     def __init__(self, root):
#         """ClickFrame(root) -> ClickFrame
#         initializes a ClickFrame"""
#         Frame.__init__(self, root)
#         self.grid()
#         
#         self.button = Button(self, text = "Click me!", command = self.display_count)
#         self.button.grid(row = 0, column = 0)
#         self.count = 0
#         
#         self.label = Label(self, text = str(self.count) + " clicks.")
#         self.label.grid(row = 1, column = 0)
#         
#     def display_count(self):
#         """ClickFrame.display_count() -> None
#         updates click count and displays it on label"""
#         self.count+=1
#         self.label['text'] = str(self.count) + " clicks."
# 
# root = Tk()
# cframe = ClickFrame(root)
# root.mainloop()
# =============================================================================
# =============================================================================
# from tkinter import *
# 
# class EntryDemo(Frame):
#     '''demo of Entry widget'''
# 
#     def __init__(self,master):
#         '''EntryDemo(master) -> new EntryDemo frame'''
#         Frame.__init__(self,master)
#         self.grid()
# 
#         # set up control variables
#         self.inputValue = IntVar()
#         self.outputValue = IntVar()
# 
#         # set up widgets
#         Label(self,text='Input').grid(row=0,column=0)
#         Label(self,text='Input Value').grid(row=0,column=1)
#         Label(self,text='Result').grid(row=0,column=3)
#         Entry(self,width=5,textvariable=self.inputValue).grid(row=1,column=0)
#         Label(self,textvariable=self.inputValue).grid(row=1,column=1)
#         Button(self,text='>>>>>',command=self.set_output_value).grid(row=1,column=2)
#         Label(self,textvariable=self.outputValue).grid(row=1,column=3)
# 
#     def set_output_value(self):
#         '''update the output value'''
#         self.outputValue.set(2*self.inputValue.get())
# 
# root = Tk()
# root.title('Control Variable Demo')
# demo = EntryDemo(root)
# demo.mainloop()
# =============================================================================
# =============================================================================
# from tkinter import *
# 
# class Temperatures(Frame):
#     '''temperature conversion app'''
#     
#     def __init__(self,master):
#         '''Temperatures(master) -> new temperature conversion window'''
#         Frame.__init__(self,master)
#         self.grid()
#         # set up control variables
#         # (tkinter uses DoubleVar() for floats)
#         self.fahr = DoubleVar()
#         self.cels = DoubleVar()
#         # initialize values to freezing point of water
#         self.fahr.set(32.0)
#         self.cels.set(0.0)
#         # set up widgets
#         Label(self,text="Fahrenheit").grid(row=0,column=0)
#         Label(self,text="Celsius").grid(row=0,column=1)
#         Entry(self,textvariable=self.fahr).grid(row=1,column=0)
#         Entry(self,textvariable=self.cels).grid(row=1,column=1)
#         Button(self,text=">>>>>",command=self.fahr_to_cels).grid(row=2,column=0)
#         Button(self,text="<<<<<",command=self.cels_to_fahr).grid(row=2,column=1)
#         
#     # you have to write the handler methods
#     def fahr_to_cels(self):
#         """Temperatures.fahr_to_cels() -> None
#         converts fahr to cels"""
#         self.cels.set(5/9 * (self.fahr.get() - 32))
#         
#     def cels_to_fahr(self):
#         """Temperatures.cels_to_fahr() -> None
#         converts cels to fahr"""
#         self.fahr.set(9/5 * self.cels.get() + 32)
#         
#     
# root = Tk()
# root.title('Temperature Conversion')
# temps = Temperatures(root)
# temps.mainloop()
# =============================================================================
import turtle

class SuperAwesomeTurtle(turtle.Turtle):
    '''a super awesome turtle!'''

    def __init__(self):
        """SuperAwesomeTurtle() -> SuperAwesomeTurtle
        initializes a super awesome turtle"""
        turtle.Turtle.__init__(self)
        self.speed = 0
        self.getscreen().onkey(self.speedup, "Up")
        self.getscreen().onkey(self.slowdown, "Down")
        self.getscreen().onkey(self.tleft, "Left")
        self.getscreen().onkey(self.tright, "Right")
        self.getscreen().onkey(self.stop, "s")
        self.getscreen().onkey(self.qquit, "q")
        
        self.goforward()
        
    def goforward(self):
        self.forward(self.speed)
        self.getscreen().ontimer(self.goforward, 40)
        
    def speedup(self):
        self.speed += 1
        
    def slowdown(self):
        self.speed -= 1
        
    def tleft(self):
        self.left(90)
        
    def tright(self):
        self.right(90)
        
    def stop(self):
        self.speed = 0
        
    def qquit(self):
        self.getscreen().bye()

wn = turtle.Screen()
pete = SuperAwesomeTurtle()
wn.listen()
wn.mainloop()