# coding=gbk
class Settings():
	"""���桶һ�����ӵ��ճ������������õ���"""
	def __init__(self):
		"""��ʼ����Ϸ������"""
		#��Ļ����
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		
		#Сˮ����ϴ���ٶ�
		self.smallfish_speed_factor = 1.5
		self.oldbig_speed_factor = 1
		#oldbig_directionΪ1��ʾ�����ƶ���Ϊ-1��ʾ�����ƶ�
		self.oldbig_direction = 1
		#���ֵ�����
		self.words_color = (0, 0, 0)
		self.words_speed_factor = 0.9
		#����������
		self.background_white = (255, 255, 255)
		self.background_green = (0, 255, 0)
		
		self.background_speed_factor = 1
		
		#�������ֵĲ���
		self.words_allowed = 3
		
		#Ѫ��������
		self.blood_limit = 500
