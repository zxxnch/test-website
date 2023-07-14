import pyautogui
import time
import pyperclip
import sys

def check_img(image_filenames, target_url):
    count = 0
    timePre = time.time()
    timeElapsedPre = 0
    retry_count = 0
    max_retries = 3

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
                    time.sleep(3)
                    
                   
                else:
                    isSuccess = False
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

image_filenames = ["google.png", "naver.png"]
target_url = "naver.com"

check_img(image_filenames, target_url)
