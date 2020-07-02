import pygame
pygame.init()

#colours
blue = (102,255,255)
white=(255,255,255)
dblack=(0,0,0)
green = (51,255,51)
bg1 = (153, 0, 76)
bg2 = (255,51,51)
ic = (178,255,102)
solve = (51,255,51)
reset = (255,255,51)

#game logo and title
logo = pygame.image.load('joystick.png')
pygame.display.set_icon(logo)
pygame.display.set_caption('Suduko solver')

#game window
screen = pygame.display.set_mode((410, 500))

game_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]




colour = [white,ic]
class block():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.colour = colour
        self.num = [256,257,258,259,260,261,262,263,264,265]
        self.icolour = white
        self.acolour = green
    
    
    def first_block(self,grid):
        grid[self.y][self.x]=1
        return grid

    def erase(self,grid):
        grid[self.y][self.x] = 0
        return grid

    def move_left(self,grid):
        result = (self.x>0)
        if result:
            self.erase(grid)
            self.x += -1
        return grid

    def move_right(self,grid):
        result = (self.x <8)
        if result:
            self.erase(grid)
            self.x += 1
        return grid

    def move_up(self,grid):
        result = (self.y > 0)
        if result:
            self.erase(grid)
            self.y += -1
        return grid

    def move_down(self,grid):
        result = (self.y < 8)
        if result:
            self.erase(grid)
            self.y += 1
        return grid

    def input(self,key):
        game_grid[self.y].pop(self.x)
        game_grid[self.y].insert(self.x,key%256)


def draw_grid(grid):
    game.first_block(grid)
    for x in range(9):
        for y in range(9):
            pygame.draw.rect(screen,colour[grid[y][x]],(25+x*40+3,60+y*40+3,35,35))

def draw_game_grid(game_grid):
    for x in range(9):
        for y in range(9):
            q = game_grid[y][x]
            if q > 0:
                message_to_screen(str(q),30,dblack,25+x*40+10,60+y*40+8)

def reset():
    for y in range(9):
        for x in range(9):
            game_grid[y][x] = 0


def solve(bo):
    find = find_empty(bo)
    if not find:  # if find is None or False
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if valid(bo, num, (row, col)):
            bo[row][col] = num

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):

    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
        	print(bo[i][j], end=" ")
        print()

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row, column

    return None

def message_to_screen(q,size,colour,x,y):
    message = pygame.font.Font('freesansbold.ttf',size)
    messages = message.render(q,True,colour)
    screen.blit(messages,(x,y))

def frame():
    pygame.draw.rect(screen, bg1, (0, 0, 410, 160))
    pygame.draw.rect(screen, bg2, (0, 160, 410, 340))
    pygame.draw.rect(screen, white, (25, 60, 360, 360))
        
    i = 1
    for x in range(10):
        if x%3 == 0:
            i=3
        pygame.draw.line(screen, dblack, (25+x*40, 60), (25+x*40, 420),i)
        i=1
        for y in range(10):
            if y%3 ==0:
                i=3
            pygame.draw.line(screen,dblack,(25,60+y*40),(385,60+y*40),i)
            i=1
    message_to_screen("Sudoko solver",40,blue,65,10)
    message_to_screen("-Press 'Enter' to solve",15,dblack,25,425)
    message_to_screen("-Press 'Backspace' to reset",15,dblack,25,445)
    message_to_screen("-Press '0' to reset particular cell",15,dblack,25,465)

game = block()
running = True
while running:
    screen.fill((dblack))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key in game.num:
                game.input(event.key)
            elif event.key == pygame.K_RETURN:
                solve(game_grid)
            elif event.key == pygame.K_BACKSPACE:
                reset()
            elif event.key == pygame.K_RIGHT:
                game.move_right(grid)
            elif event.key == pygame.K_LEFT:
                game.move_left(grid)
            elif event.key == pygame.K_UP:
                game.move_up(grid)
            elif event.key == pygame.K_DOWN:
                game.move_down(grid)
    
    
    frame()
    draw_grid(grid)
    draw_game_grid(game_grid)
    pygame.display.update()