# By Joshua Pardhe. Copyright 2020. Free to use with attribution.

import pygame
import sys
import os
import random

hitcount = 0

currPath = os.path.dirname('Pygame')
pygame.mixer.pre_init(44100, 16, 2, 4096)

pygame.init()

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("dis a c00l game")

walkRight = [pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\R1.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\R2.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\R3.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\R4.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\R5.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\R6.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\R7.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\R8.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\R9.png")]
walkLeft = [pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\L1.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\L2.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\L3.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\L4.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\L5.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\L6.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\L7.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\L8.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\L9.png")]
bg = pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\bg.jpg")
char = pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\standing.png")

clock = pygame.time.Clock()
# bulletSound = pygame.mixer.Sound(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\shotNew.mp3")
# hitSound = pygame.mixer.Sound(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\diedsound.mp3")
music = pygame.mixer.music.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\music.mp3")
pygame.mixer.music.play(-1)
score = 0

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 100
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('cancun', 100)
        text = font1.render('-5', 1, (255, 0, 0))
        win.blit(text, (250 - (text.get_width()/2), 200))
        pygame.display.update()
        i = 0
        while i < 100:
            pygame.time.delay(5)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()

class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x= x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class enemy(object):
    walkRight = [pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\R1E.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\R2E.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\R3E.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\R4E.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\R5E.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\R6E.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\R7E.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\R8E.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\R9E.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\R10E.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\R11E.png")]
    walkLeft = [pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\L1E.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\L2E.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\L3E.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\L4E.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\L5E.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\L6E.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\L7E.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\L8E.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\L9E.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\L10E.png"), pygame.image.load(r"C:\Users\Joshua Pardhe\Documents\Summer20Work\Pygame\L11E.png")]

    def __init__(self, x, y, width, height, end, start):
        self.x = x
        self.y = y
        self.start = start
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10 # health of the character
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5*(10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            # pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health != 0:
            self.health -= 1
        else:
            self.visible = False
        print("hit")



# redraw function at 27fps, I have 27 sprites
def redrawGameWindow():
    win.blit(bg, (0,0))
    text = font.render('Score: ' + str(score), 1, (0, 0, 0))
    win.blit(text, (385, 10))
    mainPlayer.draw(win)
    enemyCharacter.draw(win)
    for bullet in bullets :
        bullet.draw(win)
    pygame.display.update()

# main loop
font = pygame.font.SysFont('cancun', 30, True) # type, size bold, italics
mainPlayer = player(300, 410, 64, 64)
enemyCharacter = enemy(100, 410, 64, 64, 450)
shootLoop = 0
bullets = []
run = True
respawnCounter = 0
randomXVal = [100, 150, 200, 135, 400]


while run:
    clock.tick(27)

    if enemyCharacter.visible == False:
        if respawnCounter > 50:
            enemyCharacter = enemy(random.choice(randomXVal), 410, 64, 64, 450)
        else:
            respawnCounter += 1
    else:
        respawnCounter = 0

    if enemyCharacter.visible == True:
        if mainPlayer.hitbox[1] < enemyCharacter.hitbox[1] + enemyCharacter.hitbox[3] and mainPlayer.hitbox[1] + mainPlayer.hitbox[3] > enemyCharacter.hitbox[1]:
            if mainPlayer.hitbox[0] + mainPlayer.hitbox[2] > enemyCharacter.hitbox[0] and mainPlayer.hitbox[0] < enemyCharacter.hitbox[0] + enemyCharacter.hitbox[2]:
                mainPlayer.hit()
                score -= 5

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit(0)

    for bullet in bullets:
        if bullet.y - bullet.radius < enemyCharacter.hitbox[1] + enemyCharacter.hitbox[3] and bullet.y + bullet.radius > enemyCharacter.hitbox[1]:
            if bullet.x + bullet.radius > enemyCharacter.hitbox[0] and bullet.x - bullet.radius < enemyCharacter.hitbox[0] + enemyCharacter.hitbox[2]:
                # hitSound.play()
                if enemyCharacter.visible == True:
                    enemyCharacter.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        # bulletSound.play()
        if mainPlayer.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 10:
            bullets.append(projectile(round(mainPlayer.x + mainPlayer.width // 2), round(mainPlayer.y + mainPlayer.height // 2), 5, (0, 0, 0), facing))

        shootLoop = 1

    if keys[pygame.K_LEFT] and mainPlayer.x > 5:
        mainPlayer.x -= mainPlayer.vel
        mainPlayer.left = True
        mainPlayer.right = False
        mainPlayer.standing = False
    elif keys[pygame.K_RIGHT] and mainPlayer.x < 431:
        mainPlayer.x += mainPlayer.vel
        mainPlayer.left = False
        mainPlayer.right = True
        mainPlayer.standing = False
    else:
        mainPlayer.standing = True
        mainPlayer.walkCount = 0
    if not(mainPlayer.isJump):
        if keys[pygame.K_UP] and mainPlayer.y < 431:
            mainPlayer.isJump = True
            mainPlayer.left = False
            mainPlayer.right = False
            mainPlayer.walkCount = 0

    else:
        if mainPlayer.jumpCount >= -10:
            neg = 1
            if mainPlayer.jumpCount < 0:
                neg = -1
            mainPlayer.y -= (mainPlayer.jumpCount ** 2) * 0.5 * neg
            mainPlayer.jumpCount -= 1
        else:
            mainPlayer.isJump = False
            mainPlayer.jumpCount = 10

    redrawGameWindow()


# Keep the window open until closed
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#              sys.exit(0)
