# coding=gbk
import pygame.font
import random
from pygame.sprite import Sprite

class Small_words(Sprite):
	"""管理发言的类"""
	def __init__(self, ai_settings, screen, smallfish):
		"""在小水鱼的左边创建一个发言对象"""
		super(Small_words, self).__init__()
		"""初始化小水鱼的发言文字并设置其起始位置"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.sf = smallfish

		self.speed_factor = ai_settings.words_speed_factor

		self.font = pygame.font.Font('simsun/simsun.ttf', 30)
		
		filename = 'small_words.txt'
		with open(filename, encoding = 'utf-8') as file_object:
			lines = file_object.readlines()
			
		self.small_surface = self.font.render(random.choice(lines), True, self.ai_settings.words_color)
		#获取文字的矩形，再设置其正确的位置
		self.small_words_rect = self.small_surface.get_rect()
		self.small_words_rect.centery = self.sf.rect.centery
		self.small_words_rect.right = self.sf.rect.left - 20
		self.x = float(self.small_words_rect.x)

	def draw_green_background(self):
		"""画出文字的蓝色背景"""
		background_width = self.small_words_rect.right - self.small_words_rect.left + 10
		self.rect = pygame.Rect(0, 0, background_width, 50)
		self.rect.centery = self.small_words_rect.centery
		self.rect.centerx = self.small_words_rect.centerx - 8
		pygame.draw.rect(self.screen, self.ai_settings.background_green, self.rect)
		
	def update(self):
		"""向左移动小水鱼的文字"""
		#更新文字位置的小数值
		self.x -= self.speed_factor
		#更新文字的位置
		self.small_words_rect.x = self.x


	def show_small_words(self):
		"""在指定位置绘制小水鱼的发言"""
		self.screen.blit(self.small_surface, self.small_words_rect)
