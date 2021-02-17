# coding=gbk
import sys

import pygame
from pygame.locals import *
from settings import Settings
from wechat import Wechat
from end import End
from smallfish import Smallfish
from oldbig import Oldbig
from small_words import Small_words
from old_words import Old_words
from game_stats import GameStats
from bloodboard import Bloodboard
import game_functions as gf
from pygame.sprite import Group

def run_game():
	#初始化游pygame、设置和屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("喷子小水鱼的日常")
	
	#创建微信聊天界面
	wechat = Wechat(screen)
	end = End(screen)

	#创建一个小水鱼头像
	smallfish = Smallfish(ai_settings, screen)
	
	#创建一个老大头像
	oldbig = Oldbig(ai_settings, screen)
	
	#创建一个用于储存小水鱼文字的实例
	sw = Group()
	
	#创建一个用于储存老大文字的实例
	ow = Group()
	
	#创建一个用于储存游戏统计信息的实例，创建记分牌
	stats = GameStats(ai_settings)
	bb = Bloodboard(ai_settings, screen, stats)

	#开始游戏的主循环
	while True:
		
		gf.check_events(ai_settings, screen, smallfish, oldbig, sw, ow)
		
		smallfish.update()
		gf.update_oldbig(ai_settings, oldbig)
		gf.update_small_words(ai_settings, screen, stats, bb, smallfish, oldbig, sw)
		gf.update_old_words(ai_settings, screen, stats, bb, smallfish, oldbig, ow)
		
		
		#每次循环重绘屏幕

		gf.update_screen(ai_settings, screen, stats, bb, wechat, end, smallfish, oldbig, sw, ow)
	

run_game()
