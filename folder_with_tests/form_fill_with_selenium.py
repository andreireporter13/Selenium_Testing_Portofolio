#
#
#
# Form fill with Selenium
#
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#
from time import sleep


# ---> Send Message with selenium ############# SA-L REFAC CU CLASE, ca sa para mai profi
def form_fill_ideisioferte(driver):
    """
    This func() fill contact for on ideisioferte.ro in automatic way.
    """

    message_text = """
        Hi. This is a test message. It send with selenium.
    Interesting moment.

    With respect,
    Selenium Bot.
            """

    try:
        driver.get('https://ideisioferte.ro/contact/')

        name_surname = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "wpforms-312-field_0")))
        driver.execute_script("arguments[0].scrollIntoView();", name_surname)
        name_surname.send_keys('Andrei Cojocaru')

        email_data = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "wpforms-312-field_1"))).send_keys('contact@webautomation.ro')
        message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "wpforms-312-field_2"))).send_keys(message_text)
        gdpr_acord = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "wpforms-312-field_4_1"))).click()
        sleep(1)

        # submit
        submit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "wpforms-submit-312"))).click()
        sleep(0.5)

    except Exception as ex:
        print(ex)

    finally:
        sleep(10)
        driver.quit()
