import pytest
from threading import Thread
from app import create_app
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


app = create_app()

def pause(seconds=2):
    time.sleep(seconds)


# Start the Flask app in a separate thread
@pytest.fixture(scope='module')
def test_app():
    app_thread = Thread(target=app.run, kwargs={
        'port': 5000, 'debug': True, 'use_reloader': False})
    app_thread.daemon = True
    app_thread.start()
    pause(2)  # Allow time for the server to start.
    yield
    # Teardown to stop the Flask app thread.
    # app_thread.join(timeout=1)

   
# Set up the Selenium WebDriver using Chrome
@pytest.fixture(scope='module')
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )    

    yield driver
    driver.quit()

# function to test if the page loads
def test_page_loads(driver, test_app):
    # Navigate to your Flask app
    driver.get("http://127.0.0.1:5000/")
    pause(2)

    # Wait for the element to be visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))

    # Verify the title contains the search term
    assert "Recipe Finder" in driver.title
    assert driver.find_element(By.TAG_NAME, "h1").text == "Recipe Finder"

def test_page_search(driver, test_app):
    driver.get("http://127.0.0.1:5000/")
    pause(2)

    # enter ingredients and click button to search for recipe
    driver.find_element(By.ID, 'ingredients').send_keys('chicken')
    driver.find_element(By.ID, 'recipeFindBtn').click()
    pause(2)

    # Wait for the element to be visible
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'recipeImage1')))
    pause(2)

    # Click on the first recipe image
    driver.find_element(By.ID, 'recipeImage1').click()
    pause(2)

    # Check if the popup is displayed with flex
    popup = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'popup'))
    )
    assert popup.value_of_css_property('display') == 'flex'
    pause(2)