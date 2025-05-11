import pygame
import sys
import time

# --- Initialisation ---
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Aventure Museum")
clock = pygame.time.Clock()

# --- Polices ---
font = pygame.font.SysFont("Courier", 40)

# --- Fonctions utiles ---
def draw_text_with_shadow(text, font, pos, color, shadow_color=(30, 30, 30), offset=(2, 2)):
    shadow = font.render(text, True, shadow_color)
    screen.blit(shadow, (pos[0] + offset[0], pos[1] + offset[1]))
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, pos)

# --- Écran titre ---
def start_screen():
    pygame.mixer.music.load("Music/Avo3-_backup_.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    title_font = pygame.font.SysFont("Courier", 60, bold=True)
    subtitle_font = pygame.font.SysFont("Courier", 20)

    title_text = "Aventure Museum"
    subtitle_text = "Appuie sur ESPACE pour commencer"
    title_displayed = ""
    subtitle_displayed = ""

    title_done = False
    subtitle_done = False

    blink = True
    blink_timer = 0
    blink_interval = 500

    last_char_time = pygame.time.get_ticks()
    char_delay = 80

    while True:
        screen.fill((0, 0, 0))
        now = pygame.time.get_ticks()

        # Animation lettre par lettre
        if not title_done and now - last_char_time > char_delay:
            if len(title_displayed) < len(title_text):
                title_displayed += title_text[len(title_displayed)]
                last_char_time = now
            else:
                title_done = True
                last_char_time = now + 300

        elif title_done and not subtitle_done and now - last_char_time > char_delay:
            if len(subtitle_displayed) < len(subtitle_text):
                subtitle_displayed += subtitle_text[len(subtitle_displayed)]
                last_char_time = now
            else:
                subtitle_done = True
                blink_timer = now

        # Affichage
        draw_text_with_shadow(title_displayed, title_font, (80, 200), (255, 255, 0))
        if subtitle_done:
            if now - blink_timer > blink_interval:
                blink = not blink
                blink_timer = now
            if blink:
                draw_text_with_shadow(subtitle_displayed, subtitle_font, (100, 400), (200, 200, 200))
        else:
            draw_text_with_shadow(subtitle_displayed, subtitle_font, (100, 400), (200, 200, 200))

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and subtitle_done:
                return

# --- Intro avec effet terminal ---
def intro():
    message = "Chargerment du systeme...\nChargement du musée...\nBienvenue, explorateur."
    font_intro = pygame.font.SysFont("Courier", 40)
    lines = message.split('\n')
    y = 200
    for line in lines:
        displayed_text = ""
        for char in line:
            displayed_text += char
            screen.fill((0, 0, 0))
            text = font_intro.render(displayed_text, True, (0, 255, 0))
            screen.blit(text, (100, y))
            pygame.display.flip()
            time.sleep(0.1)  # Vitesse du texte plus rapide
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        y += 50
    time.sleep(1.5)

# --- Transition vers le jeu principal ---
def transition_to_game():
    fade_surface = pygame.Surface((800, 600))
    fade_surface.fill((0, 0, 0))
    for alpha in range(0, 255, 5):  # Augmenter la valeur pour un fondu plus rapide
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        clock.tick(60)
    time.sleep(0.5)  # Pause avant de commencer le jeu

# --- Lancement ---
start_screen()
pygame.mixer.music.fadeout(1000)
intro()
transition_to_game()

# --- Appel au jeu principal (à insérer ici) ---
