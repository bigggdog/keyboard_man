# coding=gbk
import pygame.font
from oldbig import Oldbig
from smallfish import Smallfish

class Bloodboard():
	"""显示得分信息的类"""
	
	def __init__(self, ai_settings, screen, stats):
		"""初始化显示得分涉及的属性"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		
		#显示得分信息时使用的字体设置
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont("arial", 40)
		
		#准备初始得分图像
		self.prep_small_blood()
		self.prep_old_blood()
		
	def prep_small_blood(self):
		"""将得分转换成一幅渲染的图像"""
		rounded_small_blood = int(round(self.stats.small_blood_left, -1))
		small_blood_str = "{:,}".format(rounded_small_blood)
		self.small_blood_image = self.font.render(small_blood_str, True, self.text_color, 
					self.ai_settings.bg_color)
					
		#将得分放在屏幕右上角
		self.small_blood_rect = self.small_blood_image.get_rect()
		self.small_blood_rect.right = self.screen_rect.right -20
		self.small_blood_rect.top = 20
		
	def prep_old_blood(self):
		"""将得分转换成一幅渲染的图像"""
		rounded_old_blood = int(round(self.stats.old_blood_left, -1))
		old_blood_str = "{:,}".format(rounded_old_blood)
		self.old_blood_image = self.font.render(old_blood_str, True, self.text_color, 
					self.ai_settings.bg_color)
					
		#将得分放在屏幕右上角
		self.old_blood_rect = self.old_blood_image.get_rect()
		self.old_blood_rect.left = 20
		self.old_blood_rect.top = 20

	def show_score(self):
		"""在屏幕上显示得分和最高分"""
		self.screen.blit(self.small_blood_image, self.small_blood_rect)
		self.screen.blit(self.old_blood_image, self.old_blood_rect)
