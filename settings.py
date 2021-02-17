# coding=gbk
class Settings():
	"""储存《一个喷子的日常》的所有设置的类"""
	def __init__(self):
		"""初始化游戏的设置"""
		#屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		
		#小水鱼和老大的速度
		self.smallfish_speed_factor = 1.5
		self.oldbig_speed_factor = 1
		#oldbig_direction为1表示向下移动，为-1表示向上移动
		self.oldbig_direction = 1
		#文字的设置
		self.words_color = (0, 0, 0)
		self.words_speed_factor = 0.9
		#背景的设置
		self.background_white = (255, 255, 255)
		self.background_green = (0, 255, 0)
		
		self.background_speed_factor = 1
		
		#设置文字的参数
		self.words_allowed = 3
		
		#血量的设置
		self.blood_limit = 500
