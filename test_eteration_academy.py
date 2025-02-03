from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker
import time
import unittest

class TestEterationAcademy(unittest.TestCase):
    def setUp(self):
        """Set up test environment before each test"""
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.fake = Faker()

    def tearDown(self):
        """Clean up after each test"""
        if self.driver:
            self.driver.quit()

    def test_01_instructor_count(self):
        """Test to verify instructors are present on the instructors page"""
        try:
            # Navigate to the instructors page
            print("\nTest 1: Checking instructor count...")
            print("Navigating to the instructors page...")
            self.driver.get("https://academy.eteration.com/instructors")
            
            time.sleep(3)  # Wait for page load
            
            # Try different selectors to find instructors
            selectors = [
                "div.instructor-list div.instructor-item",
                "div[class*='instructor-list'] div[class*='instructor-item']",
                "div.instructor-item",
                "div[class*='instructor']"
            ]
            
            instructors = None
            for selector in selectors:
                try:
                    instructors = WebDriverWait(self.driver, 3).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
                    )
                    if instructors:
                        print(f"Found {len(instructors)} instructors using selector: {selector}")
                        break
                except:
                    continue
            
            if not instructors:
                raise Exception("Could not find any instructors")
            
            instructor_count = len(instructors)
            
            # Print instructor details if available
            try:
                for i, instructor in enumerate(instructors, 1):
                    name = instructor.find_element(By.CSS_SELECTOR, "h3").text
                    print(f"Instructor {i}: {name}")
            except Exception as e:
                print(f"Could not get instructor details: {str(e)}")
            
            self.assertTrue(instructor_count > 0, "Instructor list is empty!")
            print(f"\nFound {instructor_count} instructors.")
            print("Instructor count test completed successfully!")
            
        except Exception as e:
            print(f"Instructor test failed! Error: {str(e)}")
            raise e

    def test_02_newsletter_subscription(self):
        """Test to subscribe to the newsletter on homepage"""
        try:
            # Step 1: Navigate to homepage
            print("\nTest 2: Testing newsletter subscription...")
            print("Step 1: Navigating to homepage...")
            self.driver.get("https://academy.eteration.com/")
            
            # Step 2: Wait and scroll to footer
            print("Step 2: Scrolling to footer...")
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            
            # Step 3: Find newsletter input
            print("Step 3: Finding newsletter input...")
            selectors = [
                "input[name='email']",
                "input[type='email']",
                "input[placeholder*='mail']",
                "input[name*='mail']"
            ]
            
            email_input = None
            for selector in selectors:
                try:
                    email_input = WebDriverWait(self.driver, 3).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    if email_input:
                        print(f"Found input with selector: {selector}")
                        break
                except:
                    continue
            
            if not email_input:
                raise Exception("Could not find newsletter email input")
            
            # Ensure element is visible and clickable
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", email_input)
            time.sleep(1)
            
            # Focus and click
            self.driver.execute_script("arguments[0].focus();", email_input)
            self.driver.execute_script("arguments[0].click();", email_input)
            
            # Step 4: Enter test email
            print("Step 4: Entering test email...")
            test_email = self.fake.email()
            email_input.send_keys(test_email)
            time.sleep(1)
            
            # Step 5: Submit form
            print("Step 5: Submitting form...")
            email_input.submit()
            
            # Step 6: Wait for response
            print("Step 6: Waiting for submission response...")
            time.sleep(3)
            
            print("Newsletter subscription test completed successfully!")
            
        except Exception as e:
            print(f"Newsletter test failed! Error: {str(e)}")
            raise e

if __name__ == "__main__":
    unittest.main(verbosity=2)
