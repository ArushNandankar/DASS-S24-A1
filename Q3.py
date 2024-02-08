import pygame

# top to bottom left to right
CoordinatesToPoints = {
    (385, 39): 1,
    (51, 277): 2,
    (312, 292): 3,
    (466, 286): 4,
    (722, 285): 5,
    (261, 444): 6,
    (511, 446): 7,
    (386, 541): 8,
    (179, 703): 9,
    (592, 702): 10,
}

PointsToCoordinates = {
    1: (385, 39),
    2: (51, 277),
    3: (312, 292),
    4: (466, 286),
    5: (722, 285),
    6: (261, 444),
    7: (511, 446),
    8: (386, 541),
    9: (179, 703),
    10: (592, 702),
}

directNeighbours = [
    (1, 3),
    (3, 1),
    (1, 4),
    (4, 1),
    (2, 3),
    (3, 2),
    (2, 6),
    (6, 2),
    (3, 4),
    (4, 3),
    (3, 6),
    (6, 3),
    (4, 5),
    (5, 4),
    (4, 7),
    (7, 4),
    (5, 7),
    (7, 5),
    (6, 8),
    (8, 6),
    (6, 9),
    (9, 6),
    (7, 8),
    (8, 7),
    (7, 10),
    (10, 7),
    (8, 9),
    (9, 8),
    (8, 10),
    (10, 8),
]
threeInRow = [
    (1, 3, 6),
    (6, 3, 1),
    (1, 4, 7),
    (7, 4, 1),
    (2, 3, 4),
    (4, 3, 2),
    (2, 6, 8),
    (8, 6, 2),
    (5, 4, 3),
    (3, 4, 5),
    (5, 7, 8),
    (8, 7, 5),
    (9, 6, 3),
    (3, 6, 9),
    (9, 8, 7),
    (7, 8, 9),
    (10, 7, 4),
    (4, 7, 10),
    (10, 8, 6),
    (6, 8, 10),
]


def give_point(coordinates) -> int:
    for pointCoordinates in CoordinatesToPoints.keys():
        diff = abs(coordinates[0] - pointCoordinates[0]) + abs(
            coordinates[1] - pointCoordinates[1]
        )
        if diff < 40:
            return CoordinatesToPoints[pointCoordinates]
    return -1


def give_pos_exact(coordinates) -> tuple:
    for pointCoordinates in CoordinatesToPoints.keys():
        diff = abs(coordinates[0] - pointCoordinates[0]) + abs(
            coordinates[1] - pointCoordinates[1]
        )
        if diff < 40:
            return pointCoordinates


def can_kill(crow_points, vulture_point) -> bool:
    for i in crow_points:
        for j in range(11):
            if j == i or j == vulture_point:
                continue
            if (vulture_point, i, j) in threeInRow and j not in crow_points:
                return True
    return False


pygame.init()
pygame.mixer.init()

sound = pygame.mixer.Sound('sound.mp3')

board_img = pygame.image.load("board.png")
board_img = pygame.transform.scale(board_img, (800, 800))
rect = board_img.get_rect()

crow_img = pygame.image.load("crow.png")
crow_img = pygame.transform.scale(crow_img, (100, 100))
# rectc = crow_img.get_rect()

vulture_img = pygame.image.load("vulture.png")
vulture_img = pygame.transform.scale(vulture_img, (100, 100))
# rectv = vulture_img.get_rect()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(None, 36)

run = True
turn = 1

crows_placed = 0
crows_eaten = 0
crow_points = []
crow_positions = []
vulture_point = -1

state = 1  # all the crows have not been placed yet

def print_to_display(text_data):
    text = font.render(text_data, True, (0, 0, 0))  # Change the color to black
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()  # Update the display
    pygame.time.wait(400)

while run:
    screen.fill([255, 255, 255])
    screen.blit(board_img, rect)

    # Draw the crow image at all the stored positions
    for pos in crow_positions:
        screen.blit(crow_img, pos)

    if vulture_point != -1:
        vpos = PointsToCoordinates[vulture_point]
        screen.blit(vulture_img, vpos)

    if crows_eaten == 4:
        print_to_display("VULTURE WON")
        print ("VULTURE WON")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            if run == False:
                break
    if run == False:
        break

    # if vulure can't move crows have won
    canWin = False
    if vulture_point != -1:
        for i in range(11):
            if i in crow_points:
                continue
            if (vulture_point, i) in directNeighbours:
                canWin = True

        for i in range(11):
            for j in range(11):
                if i == vulture_point or j == vulture_point:
                    continue
                if j in crow_points:
                    continue
                if i not in crow_points:
                    continue
                if (vulture_point, i, j) in threeInRow:
                    canWin = True
    else:
        canWin = True

    if not canWin:
        print_to_display("CROWS WIN")
        print("CROWS WIN")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            if run == False:
                break
    if run == False:
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if give_point(pos) == -1:
                continue
            if turn % 2 == 1 and state == 1:
                ppoint = give_point(pos)
                if ppoint in crow_points or ppoint == vulture_point:
                    print_to_display("INVALID MOVE")
                    print("INVALID MOVE")
                    continue
                crow_points.append(give_point(pos))
                crow_positions.append(give_pos_exact(pos))
                crows_placed = crows_placed + 1
                if crows_placed == 7:
                    state = 2
                turn = turn + 1
            elif turn % 2 == 1 and state == 2:
                curr_point = give_point(pos)
                curr_pos = give_pos_exact(pos)
                if curr_point not in crow_points:
                    print_to_display("INVALID MOVE")
                    print("INVALID MOVE")
                    continue
                while True:
                    ok = False
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                            ok = True
                            break
                        if event.type == pygame.MOUSEBUTTONUP:
                            pos2 = pygame.mouse.get_pos()
                            new_point = give_point(pos2)
                            ok = True
                            break
                    if ok:
                        break

                if run == False:
                    break
                if new_point == -1:
                    continue
                if new_point == vulture_point:
                    print_to_display("INVALID MOVE")
                    print("INVALID MOVE")
                    continue
                if new_point in crow_points:
                    print_to_display("INVALID MOVE")
                    print("INVALID MOVE")
                    continue
                if (curr_point, new_point) not in directNeighbours:
                    print_to_display("INVALID MOVE")
                    print("INVALID MOVE")
                    continue
                new_point = give_point(pos2)
                new_pos = give_pos_exact(pos2)
                crow_points.remove(curr_point)
                crow_positions.remove(curr_pos)
                crow_points.append(new_point)
                crow_positions.append(new_pos)
                turn = turn + 1
            else:
                vulture_point_new = give_point(pos)
                if (
                    vulture_point_new in crow_points
                    or vulture_point_new == vulture_point
                ):
                    print_to_display("INVALID MOVE")
                    print("INVALID MOVE")
                    continue
                if (
                    vulture_point == -1
                    or (vulture_point_new, vulture_point) in directNeighbours
                ) and not can_kill(crow_points, vulture_point):
                    vulture_point = vulture_point_new
                    turn = turn + 1
                    continue
                if can_kill(crow_points, vulture_point):
                    ok = False
                    for i in crow_points:
                        if (vulture_point, i, vulture_point_new) in threeInRow:
                            crow_points.remove(i)
                            crow_positions.remove(PointsToCoordinates[i])
                            vulture_point = vulture_point_new
                            turn = turn + 1
                            crows_eaten = crows_eaten + 1
                            print_to_display("KILLED")
                            print("KILLED")
                            sound.play()
                            ok = True
                    if not ok:
                        print_to_display("KILL CROW")
                        print("KILL CROW")
                    continue

                else:
                    print_to_display("INVALID MOVE")
                    print("INVALID MOVE")
                    continue

    pygame.display.update()
pygame.quit()
