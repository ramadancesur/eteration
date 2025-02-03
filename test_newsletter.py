from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from faker import Faker
import time

def test_newsletter_subscription():
    # Initialize Faker for generating test email
    fake = Faker()
    
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    
    # Setup Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        # Navigate to the homepage
        print("Navigating to the homepage...")
        driver.get("https://academy.eteration.com/")
        
        # Wait for page to load and scroll to bottom
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        
        # Try different selectors for the newsletter form
        selectors = [
            "input[placeholder*='mail']",
            "input[name*='mail']",
            "input[class*='newsletter']",
            "form input[type='email']"
        ]
        
        email_input = None
        for selector in selectors:
            try:
                print(f"Trying to find email input with selector: {selector}")
                email_input = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                )
                if email_input:
                    print(f"Found email input with selector: {selector}")
                    break
            except Exception:
                continue
        
        if not email_input:
            raise Exception("Could not find newsletter email input field")
        
        # Generate a test email
        test_email = fake.email()
        print(f"Using test email: {test_email}")
        
        # Enter the email
        email_input.clear()
        email_input.send_keys(test_email)
        time.sleep(1)
        email_input.send_keys(Keys.RETURN)
        
        print("Submitted newsletter form")
        
        # Wait a moment to see if there's any response
        time.sleep(3)
        
        print("Newsletter subscription test completed!")
        
    except Exception as e:
        print(f"Test failed! Error: {str(e)}")
        raise e
        
    finally:
        # Close the browser
        time.sleep(2)  # Small delay to see the results
        driver.quit()

if __name__ == "__main__":
    test_newsletter_subscription()
