import pygame

# sounds reference 
# https://bigsoundbank.com/detail-0128-sword-through-the-air.html
# https://bigsoundbank.com/detail-0127-sword-that-cuts.html
# https://github.com/Mostafatalaat770/Fruit-Ninja-Game/tree/master/sounds
# https://www.youtube.com/watch?v=2BikxsbkuIU

#load sounds
pygame.mixer.init()
clock = pygame.time.Clock()
bladeSound = pygame.mixer.Sound('sliceAir.wav')
sliceSound = pygame.mixer.Sound('sliceCut.wav')
drawSound = pygame.mixer.Sound('FruitThrow.wav')
gameOverSound = pygame.mixer.Sound('GameOver.wav')
loseLifeSound = pygame.mixer.Sound('LoseLife.wav')

#play the continuous background music
startGameSound = pygame.mixer.Sound('gameStart.wav')
music = pygame.mixer.music.load('MainTheme.wav')