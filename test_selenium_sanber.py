import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"email").send_keys("rofiqorapitasari@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("fiqo456") # isi password
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,('button[type=submit]')).submit() # klik tombol masuk

        # validasi
        # response_data = browser.find_element(By.__class__,"swal2-title").text
        # response_message = browser.find_element(By.ID,"swal2-content").text

        # self.assertIn('Welcome', response_data)
        # self.assertEqual(response_message, 'Anda Berhasil Masuk')

    def test_b_failed_login_with_empty_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"email").send_keys("rofiqorapitasari@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,('button[type=submit]')).submit() # klik tombol masuk

        # validasi
        # response_data = browser.find_element(By.CSS_SELECTOR,'div[data-testid="error-password"]').text
        response_message = browser.find_element(By.CSS_SELECTOR,'div[data-testid="error-password"]').text

        # self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'diperlukan kata sandi')

    def test_c_failed_login_with_empty_email_and_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"email").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,('button[type=submit]')).submit() # klik tombol masuk

        # validasi
        # response_data = browser.find_element(By.CSS_SELECTOR,'div[data-testid="error-password"]').text
        response_message = browser.find_element(By.CSS_SELECTOR,'div[data-testid="error-email"]').text

        # self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'diperlukan email')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()