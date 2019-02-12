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

        for i in range(10):
            rowNum = random.randint(0, height - 1)
            colNum = random.randint(0, width - 1)

            self.space[rowNum][colNum] = '*'

        # todo: add random stars

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

    def __str__(self):
        s = ''

        for row in self.space:
            s += ''.join(row) + '\n'

        return s


s = Space(15, 10)
p = Player(15 // 2, 10 // 2)

while True:
    s.print_map(p)
    dir = input('>> ')

    if dir == 'n':
        p.y -= 1
    elif dir == 's':
        p.y += 1

# print(s)
