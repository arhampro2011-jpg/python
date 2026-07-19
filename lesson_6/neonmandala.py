import turtle

screen=turtle.Screen()
screen.bgcolor('black')
screen.title('mandala')

board=turtle.Turtle()
board.speed('fastest')
board.shape('turtle')


colors=['blue','yellow','green','magenta','pink','cyan','white']
for i in range(100):
    board.color(colors[i % len(colors)])
    board.width(3)
    board.forward(i*2)
    board.dot(15)
    board.right(91)
    
turtle.done()