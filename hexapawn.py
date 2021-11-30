import pygame
from pygame.locals import (QUIT)
from teams import Team

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
clock = pygame.time.Clock()
teams = {"AI": Team("AI"), "Human": Team("Human")}

running = True
colors = {"AI": (255,165,0,255), "Human": (0,0,255,255)}

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running=False
    screen.fill((0,0,0,0))
    for team in teams:
        for pawn in team.pawns:
            verticies = pawn.convert_tile_to_verticies(pawn.tile)
            pygame.draw.polygon(screen, colors[str(team)], verticies)
