from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


BASE_URL = "https://www.saucedemo.com/"
VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"
TIMEOUT = 10


def create_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    return webdriver.Chrome(options=options)


def wait_for_visible(driver, locator, timeout=TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))


def wait_for_clickable(driver, locator, timeout=TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))


def open_login_page(driver):
    driver.get(BASE_URL)
    wait_for_visible(driver, (By.ID, "user-name"))


def login(driver, username=VALID_USER, password=VALID_PASSWORD):
    open_login_page(driver)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, TIMEOUT).until(EC.url_contains("/inventory.html"))
    wait_for_visible(driver, (By.CLASS_NAME, "inventory_list"))


def get_inventory_title(driver):
    return wait_for_visible(driver, (By.CLASS_NAME, "title")).text


def get_brand_title(driver):
    return wait_for_visible(driver, (By.CLASS_NAME, "app_logo")).text


def get_first_product(driver):
    product = wait_for_visible(driver, (By.CLASS_NAME, "inventory_item"))
    name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
    price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
    return product, name, price


def add_first_product_to_cart(driver):
    product, name, price = get_first_product(driver)
    product.find_element(By.CSS_SELECTOR, "button[id^='add-to-cart']").click()
    wait_for_visible(driver, (By.CLASS_NAME, "shopping_cart_badge"))
    return name, price


def open_cart(driver):
    wait_for_clickable(driver, (By.CLASS_NAME, "shopping_cart_link")).click()
    WebDriverWait(driver, TIMEOUT).until(EC.url_contains("/cart.html"))
    wait_for_visible(driver, (By.CLASS_NAME, "cart_list"))


def save_screenshot(driver, test_name):
    screenshots_dir = Path(__file__).resolve().parents[1] / "screenshots"
    screenshots_dir.mkdir(exist_ok=True)
    file_path = screenshots_dir / f"{test_name}.png"
    driver.save_screenshot(str(file_path))
    return file_path
