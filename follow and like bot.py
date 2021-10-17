#like and follow bot using selenium 

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time,os


username=input("Enter the insta username : ")
password=input("Enter the password of your insta username : ")
follow=input("Enter the username of target account for followers : ")
link=input("Enter the link of post u wanna get likes on : ")
option=webdriver.ChromeOptions()
option.headless =True
driver = webdriver.Chrome(ChromeDriverManager().install(),options=option)
url1="https://takipcimx.com/"
url2="https://igfollower.net/girisyap"
url3="https://freefollowerx.com/login"
url4="https://instahilecin.com/login"
url5="https://takipcikutusu.com/member"
url6="https://gramtakipci.com/girisyap"
url7="https://begeni.vip/girisyap"
url8="https://fastfollow.in/member"

c=1


# first follow sender
driver.get(url1)
sign_in=driver.find_element_by_id("loginAsUser")
sign_in.click()
time.sleep(2)
user_in=driver.find_element_by_id("username")
user_in.send_keys(username)
password_in=driver.find_element_by_xpath("//span[@id='react-root']/section/main/article/div/div/div[3]/form/div[2]/input")
password_in.send_keys(password)
login=driver.find_element_by_id("login_insta")
login.click()
while(1):
    time.sleep(2)
    check=driver.current_url
    checker="https://takipcimx.com/tools"
    if(check==checker):
        driver.get("https://takipcimx.com/tools/send-follower")
        follow_send=driver.find_element_by_name("username")
        follow_send.send_keys(follow)
        search=driver.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/form/button")
        search.click()
        no_follow=driver.find_element_by_name("adet")
        no_follow.send_keys("0")
        send=driver.find_element_by_id("formTakipSubmitButton")
        send.click()
        time.sleep(10)





        # first like sender
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[c])
        driver.get("https://takipcimx.com/tools/send-like")
        like_send=driver.find_element_by_name("mediaUrl")
        like_send.send_keys(link)
        search=driver.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/form/button")
        search.click()
        text="Sorry! The page you are looking for can not be found. It may be removed, deleted."
        n=1
        while(n<2):
            if text in driver.page_source:
                driver.get("https://takipcimx.com/tools/send-like")
                like_send=driver.find_element_by_name("mediaUrl")
                like_send.send_keys(link)
                search=driver.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/form/button")
                search.click()
            else:        
                no_follow=driver.find_element_by_name("adet")
                no_follow.send_keys("00")
                send=driver.find_element_by_id("formBegeniSubmitButton")
                send.click()
                time.sleep(10)
            n=n+1
        c=c+1
        break








#second follow sender
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[c])
driver.get(url2)
sign_in2=driver.find_element_by_id("username")
sign_in2.send_keys(username)
password_in2=driver.find_element_by_name("password")
password_in2.send_keys(password)
driver.find_element_by_id("login_insta").click()
c=c+1
while(1):
    time.sleep(2)
    check=driver.current_url
    checker="https://igfollower.net/tools/send-follower"
    if(check==checker):
        follow_send2=driver.find_element_by_xpath("html/body/section/div/div/div[2]/div/div[2]/div[3]/form/div/input")
        follow_send2.send_keys(follow)
        search2=driver.find_element_by_xpath("html/body/section/div/div/div[2]/div/div[2]/div[3]/form/center/button")
        search2.click()
        no_follow2=driver.find_element_by_name("adet")
        no_follow2.send_keys("00")
        send2=driver.find_element_by_id("formTakipSubmitButton")
        send2.click()
        time.sleep(10)





        #second like sender
        
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[c])
        driver.get("https://igfollower.net/tools/send-like")
        like_send=driver.find_element_by_name("mediaUrl")
        like_send.send_keys(link)
        search=driver.find_element_by_xpath("html/body/section/div/div/div[2]/div/div[2]/div[3]/form/center/button")
        search.click()
        text="Sorry! The page you are looking for can not be found. It may be removed, deleted."
        n=1
        while(n<2):
            if text in driver.page_source:
                driver.get("https://igfollower.net/tools/send-like")
                like_send=driver.find_element_by_name("mediaUrl")
                like_send.send_keys(link)
                search=driver.find_element_by_xpath("html/body/section/div/div/div[2]/div/div[2]/div[3]/form/center/button")
                search.click()
            else:
                no_follow=driver.find_element_by_name("adet")
                no_follow.send_keys("00")
                send=driver.find_element_by_id("formBegeniSubmitButton")
                send.click()
                time.sleep(15)
            n=n+1
        c=c+1
        break


# #third follow sender
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[c])
driver.get(url3)
sign_in3=driver.find_element_by_id("username")
sign_in3.send_keys(username)
password_in3=driver.find_element_by_name("password")
password_in3.send_keys(password)
driver.find_element_by_id("login_insta").click()
c=c+1
while(1):
    time.sleep(2)
    check=driver.current_url
    checker="https://freefollowerx.com/tools"
    if(check==checker):
        driver.get("https://freefollowerx.com/tools/send-follower")
        follow_send3=driver.find_element_by_name("username")
        follow_send3.send_keys(follow)
        search3=driver.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/form/button")
        search3.click()
        no_follow3=driver.find_element_by_name("adet")
        no_follow3.send_keys("00")
        send3=driver.find_element_by_id("formTakipSubmitButton")
        send3.click()
        time.sleep(10)





        #third like sender
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[c])
        driver.get("https://freefollowerx.com/tools/send-like")
        like_send=driver.find_element_by_name("mediaUrl")
        like_send.send_keys(link)
        search=driver.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/form/button")
        search.click()
        text="Sorry! The page you are looking for can not be found. It may be removed, deleted."
        n=1
        while(n<2):
            if text in driver.page_source:
                driver.get("https://freefollowerx.com/tools/send-like")
                like_send=driver.find_element_by_name("mediaUrl")
                like_send.send_keys(link)
                search=driver.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/form/button")
                search.click()
            else:
                no_follow=driver.find_element_by_name("adet")
                no_follow.send_keys("00")
                send=driver.find_element_by_id("formBegeniSubmitButton")
                send.click()
                time.sleep(15)
            n=n+1
        c=c+1
        break



# #forth follow sender
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[c])
driver.get(url4)
sign_in4=driver.find_element_by_id("username")
sign_in4.send_keys(username)
password_in4=driver.find_element_by_name("password")
password_in4.send_keys(password)
driver.find_element_by_id("login_insta").click()
c=c+1
while(1):
    time.sleep(2)
    check=driver.current_url
    checker="https://instahilecin.com/tools"
    if(check==checker):
        driver.get("https://instahilecin.com/tools/send-follower")
        follow_send4=driver.find_element_by_name("username")
        follow_send4.send_keys(follow)
        search4=driver.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/form/button")
        search4.click()
        no_follow4=driver.find_element_by_name("adet")
        no_follow4.send_keys("00")
        send4=driver.find_element_by_id("formTakipSubmitButton")
        send4.click()
        time.sleep(10)


        #forth like sender
        driver.execute_script("window.open('');")   
        driver.switch_to.window(driver.window_handles[c])   
        driver.get("https://instahilecin.com/tools/send-like")
        like_send=driver.find_element_by_name("mediaUrl")
        like_send.send_keys(link)
        search=driver.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/form/button")
        search.click()
        text="Sorry! The page you are looking for can not be found. It may be removed, deleted."
        n=1
        while(n<2):
            if text in driver.page_source:
                driver.get("https://instahilecin.com/tools/send-like")
                like_send=driver.find_element_by_name("mediaUrl")
                like_send.send_keys(link)
                search=driver.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/form/button")
                search.click()
            else:
                no_follow=driver.find_element_by_name("adet")
                no_follow.send_keys("00")
                send=driver.find_element_by_id("formBegeniSubmitButton")
                send.click()
                time.sleep(15)
            n=n+1
        c=c+1
        break





# #fifth follow sender
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[c])
driver.get(url5)
sign_in5=driver.find_element_by_id("username")
sign_in5.send_keys(username)
time.sleep(5)
password_in5=driver.find_element_by_name("password")
password_in5.send_keys(password)
driver.find_element_by_id("login_insta").click()
c=c+1
while(1):
    time.sleep(2)
    check=driver.current_url
    checker="https://takipcikutusu.com/tools"
    if(check==checker):
        driver.get("https://takipcikutusu.com/tools/send-follower")
        follow_send5=driver.find_element_by_name("username")
        follow_send5.send_keys(follow)
        search5=driver.find_element_by_xpath("html/body/div[3]/div[2]/div/div[3]/div[2]/form/button")
        search5.click()
        no_follow5=driver.find_element_by_name("adet")
        no_follow5.send_keys("00")
        send5=driver.find_element_by_id("formTakipSubmitButton")
        send5.click()
        time.sleep(10)



        # fifth like sender
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[c])
        driver.get("https://takipcikutusu.com/tools/send-like")
        like_send=driver.find_element_by_name("mediaUrl")
        like_send.send_keys(link)
        search=driver.find_element_by_xpath("html/body/div[3]/div[2]/div/div/div[2]/form/button")
        search.click()
        text="Sorry! The page you are looking for can not be found. It may be removed, deleted."
        n=1
        while(n<2):
            if text in driver.page_source:
                driver.get("https://takipcikutusu.com/tools/send-like")
                like_send=driver.find_element_by_name("mediaUrl")
                like_send.send_keys(link)
                search=driver.find_element_by_xpath("html/body/div[3]/div[2]/div/div/div[2]/form/button")
                search.click()
            else:
                no_follow=driver.find_element_by_name("adet")
                no_follow.send_keys("00")
                send=driver.find_element_by_id("formBegeniSubmitButton")
                send.click()
                time.sleep(15)
            n=n+1
        c=c+1
        break



# #sixth follow sender
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[c])
driver.get(url6)
time.sleep(5)
sign_in6=driver.find_element_by_xpath("html/body/span/section/main/article/div/div/div/form/div/input")
sign_in6.send_keys(username)
password_in6=driver.find_element_by_name("password")
password_in6.send_keys(password)
driver.find_element_by_id("login_insta").click()
c=c+1
while(1):
    time.sleep(2)
    check=driver.current_url
    checker="https://gramtakipci.com/packages"
    if(check==checker):
        driver.get("https://gramtakipci.com/tools/send-follower")
        follow_send5=driver.find_element_by_name("username")
        follow_send5.send_keys(follow)
        search5=driver.find_element_by_css_selector("center button.btn.btn-grs[type='submit']")
        search5.click()
        time.sleep(5)
        no_follow5=driver.find_element_by_name("adet")
        no_follow5.send_keys("100")
        send5=driver.find_element_by_id("formTakipSubmitButton")
        send5.click()
        time.sleep(10)




        #sixth like sender
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[c])
        driver.get("https://gramtakipci.com/tools/send-like")
        like_send=driver.find_element_by_name("mediaUrl")
        like_send.send_keys(link)
        search=driver.find_element_by_css_selector("center button.btn.btn-grs[type='submit']")
        search.click()
        text="Sorry! The page you are looking for can not be found. It may be removed, deleted."
        n=1
        while(n<2):
            if text in driver.page_source:
                driver.get("https://gramtakipci.com/tools/send-like")
                like_send=driver.find_element_by_name("mediaUrl")
                like_send.send_keys(link)
                time.sleep(2)
                search=driver.find_element_by_css_selector("center button.btn.btn-grs[type='submit']")
                search.click()
            else:
                no_follow=driver.find_element_by_name("adet")
                no_follow.send_keys("00")
                send=driver.find_element_by_id("formBegeniSubmitButton")
                send.click()
                time.sleep(15)
            n=n+1
        c=c+1
        break




#seventh follow sender
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[c])
driver.get(url7)
time.sleep(5)
sign_in6=driver.find_element_by_xpath("html/body/span/section/main/article/div/div/div/form/div/input")
sign_in6.send_keys(username)
password_in6=driver.find_element_by_name("password")
password_in6.send_keys(password)
driver.find_element_by_id("login_insta").click()
c=c+1
while(1):
    time.sleep(2)
    check=driver.current_url
    checker="https://begeni.vip/tools/send-follower"
    if(check==checker):
        follow_send5=driver.find_element_by_name("username")
        follow_send5.send_keys(follow)
        search5=driver.find_element_by_xpath("html/body/section/div/div/div[2]/div/div[3]/div[3]/form/center/button")
        search5.click()
        no_follow5=driver.find_element_by_name("adet")
        no_follow5.send_keys("00")
        send5=driver.find_element_by_id("formTakipSubmitButton")
        send5.click()
        time.sleep(10)



        #seventh like sender
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[c])
        driver.get("https://begeni.vip/tools/send-like")
        like_send=driver.find_element_by_name("mediaUrl")
        like_send.send_keys(link)
        search=driver.find_element_by_xpath("html/body/section/div/div/div[2]/div/div[2]/div[3]/form/center/button")
        search.click()
        text="Sorry! The page you are looking for can not be found. It may be removed, deleted."
        n=1
        while(n<2):
            if text in driver.page_source:
                driver.get("https://begeni.vip/tools/send-like")
                like_send=driver.find_element_by_name("mediaUrl")
                like_send.send_keys(link)
                search=driver.find_element_by_xpath("html/body/section/div/div/div[2]/div/div[2]/div[3]/form/center/button")
                search.click()
            else:
                no_follow=driver.find_element_by_name("adet")
                no_follow.send_keys("00")
                send=driver.find_element_by_id("formBegeniSubmitButton")
                send.click()
                time.sleep(15)
            n=n+1
        c=c+1
        break




#eightth follow sender
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[c])
driver.get(url8)
time.sleep(5)
sign_in6=driver.find_element_by_id("username")
sign_in6.send_keys(username)
password_in6=driver.find_element_by_name("password")
password_in6.send_keys(password)
driver.find_element_by_id("login_insta").click()
c=c+1
while(1):
    time.sleep(2)
    check=driver.current_url
    checker="https://fastfollow.in/tools"
    if(check==checker):
        driver.get("https://fastfollow.in/tools/send-follower")
        follow_send5=driver.find_element_by_name("username")
        follow_send5.send_keys(follow)
        search5=driver.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/form/button")
        search5.click()
        no_follow5=driver.find_element_by_name("adet")
        no_follow5.send_keys("00")
        send5=driver.find_element_by_id("formTakipSubmitButton")
        send5.click()
        time.sleep(10)


        #eightth like sender
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[c])
        driver.get("https://fastfollow.in/tools/send-like")
        like_send=driver.find_element_by_name("mediaUrl")
        like_send.send_keys(link)
        search=driver.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/form/button")
        search.click()
        text="Sorry! The page you are looking for can not be found. It may be removed, deleted."
        n=1
        while(n<2):
            if text in driver.page_source:
                driver.get("https://fastfollow.in/tools/send-like")
                like_send=driver.find_element_by_name("mediaUrl")
                like_send.send_keys(link)
                search=driver.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/form/button")
                search.click()
            else:
                no_follow=driver.find_element_by_name("adet")
                no_follow.send_keys("00")
                send=driver.find_element_by_id("formBegeniSubmitButton")
                send.click()
                time.sleep(15)
            n=n+1
        c=c+1
        break




