# coding=gbk
class GameStats():
	"""������Ϸ��ͳ����Ϣ"""
	def __init__(self, ai_settings):
		"""��ʼ��ͳ����Ϣ"""
		self.ai_settings = ai_settings
		self.reset_stats()
	
		
	def reset_stats(self):
		"""��ʼ������Ϸ�����ڼ���ܱ仯��ͳ����Ϣ"""
		self.small_blood_left = self.ai_settings.blood_limit
		self.old_blood_left = self.ai_settings.blood_limit
