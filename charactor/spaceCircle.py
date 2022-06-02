import pygame

dis_x = 0
dis_y = 0
class SpaceCircle:
    def __init__(self, display) -> None:
        self.display = display
        self.life_count = 3
        self.out_count = 0
        self.game_score = 0
        self.p_x = 200
        self.p_y = 100
        self.v_x = 0.0
        self.v_y = 0.0
        self.max_v_x = 0
        self.max_v_y = 0
    def x_posMove(self):
        self.p_x += self.v_x
        if self.v_x > 0: # 속도가 오른쪽 일 때
            if self.p_x >=dis_x -18:
                self.v_x = -self.v_x
        elif self.v_x < 0:
            if self.p_x <= 18:
                self.v_x = abs(self.v_x)
    def y_posMove(self):
        self.p_y += self.v_y
        if self.v_y > 0: # 속도가 오른쪽 일 때
            if self.p_y >=dis_y -18:
                self.v_y = -self.v_y
        elif self.v_y < 0:
            if self.p_y <= 18:
                self.v_y = abs(self.v_y)

    def draw(self):
        self.display.fill((255,255,255))
        pygame.draw.circle(self.display, (0,0,0), (self.p_x, self.p_y), 20)

    def max_cheacker(self):
        if abs(self.v_x)  > self.max_v_x:
            self.max_v_x = abs(self.v_x)
        if abs(self.v_y)  > self.max_v_y:
            self.max_v_y = abs(self.v_y)

        if self.max_v_x > abs(self.v_x):
            self.out_count += 1
            self.max_v_x = self.v_x
        if self.max_v_y > abs(self.v_y):
            self.out_count += 1
            self.max_v_y = self.v_y


    def game_life_count(self):
        if abs(self.v_x):
            pass