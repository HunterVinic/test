from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "platformVersion": "11.0",
    "deviceName": "emulator-5554",
    "app": "/path/to/app.apk",
    "automationName": "UiAutomator2"
}

def main():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    try:
        driver.find_element_by_id("com.example.app:id/username").send_keys("testuser")
        driver.find_element_by_id("com.example.app:id/password").send_keys("password123")
        driver.find_element_by_id("com.example.app:id/login").click()
        print("Login successful.")

        driver.find_element_by_id("com.example.app:id/menu").click()
        driver.find_element_by_xpath("//android.widget.TextView[@text='Submit Data']").click()
        driver.find_element_by_id("com.example.app:id/input_field").send_keys("Test Data")
        driver.find_element_by_id("com.example.app:id/submit_button").click()
        print("Data submitted successfully.")

    except Exception as e:
        print("Error during automation:", str(e))
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
