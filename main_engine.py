#
#
#
# -------------------> Selenium Projects <---------------------------
# Author     -> Andrei C. Cojocaru
# LinkedIn   ->
# Github     ->
# Youtube    ->
# Facebook   ->
# Tiktok     ->
#
#
from browser_settings import chromedriver_config
#
from time import sleep
#
from folder_with_tests import form_fill_ideisioferte


if __name__ == "__main__":

    driver = chromedriver_config()

    # test form fill ideisioferte.ro!
    form_fill_ideisioferte(driver)
