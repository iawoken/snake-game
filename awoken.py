import turtle # Asıl kullanacak olduğumuz modülü projemize ekledik.
import time, random # Diğer gerekli modülleri projemize tanımladık.

class SnakeGame():
    def __init__(self):
        self.sure = 0.15 # Yılanımızın hızını buradan belirliyoruz.
        self.puan = 0 # Oyun başlangıcında skorumuzun ne olacağını belirtiyoruz.
        self.kuyruklar = [] # Yılan'ın kuyruklarını tanımlıyoruz. (Boş bir liste oluşturduk)
        # - Oyun'un penceresini oluşturalım - #
        self.anaPencere = turtle.Screen() # Oyunumuzun ana penceresini tanımladık.
        self.anaPencere.title('Snake Game by awoken :)') # Pencere ismini belirliyoruz.
        self.anaPencere.bgcolor('peru') # Oyunumuzun arka plan rengini belirliyoruz.
        self.anaPencere.setup(width=600, height=600) # Oyunun pencere boyutunu belirliyoruz.
        self.anaPencere.tracer(0) # Oyun ekranının güncellenmesini engelliyoruz.
        # - Yılanımızı oluşturalım - #
        self.snake = turtle.Turtle() # Yılan objesini oluşturduk.
        self.snake.speed(0) # Yılanımızın hızını ayarladık.
        self.snake.shape('square') # Yılanımızın görünüşünü ayarladık. (square => Kare)
        self.snake.color('black') # Yılanımızın rengini ayarladık.
        self.snake.penup() # Yılanımız hareket ederken bir şeyler yazmayacağı için bunu kapatıyoruz.
        self.snake.goto(0, 100) # Yılanımız, oyun başlangıcında merkezde belirecek.
        self.snake.direction = 'stop' # Yılanımızın hareket etmesini engelledik.
        # - Yemeği oluşturalım - #
        self.yemek = turtle.Turtle() # Yemek objesini oluşturduk.
        self.yemek.speed(0) # Yemeğimizin hareket etmemesini ayarladık.
        self.yemek.shape('circle') # Yemek objemizin yuvarlak olmasını tanımladık.
        self.yemek.color('blue') # Yemek objesinin mavi renkte olmasını ayarladık.
        self.yemek.penup() # Yemek objesinin hareket ederken çizim yapmasını engelledik.
        self.yemek.shapesize(0.80, 0.80) # Oluşturduğumuz yuvarlak yemek objesinin boyutunu belirledik.
        self.yemek.goto(0, 0) # Yemek objemizin oyunda bulunduğu yeri tanımlıyoruz.
        # - Skor tablosunu oluşturalım - #
        self.skor = turtle.Turtle() # Skor tablosunu oluşturduk.
        self.skor.speed(0) # Skor tablomuzun hızını ayarladık. (Hareket etmeyeceği için 0 değerini tanımlıyoruz.)
        self.skor.shape('square') # Skor tablomuzun biçimini tanımlıyoruz.
        self.skor.color('dark slate gray') # Skor tablomuzun rengini belirledik.
        self.skor.penup() # Skor tablomuzun hareket ederken çizim yapmasını engelledik.
        self.skor.hideturtle() # Bu objeyi gizliyoruz.
        self.skor.goto(0, 260) # Objemizin yerini tanımlıyoruz.
        self.skor.write("Skor: {}".format(self.puan), align="center", font=("Courier", 24, "normal")) # Skor'umuzu yazdırıyoruz. Ayrıca font ve yazı büyüklüğü ayarlarını yapıyoruz.
        # - Sahip bilgileri - #
        self.sahipInfo = turtle.Turtle() # Skor tablosunu oluşturduk.
        self.sahipInfo.speed(0) # Skor tablomuzun hızını ayarladık. (Hareket etmeyeceği için 0 değerini tanımlıyoruz.)
        self.sahipInfo.shape('square') # Skor tablomuzun biçimini tanımlıyoruz.
        self.sahipInfo.color('dark slate gray') # Skor tablomuzun rengini belirledik.
        self.sahipInfo.penup() # Skor tablomuzun hareket ederken çizim yapmasını engelledik.
        self.sahipInfo.hideturtle() # Bu objeyi gizliyoruz.
        self.sahipInfo.goto(0, -275) # Objemizin yerini tanımlıyoruz.
        self.sahipInfo.write("Program awoken tarafından kodlanmıştır.", align="left", font=("Courier", 9, "normal")) # Skor'umuzu yazdırıyoruz. Ayrıca font ve yazı büyüklüğü ayarlarını yapıyoruz.
        # - Oyunumuzu başlatan fonksiyonu tanımlayalım - #
        self.Game()

    # - Yılanımızın hareketi için gerekli fonksiyonları yazalım - #
    
    def hareket(self):
        if self.snake.direction == "up":
            y = self.snake.ycor()
            self.snake.sety(y + 20)

        if self.snake.direction == "down":
            y = self.snake.ycor()
            self.snake.sety(y - 20)

        if self.snake.direction == "right":
            x = self.snake.xcor()
            self.snake.setx(x + 20)

        if self.snake.direction == "left":
            x = self.snake.xcor()
            self.snake.setx(x - 20)

    def yukariGit(self):
        if self.snake.direction != "down":
            self.snake.direction = "up"
        
    def asagiGit(self):
        if self.snake.direction != "up":
            self.snake.direction = "down"

    def sagaGit(self):
        if self.snake.direction != "left":
            self.snake.direction = "right"
        
    def solaGit(self):
        if self.snake.direction != "right":
            self.snake.direction = "left"

    def Game(self):
        self.anaPencere.listen() # Yılanımızın hareketi için klavye tuşlarını dinliyoruz.
        self.anaPencere.onkey(self.yukariGit, "Up") # Yukarı ok tuşuna basılınca yapılacak işlem.
        self.anaPencere.onkey(self.asagiGit, "Down") # Aşağı ok tuşuna basılınca yapılacak işlem.
        self.anaPencere.onkey(self.sagaGit, "Right") # Sağ ok tuşuna basılınca yapılacak işlem.
        self.anaPencere.onkey(self.solaGit, "Left") # Sol ok tuşuna basılınca yapılacak işlem.
        while True:
            self.anaPencere.update()

            if self.snake.xcor() > 300 or self.snake.xcor() < -300 or self.snake.ycor() > 300 or self.snake.ycor() < -300:
                # Yılanımızın duvarlara çarpınca durmasını ve skoru sıfırlamasını ayarlıyoruz.
                time.sleep(0.75) # 0.75 saniye beklemesini istedik.
                self.snake.goto(0, 0) # Yılanımızı merkeze tekrar gönderdik.
                self.snake.direction = "stop" # Yılanımızı durdurduk.
                for kuyruk in self.kuyruklar:
                    kuyruk.goto(1000, 1000) # Kuyruklarımızı belirtilen kordinata gönderiyoruz.
                self.puan = 0 # Skorumuzu sıfırladık.
                self.kuyruklar = [] # Yılan'ın kuyruklarını sıfırladık.
                self.skor.clear() # Skor tablosunu sıfırladık.
                self.skor.write("Skor: {}".format(self.puan), align="center", font=("Courier", 24, "normal")) # Skor'umuzu yazdırıyoruz. Ayrıca font ve yazı büyüklüğü ayarlarını yapıyoruz.
            
            if self.snake.distance(self.yemek) < 20:
                # Yılan yemeği yer ise yapılacak işlemler.
                x = random.randint(-250, 250) # -250 ve 250 arasında rastgele bir tam sayı değeri veriyoruz. Bu bizim "X" kordinatımız.
                y = random.randint(-250, 250) # -250 ve 250 arasında rastgele bir tam sayı değeri veriyoruz. Bu bizim "Y" kordinatımız.
                
                self.yemek.goto(x, y) # Yemek objemizi belirtilen kordinatlara gönderiyoruz.

                yeniKuyruk = turtle.Turtle() # Yeni bir kuyruk objesi oluşturuyoruz.
                yeniKuyruk.speed(0) # Kuyruk objesinin hızını belirtiyoruz.
                yeniKuyruk.shape("square") # Kuyruk objesinin görünümünü ayarladık.
                yeniKuyruk.color("tomato") # Kuyruk objesinin rengini belirtiyoruz.
                yeniKuyruk.penup() # Oluşturduğumuz kuyruğun hareket ederken çizim yapmasını engelledik.

                self.kuyruklar.append(yeniKuyruk) # Yılanımıza oluşturduğumuz kuyruk(ları) ekliyoruz.
                
                self.sure -= 0.001 # Yılanımızı hızlandırıyoruz.
                self.puan += 10 # Skorumuzu "10" arttırıyoruz.

                self.skor.clear() # Skorumuzu temizliyoruz.
                self.skor.write("Skor: {}".format(self.puan), align="center", font=("Courier", 24, "normal")) # Skor'umuzu yazdırıyoruz. Ayrıca font ve yazı büyüklüğü ayarlarını yapıyoruz.

            for yilan in range(len(self.kuyruklar) - 1, 0, -1):
                # Yılan'ın kuyruklarını "yilan" değerine atıyoruz.
                x = self.kuyruklar[yilan - 1].xcor() # "X" kordinatlarını belirledik.
                y = self.kuyruklar[yilan - 1].ycor() # "Y" kordinatlarını belirledik.

                self.kuyruklar[yilan].goto(x, y) # Yılanımızın kuyruklarını yılanımız ile birleştiriyoruz.

            if len(self.kuyruklar) > 0: 
                # Yılanımızın kuyruğu var ise yapılacak işlemler:
                x = self.snake.xcor() # Yılanımızın "X" kordinatlarını aldık.
                y = self.snake.ycor() # Yılanımızın "Y" kordinatlarını aldık.
                self.kuyruklar[0].goto(x, y) # Yılanımızın kuyruk(larını) yılanımız ile birleştiriyoruz.

            self.hareket()
            time.sleep(self.sure)

try:
    if __name__ == "__main__":
        SnakeGame()
except:
    print("Program üzerinde bir hata meydana geldi.")
    time.sleep(0.5)
    exit()