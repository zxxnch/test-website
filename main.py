import tkinter as tk
from tkinter import font
from indy_utils import indydcp_client as client
import pyautogui
import time
import pyperclip
import cv2
import numpy as np
from PIL import Image
import os
import sys
from tkinter import messagebox


robot_ip = "192.168.0.176"  # Robot (Indy) IP
robot_name = "NRMK-Indy7"  # Robot name (Indy7)
indy = client.IndyDCPClient(robot_ip, robot_name)

########################################################################checkimg함수#######################################################

def check_img(image_filenames, target_url):
    count = 0
    timePre = time.time()
    timeElapsedPre = 0
    retry_count = 0
    max_retries = 3
    found_page = False

    while count < 1 and retry_count < max_retries:
        timeElapsed = int(time.time() - timePre)
        if timeElapsed >= 3:
            print('3초후 자동화 프로그램 실행됩니다  ')
            print(timeElapsed, '초')
            pyautogui.hotkey('win', 'q')
            pyperclip.copy('chrome')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.typewrite(['enter'])
            time.sleep(3)

            isSuccess = True
            for i, fname in enumerate(image_filenames):
                poi = pyautogui.locateCenterOnScreen(fname, confidence=0.8)
                print(fname, poi)
                print('chrome이동 ')
                if poi is not None:
                    pyautogui.click(poi, duration=0.5)
                    time.sleep(3)

                    if i == 1:
                        pyautogui.scroll(-1200)
                        time.sleep(3)
                    if i == 2:
                        time.sleep(5)

                    pyperclip.copy(target_url)
                    pyautogui.hotkey('ctrl', 'v')
                    pyautogui.typewrite(['enter'])
                    print('페이지이동 ')
                    found_page = True  
                    time.sleep(3)
                    break  

            if isSuccess:
                count += 1
                print("실행 완료")
                break
            else:
                retry_count += 1
                print("이미지를 찾지 못했습니다. 재시도:", retry_count)

            pyautogui.hotkey('alt', 'f4')
            print('...')
            timePre = time.time()
        else:
            if timeElapsed != timeElapsedPre:
                print(timeElapsed, '초')
                timeElapsedPre = timeElapsed

    if retry_count == max_retries:
        print("이미지를 찾지 못해 프로그램을 종료합니다.")
        return False
    
    if found_page:
        return True
    else:
        return False





image_filenames = ["google.png", "naver.png"]
image_filenames2=['google.png','daum.png']
image_filenames3=['google.png','neuromeka.png']
target_url = "naver.com"
target_url2='daum.net'
target_url3='neuromeka.com'
############################################################tkinter #######################################################################


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('MECRO')
        self.geometry('450x100')
        # self.protocol("WM_DELETE_WINDOW", self.on_close)  # Execute on_close() when the window is closed

        # style
        button_font = font.Font(family="Times New Roman", size=12, weight="bold")
        button_bg = "#0000FF"  # bg
        button_fg = "#FFFFFF"  # fg
        button_width = 8  # width
        button_height = 2  # height
        resetbtn_bg = '#616161'

        # input_button
        self.input_spinbox = tk.Spinbox(self, from_=0, to=3, font=('Times New Roman', 14), width=5)
        self.input_spinbox.pack(side='left', padx=10, pady=10)

        self.btn1 = tk.Button(self, text='Input',font=button_font, bg=button_bg, fg=button_fg,
                              width=button_width, height=button_height, command=self.btn1_clicked)
        self.btn1.pack(side='left', padx=(0, 10), pady=10)

        # reset_button
        self.reset_btn = tk.Button(self, text='Reset', font=button_font, bg=resetbtn_bg, fg=button_fg,
                                   width=button_width, height=button_height, command=self.resetbtn_clicked)
        self.reset_btn.pack(side='left', padx=(0, 10), pady=10)

        # connection status label
        self.status_label = tk.Label(self, text='Disconnected', font=('Times New Roman', 12), fg='red')
        self.status_label.pack(pady=10)

        self.connected = False
        self.connect_to_robot()

##################################################################버튼생성및 디자인 #################################################################
    def check_img(self, image_filenames, target_url):
        count = 0
        timePre = time.time()
        timeElapsedPre = 0
        retry_count = 0
        max_retries = 3
        found_page = False

        while count < 1 and retry_count < max_retries:
            timeElapsed = int(time.time() - timePre)
            if timeElapsed >= 3:
                print(timeElapsed, '초')
                pyautogui.hotkey('win', 'q')
                pyperclip.copy('chrome')
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.typewrite(['enter'])
                time.sleep(3)

                isSuccess = True
                for i, fname in enumerate(image_filenames):
                    poi = pyautogui.locateCenterOnScreen(fname, confidence=0.8)
                    print(fname, poi)
                    print('chrome이동 ')
                    if poi is not None:
                        pyautogui.click(poi, duration=0.5)
                        time.sleep(3)

                        if i == 1:
                            pyautogui.scroll(-1200)
                            time.sleep(3)
                        if i == 2:
                            time.sleep(5)

                        pyperclip.copy(target_url)
                        pyautogui.hotkey('ctrl', 'v')
                        pyautogui.typewrite(['enter'])
                        print('페이지이동 ')
                        found_page = True  
                        time.sleep(3)
                        break  

                if isSuccess:
                    count += 1
                    print("실행 완료")
                    break
                else:
                    retry_count += 1
                    print("이미지를 찾지 못했습니다. 재시도:", retry_count)

                pyautogui.hotkey('alt', 'f4')
                print('...')
                timePre = time.time()
            else:
                if timeElapsed != timeElapsedPre:
                    print(timeElapsed, '초')
                    timeElapsedPre = timeElapsed

        if retry_count == max_retries:
            print("이미지를 찾지 못해 프로그램을 종료합니다.")
            return False

        if found_page:
            return True
        else:
            return False




    image_filenames = ["google.png", "naver.png"]
    image_filenames2=['google.png','daum.png']
    image_filenames3=['google.png','neuromeka.png']
    target_url = "naver.com"
    target_url2='daum.net'
    target_url3='neuromeka.com'
##################################################################로봇 커넥트 확인 ##################################################################
    def connect_to_robot(self):
        try:
            if not self.connected:
                indy.connect()
                self.connected = True
                self.status_label.config(text='● Connected', fg='green')
                
        except Exception as e:
            self.connected = False
            self.status_label.config(text='○ Disconnected', fg='red')
            print('Connection failed:', str(e))

    def on_close(self):
        indy.disconnect()  
        self.destroy()
        print('-------FINISH--------')
##############################################################콘티연동 매크로 [main]#########################################################
    def btn1_clicked(self):  # input
        try:
            number = int(self.input_spinbox.get())
            indy.write_direct_variable(0, 100, number)
            data = indy.read_direct_variable(0, 100)
            print('입력한 숫자:', data)

            try:
                val = indy.read_direct_variable(0, 500)

                if val == 1:
                    self.check_img(image_filenames, target_url)
                    self.input_spinbox.delete(0, tk.END)
                    self.input_spinbox.insert(tk.END, "0")
                    print('B500end:', val)
                elif val == 2:
                    self.check_img(image_filenames2, target_url2)
                    self.input_spinbox.delete(0, tk.END)
                    self.input_spinbox.insert(tk.END, "0")
                    print('B500end', val)
                elif val == 3:
                    self.check_img(image_filenames3, target_url3)
                    self.input_spinbox.delete(0, tk.END)
                    self.input_spinbox.insert(tk.END, "0")
                    print('B500end', val)
                else:
                    print('B500miss:')
                    messagebox.showinfo("Error", "B500miss occurred. Please try again.")
                    return

                return indy.read_direct_variable(0, 500)

            finally:
                time.sleep(0.05)
                indy.write_direct_variable(0, 100, 0)
                wait = indy.read_direct_variable(0, 100)
                print('waitfor:', wait)
                time.sleep(0.05)
                mec = indy.read_direct_variable(0, 500)
                print('B500check', mec)

        except ValueError:
            print('올바른 숫자를 입력하세요.')

    def resetbtn_clicked(self):
        self.input_spinbox.delete(0, tk.END)
        self.input_spinbox.insert(tk.END, "0")
        indy.write_direct_variable(0, 100, 0)


if __name__ == '__main__':
    app = App()
    app.mainloop()
