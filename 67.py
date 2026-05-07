import turtle
import random

def start_dvd_screen():
    # Set up the screen
    screen = turtle.Screen()
    screen.title("67 DVD Screen Saver")
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.tracer(0) # Turns off automatic updates for smooth animation

    # Create the '67' turtle
    logo = turtle.Turtle()
    logo.speed(0)
    logo.color("white")
    logo.penup()
    logo.hideturtle()
    
    # Initial position and speed
    logo.goto(0, 0)
    x_speed = 0.5
    y_speed = 0.5
    
    # Colors to cycle through
    colors = ["red", "green", "blue", "yellow", "magenta", "orange", "cyan"]

    while True:
        screen.update() # Manually update screen
        
        # Move the turtle
        logo.setx(logo.xcor() + x_speed)
        logo.sety(logo.ycor() + y_speed)
        
        # Draw the "67"
        logo.clear()
        logo.write("67", align="center", font=("Arial", 60, "bold"))
        
        # Get current coordinates
        x = logo.xcor()
        y = logo.ycor()
        
        # Check for collision with walls and bounce
        # 400 and 300 are half of the screen width/height
        if x > 380 or x < -380:
            x_speed *= -1
            logo.color(random.choice(colors)) # Change color
            
        if y > 280 or y < -280:
            y_speed *= -1
            logo.color(random.choice(colors)) # Change color

# --- Main Program ---
ka = False
while ka == False:
    try:
        print("What is the best number")
        num = int(input())
        if num == 67:
            ka = True
            start_dvd_screen()
        else:
            print("You stink")
    except ValueError:
        print("You stink")
