class Space:
    def __init__(self, width, height):

        # todo: allocate 20 lists to hold space
        self.space = []

        for i in range(height):
            row = ['.'] * width
            self.space.append(row)

        print(self.space)

        # todo: add random stars

        #todo: methods


s = Space(15, 10)
