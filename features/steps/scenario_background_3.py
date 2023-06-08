import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given('launch browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()


@when('open homepage')
def openHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)


@then('verify that the logo present')
def verifyLogo(context):
    status = context.driver.find_element(By.XPATH,
                                         "//div[contains(@class,'orangehrm-login-layout-blob')]//div[@class='orangehrm-login-logo']").is_displayed()
    assert status is True


@then('close the browser')
def closeBrowser(context):
    context.driver.close()


@when('Enter user "{user}" and password "{pwd}"')
def enterCredentials(context,user,pwd):
    context.driver.find_element(By.XPATH, "//input[@name='username']").clear()
    context.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(user)
    context.driver.find_element(By.XPATH, "//input[@name='username']").clear()
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(pwd)


@when('Click login button')
def clickLoginButton(context):
    context.driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()


@then('User must successfully login to the dashboard')
def LoginTest(context):
    time.sleep(5)
    try:
        header = context.driver.find_element(By.XPATH, "//h6[contains(@class,'topbar-header-breadcrumb-module')]").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if header == "Dashboard":
        context.driver.close()
        assert True, "Test passed"
