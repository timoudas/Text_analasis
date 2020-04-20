import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



def get_report():
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory": "/Users/andreas/Desktop/Python/Portfolio/IMF_Publications/"}
    chromeOptions.add_experimental_option("prefs", prefs)
    chromedriver = "/Users/andreas/.wdm/chromedriver/75.0.3770.8/mac64/chromedriver"
    driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)

    # driver = webdriver.Chrome(ChromeDriverManager().install())  # Optional argument, if not specified will search path.
    driver.get('https://www.imf.org/en/publications')  # GET the link
    time.sleep(1)  # Let the user actually see something!
    try:
        publications = driver.find_element_by_xpath("//div[@class='homebelt']/div/a")  # Find the publications link
        time.sleep(1)  # Let the user actually see something!
        publications.click()  # Clicks the link
        time.sleep(1)  # Let the user actually see something!
    except:
        print('not found')
        driver.quit()

    try:
        report = [link.get_attribute('href') for link in
                  driver.find_elements_by_xpath("//div[@class='result-row pub-row']/h6/a")]
        print(report)
        time.sleep(1)  # Let the user actually see something!
    except:
        print('Not Found reports')
        driver.quit()

    print('Trying to get reports')
    for link in report:
        driver.get(link)
        time.sleep(5)
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present(),
                                           'Timed out waiting for PA creation ' +
                                           'confirmation popup to appear.')

            alert = browser.switch_to.alert
            alert.dismiss()
            print("alert accepted")
        except TimeoutException:
            print("no alert")
        try:
            # Switch the control to the Alert window
            driver.find_element_by_xpath("//a[@class='pdf']").click()
            driver.find_element_by_xpath("//a[@class='Full Text']").click()
            time.sleep(5)
        except Exception as e:
            print(e)

        time.sleep(5)
    driver.quit()

get_report()