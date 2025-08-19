from pygame import*

mixer.init()
mixer.music.load('c2b241eaaf1726a.mp3')
mixer.music.play()
jump = mixer.Sound('otskok-myacha.ogg')
win_lose = mixer.Sound('40a84da0291a73b-1.mp3')
lose_win = mixer.Sound('9996d7395fd837fc14.mp3')

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


back = (200, 255, 255)
win_wight = 600
win_height = 500
window = display.set_mode((win_wight, win_height))
back = transform.scale(image.load('tennisnyi-kort-s-vozduha.jpg'), (win_wight,win_height))


game = True
finish= False
clock = time.Clock()
FPS = 60


rocket1 = Player('sport_12364818.png', 30, 200, 4, 50, 150)
rocket2 = Player('sport_12364818.png', 520, 200, 4, 50, 150)
ball = GameSprite('beach-ball_8881052.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render("Игрок 1 проиграл!", True,(240, 232, 10))
lose2 = font.render("Игрок 2 проиграл!",True, (240, 232, 10))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if finish != True:
        window.blit(back,(0 , 0))
        rocket1.update_l()
        rocket2.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(rocket1, ball) or  sprite.collide_rect(rocket2, ball):
            speed_x *= -1
            speed_x *= 1.025
            speed_y *= 1.025
            jump.play()
        
        if ball.rect.bottom > win_height or ball.rect.y < 0:
            speed_y *= -1
            speed_y *= 1.025
            speed_x *= 1.025
            jump.play()

        
        if ball.rect.x < -50:
            finish = True
            window.blit(lose1, (200,200))
            win_lose.play()

        if ball.rect.x > win_wight:
            finish = True
            window.blit(lose2,(200,200))
            lose_win.play()
        

        rocket1.reset()
        rocket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
