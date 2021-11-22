#Faça um programa em Python que abre e reproduza o áudio de um arquivo mp3.
import pygame
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
input('Agora você escuta?')
#input serve para o evento não finalizar enquanto toca a musica