import pygame
import os
import datetime

_image_library = {}

def get_image(path):
    global _image_library 
    image = _image_library.get(path)
    if image is None:
        canonicalized_path = path.replace("/", os.sep).replace("\\", os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[canonicalized_path] = image
    return image

def blitRotate(screen, img, pos, angle):
    rotated_img = pygame.transform.rotate(img, angle)
    new_rect = rotated_img.get_rect(center=img.get_rect(center=pos).center)
    screen.blit(rotated_img, new_rect.topleft)

pygame.init()

screen = pygame.display.set_mode((1200, 800))
w, h = screen.get_size()
pygame.display.set_caption("Mickey's Clock")

bg = pygame.transform.scale(get_image("clock_face.png"), (w, h))
left_hand = get_image("left_hand.png")
right_hand = get_image("right_hand.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    today = datetime.datetime.now()
    minutes = today.minute
    seconds = today.second

    angle_min = -6 * minutes - 53
    angle_sec = -6 * seconds

    screen.blit(bg, (0, 0))
    pos = (w // 2, h // 2)

    blitRotate(screen, left_hand, pos, angle_sec)
    blitRotate(screen, right_hand, pos, angle_min)

    pygame.display.flip()
    pygame.time.delay(1000)

pygame.quit()