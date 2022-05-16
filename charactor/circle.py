import pygame


class Circle:
    def __init__(self, display):
        self.display = display
        self.p_x = 200.0
        self.p_y = 30.0
        self.v = 0.0
        self.ang_v = 1.0
        self.acceleration = 0.1
        self.type = "down"
        self.angType = 'right'

    def accel(self):
        if self.type == "down":
            self.v += self.acceleration
            self.p_y += self.v
            if self.p_y >= 410:
                self.type = "up"
                print(f'{self.type}:{self.p_y}')
        else:
            self.p_y -= self.v
            self.v -= self.acceleration
            if self.v <= 0:
                self.type = "down"
                # self.p_x = 200.0
                # self.p_y = 30
                print(self.type, ",", self.p_y)

    def angry(self):
        if self.angType == 'right':
            self.p_x += self.ang_v
            if self.p_x >= 610:
                self.angType = 'left'
        else:
            self.p_x -= self.ang_v
            if self.p_x <= 0:
                self.angType = 'right'
    def draw(self):
        self.display.fill((255, 255, 255))
        pygame.draw.circle(self.display, (0, 0, 255), (self.p_x, self.p_y), 30)
