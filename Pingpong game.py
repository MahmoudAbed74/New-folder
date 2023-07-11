import turtle

window = turtle.Screen()#بتستدعي الشاشة
window.title("pingpong by mahmoud")
window.bgcolor("Black")
window.setup(width=800,height=600)
window.tracer(0)#دا بيمنع ننا نعمل تحديث للشاشة عشان لو عاوز اسرع اللعبة

#madrab1
madrab1 = turtle.Turtle()#عرفت المضرب و هبدا استدعي المكتبة بتاعته مسستخدمه عن طريق الاوبجكت
madrab1.speed(0)#دي سرعة تحديث اامضرب علي الشاشة عشان محسش بلاج
madrab1.shape("square")#بحدد شكل المضرب
madrab1.color("blue")
madrab1.shapesize(stretch_wid=5,stretch_len=1)
madrab1.penup()#مش هيخلي المضرب يرسم اي خطوط بعد ما يتحرك
madrab1.goto(-370,0)#بحدد يظهر فين عن طريق (x,y)

#madrabe2
madrab2 = turtle.Turtle()#عرفت المضرب و هبدا استدعي المكتبة بتاعته مسستخدمه عن طريق الاوبجكت
madrab2.speed(0)#دي سرعة تحديث اامضرب علي الشاشة عشان محسش بلاج
madrab2.shape("square")#بحدد شكل المضرب
madrab2.color("red")
madrab2.shapesize(stretch_wid=5,stretch_len=1)
madrab2.penup()#مش هيخلي المضرب يرسم اي خطوط بعد ما يتحرك
madrab2.goto(370,0)#بحدد يظهر فين عن طريق (x,y)

#ball
ball = turtle.Turtle()#عرفت المضرب و هبدا استدعي المكتبة بتاعته مسستخدمه عن طريق الاوبجكت
ball.speed(0)#دي سرعة تحديث اامضرب علي الشاشة عشان محسش بلاج
ball.shape("square")#بحدد شكل المضرب
ball.color("green")
ball.penup()#مش هيخلي المضرب يرسم اي خطوط بعد ما يتحرك
ball.goto(0,0)#بحدد يظهر فين عن طريق (x,y)
ball.dx = .1 # بتتحرك مقدار 2.5 اي سرعة بتاعتها
ball.dy = .1 

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player1: 0   palyer2: 0 ",align="center",font=("Courier",24,"normal"))
#functions
def madrab1_up():
    y =madrab1.ycor() #اعرفلي قيمة y الحالية
    y += 20 #زودلي عليها 20
    madrab1.sety(y) #سجلي مكانها دا الاساسي
#keyboard bindings
window.listen()
window.onkeypress(madrab1_up,"w") #لما تتدوس فوق علي w small  يتحرك لفوق

def madrab1_down():
    y =madrab1.ycor() #اعرفلي قيمة y الحالية
    y -= 20 #زودلي عليها 20
    madrab1.sety(y) #سجلي مكانها دا الاساسي
#keyboard bindings

window.onkeypress(madrab1_down,"s") #لما تتدوس فوق علي w small  يتحرك لفوق

def madrab2_up():
    y =madrab2.ycor() #اعرفلي قيمة y الحالية
    y += 20 #زودلي عليها 20
    madrab2.sety(y) #سجلي مكانها دا الاساسي
#keyboard bindings

window.onkeypress(madrab2_up,"Up") #لما تتدوس فوق علي w small  يتحرك لفوق

def madrab2_down():
    y =madrab2.ycor() #اعرفلي قيمة y الحالية
    y -= 20 #زودلي عليها 20
    madrab2.sety(y) #سجلي مكانها دا الاساسي
#keyboard bindings

window.onkeypress(madrab2_down,"Down") #لما تتدوس فوق علي w small  يتحرك لفوق

while True:
    window.update()

    #move the ball
    ball.setx(ball.xcor()+ ball.dx)#مكان الكورة النهائي بيساوي  dx + مكان الكورة الحالي x.cor
    ball.sety(ball.ycor()+ball.dy)

    #border check 
    if ball.ycor() >290: #ليه اكبر عشان الشاشة من فوق اكبر من 300 عشان موجب ف كدا هتعدي الشاشة
        ball.sety(290)#رجعها لمكان اخر الشاشة
        ball.dy *= -1 #تنعكس لاتجاه المعاكس او تخليها تنقص ف ترد الناحية التانية
    if ball.ycor() <-290:#ليه اكبر عشان الشاشة من فوق اصغراكبر من -300 عشان سالب ف كدا هتعدي الشاشة
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor()> 390:
       ball.goto(0,0)
       ball.dx *= -1
       score2 += 1
       score.clear()
       score.write("player1: {}   palyer2: {} ".format(score1,score2),align="center",font=("Courier",24,"normal"))

    if ball.xcor()< -390 :
       ball.goto(0,0)  
       ball.dx *= -1
       score1 += 1
       score.clear()
       score.write("player1: {}   palyer2: {} ".format(score1,score2),align="center",font=("Courier",24,"normal"))

    if (ball.xcor()  > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor()  < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor()+40 and ball.ycor() > madrab1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1


