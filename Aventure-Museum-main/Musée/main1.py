import pygame
import Intro
xperso = 415 # Abscisse du personnage(sans aide de chatgpt)
yperso = 650 # Ordonnée du personnage (sans aide de chatgpt)
speed = 5 # vitesse du personnage (sans l'aide de chatgpt)
alien_speed = 5 #vitesse de l'alien
xplante = 300
yplante = 450
xaln = 200
yaln = 200
xpnj = 600
ypnj = 300
s2 = 0
s3 = 0
s1 = 1

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# Charger et lancer la musique
pygame.mixer.music.load("Music/Avo3-Aventure-Museum-theme.mp3")
pygame.mixer.music.play(-1)
# Création de la fenêtre redimensionnable(sans aide)
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Aventure Museum")

# Charger les images (sans ide de chatgpt)
background1 = pygame.image.load("content/Design/salle 1 (1) (2).png")
perso = pygame.image.load("content/Design/Perso.png")
plante = pygame.image.load("content/Design/Plante 1.png")
alien = pygame.image.load("content/Design/alien.png")
background2 = pygame.image.load("content/Design/Salle 2.png")
background3 = pygame.image.load("content/Design/Salle 3.png")
enter = pygame.image.load("content/Design/enter-button.png")
pnj = pygame.image.load("content/Design/pnj1.png")

# Rotozoom pour taille et angle
perso1 = pygame.transform.rotozoom(perso, 0, 1)
persorct = perso1.get_rect()
persorct.x = xperso
persorct.y = yperso

# Afficher la première plante
plante = pygame.transform.rotozoom(plante, 0, 1.125)
planterct1 = plante.get_rect()

# Afficher la taille et l'angle de la plante
screen.blit(background1, (0, 0))
screen.blit(plante, (xplante,yplante))

# Afficher l'alien guide
aln1 = pygame.transform.rotozoom(alien, 0, 0.9)
alnrct = aln1.get_rect()
alnrct.x = xaln
alnrct.y = yaln-10
screen.blit(aln1, (xaln, yaln))
# Afficher le pnj
pnj = pygame.transform.rotozoom(pnj, 0, 1)
pnjrct = pnj.get_rect()
pnjrct.x = xpnj
pnjrct.y = ypnj
screen.blit (pnj, (xpnj,ypnj))
# Rotozoom salle 2
bg2 = pygame.transform.rotozoom(background2, 0, 7.0625)
# test de boîte de dialogue
font= pygame.font.SysFont(None, 32)

def dialogue_box(texte):
    # Boîte
    pygame.draw.rect(screen, (0, 0, 0), (100, 650, 800, 100))  # fond noir
    pygame.draw.rect(screen, (255, 255, 255), (100, 650, 800, 100), 3)  # bord blanc
    
    # Texte
    lignes = texte.split('\n')  # pour plusieurs lignes
    for i, ligne in enumerate(lignes):
        text_surface = font.render(ligne, True, (255, 255, 255))
        screen.blit(text_surface, (120, 660 + i*30))
# Boucle du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Affichage
    screen.blit(background1, (0, 0))            # fond
    screen.blit(plante, (xplante,yplante))     # plante
    screen.blit(plante, (xplante+215,yplante)) # plante 2
    screen.blit(aln1, (xaln,yaln))             # alien
    screen.blit(perso1, (persorct.x,persorct.y))       # personnage
    screen.blit(pnj, (pnjrct.x,pnjrct.y)) # Pnj

    # Gestion des touches
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        persorct.x -= speed
        if persorct.colliderect(alnrct) :
            persorct.x += speed
            print("yo")
            screen.blit(enter, (persorct.x + 40, persorct.y))
        if persorct.colliderect(pnjrct):
            persorct.x += speed
            print("bouh")
            screen.blit(enter, (persorct.x + 40, persorct.y))
            
    if keys[pygame.K_RIGHT]:
        persorct.x += speed
        if persorct.colliderect(alnrct) :
            persorct.x -= speed
            screen.blit(enter, (persorct.x + 40, persorct.y))
        if persorct.colliderect(pnjrct) :
            persorct.x += speed
            screen.blit(enter, (persorct.x + 40, persorct.y))
            
    if keys[pygame.K_UP]:
        persorct.y -= speed
        if persorct.colliderect(alnrct) :
            persorct.y += speed
            screen.blit(enter, (persorct.x + 40, persorct.y))
        if persorct.colliderect(pnjrct) :
            persorct.x += speed
            screen.blit(enter, (persorct.x + 40, persorct.y))
            
    if keys[pygame.K_DOWN]:
        persorct.y += speed
        if persorct.colliderect(alnrct) :
            persorct.y -= speed
            screen.blit(enter, (persorct.x + 40, persorct.y))
        if persorct.colliderect(pnjrct) :
            persorct.x += speed
            screen.blit(enter, (persorct.x + 40, persorct.y))
    print(persorct.x)
    pygame.display.flip()
    # Collisions sur les murs
    if persorct.left < 0 :
        persorct.left = 0
    if persorct.right > 1000 :
        persorct.right = 1000
    if persorct.top < 0 :
        persorct.top = 0
    if persorct.bottom > 800:
        persorct.bottom = 800
clock.tick(60)
pygame.mixer.music.stop()
pygame.quit()
