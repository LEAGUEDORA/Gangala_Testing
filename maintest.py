            # # # #                                                             WORKING code**************@*
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
import time
import getpass
import pyautogui
import random                                                               
import json
import pandas as pd
lis,li,ml,mpl,bug_list=[],[],[],[],[]
import gspread
#import os
#os.path.join("selitestcerd.json")
gc = gspread.service_account(filename = "D:\\ref\\templates\\Python Codes\\Selenium\\selitestcerd.json")
sh = gc.open_by_key("1og5kORoM3-82yg_uV34e39gh6EYht7lZxmHqG6QLApQ")
worksheet = sh.sheet1
global coun

f = open("D:\\ref\\templates\\Python Codes\\Selenium\\seleniumroughdata.json")
f = json.load(f)

# data = pd.read_excel("data.xlsx",sheet_name="Intent Training Phrases")
# data=data[["Intent training phrase 1","Intent training phrase 2"]]
# data = data.to_json(orient="records")

# with open("dataa.json", "w") as json_file:
#     json_file.write(data)

with open("D:\\ref\\templates\\Python Codes\\dataa.json") as json_file:
    data = json.load(json_file)

Path = "D:\Download(D)\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(Path)

driver.get("http://172.105.33.88/interactive")
driver.maximize_window()
driver.find_element_by_name("password").send_keys("Venkat_bot")
time.sleep(1)
pyautogui.press("enter")
time.sleep(0.5)
time.sleep(3)
pyautogui.moveTo(30,200,duration=1)
pyautogui.click()
pyautogui.moveTo(900,800,duration=1)
time.sleep(5)
driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div/div/div/div/div[2]/div/div[2]/div/button[1]').click()
time.sleep(3)

class functions():
    def re():
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/div[1]/textarea').click()
        time.sleep(1)
        pyautogui.write("/restart")
        pyautogui.press("enter")
        pyautogui.scroll(-140)
        time.sleep(2)
        pyautogui.moveTo(1100,750,duration=2)
        pyautogui.doubleClick()
        driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/div[2]/ul/div[1]/div[2]/div[2]/button[2]").click()
        time.sleep(2)
        pyautogui.moveTo(900,800,duration=2)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/div[1]/textarea').click()
        v = data[random.randint(0,len(data)-1)]["Intent training phrase {}".format(random.choice([1,2]))]
        pyautogui.write(v)
        pyautogui.press("enter")
        pyautogui.scroll(-140)
        time.sleep(2)

    def wrksheet():
        global bug_list,lis
        lis,bug_list=[],[]
        worksheet.append_row(ml)
        worksheet.append_row(kk)
        worksheet.append_row(["NEXT"])
        res = worksheet.get_all_values()
        bug_list =[]
        lis =[]
        functions.re()

    def ex():
        coun = 0
        pyautogui.moveTo(900,800)
        pyautogui.doubleClick()
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/div[1]/textarea').click()
        ml.append(driver.find_elements_by_class_name("css-1di2tiy")[-1].text)
        for i in driver.find_elements_by_class_name("css-1di2tiy")[-1].text.split(" "):
            if i.lower().strip() in f:
                pyautogui.write(random.choice(f[i.lower()]))
                coun=1
        if coun == 0:
            pyautogui.write("abc")
        pyautogui.press("enter")
        pyautogui.scroll(-140)
        time.sleep(5)
        pyautogui.doubleClick()

v = data[random.randint(0,len(data))]["Intent training phrase {}".format(random.choice([1,2]))]
driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/div[1]/textarea').send_keys(v)
ml.append(v)
pyautogui.press("enter")
time.sleep(3)

while True:
    try:
        if driver.find_elements_by_class_name("css-1wvkf5u"):
            kk =[i.text for i in driver.find_elements_by_class_name("css-1wvkf5u")]
            mpl.append(driver.find_elements_by_class_name("css-1wvkf5u")[-1].text)
        if driver.find_element_by_class_name("css-1di2tiy"):
            if driver.find_elements_by_class_name("css-1di2tiy")[-1].text not in (bug_list) :
                bug_list=[]
                bug_list.append(driver.find_elements_by_class_name("css-1di2tiy")[-1].text)
            elif driver.find_elements_by_class_name("css-d6yrmz"):
                for i in driver.find_elements_by_class_name("css-d6yrmz"):
                    lis.append(i.text)
                if lis not in (bug_list):
                    bug_list.append(lis)
                else:
                    functions.wrksheet()
            else:
                functions.wrksheet()
        time.sleep(2)
        if driver.find_elements_by_class_name("css-d6yrmz"):
            time.sleep(1)
            b= random.choice(driver.find_elements_by_class_name("css-d6yrmz"))
            ml.append(b.text)
            b.click()
            pyautogui.scroll(-140)
            time.sleep(3)
        else:
            try:
                if driver.find_elements_by_class_name("css-1di2tiy")[-2].text:
                    if "The details of your action" in driver.find_elements_by_class_name("css-1di2tiy")[-2].text or "You can check your auction status" in driver.find_elements_by_class_name("css-1di2tiy")[-2].text or "Please click here to follow up on your requirement" in driver.find_elements_by_class_name("css-1di2tiy")[-2].text:
                        time.sleep(3)
                        continue
            except:
                if driver.find_elements_by_class_name("css-1di2tiy").text:
                    if driver.find_elements_by_class_name("css-1di2tiy")[-1].text:
                        functions.ex()
            else:    
                functions.ex()
    except Exception as eee:
            functions.ex()
