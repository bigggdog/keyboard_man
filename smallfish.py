# coding=gbk
import pygame

class Smallfish():
	
	def __init__(self, ai_settings, screen):
		"""初始化小水鱼头像并设置其初始位置"""
		self.screen = screen
		self.ai_settings = ai_settings
		#加载小水鱼头像并获取其外接矩形
		self.image = pygame.image.load('images/smallfish.bmp').convert()
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#将小水鱼头像放在屏幕右侧中央
		self.rect.centery = self.screen_rect.centery
		self.rect.right = self.screen_rect.right
		
		#在小水鱼的属性中储存小数值
		self.center = float(self.rect.centery)
		
		#移动标志
		self.moving_top = False
		self.moving_bottom = False
		
	def update(self):
		"""根据移动标志调整小水鱼的位置"""
		if self.moving_top and self.rect.top > 80:
			self.center -= self.ai_settings.smallfish_speed_factor
			#根据self.center更新rect对象，这个功能暂时没用
			self.rect.centery = self.center
		if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom-62:
			self.center += self.ai_settings.smallfish_speed_factor
			#根据self.center更新rect对象，这个功能暂时没用
			self.rect.centery = self.center
		
	def blitme(self):
		"""在指定位置绘制小水鱼头像"""
		self.screen.blit(self.image, self.rect)
