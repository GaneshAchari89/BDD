import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager




@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()


@when('open orangeHRM homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)


@then('verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element(By.XPATH,
                                         "//div[contains(@class,'orangehrm-login-layout-blob')]//div[@class='orangehrm-login-logo']").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()
