# coding=gbk
import sys

import pygame
import pygame.font
from small_words import Small_words
from old_words import Old_words

def check_keydown_events(event, ai_settings, screen, smallfish, oldbig, sw, ow):
	"""响应按键"""
	if event.key == pygame.K_UP:
		smallfish.moving_top = True
	elif event.key == pygame.K_DOWN:
		smallfish.moving_bottom = True
	elif event.key == pygame.K_SPACE:
		#创建新的发言，并加入到编组中
		if len(sw) < ai_settings.words_allowed:
			new_sw = Small_words(ai_settings, screen, smallfish)
			new_ow = Old_words(ai_settings, screen, oldbig)
			sw.add(new_sw)
			ow.add(new_ow)
	elif event.key == pygame.K_q:
		sys.exit()
		
def check_keyup_events(event, smallfish):
	"""响应松开"""
	if event.key == pygame.K_UP:
		smallfish.moving_top = False
	elif event.key == pygame.K_DOWN:
		smallfish.moving_bottom = False
		
def check_events(ai_settings, screen, smallfish, oldbig, sw, ow):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, smallfish, oldbig, sw, ow)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, smallfish)
			
def update_oldbig(ai_settings, oldbig):
	"""老大碰到边缘，改变移动方向"""
	if oldbig.check_edges():
		ai_settings.oldbig_direction *= -1
	oldbig.update()


def update_small_words(ai_settings, screen, stats, bb, smallfish, oldbig, sw):
	"""更新子弹位置，并删除已消失的子弹"""
	#更新文字的位置
	sw.update()
	#删除屏幕外的文字，这里的矩形参数要用small_words类中的small_words_rect
	for s in sw.copy():
		if s.small_words_rect.colliderect(oldbig):
			stats.old_blood_left -= 20
			sw.remove(s)
			bb.prep_old_blood()
		if s.small_words_rect.right <= 0:
			sw.remove(s)
		
def update_old_words(ai_settings, screen, stats, bb, smallfish, oldbig, ow):
	"""更新子弹位置，并删除已消失的子弹"""
	#更新文字的位置
	ow.update()
	#删除屏幕外的文字，这里的矩形参数要用old_words类中的old_words_rect
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

	#显示小水鱼文字
	for small_word in sw.sprites():
		small_word.draw_green_background()
		small_word.show_small_words()
	#显示老大文字
	for old_word in ow.sprites():
		old_word.draw_white_background()
		old_word.show_old_words()

	smallfish.blitme()
	oldbig.blitme()
	
	bb.show_score()
	if stats.old_blood_left <=0 or stats.small_blood_left <=0:
		end.blitme()
	#让最近绘制的屏幕可见
	pygame.display.flip()
