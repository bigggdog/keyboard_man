# coding=gbk
import pygame

class Smallfish():
	
	def __init__(self, ai_settings, screen):
		"""��ʼ��Сˮ��ͷ���������ʼλ��"""
		self.screen = screen
		self.ai_settings = ai_settings
		#����Сˮ��ͷ�񲢻�ȡ����Ӿ���
		self.image = pygame.image.load('images/smallfish.bmp').convert()
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#��Сˮ��ͷ�������Ļ�Ҳ�����
		self.rect.centery = self.screen_rect.centery
		self.rect.right = self.screen_rect.right
		
		#��Сˮ��������д���С��ֵ
		self.center = float(self.rect.centery)
		
		#�ƶ���־
		self.moving_top = False
		self.moving_bottom = False
		
	def update(self):
		"""�����ƶ���־����Сˮ���λ��"""
		if self.moving_top and self.rect.top > 80:
			self.center -= self.ai_settings.smallfish_speed_factor
			#����self.center����rect�������������ʱû��
			self.rect.centery = self.center
		if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom-62:
			self.center += self.ai_settings.smallfish_speed_factor
			#����self.center����rect�������������ʱû��
			self.rect.centery = self.center
		
	def blitme(self):
		"""��ָ��λ�û���Сˮ��ͷ��"""
		self.screen.blit(self.image, self.rect)
