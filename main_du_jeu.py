import pygame
import os
import sys
import random
import moviepy.editor
import pygame_menu as pm
import main_secondmain
import piggy_boss
import main_niveau_poubelle
import voiture_mechante
import main_final
import main_elec

user_name = ""
nom_utilisateur = ""
l1=False
l2=False
l2_5=False
l3=False
l4=False
l5=False
vol=0.5
a='e'

def reset_window_content(screen_game):
    screen_game.fill((0,0,0))
    pygame.display.flip()

def adjust_brightness(image, brightness):
    # Crée une copie de l'image
    adjusted_image = image.copy()
    # Ajuste la luminosité de l'image
    adjusted_image.fill((brightness, brightness, brightness), special_flags=pygame.BLEND_RGB_ADD)
    return adjusted_image

def display_video(video_file, title_text):
    pygame.init()
    video = moviepy.editor.VideoFileClip(video_file)
    video_size = video.size
    screen = pygame.display.set_mode(video_size)
    video.preview()
    pygame.quit()

def adjust_brightness(image, brightness):
    # Crée une copie de l'image
    adjusted_image = image.copy()
    # Ajuste la luminosité de l'image
    adjusted_image.fill((brightness, brightness, brightness), special_flags=pygame.BLEND_RGB_ADD)
    return adjusted_image

def display_name_entry(screen_game):
    # Créez une nouvelle fenêtre pour la saisie du nom
    name_window = pm.Menu("Enter Your Name (4 letters max)", 800, 600, theme=pm.themes.THEME_GREEN)

    # Définissez une variable pour stocker le nom saisi par l'utilisateur
    user_name = [""]  # Utilisez une liste pour stocker le nom afin qu'elle soit mutable dans la fonction

    # Fonction pour enregistrer le nom saisi et passer à la fenêtre principale du jeu
    def save_name():
        user_name[0] = name_input.get_value()  # Récupérer le nom saisi par l'utilisateur
        name_window.disable()  # Désactiver la fenêtre de saisie du nom
        return user_name[0]

    # Ajoutez une zone de texte pour que l'utilisateur saisisse son nom
    name_input = name_window.add.text_input("Name: ", default="", maxchar=10)

    # Ajoutez un bouton "Save" pour enregistrer le nom saisi
    name_window.add.button("Save", save_name)

    # Exécutez le menu de saisie du nom
    name_window.mainloop(screen_game)

    # Retournez le nom saisi par l'utilisateur
    return user_name[0]

def display_info_window(screen_game):
    # Créez une nouvelle fenêtre d'information
    info_window = pygame.Surface((700, 600))

    # Ajoutez un dégradé de couleur au fond
    for y in range(info_window.get_height()):
        color = (0, 0, 80 + y // 6)  # Dégradé allant du bleu foncé au bleu clair vers le bas
        pygame.draw.line(info_window, color, (0, y), (info_window.get_width(), y))

    # Ajoutez une ombre portée à la fenêtre d'information
    pygame.draw.rect(info_window, (0, 0, 0), info_window.get_rect(), 3)  # Bordure noire
    info_window.set_alpha(200)  # Réglez la transparence pour l'ombre portée

    font = pygame.font.SysFont("Rockwell", 24)
    text_credit_game = font.render("Crédit game", True, (255, 255, 255))  # Texte blanc
    info_window.blit(text_credit_game, (280, 20))

    # Ajoutez du texte à la fenêtre
    text = font.render("Crée et designé par Gabriel Lallier, Eden Elfassy,", True, (255, 255, 255))  # Texte blanc
    info_window.blit(text, (70, 150))
    text2 = font.render(
        "Alina Frederic et Paul-Emile Bertrand.",
        True, (255, 255, 255))  # Texte blanc
    info_window.blit(text2, (120, 180))
    text3 = font.render(
        "Toute copie ou violation de la propriété intellectuelle",
        True, (255, 255, 255))  # Texte blanc
    info_window.blit(text3, (40, 260))
    text4 = font.render(
        "fera l'objet de poursuite!!",
        True, (255, 255, 255))  # Texte blanc
    info_window.blit(text4, (180, 290))

    # Calculez les coordonnées pour centrer la fenêtre d'information
    window_x = (screen_game.get_width() - info_window.get_width()) // 2
    window_y = (screen_game.get_height() - info_window.get_height()) // 2

    return info_window, window_x, window_y

# Ajout DE
def display_settings_window(screen_game):
    import pygame
    import pygame_menu as pm
    global vol
    global user_name

    pygame.init()

    # Screen
    WIDTH, HEIGHT = 700, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Standard RGB colors
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    CYAN = (0, 100, 100)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Main function of the program

    def main():
        # List that is displayed while selecting the graphics level
        graphics = [("Low", "low"),
                    ("Medium", "medium"),
                    ("High", "high"),
                    ("Ultra High", "ultra high")]

        # List that is displayed while selecting the window resolution level
        resolution = [("1920x1080", "1920x1080"),
                      ("1920x1200", "1920x1200"),
                      ("1280x720", "1280x720"),
                      ("2560x1440", "2560x1440"),
                      ("3840x2160", "3840x2160")]

        # List that is displayed while selecting the difficulty
        difficulty = [("Easy", "Easy"),
                      ("Medium", "Medium"),
                      ("Expert", "Expert")]

        # List that is displayed while selecting the player's perspective
        perspectives = [("FPP", "fpp"),
                        ("TPP", "tpp")]

        # This function displays the currently selected options

        def printSettings():
            global vol
            global user_name
            print("\n\n")
            # getting the data using "get_input_data" method of the Menu class
            settingsData = settings.get_input_data()

            for key in settingsData.keys():
                print(f"{key}\t:\t{settingsData[key]}")
                if key == 'Mus':
                    vol= settingsData[key]
                elif key == 'User Name':
                    user_name = settingsData[key]
        def resetval():
            settings.reset_value
            printSettings()


            # Creating the settings menu

        settings = pm.Menu(title="Settings",
                           width=WIDTH,
                           height=HEIGHT,
                           theme=pm.themes.THEME_DEFAULT)

        # Adjusting the default values
        settings._theme.widget_font_size = 25
        settings._theme.widget_font_color = BLACK
        settings._theme.widget_alignment = pm.locals.ALIGN_LEFT

        # Text input that takes in the username
        settings.add.text_input(title="User Name : ", textinput_id="username")

        # 2 different Drop-downs to select the graphics level and the resolution level
        settings.add.dropselect(title="Graphics Level", items=graphics,
                                dropselect_id="graphics level", default=0)
        settings.add.dropselect_multiple(title="Window Resolution", items=resolution,
                                         dropselect_multiple_id="Resolution",
                                         open_middle=True, max_selected=1,
                                         selection_box_height=6)

        # Toggle switches to turn on/off the music and sound
        settings.add.toggle_switch(title="Sounds", default=False, toggleswitch_id="sound")
        vol = settings.add.range_slider(title="Music", default=0.5, range_values=(0.0, 1.0), increment=0.1, value_format=lambda x: str(float(round(x,1))), rangeslider_id="Mus")

        # Selector to choose between the types of difficulties available
        settings.add.selector(title="Difficulty\t", items=difficulty,
                              selector_id="difficulty", default=0)

        # Range slider that lets to choose a value using a slider
        settings.add.range_slider(title="FOV", default=60, range_values=(
            50, 100), increment=1, value_format=lambda x: str(int(x)), rangeslider_id="fov")

        # Fancy selector (style added to the default selector) to choose between
        # first person and third person perspectives
        settings.add.selector(title="Perspective", items=perspectives,
                              default=0, style="fancy", selector_id="perspective")

        # clock that displays the current date and time
        settings.add.clock(clock_format="%d-%m-%y %H:%M:%S",
                           title_format="Local Time : {0}")

        # 3 different buttons each with a different style and purpose
        settings.add.button(title="Print Settings", action=printSettings,
                            font_color=WHITE, background_color=GREEN)
        settings.add.button(title="Restore Defaults", action=resetval,
                            font_color=WHITE, background_color=RED)
        settings.add.button(title="Return To Main Menu",
                            action=pm.events.BACK, align=pm.locals.ALIGN_CENTER)

        # Creating the main menu
        mainMenu = pm.Menu(title="Main Menu",
                           width=WIDTH,
                           height=HEIGHT,
                           theme=pm.themes.THEME_DEFAULT)

        # Adjusting the default values
        mainMenu._theme.widget_alignment = pm.locals.ALIGN_CENTER

        # Button that takes to the settings menu when clicked
        mainMenu.add.button(title="Settings", action=settings,
                            font_color=WHITE, background_color=GREEN)

        # An empty label that is used to add a seperation between the two buttons
        mainMenu.add.label(title="")

        # Exit button that is used to terminate the program
        mainMenu.add.button(title="Exit", action=exit,
                            font_color=WHITE, background_color=RED)


        # Lets us loop the main menu on the screen
        mainMenu.mainloop(screen)


    if __name__ == "__main__":
        main()


winrate=0
info_window_open = False
def display_image(image_file, title_text):
    import pygame
    global user_name
    global winrate
    global text_surface
    global l1,l2,l3,l4,l5,l2_5
    global vol
    global a
    global info_window_open

    vol=round(vol,1)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.quit()
    screen_game = pygame.display.set_mode((1200, 800))
    image = pygame.image.load(image_file).convert_alpha()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    level_1_bool = False
    level_2_bool = False
    level_2_5_bool = False
    level_3_bool = False
    level_4_bool = False
    level_5_bool = False


    # Chargement de l'image pour le bouton "info"
    info_button = pygame.image.load("bouton/info.png").convert_alpha()
    info_button = pygame.transform.scale(info_button, (100, 100))
    info_button_rect = info_button.get_rect()
    info_button_rect.center = (1100, 710)

    button_info_hover = False
    button_info_clicked = False

    info_window_surface = None

    # Ajout DE:
    window_settings_open = False
    window_settings_surface = None
    window_entry_name_close = False
    text_x = 800
    text_y = 100
    scroll_speed = 2

    # Fin Ajout DE

    # Chargement de l'image pour le bouton "settings"
    settings_button = pygame.image.load("bouton/settings.png").convert_alpha()
    settings_button = pygame.transform.scale(settings_button, (100, 100))
    settings_button_rect = settings_button.get_rect()
    settings_button_rect.center = (100, 710)

    play_font = pygame.image.load("bouton/play.png").convert_alpha()
    play_font = pygame.transform.scale(play_font,(400,130))
    play_font_rect = play_font.get_rect()
    play_font_rect.center = (600,400)

    quit_font = pygame.image.load("bouton/Quit.png").convert_alpha()
    quit_font = pygame.transform.scale(quit_font,(400,180))
    quit_font_rect = play_font.get_rect()
    quit_font_rect.center = (600,530)

    return_font = pygame.image.load("bouton/return_arrow.png").convert_alpha()
    return_font = pygame.transform.scale(return_font, (200, 200))
    return_font_rect = return_font.get_rect()
    return_font_rect.center = (200, 200)

    level_1_font = pygame.image.load("bouton/level_1.png").convert_alpha()
    level_1_font = pygame.transform.scale(level_1_font,(200,200))
    level_1_font_rect = level_1_font.get_rect()
    level_1_font_rect.center = (450,200)



    if winrate>0:
        level_2_font = pygame.image.load("bouton/level_2.png").convert_alpha()
        level_2_font = pygame.transform.scale(level_2_font, (200, 200))
        level_2_font_rect = level_2_font.get_rect()
        level_2_font_rect.center = (800, 200)
    else:
        level_2_font = pygame.image.load("bouton/level_2_lock.png").convert_alpha()
        level_2_font = pygame.transform.scale(level_2_font, (350, 200))
        level_2_font_rect = level_2_font.get_rect()
        level_2_font_rect.center = (800, 200)

    if winrate>1:
        level_2_5 = pygame.image.load("bouton/niveau_elec.png").convert_alpha()
        level_2_5_font = pygame.transform.scale(level_2_5, (200, 200))
        level_2_5_font_rect = level_2_5_font.get_rect()
        level_2_5_font_rect.center = (950, 475)
    else:
        level_2_5 = pygame.image.load("bouton/niveau_elec_lock.png").convert_alpha()
        level_2_5_font = pygame.transform.scale(level_2_5, (200, 200))
        level_2_5_font_rect = level_2_5_font.get_rect()
        level_2_5_font_rect.center = (925, 475)

    if winrate>2:
        level_3_font = pygame.image.load("bouton/level_3.png").convert_alpha()
        level_3_font = pygame.transform.scale(level_3_font, (200, 200))
        level_3_font_rect = level_3_font.get_rect()
        level_3_font_rect.center = (700, 650)
    else:
        level_3_font = pygame.image.load("bouton/level_3_lock.png").convert_alpha()
        level_3_font = pygame.transform.scale(level_3_font, (230, 180))
        level_3_font_rect = level_3_font.get_rect()
        level_3_font_rect.center = (700, 650)

    if winrate>3:
        level_4_font = pygame.image.load("bouton/level_4.png").convert_alpha()
        level_4_font = pygame.transform.scale(level_4_font, (200, 200))
        level_4_font_rect = level_4_font.get_rect()
        level_4_font_rect.center = (350, 600)
    else:
        level_4_font = pygame.image.load("bouton/level_4_lock.png").convert_alpha()
        level_4_font = pygame.transform.scale(level_4_font, (210, 180))
        level_4_font_rect = level_4_font.get_rect()
        level_4_font_rect.center = (350, 600)

    if winrate > 4:
        level_5_font = pygame.image.load("bouton/start-1436754_1280.png").convert_alpha()
        level_5_font = pygame.transform.scale(level_5_font, (200, 200))
        level_5_font_rect = level_5_font.get_rect()
        level_5_font_rect.center = (625, 425)
    else:
        level_5_font = pygame.image.load("bouton/fauxbtn.png").convert_alpha()
        level_5_font = pygame.transform.scale(level_5_font, (200, 200))
        level_5_font_rect = level_5_font.get_rect()
        level_5_font_rect.center = (625, 425)



    button_hover = False
    button_clicked = False

    # Créer un objet font

    # Surface pour le contenu à afficher lorsque le bouton "info" est cliqué
    new_content_surface = pygame.Surface((800, 600))
    new_content_surface.fill((255, 255, 255))  # Remplir avec une couleur de fond blanche par défauts
    if not user_name:
        user_name = display_name_entry(screen_game)

        window_entry_name_close = True

    pygame.mixer.init()
    s = pygame.mixer.Sound("musique/son_operationE.mp3")
    s.set_volume(vol)
    s.play(-1)

    button_hover_play = False
    button_hover_quit = False
    settings_menu_open = False
    game_playing = False
    button_state_return = False
    button_hover_level_1 = False
    button_hover_level_2 = False
    button_hover_level_2_5 = False
    button_hover_level_3 = False
    button_hover_level_4 = False
    button_hover_level_5 = False


    continuer = True
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
                pygame.quit()

            elif event.type == pygame.MOUSEMOTION:
                if level_1_font_rect.collidepoint(event.pos):
                    button_hover_level_1 = True
                else :
                    button_hover_level_1 = False

                if level_2_font_rect.collidepoint(event.pos):
                    button_hover_level_2 = True
                else :
                    button_hover_level_2 = False

                if level_2_5_font_rect.collidepoint(event.pos):
                    button_hover_level_2_5 = True
                else :
                    button_hover_level_2_5 = False

                if level_3_font_rect.collidepoint(event.pos):
                    button_hover_level_3 = True
                else :
                    button_hover_level_3 = False

                if level_4_font_rect.collidepoint(event.pos):
                    button_hover_level_4 = True
                else :
                    button_hover_level_4 = False

                if level_5_font_rect.collidepoint(event.pos):
                    button_hover_level_5 = True
                else :
                    button_hover_level_5 = False



                if return_font_rect.collidepoint(event.pos):
                    button_state_return = True
                else :
                    button_state_return = False

                if play_font_rect.collidepoint(event.pos):

                    button_hover_play = True
                else :
                    button_hover_play = False

                if quit_font_rect.collidepoint(event.pos):
                    button_hover_quit = True
                else :
                    button_hover_quit = False

                if settings_button_rect.collidepoint(event.pos):
                    button_hover = True
                else:
                    button_hover = False

                if info_button_rect.collidepoint(event.pos):
                    button_info_hover = True
                else:
                    button_info_hover = False




            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_font_rect.collidepoint(event.pos):
                    pygame.mixer.Sound("musique/son_play.mp3").play()
                    reset_window_content(screen_game)
                    image = pygame.image.load("menu/earth bad mood.png").convert()
                    a='e'
                    screen_game.blit(image, (240,40))
                    pygame.display.flip()
                    game_playing = True
                    play_font_rect.center = (-100, -100)
                    quit_font_rect.center = (-100, -100)

                    if not user_name:
                        user_name = display_name_entry(screen_game)

                if quit_font_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                    play_font_rect.center = (-100, -100)
                    quit_font_rect.center = (-100, -100)

                if return_font_rect.collidepoint(event.pos):
                    game_playing = False


                if settings_button_rect.collidepoint(event.pos):
                    settings_menu_open = True
                else:
                    settings_menu_open = False


                if info_button_rect.collidepoint(event.pos):
                    if info_window_open:  # Si la fenêtre d'information est déjà ouverte
                        info_window_open = False  # Ferme la fenêtre d'information
                    else:
                        info_window_surface, window_x, window_y = display_info_window(screen_game)
                        info_window_open = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if settings_button_rect.collidepoint(event.pos):
                    if button_clicked:
                        print("Settings Button clicked !")
                        button_clicked = False
                if info_button_rect.collidepoint(event.pos):
                    if button_info_clicked:
                        print("Info Button clicked !")
                        button_info_clicked = False

                if level_2_font_rect.collidepoint(event.pos):
                    level_2_bool = True

                if  level_2_5_font_rect.collidepoint(event.pos):
                    level_2_5_bool = True

                if level_1_font_rect.collidepoint(event.pos):
                    level_1_bool = True

                if level_3_font_rect.collidepoint(event.pos):
                    level_3_bool = True

                if level_4_font_rect.collidepoint(event.pos):
                    level_4_bool = True

                if level_5_font_rect.collidepoint(event.pos):
                    level_5_bool = True



        if level_1_bool :
            level_2_selected = False
            print("Level 1 selected")
            if True: #main_niveau_poubelle.start_benwars(vol) and not l1:
                winrate+=1
                l1=True
            start_mainjeu()

        if level_2_bool and winrate==1:
            level_2_selected = False
            print("Level 2 selected")
            # Importer et exécuter le script du niveau 2
            if True: #voiture_mechante.start_badcars(vol) and not l2:
                winrate+=1
                l2=True
            start_mainjeu()

        if level_2_5_bool and winrate==2:
            level_2_5_selected = False
            print("Level 2.5 selected")
            # Importer et exécuter le script du niveau 2.5
            if True: #main_elec.starting_eleco(vol) and not l2_5:
                winrate += 1
                l2_5 = True
            start_mainjeu()

        if level_3_bool and winrate==3:
            level_2_selected = False
            print("Level 3 selected")
            # Importer et exécuter le script du niveau 2
            if True: #piggy_boss.start_piggy(vol) and not l3:
                winrate+=1
                l3=True
            start_mainjeu()

        if level_4_bool and winrate==4:
            level_2_selected = False
            print("Level 4 selected")
            # Importer et exécuter le script du niveau 2
            if main_secondmain.starting_secondhand(vol) and not l4:
                winrate+=1
                l4=True
            start_mainjeu()

        if level_5_bool and winrate==5:
            print("Level 5 selected")
            # Importer et exécuter le script du niveau 2
            if main_final.start_final(vol) and not l5:
                main_secondmain.play_video('video/FIN.mp4')
                pygame.quit()
            else:
                start_mainjeu()
        if a=='g':
            screen_game.blit(image, (0, 0))  # Dessiner l'image de fond
        if not game_playing :
            play_font_rect.center = (600, 400)
            quit_font_rect.center = (600, 530)

            if button_hover:
                screen_game.blit(adjust_brightness(settings_button, 50), settings_button_rect)  # Ajuste la luminosité du bouton pour la surbrillance
            else:
                screen_game.blit(settings_button, settings_button_rect)

            if button_info_hover:
                screen_game.blit(adjust_brightness(info_button, 50), info_button_rect)  # Ajuste la luminosité du bouton pour la surbrillance
            else:
                screen_game.blit(info_button, info_button_rect)

            if button_hover_play:
                screen_game.blit(adjust_brightness(play_font, 50), play_font_rect)
                # Bouton en surbrillance
            else:
                screen_game.blit(play_font, play_font_rect)  # Bouton normal
            image=pygame.image.load('menu/galaxy.jpg')
            a='g'

            # Dessiner le bouton "Quit"
            if button_hover_quit:
                screen_game.blit(adjust_brightness(quit_font, 50), quit_font_rect)  # Bouton en surbrillance
            else:
                screen_game.blit(quit_font, quit_font_rect)

            if settings_menu_open:
                display_settings_window(screen_game)

            if window_entry_name_close == False and info_window_open == False:
                text_x -= scroll_speed
                if text_x < -text_surface.get_width():
                    text_x = 800
                screen_game.blit(text_surface, (text_x, text_y))  # Dessiner le titre animé

            # Ajout DE

            # des la fermeture de la fenetre permettant à user d'entrer son nom:

            if window_entry_name_close == True and info_window_open == False:

                nom_utilisateur=''
                if len(user_name) == 0:
                    nom_utilisateur = "User" + str(random.randint(45085,95432))
                else:
                    for polenta in range(0, min(3,len(user_name))):
                        nom_utilisateur+= user_name[polenta]

                texte_complet = "Operation E" + " - User : " + nom_utilisateur
                font = pygame.font.SysFont("Rockwell", 150)
                text_surface = font.render(texte_complet, True, (192, 192, 192))

                text_x = 800
                text_y = 100
                scroll_speed = 2

                screen_game.blit(text_surface, (text_x, text_y))  # Dessiner le titre animé

                window_entry_name_close = False

            # Fin ajout DE

            # Afficher la nouvelle surface du contenu si le bouton "info" a été cliqué
            if info_window_open:
                screen_game.blit(info_window_surface, (window_x, window_y))  # Dessiner la fenêtre d'information sur l'écran principal

        # Ajout DE
            if window_settings_open:
                screen_game.blit(window_settings_surface,(window_x, window_y))
        # Dessiner la fenêtre d'information sur l'écran principal
            # Fin ajout DE

        else :
            if game_playing:
                if button_state_return :
                    screen_game.blit(adjust_brightness(return_font,50),return_font_rect)

                else :
                    screen_game.blit(return_font,return_font_rect)

                if button_hover_level_1:
                    screen_game.blit(adjust_brightness(level_1_font,50),level_1_font_rect)
                else :
                    screen_game.blit(level_1_font, level_1_font_rect)

                if button_hover_level_2 :
                    screen_game.blit(adjust_brightness(level_2_font,50),level_2_font_rect)
                else :
                    screen_game.blit(level_2_font, level_2_font_rect)

                if button_hover_level_2_5 :
                    screen_game.blit(adjust_brightness(level_2_5_font,50),level_2_5_font_rect)
                else :
                    screen_game.blit(level_2_5_font, level_2_5_font_rect)

                if button_hover_level_3 :
                    screen_game.blit(adjust_brightness(level_3_font,50),level_3_font_rect)
                else :
                    screen_game.blit(level_3_font, level_3_font_rect)

                if button_hover_level_4:
                    screen_game.blit(adjust_brightness(level_4_font,50),level_4_font_rect)
                else :
                    screen_game.blit(level_4_font,level_4_font_rect)

                if button_hover_level_5:
                    screen_game.blit(adjust_brightness(level_5_font,50),level_5_font_rect)
                else :
                    screen_game.blit(level_5_font,level_5_font_rect)






        pygame.display.flip()
        pygame.time.Clock().tick(60)


# Afficher la seconde fenêtre avec une image


#nom_utilisateur = ""
#def chaine_qui_defile(title_text):
#    font = pygame.font.SysFont("Rockwell", 150)
#    text_surface = font.render(title_text, True, (192, 192, 192))

#    text_x = 800
#    text_y = 100
#    scroll_speed = 2
def start_mainjeu():
    display_image("menu/galaxy.jpg", f"Operation - E ; user:" + nom_utilisateur)
def exit():
    global info_window_open
    info_window_open = False
    start_mainjeu()


display_video('video/video.mp4','studio')
display_video('video/Start.mp4','start')

start_mainjeu()

# Utiliser split pour diviser la chaîne en mots
# mots = user_name[0].split()

# Maintenant, mots est une liste contenant tous les mots dans la chaîne. On prend le premier.
# premier_mot = mots[0]
pygame.quit()
sys.exit()
