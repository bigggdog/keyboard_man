# coding=gbk
import pygame.font
import random
from pygame.sprite import Sprite

class Old_words(Sprite):
	def __init__(self, ai_settings, screen, oldbig):
		super(Old_words, self).__init__()
		"""初始化老大的发言文字并设置其起始位置"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.oldbig = oldbig

		self.speed_factor = ai_settings.words_speed_factor

		self.font = pygame.font.Font('simsun/simsun.ttf', 30)
		
		filename = 'oldbig_words.txt'
		with open(filename, encoding = 'utf-8') as file_object:
			lines = file_object.readlines()
			
		self.old_surface = self.font.render(random.choice(lines), True, self.ai_settings.words_color)
		#获取文字的矩形，再设置其正确的位置
		self.old_words_rect = self.old_surface.get_rect()
		self.old_words_rect.centery = self.oldbig.rect.centery
		self.old_words_rect.left = self.oldbig.rect.right + 20
		self.x = float(self.old_words_rect.x)

	def draw_white_background(self):
		"""画出文字的白色背景"""
		background_width = self.old_words_rect.right - self.old_words_rect.left + 10
		self.rect = pygame.Rect(0, 0, background_width, 50)
		self.rect.centery = self.old_words_rect.centery
		self.rect.centerx = self.old_words_rect.centerx - 8
		pygame.draw.rect(self.screen, self.ai_settings.background_white, self.rect)
		
	def update(self):
		"""向右移动老大的文字"""
		#更新文字位置的小数值
		self.x += self.speed_factor
		#更新文字的位置
		self.old_words_rect.x = self.x

	def show_old_words(self):
		"""在指定位置绘制老大的发言"""
		self.screen.blit(self.old_surface, self.old_words_rect)
