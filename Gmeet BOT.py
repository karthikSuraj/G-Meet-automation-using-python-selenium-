import config
from selenium  import  webdriver
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from  config import  USERNAME,PASSWORD,WEEKDAY
import datetime
import time
from datetime import datetime
class automatic:
    def meetOpener():
        now = datetime.now()


        string=now.strftime('%I:%M')
        li = list(string.split(":"))
        hour=int(li[0])
        minute=int(li[1])
        weekday = config.WEEKDAY
        #print(weekday,hour)


        #open google chrome
        #give the path correctly
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        opt=Options()
        opt.add_argument("start-maximized")
        opt.add_argument("--disable-extensions")
        opt.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1
        })


        driver=webdriver.Chrome(chrome_options=opt, executable_path=PATH)


        #open Google Clssroom

        driver.get('https://accounts.google.com/ServiceLogin/signinchooser?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2F&followup=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        #login
        username_input=driver.find_element_by_css_selector('input[type="email"]')
        username_input.send_keys(config.USERNAME)
        time.sleep(4)
        username_input.send_keys(Keys.RETURN)
        time.sleep(3)
        password_input=driver.find_element_by_css_selector('input[type="password"]')
        password_input.send_keys(config.PASSWORD)
        time.sleep(3)
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)

        #all classrooms
        # give the URLS of all Meet Links
        class_link1='NA'
        class_link2 = 'NA'
        #......... all the links


        #to open class 1 on apurticular day....
        # weekday 1= monday
        # weekday 2= tuesday
        # weekday 3= wednesday
        # weekday 4= thurday
        # weekday 5= frinday
        # weekday 6= satday
        # weekday 7= sunday

        #write the if statement by looking at your time table
        #you need to have multiple if statements
        #each if statement for ecah class
        # it is a 12 hours clock

     #ex class one is on monday 10 am to 11 am and tuesday 2pm to 4pm and wednesday 2pm tp 3pm
        if ((weekday==1 and  hour>=10 and hour<=11) or  (weekday==2 and hour>=2 and hour<=4) or  (weekday==3 and hour>=2 and hour<=3)) :
            #class1
            driver.get(class_link1)






        time.sleep(5)


        #Turns off mic and camera and joins the meet
        camera=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div')

        camera.click()
        time.sleep(5)

        mic=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div')

        mic.click()
        time.sleep(5)

        join=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span')
        join.click()

        time.sleep(20)

        msg=driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[2]/div/div/div[3]/span/button/i[1]')

        msg.click()
        time.sleep(10)

        attendence=driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div[2]/div[2]/div/div[4]/div[1]/div[1]/div[2]/textarea')

        attendence.send_keys(config.ATTENDENCE)
        # enter in after how many minutes (you join the meet ) you want to upload your attendence
        time.sleep(2)
        attendence.send_keys(Keys.RETURN)

        leave = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[7]/span/button')
        # enter in after how many minutes (you join the meet ) you want to leave
        time.sleep(60*30)
        leave.click()

automatic.meetOpener()





