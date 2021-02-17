# coding=gbk
import pygame

class Oldbig():
	
	def __init__(self, ai_settings, screen):
		"""初始化老大头像并设置其初始位置"""
		self.screen = screen
		self.ai_settings = ai_settings
		#加载老大头像并获取其外接矩形
		self.image = pygame.image.load('images/oldbig.bmp').convert()
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#将老大头像放在屏幕中央
		self.rect.left = self.screen_rect.left
		self.rect.centery = self.screen_rect.centery
		
		#在老大的属性中储存小数值
		self.center = float(self.rect.centery)
		
	def check_edges(self):
		""""如果老大位于屏幕边缘，就返回True"""
		screen_rect = self.screen.get_rect()
		if self.rect.top <= 110:
			return True
		elif self.rect.bottom >= self.screen_rect.bottom-62:
			return True
		
	def update(self):
		"""自动调整老大的位置"""
		self.center += (self.ai_settings.oldbig_speed_factor * 
			self.ai_settings.oldbig_direction)
		
		#根据self.center更新rect对象
		self.rect.centery = self.center
		
	def blitme(self):
		"""在指定位置绘制老大头像"""
		self.screen.blit(self.image, self.rect)
