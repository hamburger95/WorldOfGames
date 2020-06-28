from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


site_url = "http://127.0.0.1:5000/"

driver = webdriver.Chrome(ChromeDriverManager().install())


def test_scores_service(app_url):
    try:
        driver.get(site_url)
        s_check = int(driver.find_element_by_id("score").text)
    except type:
        print("test failed")
    #finally:
        # browser switch
        #time.sleep(10)
        #driver.close()

    return (s_check >= 1 and s_check <= 1000)


def main_function():
    flag = test_scores_service(site_url)
    print(flag)
    assert flag


main_function()
