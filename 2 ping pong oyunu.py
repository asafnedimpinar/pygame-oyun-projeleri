import turtle
import pygame

# Pygame başlatma
pygame.init()

# Turtle ekranını oluşturma
pencere = turtle.Screen()
pencere.title("PingPong")
pencere.bgcolor("black")
pencere.setup(width=800, height=600)
pencere.tracer(0)

# Sol raketin oluşturulması
raket_a = turtle.Turtle()
raket_a.speed(0)
raket_a.shape("square")
raket_a.penup()
raket_a.goto(-350, 0)
raket_a.shapesize(5, 1)
raket_a.color("white")

# Sağ raketin oluşturulması
raket_b = turtle.Turtle()
raket_b.speed(0)
raket_b.shape("square")
raket_b.color("white")
raket_b.penup()
raket_b.goto(350, 0)
raket_b.shapesize(5, 1)

# Topun oluşturulması
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.dx = 0.15  
ball.dy = 0.15  

yazi = turtle.Turtle()
yazi.speed(0)
yazi.color("white")
yazi.goto(0, 260)
yazi.write("Oyuncu A: 0    Oyuncu B: 0", align="center", font=("Courier", 24, "bold"))
yazi.hideturtle()
puan_a = 0
puan_b = 0

# Ses dosyasını yükleme
pygame.mixer.music.load("plop.mp3")

# Sol raketin yukarı hareketi
def raket_a_up():
    y = raket_a.ycor()
    y += 20
    raket_a.sety(y)

# Sol raketin aşağı hareketi
def raket_a_down():
    y = raket_a.ycor()
    y -= 20
    raket_a.sety(y)

# Sağ raketin yukarı hareketi
def raket_b_up():
    y = raket_b.ycor()
    y += 20
    raket_b.sety(y)

# Sağ raketin aşağı hareketi
def raket_b_down():
    y = raket_b.ycor()
    y -= 20
    raket_b.sety(y)

# Tuş girişlerini dinleme
pencere.listen()
pencere.onkeypress(raket_a_up, "w")
pencere.onkeypress(raket_a_down, "s")
pencere.onkeypress(raket_b_up, "Up")
pencere.onkeypress(raket_b_down, "Down")

# Oyun döngüsü
while True:
    pencere.update()  

    # Topun hareketini güncelleme
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Topun sınırları kontrol etme ve yönünü değiştirme
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1
    
    # Topun sağ sınıra ulaşıp ulaşmadığını kontrol etme
    if ball.xcor() > 390:
        pygame.mixer.music.play()
        ball.goto(0, 0)
        ball.dx *= -1
        puan_a += 1
        yazi.clear()
        yazi.write("Oyuncu A: {}    Oyuncu B: {}".format(puan_a, puan_b), align="center", font=("Courier", 24, "bold"))

    # Topun sol sınıra ulaşıp ulaşmadığını kontrol etme
    if ball.xcor() < -390:
        pygame.mixer.music.play()
        ball.goto(0, 0)
        ball.dx *= -1 
        puan_b += 1
        yazi.clear()
        yazi.write("Oyuncu A: {}    Oyuncu B: {}".format(puan_a, puan_b), align="center", font=("Courier", 24, "bold"))

    
    # Topun sağ raket ile temasını kontrol etme
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < raket_b.ycor() + 60 and ball.ycor() > raket_b.ycor() - 60):
        pygame.mixer.music.play()
        ball.setx(340)
        ball.dx *= -1

    # Topun sol raket ile temasını kontrol etme
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < raket_a.ycor() + 60 and ball.ycor() > raket_a.ycor() - 60):
        pygame.mixer.music.play()
        ball.setx(-340)
        ball.dx *= -1


# Ana ekran döngüsü
pencere.mainloop()
