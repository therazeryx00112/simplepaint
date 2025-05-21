import turtle

# Основная черепашка
t = turtle.Turtle()
t.color("blue")
t.width(5)
t.shape('circle')
t.pendown()
t.speed(3)

filling = False

def draw(x, y):
    t.goto(x, y)

def setGreen():
    t.color('green')

def setBlue():
    t.color('blue')

def setRed():
    t.color('red')

def stepRight():
    t.goto(t.xcor() + 5, t.ycor())

def stepUp():
    t.goto(t.xcor(), t.ycor() + 5)

def stepLeft():
    t.goto(t.xcor() - 5, t.ycor())

def stepDown():
    t.goto(t.xcor(), t.ycor() - 5)

def endFill():
    global filling
    filling = False
    t.end_fill()

def startFill():
    global filling
    filling = True
    t.begin_fill()

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def increase_width():
    current = t.width()
    t.width(current + 1)
    print(f"Толщина пера: {t.width()}")

def decrease_width():
    current = t.width()
    if current > 1:
        t.width(current - 1)
        print(f"Толщина пера: {t.width()}")

# Очистка и выход
def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
    paint_interface()
    create_size_buttons()
    create_system_buttons()

def exit_program():
    turtle.bye()

# Кнопки + и -
def create_size_buttons():
    plus = turtle.Turtle()
    plus.hideturtle()
    plus.penup()
    plus.color("blue")
    plus.goto(150, 20)
    plus.write("+", align="center", font=("Arial", 32, "bold"))

    minus = turtle.Turtle()
    minus.hideturtle()
    minus.penup()
    minus.color("blue")
    minus.goto(150, 0)
    minus.write("-", align="center", font=("Arial", 32, "bold"))

# Цветовые кнопки
def paint_interface():
    def color_button(x, color_code, label):
        btn = turtle.Turtle()
        btn.penup()
        btn.goto(x, 400)
        btn.pendown()
        btn.color(color_code)
        btn.begin_fill()
        btn.circle(15)
        btn.end_fill()

        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.goto(x - 5, 379)
        text.color("black")
        text.write(label, font=("Arial", 14, "bold"))

    color_button(-100, 'red', "R")
    color_button(-65, 'green', "G")
    color_button(-20, 'blue', "B")

# Новые интерфейсные кнопки: очистка и выход
def create_system_buttons():
    # Кнопка очистки экрана
    clear_btn = turtle.Turtle()
    clear_btn.penup()
    clear_btn.goto(200, 400)
    clear_btn.pendown()
    clear_btn.color('orange')
    clear_btn.begin_fill()
    clear_btn.circle(15)
    clear_btn.end_fill()

    clear_text = turtle.Turtle()
    clear_text.hideturtle()
    clear_text.penup()
    clear_text.goto(192, 379)
    clear_text.color("black")
    clear_text.write("C", font=("Arial", 14, "bold"))

    # Кнопка выхода
    quit_btn = turtle.Turtle()
    quit_btn.penup()
    quit_btn.goto(250, 400)
    quit_btn.pendown()
    quit_btn.color('gray')
    quit_btn.begin_fill()
    quit_btn.circle(15)
    quit_btn.end_fill()

    quit_text = turtle.Turtle()
    quit_text.hideturtle()
    quit_text.penup()
    quit_text.goto(243, 379)
    quit_text.color("black")
    quit_text.write("Esc", font=("Arial", 14, "bold"))

# Настройка управления клавишами
scr = turtle.Screen()
scr.listen()

# Цвета
scr.onkey(setGreen, 'g')
scr.onkey(setBlue, 'b')
scr.onkey(setRed, 'r')

# Движение
scr.onkey(stepRight, 'Right')
scr.onkey(stepUp, 'Up')
scr.onkey(stepLeft, 'Left')
scr.onkey(stepDown, 'Down')

# Заливка
scr.onkey(startFill, 'f')
scr.onkey(endFill, 'e')

# Толщина
scr.onkey(increase_width, '=')
scr.onkey(decrease_width, '-')

# Очистка и выход
scr.onkey(clear_screen, 'c')      # Очистка
scr.onkey(exit_program, 'Escape') # Выход

# Другое
t.ondrag(draw)
scr.onscreenclick(move)

# Интерфейс
paint_interface()
create_size_buttons()
create_system_buttons()

turtle.done()


