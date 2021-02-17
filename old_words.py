# coding=gbk
import pygame.font
import random
from pygame.sprite import Sprite

class Old_words(Sprite):
	def __init__(self, ai_settings, screen, oldbig):
		super(Old_words, self).__init__()
		"""��ʼ���ϴ�ķ������ֲ���������ʼλ��"""
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
		#��ȡ���ֵľ��Σ�����������ȷ��λ��
		self.old_words_rect = self.old_surface.get_rect()
		self.old_words_rect.centery = self.oldbig.rect.centery
		self.old_words_rect.left = self.oldbig.rect.right + 20
		self.x = float(self.old_words_rect.x)

	def draw_white_background(self):
		"""�������ֵİ�ɫ����"""
		background_width = self.old_words_rect.right - self.old_words_rect.left + 10
		self.rect = pygame.Rect(0, 0, background_width, 50)
		self.rect.centery = self.old_words_rect.centery
		self.rect.centerx = self.old_words_rect.centerx - 8
		pygame.draw.rect(self.screen, self.ai_settings.background_white, self.rect)
		
	def update(self):
		"""�����ƶ��ϴ������"""
		#��������λ�õ�С��ֵ
		self.x += self.speed_factor
		#�������ֵ�λ��
		self.old_words_rect.x = self.x

	def show_old_words(self):
		"""��ָ��λ�û����ϴ�ķ���"""
		self.screen.blit(self.old_surface, self.old_words_rect)
