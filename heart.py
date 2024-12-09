# import the turtle module
import turtle as t

#screen to draw our heart
s = t.Screen()

#background color
s.bgcolor('black')

# pen used to draw 
pen = t.Turtle()
pen.speed(1)
pen.color('red')
pen.begin_fill()
pen.fillcolor('red')
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.setheading(60)
pen.circle(-90, 200)
pen.forward(180)
# stop drawing
pen.end_fill()

#hide pen
pen.hideturtle()

#close mainloop
s.mainloop()