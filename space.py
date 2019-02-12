import random


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Space:
    def __init__(self, width, height):

        # todo: allocate 20 lists to hold space
        self.space = []

        for i in range(height):
            row = ['.'] * width
            self.space.append(row)

        # todo: add random stars
        for i in range(10):
            rowNum = random.randint(0, height - 1)
            colNum = random.randint(0, width - 1)

            self.space[rowNum][colNum] = '*'

        # todo: methods

    def print_map(self, player):
        print(f'Player is at {player.x}, {player.y}')

        for rowNum in range(len(self.space)):
            for colNum in range(len(self.space[rowNum])):
                if player.x == colNum and player.y == rowNum:
                    char = 'Y'
                else:
                    char = self.space[rowNum][colNum]

                print(f'{char} ', end='')
            print()

    def crash(self, player):
        if self.space[player.y][player.x] == '*':
            return True
        else:
            return False


s = Space(15, 10)
p = Player(15 // 2, 10 // 2)

star = 'you hit a star'

while True:
    s.print_map(p)
    dir = input('>> ')

    if dir == 'n':
        if p.y > 0:
            p.y -= 1
            if s.crash(p):
                print(f'{star}')
                break
        else:
            p.y = p.y

    elif dir == 's':
        if p.y < 9:
            p.y += 1
            if s.crash(p):
                print(f'{star}')
                break
        else:
            p.y = p.y
        if s.crash(p):
            print(f'{star}')
            break

    elif dir == 'e':
        if p.x < 14:
            p.x += 1
            if s.crash(p):
                print(f'{star}')
                break
        else:
            p.x = p.x

    elif dir == 'w':
        if p.x > 0:
            p.x -= 1
            if s.crash(p):
                print(f'{star}')
                break
        else:
            p.x = p.x

    elif dir == 'end':
        break

# print(s)
