import time

from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



@when('open OrangeHRM Home page')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(6)


@when('Enter username "{user}" and password "{pwd}"')
def enterCredentials(context, user, pwd):
    context.driver.find_element(By.XPATH, "//input[@name='username']").clear()
    context.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(user)
    context.driver.find_element(By.XPATH, "//input[@name='username']").clear()
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(pwd)


@when('Click on login button')
def clickLogin(context):
    context.driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()


@then('User must successfully login to the dashboard page')
def verifyLogin(context):
    time.sleep(5)
    header = context.driver.find_element(By.XPATH, "//h6[contains(@class,'topbar-header-breadcrumb-module')]").text
    assert header == "Dashboard"

