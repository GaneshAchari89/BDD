import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given(u'Browser launch')
def openBrowser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()


@when(u'Opening Home page of OrangeHRM')
def homePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

@when(u'Mention username "{user}" and password "{pwd}"')
def credentials(context,user,pwd):
    context.driver.find_element(By.XPATH, "//input[@name='username']").clear()
    context.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(user)
    context.driver.find_element(By.XPATH, "//input[@name='username']").clear()
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(pwd)


@when(u'Clicking login button')
def clickingLogin(context):
    context.driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()


@then(u'User successful login')
def step_impl(context):
    time.sleep(5)
    try:
        header = context.driver.find_element(By.XPATH, "//h6[contains(@class,'topbar-header-breadcrumb-module')]").text
    except:
        context.driver.close()
        assert False, "Test Failed"

    if header == "Dashboard":
        context.driver.close()
        assert True, "Test passed"


