# coding=gbk

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import threading

url = "https://alm.harman.com/qm/web/console/HCC%20Prod%20(QM)/_u9KngDdHEeeYe-w6pMegzw#action=com.ibm.rqm.planning.home.actionDispatcher&subAction=viewTestPlan&id=1251"
testenvironment = "BA9_Base_CN"
iteration = ""
iteration_row = 1
password = "GHXharman567"

class myThread (threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.run_status = "stop"
		self.run_times = 0
	def pause(self):
		self.run_status = "stop"
	def result_pass(self):
		self.run_status = "pass"
		self.run_times = int(pass_run_times.get())
	def result_block(self):
		self.run_status = "block"
		self.run_times = int(block_run_times.get())
	def run(self):
		def if_element_id_exist(element):
			try:
				browser.find_element_by_id(element)
				return True
			except:
				return False
		def if_element_xpath_exist(element):
			try:
				browser.find_element_by_xpath(element)
				return True
			except:
				return False
		browser = webdriver.Firefox()
		browser.get(url)
		nowhandle = browser.current_window_handle
		aalhandles = browser.window_handles
		for handle in aalhandles:
			if handle!=nowhandle:
				browser.switch_to_window(handle)
				flag = False
				while flag == False:
					time.sleep(3)
					flag = if_element_id_exist("jazz_app_internal_LoginWidget_0_userId")
				input_user = browser.find_element_by_id("jazz_app_internal_LoginWidget_0_userId")
				input_user.clear()
				input_user.send_keys("GHaoxiang")
				input_password = browser.find_element_by_id("jazz_app_internal_LoginWidget_0_password")
				input_password.clear()
				input_password.send_keys(password)
				login = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[3]/form/button")
				login.click()
		browser.switch_to_window(nowhandle)
		#ѡTest Case Execution Records
		flag = False
		while flag == False:
			time.sleep(3)
			flag = if_element_id_exist("com_ibm_asq_common_web_ui_internal_widgets_DirectoryPane_0.com.ibm.rqm.planning.editor.section.planTestCaseExecutionRecords")
		browser.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_DirectoryPane_0.com.ibm.rqm.planning.editor.section.planTestCaseExecutionRecords").click()
		#��filter
		flag = False
		while flag == False:
			time.sleep(3)
			flag = if_element_xpath_exist("/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/table/tbody/tr/td[2]/div[2]/div/div[32]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/table/thead/tr[6]/td/div")
		browser.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/table/tbody/tr/td[2]/div[2]/div/div[32]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/table/thead/tr[6]/td/div").click()
		#�����Ҳ���Ϣ��
		browser.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[3]/div/div[2]").click()
		time.sleep(3)
		#���Last Result
		flag = False
		while flag == False:
			time.sleep(1)
			flag = if_element_xpath_exist("/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/table/tbody/tr/td[2]/div[2]/div/div[32]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/table/thead/tr[3]/th[5]/table/tbody/tr/td[3]/div/div/div/div")
		browser.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/table/tbody/tr/td[2]/div[2]/div/div[32]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/table/thead/tr[3]/th[5]/table/tbody/tr/td[3]/div/div/div/div").click()
		#ѡ��Not Run��Blocked
		flag = False
		while flag == False:
			time.sleep(1)
			flag = if_element_xpath_exist('//*[@id="com_ibm_asq_common_web_ui_internal_widgets_layout_toggleMenuItem_64_text"]')
		browser.find_element_by_xpath('//*[@id="com_ibm_asq_common_web_ui_internal_widgets_layout_toggleMenuItem_64_text"]').click()
		browser.find_element_by_xpath('//*[@id="com_ibm_asq_common_web_ui_internal_widgets_layout_toggleMenuItem_60_text"]').click()
		#���Test Result Reason
		browser.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/table/tbody/tr/td[2]/div[2]/div/div[32]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/table/thead/tr[3]/th[7]/table/tbody/tr/td[3]/div/div/div/div").click()
		#ѡ��Unassigned
		flag = False
		while flag == False:
			time.sleep(1)
			flag = if_element_xpath_exist('//*[@id="com_ibm_asq_common_web_ui_internal_widgets_layout_toggleMenuItem_85_text"]')
		browser.find_element_by_xpath('//*[@id="com_ibm_asq_common_web_ui_internal_widgets_layout_toggleMenuItem_85_text"]').click()
		#ѡ��Iteration
		if iteration != "":
			browser.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_layout_DropDownButton_37_label").click()
			time.sleep(5)
			#���More
			for value in range(11,20):
				try:
					browser.find_element_by_id('dijit_MenuItem_' + str(value) + '_text')
				except:
					continue
				else:
					browser.find_element_by_id('dijit_MenuItem_' + str(value) + '_text').click()
					break
			time.sleep(2)
			#�����汾��
			flag = False
			while flag == False:
				time.sleep(1)
				flag = if_element_id_exist("com_ibm_asq_common_web_ui_internal_widgets_selector_InMemoryScalableSelectorDialog_0-searchText")
			input_iteration = browser.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_selector_InMemoryScalableSelectorDialog_0-searchText")
			input_iteration.clear()
			input_iteration.send_keys(iteration)
			#ѡ��汾��
			time.sleep(1)
			browser.find_element_by_xpath('/html/body/div[19]/div[2]/div[2]/div[3]/div/div[1]/span/div/div/div[5]/select/option[' + str(iteration_row + 1) + ']').click()
			time.sleep(1)
			browser.find_element_by_xpath('/html/body/div[19]/div[2]/div[2]/div[3]/div/div[2]/div[2]/span[1]/button').click()
			time.sleep(1)
		#����Test Environment
		test_environment = browser.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_layout_ASQValidateTextBox_45")
		test_environment.clear()
		test_environment.send_keys(testenvironment)
		#����Last ModifiedΪNo Sort
		browser.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_tableViewer_TableViewer_0_col_3").click()
		time.sleep(1)
		browser.find_element_by_xpath("/html/body/div[17]/div[3]/div[3]/label").click()
		time.sleep(1)
		#����Last ResultΪAscending
		browser.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_tableViewer_TableViewer_0_col_2").click()
		time.sleep(1)
		browser.find_element_by_xpath("/html/body/div[17]/div[3]/div[1]/label").click()
		time.sleep(1)
		#����NameΪAscending
		browser.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_tableViewer_TableViewer_0_col_0").click()
		time.sleep(1)
		browser.find_element_by_xpath("/html/body/div[17]/div[3]/div[1]/label").click()
		time.sleep(5)
		#���Run����filter
		target = browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/table/tbody/tr/td[2]/div[2]/div/div[32]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/table/thead/tr[4]/th/div[3]/button')
		browser.execute_script("arguments[0].scrollIntoView();", target)
		browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/table/tbody/tr/td[2]/div[2]/div/div[32]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/table/thead/tr[4]/th/div[3]/button').click()
		time.sleep(15)
		#ѡ����ʾ25��case
		try:
			Select(browser.find_element_by_id('com_ibm_asq_common_web_ui_internal_widgets_tableViewer_TableViewer_0-select-page-range')).select_by_value('25')
		except:
			print ("û��ѡ��")
		time.sleep(10)
		while True:
			if self.run_status == "pass" and self.run_times != 0:
				#���Run����filter
				browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/table/tbody/tr/td[2]/div[2]/div/div[32]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/table/thead/tr[4]/th/div[3]/button').click()
				time.sleep(3)
				#�Ƿ����µ�¼
				aalhandles = browser.window_handles
				for handle in aalhandles:
					if handle!=nowhandle:
						browser.switch_to_window(handle)
						flag = False
						while flag == False:
							time.sleep(3)
							flag = if_element_id_exist("jazz_app_internal_LoginWidget_0_userId")
						input_user = browser.find_element_by_id("jazz_app_internal_LoginWidget_0_userId")
						input_user.clear()
						input_user.send_keys("GHaoxiang")
						input_password = browser.find_element_by_id("jazz_app_internal_LoginWidget_0_password")
						input_password.clear()
						input_password.send_keys(password)
						login = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[3]/form/button")
						login.click()
				browser.switch_to_window(nowhandle)
				time.sleep(3)
				#��һ��case
				flag = False
				while flag == False:
					time.sleep(3)
					flag = if_element_xpath_exist('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/table/tbody/tr/td[2]/div[2]/div/div[32]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/table/tbody/tr[1]/td[3]/div/div/a/div')
				case = browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/table/tbody/tr/td[2]/div[2]/div/div[32]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/table/tbody/tr[1]/td[3]/div/div/a/div')
				ActionChains(browser).key_down(Keys.CONTROL).click(case).key_up(Keys.CONTROL).perform()
				time.sleep(3)
				#�Ƿ����µ�¼
				browser.switch_to_window(browser.window_handles[-1])
				time.sleep(3)
				if browser.current_url == "https://jasprod.harman.com:9643/jazzop/form/login":
					flag = False
					while flag == False:
						time.sleep(3)
						flag = if_element_id_exist("jazz_app_internal_LoginWidget_0_userId")
					input_user = browser.find_element_by_id("jazz_app_internal_LoginWidget_0_userId")
					input_user.clear()
					input_user.send_keys("GHaoxiang")
					input_password = browser.find_element_by_id("jazz_app_internal_LoginWidget_0_password")
					input_password.clear()
					input_password.send_keys(password)
					login = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[3]/form/button")
					login.click()
					browser.switch_to_window(browser.window_handles[1])
					time.sleep(3)
				#���Run
				flag = False
				while flag == False:
					time.sleep(3)
					flag = if_element_xpath_exist('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/div[1]/div/div[3]/div[2]/div/div[2]/span[4]/a/span[3]')
				time.sleep(3)
				browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/div[1]/div/div[3]/div[2]/div/div[2]/span[4]/a/span[3]').click()
				time.sleep(1)
				browser.find_element_by_id('dijit_MenuItem_5_text').click()
				#���Pass
				times = 10
				flag = False
				while flag == False and times != 0:
					times -= 1
					time.sleep(3)
					flag = if_element_xpath_exist('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[3]/div/div[5]/div/div/div[5]/table/tbody/tr/td[2]/div/div/div/div[4]/div/div/div[2]/div[6]/div[2]/div[1]/div[2]/div/div/span[1]/a/img')
				if times == 0:
					self.run_status = "stop"
					browser.switch_to_window(browser.window_handles[0])
					messagebox.showinfo('��ʾ��Ϣ', 'Case�������ֶ�ִ��')
					continue
				browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[3]/div/div[5]/div/div/div[5]/table/tbody/tr/td[2]/div/div/div/div[4]/div/div/div[2]/div[6]/div[2]/div[1]/div[2]/div/div/span[1]/a/img').click()
				time.sleep(3)
				browser.close()
				browser.switch_to_window(browser.window_handles[0])
				self.run_times -= 1
				if self.run_times == 0:
					messagebox.showinfo('��ʾ��Ϣ', '�������')
			elif self.run_status == "block" and self.run_times != 0:
				#���Run����filter
				browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/table/tbody/tr/td[2]/div[2]/div/div[32]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/table/thead/tr[4]/th/div[3]/button').click()
				time.sleep(3)
				#�Ƿ����µ�¼
				aalhandles = browser.window_handles
				for handle in aalhandles:
					if handle!=nowhandle:
						browser.switch_to_window(handle)
						flag = False
						while flag == False:
							time.sleep(3)
							flag = if_element_id_exist("jazz_app_internal_LoginWidget_0_userId")
						input_user = browser.find_element_by_id("jazz_app_internal_LoginWidget_0_userId")
						input_user.clear()
						input_user.send_keys("GHaoxiang")
						input_password = browser.find_element_by_id("jazz_app_internal_LoginWidget_0_password")
						input_password.clear()
						input_password.send_keys(password)
						login = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[3]/form/button")
						login.click()
				browser.switch_to_window(nowhandle)
				time.sleep(3)
				#��һ��case
				flag = False
				while flag == False:
					time.sleep(3)
					flag = if_element_xpath_exist('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/table/tbody/tr/td[2]/div[2]/div/div[32]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/table/tbody/tr[1]/td[3]/div/div/a/div')
				case = browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/table/tbody/tr/td[2]/div[2]/div/div[32]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/table/tbody/tr[1]/td[3]/div/div/a/div')
				ActionChains(browser).key_down(Keys.CONTROL).click(case).key_up(Keys.CONTROL).perform()
				time.sleep(3)
				#�Ƿ����µ�¼
				browser.switch_to_window(browser.window_handles[-1])
				time.sleep(3)
				if browser.current_url == "https://jasprod.harman.com:9643/jazzop/form/login":
					flag = False
					while flag == False:
						time.sleep(3)
						flag = if_element_id_exist("jazz_app_internal_LoginWidget_0_userId")
					input_user = browser.find_element_by_id("jazz_app_internal_LoginWidget_0_userId")
					input_user.clear()
					input_user.send_keys("GHaoxiang")
					input_password = browser.find_element_by_id("jazz_app_internal_LoginWidget_0_password")
					input_password.clear()
					input_password.send_keys(password)
					login = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[3]/form/button")
					login.click()
					browser.switch_to_window(browser.window_handles[1])
					time.sleep(3)
				#���Run
				flag = False
				while flag == False:
					time.sleep(3)
					flag = if_element_xpath_exist('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/div[1]/div/div[3]/div[2]/div/div[2]/span[4]/a/span[3]')
				time.sleep(3)
				browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/div[1]/div/div[3]/div[2]/div/div[2]/span[4]/a/span[3]').click()
				time.sleep(1)
				browser.find_element_by_id('dijit_MenuItem_5_text').click()
				#���Block
				times = 10
				flag = False
				while flag == False and times != 0:
					times -= 1
					time.sleep(3)
					flag = if_element_xpath_exist('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[3]/div/div[5]/div/div/div[5]/table/tbody/tr/td[2]/div/div/div/div[4]/div/div/div[2]/div[6]/div[2]/div[1]/div[2]/div/div/span[3]/a/img')
				if times == 0:
					self.run_status = "stop"
					browser.switch_to_window(browser.window_handles[0])
					messagebox.showinfo('��ʾ��Ϣ', 'Case�������ֶ�ִ��')
					continue
				browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[3]/div/div[5]/div/div/div[5]/table/tbody/tr/td[2]/div/div/div/div[4]/div/div/div[2]/div[6]/div[2]/div[1]/div[2]/div/div/span[3]/a/img').click()
				flag = False
				while flag == False:
					time.sleep(2)
					flag = browser.find_element_by_id("dijit_MenuItem_11_text").is_displayed()
					if flag == False:
						browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[3]/div/div[5]/div/div/div[5]/table/tbody/tr/td[2]/div/div/div/div[4]/div/div/div[2]/div[6]/div[2]/div[1]/div[2]/div/div/span[3]/a/img').click()
				browser.find_element_by_id("dijit_MenuItem_11_text").click()
				time.sleep(3)
				browser.close()
				browser.switch_to_window(browser.window_handles[0])
				#���Run����filter
				browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/table/tbody/tr/td[2]/div[2]/div/div[32]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/table/thead/tr[4]/th/div[3]/button').click()
				#ѡ��Test Result Comment
				flag = False
				while flag == False:
					time.sleep(3)
					flag = if_element_xpath_exist('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/table/tbody/tr/td[2]/div[2]/div/div[32]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/table/tbody/tr[1]/td[8]')
				comment = browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/table/tbody/tr/td[2]/div[2]/div/div[32]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/table/tbody/tr[1]/td[8]')
				ActionChains(browser).double_click(comment).perform()
				browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/table/tbody/tr/td[2]/div[2]/div/div[32]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/table/tbody/tr[1]/td[8]/div/a/img').click()
				time.sleep(1)
				browser.switch_to.active_element.send_keys(test_result_comment.get())
				browser.switch_to.active_element.send_keys(Keys.ENTER)
				time.sleep(3)
				#ѡ��Test Result Reason
				reason = browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/table/tbody/tr/td[2]/div[2]/div/div[32]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/table/tbody/tr[1]/td[7]')
				ActionChains(browser).double_click(reason).perform()
				time.sleep(3)
				browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div/table/tbody/tr/td[2]/div[2]/div/div[32]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/table/tbody/tr[1]/td[7]/div/a/img').click()
				if test_result_reason.get() == 'Lack of Equipment':
					Select(browser.switch_to.active_element).select_by_index("4")
				if test_result_reason.get() == 'Non Testable Requirement':
					Select(browser.switch_to.active_element).select_by_index("6")
				if test_result_reason.get() == 'Unable to create / simulate test scenario':
					Select(browser.switch_to.active_element).select_by_index("9")
				time.sleep(1)
				browser.switch_to.active_element.send_keys(Keys.ENTER)
				time.sleep(2)
				self.run_times -= 1
				if self.run_times == 0:
					messagebox.showinfo('��ʾ��Ϣ', '�������')
			else:
				time.sleep(15)

root = Tk()
root.title('RQM�ű�������')

thread1 = myThread()

def program_start():
	thread1.start()
start_button = Button(root, text="��ʼ", font=("Arial", 30), command=program_start)
start_button.grid(row=1, column=1, padx=10, pady=10)

def program_pause():
	thread1.pause()
pause_button = Button(root, text="��ͣ", font=("Arial", 30), command=program_pause)
pause_button.grid(row=1, column=2, padx=10, pady=10)

def program_pass():
	thread1.result_pass()
pause_button = Button(root, text="Pass", font=("Arial", 30), command=program_pass)
pause_button.grid(row=1, column=3, padx=10, pady=10)

def program_block():
	thread1.result_block()
pause_button = Button(root, text="Block", font=("Arial", 30), command=program_block)
pause_button.grid(row=1, column=4, padx=10, pady=10)

Label(root, text="Test Result Reason").grid(row=2, column=1, padx=10, pady=10)
ReasonList = ['Lack of Equipment','Non Testable Requirement','Unable to create / simulate test scenario',]
test_result_reason = ttk.Combobox(root, values=ReasonList)
test_result_reason.grid(row=2, column=4, padx=10, pady=10)

Label(root, text="Test Result Comment").grid(row=3, column=1, padx=10, pady=10)
test_result_comment = Entry(root)
test_result_comment.grid(row=3, column=4, padx=10, pady=10)

Label(root, text="���д���").grid(row=4, column=1, padx=10, pady=10)
pass_run_times = Entry(root)
pass_run_times.insert(END, '99')
pass_run_times.grid(row=4, column=3, padx=10, pady=10)
block_run_times = Entry(root)
block_run_times.insert(END, '99')
block_run_times.grid(row=4, column=4, padx=10, pady=10)

root.mainloop()
