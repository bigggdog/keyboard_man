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
	#��ʼ����pygame�����ú���Ļ����
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("����Сˮ����ճ�")
	
	#����΢���������
	wechat = Wechat(screen)
	end = End(screen)

	#����һ��Сˮ��ͷ��
	smallfish = Smallfish(ai_settings, screen)
	
	#����һ���ϴ�ͷ��
	oldbig = Oldbig(ai_settings, screen)
	
	#����һ�����ڴ���Сˮ�����ֵ�ʵ��
	sw = Group()
	
	#����һ�����ڴ����ϴ����ֵ�ʵ��
	ow = Group()
	
	#����һ�����ڴ�����Ϸͳ����Ϣ��ʵ���������Ƿ���
	stats = GameStats(ai_settings)
	bb = Bloodboard(ai_settings, screen, stats)

	#��ʼ��Ϸ����ѭ��
	while True:
		
		gf.check_events(ai_settings, screen, smallfish, oldbig, sw, ow)
		
		smallfish.update()
		gf.update_oldbig(ai_settings, oldbig)
		gf.update_small_words(ai_settings, screen, stats, bb, smallfish, oldbig, sw)
		gf.update_old_words(ai_settings, screen, stats, bb, smallfish, oldbig, ow)
		
		
		#ÿ��ѭ���ػ���Ļ

		gf.update_screen(ai_settings, screen, stats, bb, wechat, end, smallfish, oldbig, sw, ow)
	

run_game()
