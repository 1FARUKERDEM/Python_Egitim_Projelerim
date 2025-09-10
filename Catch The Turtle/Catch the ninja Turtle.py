import turtle
import random



game_area = turtle.Screen()
game_area.bgcolor("saddlebrown")
game_area.title("catch the ninja turtle")
game_area.setup(800, 600)
game_area.addshape("ninjakaplumbaga.gif")



# Skor ve süre
skor = 0
sure = 30
oyun_devam = True

# Skor yazıcı
skor_yazi = turtle.Turtle()
skor_yazi.hideturtle()
skor_yazi.penup()
skor_yazi.color("white")
skor_yazi.goto(0, 260)

# Süre yazıcı
sure_yazi = turtle.Turtle()
sure_yazi.hideturtle()
sure_yazi.penup()
sure_yazi.color("yellow")
sure_yazi.goto(0, 230)

# Mesaj yazıcı
mesaj = turtle.Turtle()
mesaj.hideturtle()
mesaj.penup()
mesaj.color("black")
mesaj.goto(0, 0)

def skor_guncelle():
    skor_yazi.clear()
    skor_yazi.write(f"Skor: {skor}", align="center", font=("Arial", 20, "bold"))

def sure_guncelle():
    sure_yazi.clear()
    sure_yazi.write(f"Süre: {sure}", align="center", font=("Arial", 16, "bold"))

# Kaplumbağa
shadow_gaplumbaga = turtle.Turtle("ninjakaplumbaga.gif")
shadow_gaplumbaga.color("black")
shadow_gaplumbaga.penup()
shadow_gaplumbaga.shapesize(1,1)

def new_location():
    if not oyun_devam:
        return
    shadow_gaplumbaga.hideturtle()
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    shadow_gaplumbaga.goto(x, y)
    shadow_gaplumbaga.showturtle()
    game_area.ontimer(new_location, 500)

def tiklandi(x, y):
    global skor
    if oyun_devam:
        skor += 1
        skor_guncelle()

# kaplumbağaya tıklayınca skor artacak
shadow_gaplumbaga.onclick(tiklandi)

# geri sayım fonksiyonu
def geri_sayim():
    global sure, oyun_devam
    if sure > 0:
        sure -= 1
        sure_guncelle()
        game_area.ontimer( geri_sayim,1000)
    else:
        oyun_devam = False
        shadow_gaplumbaga.hideturtle()
        mesaj.write("Yakalayamadın!", align="center", font=("Arial", 24, "bold"))

# oyun başlangıcı
shadow_gaplumbaga.goto(0, 0)
skor_guncelle()
sure_guncelle()

game_area.ontimer(new_location, 1000)
game_area.ontimer(geri_sayim, 1000)

turtle.done()
