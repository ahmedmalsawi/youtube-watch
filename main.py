import random
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

addtime = datetime.datetime.now()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--mute-audio")

videos = [
    "https://www.youtube.com/watch?v=SsYeTrVSRLs&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC",
    "https://www.youtube.com/watch?v=WcUIdmDuVUs&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=4",
    "https://www.youtube.com/watch?v=-JQG9DB1BPM&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=5",
    "https://www.youtube.com/watch?v=y61V_BtYhrk&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=6",
    "https://www.youtube.com/watch?v=ubB1wfObzbI&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=10",
    "https://www.youtube.com/watch?v=I9yKxkaPTvA&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=198",
    "https://www.youtube.com/watch?v=bmpp9v46EUY&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=135",
    "https://www.youtube.com/watch?v=TlUVgC3Qhnk&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=212",
    "https://www.youtube.com/watch?v=jbqPHcHHsyI&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=230",
    "https://www.youtube.com/watch?v=EvpIZQXytmY&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=204",
    "https://www.youtube.com/watch?v=jbqPHcHHsyI&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=231",
    "https://www.youtube.com/watch?v=191Qt-oiLY8&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=112",
    "https://www.youtube.com/watch?v=rXzs8gwxPxA&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=104",
    "https://www.youtube.com/watch?v=1QY0yOWLw9o&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=260",
    "https://www.youtube.com/watch?v=OefrJhNXOMU&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=147",
    "https://www.youtube.com/watch?v=QdYMl_klkPw&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=196",
    "https://www.youtube.com/watch?v=ubB1wfObzbI&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=10",
    "https://www.youtube.com/watch?v=YSBgJnxAPMQ&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=138",
    "https://www.youtube.com/watch?v=v77JF84Oo_Y&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=170",
    "https://www.youtube.com/watch?v=dSf_vdfuQDM&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=208",
    "https://www.youtube.com/watch?v=5pHX1zINQuo&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=105",
    "https://www.youtube.com/watch?v=I78i-ftkpw4&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=268",
    "https://www.youtube.com/watch?v=o0DQ1loIVKw&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=213",
    "https://www.youtube.com/watch?v=U_92wftJ9gI&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=155",
    "https://www.youtube.com/watch?v=gz8JHJ6PR3Y&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=82",
    "https://www.youtube.com/watch?v=1QY0yOWLw9o&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=260",
    "https://www.youtube.com/watch?v=1QY0yOWLw9o&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=260",
    "https://www.youtube.com/watch?v=1QY0yOWLw9o&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=260",
    "https://www.youtube.com/watch?v=VtoKG_J9nDc&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=163",
    "https://www.youtube.com/watch?v=rRLUyTEatno&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=164",
    "https://www.youtube.com/watch?v=3dO6pS_ttJE&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=206",
    "https://www.youtube.com/watch?v=QA3-yqt6fBY&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=165",
    "https://www.youtube.com/watch?v=SfbDyZy2G-Y&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=167",
    "https://www.youtube.com/watch?v=DVsVMAzm1t4&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=168",
    "https://www.youtube.com/watch?v=AriyK2xTrWo&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=169",
    "https://www.youtube.com/watch?v=v77JF84Oo_Y&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=170",
    "https://www.youtube.com/watch?v=jtE6pJU_tuM&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=171",
    "https://www.youtube.com/watch?v=XqptE5fIYlk&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=172",
    "https://www.youtube.com/watch?v=Rb7bJ1hB3Dc&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=173",
    "https://www.youtube.com/watch?v=0oWFbGWWyXQ&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=174",
    "https://www.youtube.com/watch?v=LiLvngINNN4&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=175",
    "https://www.youtube.com/watch?v=ZHjZFsJ2feU&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=181",
    "https://www.youtube.com/watch?v=TOQmGnwNBH0&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=182",
    "https://www.youtube.com/watch?v=D7vFDYWLuOU&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=183",
    "https://www.youtube.com/watch?v=D7vFDYWLuOU&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=183",
    "https://www.youtube.com/watch?v=D7vFDYWLuOU&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=183",
    "https://www.youtube.com/watch?v=i6uwhU4NCmc&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=184",
    "https://www.youtube.com/watch?v=i6uwhU4NCmc&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=184",
    "https://www.youtube.com/watch?v=i6uwhU4NCmc&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=184",
    "https://www.youtube.com/watch?v=i6uwhU4NCmc&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=184",
    "https://www.youtube.com/watch?v=QJl2_vIL5Xk&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=185",
    "https://www.youtube.com/watch?v=QJl2_vIL5Xk&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=185",
    "https://www.youtube.com/watch?v=QJl2_vIL5Xk&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=185",
    "https://www.youtube.com/watch?v=QJl2_vIL5Xk&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=185",
    "https://www.youtube.com/watch?v=hoEbZe79S4E&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=186",
    "https://www.youtube.com/watch?v=TtS7uSpwjHM&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=187",
    "https://www.youtube.com/watch?v=Nh9FjXIwfXU&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=188",
    "https://www.youtube.com/watch?v=8uC_AirGznk&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=189",
    "https://www.youtube.com/watch?v=8uC_AirGznk&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=189",
    "https://www.youtube.com/watch?v=hqPl9HJToxU&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=190",
    "https://www.youtube.com/watch?v=YNIKm6A8G6s&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=191"
]
small_videos = [
    "https://youtube.com/shorts/YtGE86Znp_o",
    "https://youtube.com/shorts/eki3hrD71TE",
    "https://youtube.com/shorts/nsg-LoET1xo",
    "https://youtube.com/shorts/q1l5D1dMlzA",
    "https://youtube.com/shorts/su5gt1rLYPw",
    "https://youtube.com/shorts/GS_BqPblqO4",
    "https://www.youtube.com/watch?v=R8YhqahurDE",
    "https://www.youtube.com/watch?v=HecKqfcHfYM",
    "https://youtube.com/shorts/u_ZlXMweni4",
    "https://youtube.com/shorts/yaaCfTWIDwk",
    "https://youtube.com/shorts/0uBY20n8Dnk"
]

long_videos = [
    "https://www.youtube.com/watch?v=4Ktxo4kwJuI&list=PLJ3ijxVwAC9zDwnU8dhRS8baRSZsRLHfg",
    "https://www.youtube.com/watch?v=kSzX0rkY5_s&list=PLJ3ijxVwAC9zDwnU8dhRS8baRSZsRLHfg&index=2"
]

driver = webdriver.Chrome("C:\\youtube-watch\\chromedriver.exe")
driver.implicitly_wait(0.5)

wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

vpn = "https://chrome.google.com/webstore/detail/ultrasurf-security-privac/mjnbclmflcpookeapghfhapeffmpodij"
driver.get(vpn)
print(addtime, " => running vpn")
time.sleep(5)

# ===================================================================
# ================== activate VPN in browser ==================
# ===================================================================
print(addtime, " => installing vpn")
for i in range(5):  # Presses the tab key 10 times
    pyautogui.press("tab")
pyautogui.press("enter")  # Presses the Enter key once
time.sleep(2)
pyautogui.press("tab")  # Presses the tab key once
pyautogui.press("enter")  # Presses the Enter key once
time.sleep(5)

# ===================================================================
# ================== rinstall loop in browser ==================
# ===================================================================
print(addtime, " => Enable Loop")
loopext = "https://chrome.google.com/webstore/detail/looper-for-youtube/iggpfpnahkgpnindfkdncknoldgnccdg"
driver.get(loopext)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
# ===================================================================
# ================== activate loop in browser ==================
# ===================================================================
print(addtime, " => installing loop")
for i in range(7):  # Presses the tab key 10 times
    pyautogui.press("tab")
pyautogui.press("enter")  # Presses the Enter key once
time.sleep(4)
pyautogui.press("tab")  # Presses the tab key once
pyautogui.press("enter")  # Presses the Enter key once
time.sleep(5)
# ===================================================================
# ================== change loop options in browser ==================
# ===================================================================
print(addtime, " => Setting Loop Options")
loopextoption = "chrome-extension://iggpfpnahkgpnindfkdncknoldgnccdg/options.html"
driver.get(loopextoption)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)

for i in range(3):  # Presses the tab key 6 times
    pyautogui.press("tab")
for i in range(2):  # Presses the tab key 6 times
    pyautogui.press("down")
time.sleep(2)
for i in range(4):  # Presses the tab key 6 times
    pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("end")
pyautogui.press("enter")
time.sleep(5)

driver.switch_to.window(driver.window_handles[0])
print(addtime, " => playing starting video")
driver.get("https://www.youtube.com/watch?v=QJl2_vIL5Xk&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=185")
time.sleep(4)
# driver.switch_to.window(driver.window_handles[0])
print(addtime, " => switching to youtube tab")
m = driver.find_element(By.CSS_SELECTOR, ".ytp-mute-button")
m.click()
time.sleep(2)
print(addtime, " => Enable Loop")
pyautogui.press("p")  # Presses the Enter key once

# loop = driver.find_element(By.CSS_SELECTOR, ".ytd-toggle-button-renderer")
# loop.click()

time.sleep(4)
print(addtime, " => Closing Vpn tab")
if driver.window_handles[1]:
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
driver.switch_to.window(driver.window_handles[0])

for i in range(10):
    for i in range(10):
        print(addtime, " => running the video from first list for {} time".format(i + 1))
        random_video = random.randint(1, 60)
        driver.get(videos[random_video])
        print(addtime, " => Now playing: {}".format(videos[random_video]))
        duration = driver.find_element(
            By.XPATH, "//span[@class='ytp-time-duration']").text
        x = time.strptime(duration, '%M:%S')
        video_length = datetime.timedelta(
            minutes=x.tm_min, seconds=x.tm_sec).total_seconds()
        deduction = random.randint(5, 15)
        print(addtime, " => Video Original length is {}".format(video_length))
        new_video_length = (video_length - ((video_length / 100) * deduction))
        print(addtime, " => Video Playing length is {}".format(new_video_length))
        sleep_time = new_video_length
        time.sleep(sleep_time)
    time.sleep(5)
    # play small videos list
    for i in range(5):
        print(addtime, " => running the video from second list for {} time".format(i + 1))
        small_random_video = random.randint(1, 10)
        driver.get(small_videos[small_random_video])
        print(addtime, " => Now playing: {}".format(
            small_videos[small_random_video]))
        duration = driver.find_element(
            By.XPATH, "//span[@class='ytp-time-duration']").text
        x = time.strptime(duration, '%M:%S')
        video_length = datetime.timedelta(
            minutes=x.tm_min, seconds=x.tm_sec).total_seconds()
        deduction = random.randint(5, 15)
        print(addtime, " => Video Original length is {}".format(video_length))
        new_video_length = (video_length - ((video_length / 100) * deduction))
        print(addtime, " => Video Playing length is {}".format(new_video_length))
        small_sleep_time = new_video_length
        time.sleep(small_sleep_time)

    time.sleep(5)
    # play long videos list
    for i in range(1):
        print(addtime, " => running the video from Third list for {} time".format(i + 1))
        long_random_video = random.randint(0, 1)
        print(addtime, " => Now playing: {}".format(
            long_videos[long_random_video]))
        driver.get(long_videos[long_random_video])
        duration = driver.find_element(
            By.XPATH, "//span[@class='ytp-time-duration']").text
        x = time.strptime(duration, '%M:%S')
        video_length = datetime.timedelta(
            minutes=x.tm_min, seconds=x.tm_sec).total_seconds()
        deduction = random.randint(5, 10)
        print(addtime, " => Video Original length is {}".format(video_length))
        new_video_length = (video_length - ((video_length / 100) * deduction))
        print(addtime, " => Video Playing length is {}".format(new_video_length))
        long_sleep_time = new_video_length
        time.sleep(long_sleep_time)
    print(addtime, " => All Videos have been played as ordered")
driver.quit()
