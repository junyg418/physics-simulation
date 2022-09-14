import pygame

dis_x = 0
dis_y = 0
class Circle:
    def __init__(self, display):
        self.display = display
        self.p_x = 200.0
        self.p_y = 100.0
        self.v = 0.0
        self.ang_v = 10.0
        self.acceleration = 0.1
        self.type = "down"
        self.angType = 'right'

    def accel(self):
        if self.type == "down":
            # >> 속도에 의하여 위치가 먼저 바뀌게 된다면 처음에 가속도를 받지 않고 속도가 0인 상태로 떨어지게 된다 
            # 결론 증가한 가속도 때문에 속도가 바뀌게 되는거고
            # 하강할 떄는 줄어든 속도때문에 가속도가 줄어들기에 
            # 하강할 떄는 증가한 가속도 때문에 속도가 증가하게 되니 : 가속도에 의한 속도 증가 -> 속도에 의하여 위치 변경
            # 상승할 떄는 감소한 속도 때문에 가속도가 감소하게 되니 : 위치에너지가 필요함 -> 속도 감소 > 속도감소에 의한 가속도 감소
            self.v += self.acceleration
            self.p_y += self.v
            if self.p_y >= dis_y - 5.0:
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
            if self.p_x >= dis_x -5:
                self.angType = 'left'
        else:
            self.p_x -= self.ang_v
            if self.p_x <= 5:
                self.angType = 'right'
                


    def draw(self):
        self.display.fill((255, 255, 255))
        pygame.draw.circle(self.display, (0, 0, 255), (self.p_x, self.p_y), 10)
