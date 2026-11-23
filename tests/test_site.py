
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    options.binary_location = "/usr/bin/chromium"

    driver = webdriver.Chrome(
        service=Service("/usr/bin/chromedriver"),
        options=options
    )

    driver.get(os.getenv("BASE_URL", "http://web"))
    yield driver
    driver.quit()


def test_page_title(browser):
    assert browser.title == "Wrong-Title"


def test_heading(browser):
    heading = browser.find_element(By.TAG_NAME, "h1")
    assert heading.text == "Welcome to My CI/CD Project"


def test_button_click(browser):
    browser.find_element(By.ID, "submitBtn").click()
    assert browser.find_element(By.ID, "output").text == ""


def test_textbox_input(browser):
    textbox = browser.find_element(By.ID, "userInput")
    textbox.send_keys("Hello Selenium")

    browser.find_element(By.ID, "submitBtn").click()

    output = browser.find_element(By.ID, "output")
    assert output.text == "Hello Selenium"
