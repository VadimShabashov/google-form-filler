from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import sys


def get_firefox():
    return webdriver.Firefox()


def get_chrome():
    return webdriver.Chrome()


def main():
    browser = sys.argv[1]
    presenter_name = sys.argv[2]
    title = sys.argv[3]

    my_group = "АЯ8-С1/2"
    my_uni_group = "M41411"
    my_name = "Vadim Shabashov"

    poll_link = ("https://docs.google.com/forms/d/e/1FAIpQLScr6l1eT3IQ"
                 "_s8fjYZW-zdLFgQFVIFxTxxSeZFTweYm_vfk6A/viewform?usp=sf_link")

    if browser:
        browser = get_firefox()
    else:
        browser = get_chrome()

    browser.get(poll_link)

    textboxes = browser.find_elements(by=By.CSS_SELECTOR, value="input[type='text']")
    checkboxes = browser.find_elements(by=By.CLASS_NAME, value="docssharedWizToggleLabeledContainer")

    textboxes[0].send_keys(my_name)
    textboxes[1].send_keys(my_group)
    textboxes[2].send_keys(my_uni_group)
    textboxes[3].send_keys(presenter_name)
    textboxes[4].send_keys(title)

    for ind, checkbox in enumerate(checkboxes):
        if ind % 3 == 2:
            checkbox.click()

    time.sleep(20)
    browser.quit()


if __name__ == "__main__":
    main()
