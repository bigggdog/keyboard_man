# coding=gbk
import pygame

class Oldbig():
	
	def __init__(self, ai_settings, screen):
		"""��ʼ���ϴ�ͷ���������ʼλ��"""
		self.screen = screen
		self.ai_settings = ai_settings
		#�����ϴ�ͷ�񲢻�ȡ����Ӿ���
		self.image = pygame.image.load('images/oldbig.bmp').convert()
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#���ϴ�ͷ�������Ļ����
		self.rect.left = self.screen_rect.left
		self.rect.centery = self.screen_rect.centery
		
		#���ϴ�������д���С��ֵ
		self.center = float(self.rect.centery)
		
	def check_edges(self):
		""""����ϴ�λ����Ļ��Ե���ͷ���True"""
		screen_rect = self.screen.get_rect()
		if self.rect.top <= 110:
			return True
		elif self.rect.bottom >= self.screen_rect.bottom-62:
			return True
		
	def update(self):
		"""�Զ������ϴ��λ��"""
		self.center += (self.ai_settings.oldbig_speed_factor * 
			self.ai_settings.oldbig_direction)
		
		#����self.center����rect����
		self.rect.centery = self.center
		
	def blitme(self):
		"""��ָ��λ�û����ϴ�ͷ��"""
		self.screen.blit(self.image, self.rect)
