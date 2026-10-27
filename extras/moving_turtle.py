#!/usr/bin/env python3
import turtle

# Fenster konfigurieren
screen = turtle.Screen()
screen.title("Turtle Steuerung mit Tastatur")
screen.bgcolor("white")

# Turtle konfigurieren
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("green")
pen.speed(1)

# Steuerfunktionen
def move_forward():
    pen.forward(20)

def move_backward():
    pen.backward(20)

def turn_left():
    pen.left(15)

def turn_right():
    pen.right(15)

# Tastenzuordnung
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

# Hauptloop
screen.mainloop()

