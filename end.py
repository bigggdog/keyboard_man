# coding=gbk
import pygame

class End():
	
	def __init__(self, screen):
		"""初始化微信图像并设置其初始位置"""
		self.screen = screen
		
		#加载微信图像并获取其外接矩形
		self.image = pygame.image.load('images/end.bmp').convert()
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#将微信图像放在屏幕左侧中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		
	def blitme(self):
		"""在指定位置绘制微信图像"""
		self.screen.blit(self.image, self.rect)
