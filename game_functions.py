# coding=gbk
import sys

import pygame
import pygame.font
from small_words import Small_words
from old_words import Old_words

def check_keydown_events(event, ai_settings, screen, smallfish, oldbig, sw, ow):
	"""��Ӧ����"""
	if event.key == pygame.K_UP:
		smallfish.moving_top = True
	elif event.key == pygame.K_DOWN:
		smallfish.moving_bottom = True
	elif event.key == pygame.K_SPACE:
		#�����µķ��ԣ������뵽������
		if len(sw) < ai_settings.words_allowed:
			new_sw = Small_words(ai_settings, screen, smallfish)
			new_ow = Old_words(ai_settings, screen, oldbig)
			sw.add(new_sw)
			ow.add(new_ow)
	elif event.key == pygame.K_q:
		sys.exit()
		
def check_keyup_events(event, smallfish):
	"""��Ӧ�ɿ�"""
	if event.key == pygame.K_UP:
		smallfish.moving_top = False
	elif event.key == pygame.K_DOWN:
		smallfish.moving_bottom = False
		
def check_events(ai_settings, screen, smallfish, oldbig, sw, ow):
	"""��Ӧ����������¼�"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, smallfish, oldbig, sw, ow)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, smallfish)
			
def update_oldbig(ai_settings, oldbig):
	"""�ϴ�������Ե���ı��ƶ�����"""
	if oldbig.check_edges():
		ai_settings.oldbig_direction *= -1
	oldbig.update()


def update_small_words(ai_settings, screen, stats, bb, smallfish, oldbig, sw):
	"""�����ӵ�λ�ã���ɾ������ʧ���ӵ�"""
	#�������ֵ�λ��
	sw.update()
	#ɾ����Ļ������֣�����ľ��β���Ҫ��small_words���е�small_words_rect
	for s in sw.copy():
		if s.small_words_rect.colliderect(oldbig):
			stats.old_blood_left -= 20
			sw.remove(s)
			bb.prep_old_blood()
		if s.small_words_rect.right <= 0:
			sw.remove(s)
		
def update_old_words(ai_settings, screen, stats, bb, smallfish, oldbig, ow):
	"""�����ӵ�λ�ã���ɾ������ʧ���ӵ�"""
	#�������ֵ�λ��
	ow.update()
	#ɾ����Ļ������֣�����ľ��β���Ҫ��old_words���е�old_words_rect
	for o in ow.copy():
		if o.old_words_rect.colliderect(smallfish):
			stats.small_blood_left -= 20
			ow.remove(o)
			bb.prep_small_blood()
		if o.old_words_rect.left >= 1200:
			ow.remove(o)


def update_screen(ai_settings, screen, stats, bb, wechat, end, smallfish, oldbig, sw, ow):
	screen.fill(ai_settings.bg_color)

	wechat.blitme()

	#��ʾСˮ������
	for small_word in sw.sprites():
		small_word.draw_green_background()
		small_word.show_small_words()
	#��ʾ�ϴ�����
	for old_word in ow.sprites():
		old_word.draw_white_background()
		old_word.show_old_words()

	smallfish.blitme()
	oldbig.blitme()
	
	bb.show_score()
	if stats.old_blood_left <=0 or stats.small_blood_left <=0:
		end.blitme()
	#��������Ƶ���Ļ�ɼ�
	pygame.display.flip()
