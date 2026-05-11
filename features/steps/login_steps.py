from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By

@given('que el usuario está en la página de inicio de sesión')
def step_given_user_on_login_page(context):
    context.driver = webdriver.Chrome()  # o webdriver.Firefox()
    context.driver.get("https://www.saucedemo.com/v1/index.html")
    context.login_page = LoginPage(context.driver)

@when('el usuario inicia sesión con credenciales válidas')
def step_when_user_logs_in_valid(context):
    context.login_page.login("standard_user", "secret_sauce")

@when('el usuario inicia sesión con credenciales inválidas')
def step_when_user_logs_in_invalid(context):
    context.login_page.login("invalid_user", "invalid_password")

@when('el usuario inicia sesión con credenciales vacías')
def step_when_user_logs_in_empty(context):
    context.login_page.login("", "")

@then('el usuario debería ser redirigido a la página de inventario')
def step_then_inventory_page(context):
    inventory_page = InventoryPage(context.driver)
    assert inventory_page.is_inventory_page_displayed()

@then('se debería mostrar un mensaje de error')
def step_then_error_message(context):
    error_message = context.login_page.find_element((By.CSS_SELECTOR, '[data-test="error"]')).text
    assert "Epic sadface" in error_message

def after_scenario(context, scenario):
    context.driver.quit()
