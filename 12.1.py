"""创建一个背景为蓝色的pygame窗口"""
"""
1.创建一个类，并初始化，然后定义该类的属性（如：大小，标题，颜色）
2.然后定义一个方法，运行
3.创建一个实例，然后运行
 """

import pygame
import sys

class Sky:

    def __init__ (self):
        # 初始化Pygame
        pygame.init()
        # 设置窗口大小和标题
        pygame.display.set_caption('Background Color Example')
        self.screen = pygame.display.set_mode((800, 400))
        # 设置窗口背景颜色
        self.bg_color = (230, 230, 230)


    def run_game(self):
        while True:
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     sys.exit()

                # 显示窗口
                pygame.display.flip()


if __name__ == '__main__':
    s = Sky()
    s.run_game()

