# coding=gbk
import pygame.font
import random
from pygame.sprite import Sprite

class Small_words(Sprite):
	"""�����Ե���"""
	def __init__(self, ai_settings, screen, smallfish):
		"""��Сˮ�����ߴ���һ�����Զ���"""
		super(Small_words, self).__init__()
		"""��ʼ��Сˮ��ķ������ֲ���������ʼλ��"""
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
		#��ȡ���ֵľ��Σ�����������ȷ��λ��
		self.small_words_rect = self.small_surface.get_rect()
		self.small_words_rect.centery = self.sf.rect.centery
		self.small_words_rect.right = self.sf.rect.left - 20
		self.x = float(self.small_words_rect.x)

	def draw_green_background(self):
		"""�������ֵ���ɫ����"""
		background_width = self.small_words_rect.right - self.small_words_rect.left + 10
		self.rect = pygame.Rect(0, 0, background_width, 50)
		self.rect.centery = self.small_words_rect.centery
		self.rect.centerx = self.small_words_rect.centerx - 8
		pygame.draw.rect(self.screen, self.ai_settings.background_green, self.rect)
		
	def update(self):
		"""�����ƶ�Сˮ�������"""
		#��������λ�õ�С��ֵ
		self.x -= self.speed_factor
		#�������ֵ�λ��
		self.small_words_rect.x = self.x


	def show_small_words(self):
		"""��ָ��λ�û���Сˮ��ķ���"""
		self.screen.blit(self.small_surface, self.small_words_rect)
