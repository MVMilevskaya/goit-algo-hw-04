import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

try:
    user_order = input("Введіть рівень рекурсії (рекомендується до 3-4): ")
    # Викликаємо функцію з введеним користувачем значенням
    user_order = int(user_order.replace(',', '.'))
    if user_order > 5:
            print("Увага: занадто великий рівень може «повісити» комп'ютер!")
    draw_koch_snowflake(user_order)
except ValueError:
    print("Будь ласка, введіть ціле число!")
except KeyboardInterrupt:
    print("\nПрограму зупинено користувачем (Ctrl + C). До побачення!")