#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect, KEYDOWN, K_ESCAPE
from pygame.font import Font
from code.Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, WIN_HEIGHT, C_CIAN, C_PURPLE


class Menu:
    def __init__(self, window):
        self.window = window
        # Carregar e redimensionar a imagem do fundo
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))  # Redimensiona a imagem
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # Desenhando a imagem redimensionada
            self.window.blit(source=self.surf, dest=self.rect)

            title_size = int(WIN_WIDTH * 0.20)  # 8% da largura da tela para o título
            option_size = int(WIN_WIDTH * 0.05)  # 5% da largura da tela para as opções

            # Títulos
            self.menu_text(title_size, "Cyber", C_PURPLE, ((WIN_WIDTH / 2), 70))
            self.menu_text(title_size, "Battle", C_CIAN, ((WIN_WIDTH / 2), 140))

            # Opções do menu
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(option_size, MENU_OPTION[i], C_PURPLE, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(option_size, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end_pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]

                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            pygame.quit()  # Close Window
                            quit()  # end_pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
