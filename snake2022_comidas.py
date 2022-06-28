import turtle
import tkinter
import time
import random

posponer = 0.1

score = 0
high_score = 0

ventana = tkinter.Tk()
tabla = []

wn = turtle.Screen()
wn.title("Juego Snake")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)


comida = turtle.Turtle()
comida.speed(0)
comida.shape("triangle")
comida.color("red")
comida.penup()
comida.goto(0,100)


def jugar():
    for k in range(10):
        tabla[k][k].config(bg='Blue')
        time.sleep(1)


for i in range(10):
    fila = []
    for j in range(10):
        boton = tkinter.Button(ventana, bg='Orange', command=jugar)
        boton.config(relief=tkinter.SUNKEN)
        boton.grid(column=i, row=j)
        fila.append(boton)
    tabla.append(fila)
    
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,0)


def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"
    
def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
        
    if cabeza.direction == "left":
        x = cabeza.ycor()
        cabeza.setx(x - 20)
        
    if cabeza.direction == "right":
        x = cabeza.ycor()
        cabeza.setx(x + 20)

wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

while True:
    wn.update()
    
    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)
    
    mov()
    time.sleep(posponer)
 
ventana.mainloop()

    
