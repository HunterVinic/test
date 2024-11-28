import uiautomator2 as u2


def main():
    try:
        device = u2.connect()
        print("Connected to device:", device.info["serial"])
    except Exception as e:
        print("Failed to connect to the device:", str(e))
        return

    package_name = "com.example.app"
    try:
        device.app_start(package_name)
        print(f"App '{package_name}' launched successfully.")
    except Exception as e:
        print(f"Failed to start the app: {str(e)}")
        return

    device.wait_timeout = 10

    try:
        if device(text="Next").exists(timeout=5):
            device(text="Next").click()
            print("Navigated to the next screen.")

        if device(text="Accept").exists(timeout=5):
            device(text="Accept").click()
            print("Accepted terms and conditions.")
    except Exception as e:
        print(f"Error during navigation: {str(e)}")
        return

    try:
        element_id = "com.example.app:id/target_text"
        if device(resourceId=element_id).exists(timeout=5):
            extracted_text = device(resourceId=element_id).get_text()
            print(f"Extracted Text: {extracted_text}")
        else:
            print(f"Element with resource ID '{element_id}' not found.")
    except Exception as e:
        print(f"Error extracting text: {str(e)}")

    try:
        device.app_stop(package_name)
        print(f"App '{package_name}' stopped successfully.")
    except Exception as e:
        print(f"Error stopping the app: {str(e)}")


if __name__ == "__main__":
    main()
