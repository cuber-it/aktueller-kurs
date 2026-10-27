#!/usr/bin/env python3
import turtle
import time

# Fenster konfigurieren
screen = turtle.Screen()
screen.title("Turtle Square Demo")
screen.bgcolor("lightblue")

# Turtle konfigurieren
pen = turtle.Turtle()
pen.pensize(3)
pen.color("darkblue")

# Quadrat zeichnen
for _ in range(4):
    pen.forward(100)
    time.sleep(5)
    pen.right(90)
    time.sleep(5)

# Fenster offen lassen bis Klick
screen.exitonclick()
