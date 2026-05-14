from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def google_search(query):
    driver = create_driver()

    try:
        driver.get("https://www.google.com")

        wait = WebDriverWait(driver, 15)

        try:
            buttons = driver.find_elements(By.TAG_NAME, "button")
            for button in buttons:
                text = button.text.lower()
                if "nõustu" in text or "accept" in text or "agree" in text:
                    button.click()
                    break
        except Exception:
            pass

        search_box = wait.until(
            EC.element_to_be_clickable((By.NAME, "q"))
        )

        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.ENTER)

        wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        print("Otsing tehtud:", query)
        print("Esimesed leitud tulemused:")

        results = driver.find_elements(By.CSS_SELECTOR, "h3")

        if len(results) == 0:
            print("Tulemusi ei leitud või Google kuvab kontroll-/küpsiste lehte.")
        else:
            for index, result in enumerate(results[:5], start=1):
                if result.text.strip():
                    print(f"{index}. {result.text}")

    finally:
        input("Vajuta Enter, et brauser sulgeda...")
        driver.quit()


if __name__ == "__main__":
    search_query = input("Sisesta Google'i otsingupäring: ")
    google_search(search_query)