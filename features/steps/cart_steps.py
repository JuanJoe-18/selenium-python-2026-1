from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import time

@given("que he iniciado sesión en la página de inventario")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(context.driver)
    login_page.login("standard_user", "secret_sauce")
    context.inventory_page = InventoryPage(context.driver)

@when('agrego el producto "{product_name}" al carrito')
def step_impl(context, product_name):
    context.inventory_page.add_product_to_cart(product_name)

@then("debería ver 1 artículo en el carrito")
def step_impl(context):
    time.sleep(1)
    cart_count = context.inventory_page.get_cart_count()
    assert cart_count == "1"
    context.driver.quit()
