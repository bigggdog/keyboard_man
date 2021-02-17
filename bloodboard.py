# coding=gbk
import pygame.font
from oldbig import Oldbig
from smallfish import Smallfish

class Bloodboard():
	"""��ʾ�÷���Ϣ����"""
	
	def __init__(self, ai_settings, screen, stats):
		"""��ʼ����ʾ�÷��漰������"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		
		#��ʾ�÷���Ϣʱʹ�õ���������
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont("arial", 40)
		
		#׼����ʼ�÷�ͼ��
		self.prep_small_blood()
		self.prep_old_blood()
		
	def prep_small_blood(self):
		"""���÷�ת����һ����Ⱦ��ͼ��"""
		rounded_small_blood = int(round(self.stats.small_blood_left, -1))
		small_blood_str = "{:,}".format(rounded_small_blood)
		self.small_blood_image = self.font.render(small_blood_str, True, self.text_color, 
					self.ai_settings.bg_color)
					
		#���÷ַ�����Ļ���Ͻ�
		self.small_blood_rect = self.small_blood_image.get_rect()
		self.small_blood_rect.right = self.screen_rect.right -20
		self.small_blood_rect.top = 20
		
	def prep_old_blood(self):
		"""���÷�ת����һ����Ⱦ��ͼ��"""
		rounded_old_blood = int(round(self.stats.old_blood_left, -1))
		old_blood_str = "{:,}".format(rounded_old_blood)
		self.old_blood_image = self.font.render(old_blood_str, True, self.text_color, 
					self.ai_settings.bg_color)
					
		#���÷ַ�����Ļ���Ͻ�
		self.old_blood_rect = self.old_blood_image.get_rect()
		self.old_blood_rect.left = 20
		self.old_blood_rect.top = 20

	def show_score(self):
		"""����Ļ����ʾ�÷ֺ���߷�"""
		self.screen.blit(self.small_blood_image, self.small_blood_rect)
		self.screen.blit(self.old_blood_image, self.old_blood_rect)
