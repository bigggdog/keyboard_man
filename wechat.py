# coding=gbk
import pygame

class Wechat():
	
	def __init__(self, screen):
		"""��ʼ��΢��ͼ���������ʼλ��"""
		self.screen = screen
		
		#����΢��ͼ�񲢻�ȡ����Ӿ���
		self.image = pygame.image.load('images/wechat.bmp').convert()
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#��΢��ͼ�������Ļ�������
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		
	def blitme(self):
		"""��ָ��λ�û���΢��ͼ��"""
		self.screen.blit(self.image, self.rect)
