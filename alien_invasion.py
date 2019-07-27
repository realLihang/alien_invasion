import sys

import pygame

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats as gs
from button import Button
from scoreboard import Scoreboard

def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    # 设置模式
    # 创建一个 Settings 实例
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    # 设置标题
    pygame.display.set_caption("外星人入侵")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于储存游戏统计信息的实例，并创建记分牌
    stats = gs(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于储存子弹的编组
    bullets = Group()

    # 设置背景色
    bg_color = (230, 230, 230)

    # 创建一个外星人编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, 
                aliens, bullets)

        if stats.game_active:
            # 实现飞机的移动
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                    bullets)
            # 实现子弹的移动
            bullets.update()
        
            # 删除已消失的子弹
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, 
                    bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, 
                    bullets)

        # 没次循环时都绘制屏幕
        # 让最近绘制的屏幕可见
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, 
                bullets, play_button)

run_game()
