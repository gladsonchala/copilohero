from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time

class WebpageScreenshot:
    def __init__(self, url, width=1920, height=1080, zoom=1.0, output_path='screenshot.png'):
        """
        Initializes the WebpageScreenshot instance with preferences.
        
        :param url: URL of the webpage to capture.
        :param width: Width of the browser window.
        :param height: Height of the browser window.
        :param zoom: Zoom level of the page.
        :param output_path: Output path for the screenshot.
        """
        self.url = url
        self.width = width
        self.height = height
        self.zoom = zoom
        self.output_path = output_path

    def capture(self):
        # Set up Chrome options for a headless browser
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"--window-size={self.width},{self.height}")
        
        # Initialize WebDriver
        driver = webdriver.Chrome(options=options)
        
        try:
            # Open the webpage
            driver.get(self.url)
            time.sleep(2)  # Wait for the page to fully load
            
            # Set the zoom level with JavaScript
            if self.zoom != 1.0:
                driver.execute_script(f"document.body.style.zoom='{self.zoom}'")

            # Take a screenshot
            screenshot_data = driver.get_screenshot_as_png()

            # Save the screenshot
            with open(self.output_path, 'wb') as file:
                file.write(screenshot_data)
            
            # Open and confirm the screenshot as an image
            screenshot = Image.open(self.output_path)
            screenshot = screenshot.convert("RGB")
            screenshot.save(self.output_path, "PNG")
            
            print(f"Screenshot saved as {self.output_path}")

        finally:
            driver.quit()

# Example usage:
if __name__ == "__main__":
    url = "https://teable.io"
    screenshot = WebpageScreenshot(url, width=1080, height=720, zoom=1.0, output_path="example_screenshot.png")
    screenshot.capture()
