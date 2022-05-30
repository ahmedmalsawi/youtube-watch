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
    "https://www.youtube.com/watch?v=I9yKxkaPTvA&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=198",
    "https://www.youtube.com/watch?v=191Qt-oiLY8&list=PLJ3ijxVwAC9xo8Q6eYba-5TLiRJoRJHlC&index=112"

]
small_videos = [
    "https://youtube.com/shorts/YtGE86Znp_o",
    "https://youtube.com/shorts/eki3hrD71TE",
    "https://youtube.com/shorts/su5gt1rLYPw"

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

for i in range(200):
    print(addtime, " => running the video from first list for {} time".format(i + 1))
    random_video = random.randint(1, 2)
    driver.get(videos[random_video])
    print(addtime, " => Now playing: {}".format(videos[random_video]))
    # duration = driver.find_elements_by_xpath("//span[@class='ytp-time-duration']")[0].text
    # duration = driver.find_elements(by=By.XPATH, value="//span[@class='ytp-time-duration']"[0]).getText()
    duration = driver.find_element(By.XPATH, "//span[@class='ytp-time-duration']").text

    x = time.strptime(duration, '%M:%S')
    video_length = datetime.timedelta(
        minutes=x.tm_min, seconds=x.tm_sec).total_seconds()
    deduction = random.randint(5, 15)
    print(addtime, " => Video Original length is {}".format(video_length))
    new_video_length = (video_length - ((video_length / 100) * deduction))
    print(addtime, " => Video Playing length is {}".format(new_video_length))

    sleep_time = new_video_length
    print(addtime, " => Play Time is: {}".format(sleep_time))
    time.sleep(sleep_time)


driver.quit()
