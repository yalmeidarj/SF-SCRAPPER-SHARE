import csv
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import tkinter
from tkinter import messagebox

from selenium import webdriver
# Uncomment to use:
# chrome service (service)
# from selenium.webdriver.chrome.service import Service


# Headless browser from chrome (options)
from selenium.webdriver.chrome.options import Options



class FetcherBot:
    """
    ## FetcherBot
    #### A Selenium-based web automation class designed to interact with specific web pages, handle navigation, and perform various actions such as selecting sites from a dropdown menu, clicking buttons to navigate through pages, and handling login confirmation.\n
    #### Methods:

    - `go_to_url(url: str) -> bool`:
        - Navigates to the given URL.
        - Returns True if successful, False otherwise.

    - `select_site(site_name: str) -> bool`:
        - Selects a specific site from a dropdown menu.
        - Returns True if successful, False otherwise.

    - `click_100_views_button() -> bool`:
        - Clicks the button to display 100 views on a web page.
        - Returns True if successful, False otherwise.

    - `click_next_page_button() -> bool`:
        - Clicks the button to navigate to the next page.
        - Returns True if successful, False otherwise.

    - `get_login_confirmation() -> bool`:
        - Prompts the user to confirm login using a dialog box.
        - Returns the result of the user's confirmation.

    - `update_site(data: dict) -> Optional[dict]`:
        - Updates the site with the provided data by filling in a form.
        - Returns relevant data if successful, None otherwise.

    - `find_matching_addresses_from_table(data: dict) -> bool`:
        - Finds matching addresses from a table and performs related actions.
        - Returns True if successful, False otherwise.

    #### Attributes:

    - `self.driver`:
        - The Selenium WebDriver instance used to interact with the web browser.

    - `self.xpath_iframe_complete`:
        - XPATH for the iframe to be selected (used in `select_site` method).

    #### Usage:
    - Initialize an instance of the FetcherBot class with appropriate configurations.
    - Use the available methods to navigate and interact with specific web pages.

    #### Note:
    - Ensure that the WebDriver is correctly initialized and configured before using this class.
    - Be aware of the specific web elements and structures that this class is designed to interact with.
    """

    def __init__(self):
        self.draw_script = """
        var context = arguments[0].getContext('2d');
        context.beginPath();
        context.moveTo(50, 50);  # Start point
        context.lineTo(200, 200);  # End point
        context.stroke();
        """
                # Create ChromeOptions object with headless mode
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless=new")
        self.chrome_options.add_argument('--disable-gpu')  # Disable GPU usage when in headless mode
        self.chrome_options.add_argument('--no-sandbox')   # Optional, may be required in some environments



        # self.service = Service("C:/Users/yalme/Desktop/gate/chromedriver.exe")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.xpath_iframe_complete = "/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/force-aloha-page/div/iframe"
        self.form_iframe_xpath = "/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/force-aloha-page/div/iframe"
        self.second_form_iframe_xpath = "/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/force-aloha-page/div/iframe"
        self.canvas_iframe_xpath = "/html/body/div/div[2]/div/div/form/div[5]/div[3]/canvas[1]"

    def go_to_url(self, url):
        """
        ## Navigates to a specific URL using the Selenium WebDriver.
        #### This method is part of a class that uses Selenium WebDriver to control a web browser. It takes a URL and directs the browser to navigate to that location.

        - param url: String representing the URL that the browser should navigate to.

        - return: True if the navigation is successful, False if an exception occurs during the process.

        #### Note:
        - Ensure that the WebDriver is correctly initialized and configured before calling this method.
        - The URL should be properly formatted and include the protocol (e.g., 'http://', 'https://').
        """
        try:
            self.driver.get(url)
            return True
        except Exception as e:
            print(f"Error: Unable to go to url\n{e}")
            return False

    def login(self, username: str, password: str) -> bool:
        """
        ## Logs in by entering username and password
        #### This method is part of a class that uses Selenium WebDriver to control a web browser. It takes a username and password and enters them into the appropriate fields on the login page.
        - param username: String representing the username to be entered.
        - param password: String representing the password to be entered.

        - return: True if the login process is successfully initiated, False if an exception occurs.

        #### Note:
        - This method assumes that the login page has been loaded, and the username and password fields,
          as well as the login button, are present on the page.
        """
        try:
            username_box = self.driver.find_element(By.NAME, 'username')
            password_box = self.driver.find_element(By.NAME, 'pw')

            username_box.send_keys(username)
            password_box.send_keys(password)

            login_button = self.driver.find_element(By.NAME, 'Login')
            login_button.click()
            time.sleep(5)
            print(f"5 Seconds has passed after loggin")
            return True
        except Exception as e:
            print(f"Error during login process:\n{e}")
            return False

    def get_login_confirmation(self):
        """
        ## Waits for user confirmation regarding login completion.
        #### This method leverages the tkinter library to display a dialog box that asks the user to confirm when the login process is finished. The user can click the OK button to confirm or the Cancel button to indicate failure.

        - return: True if the user clicks OK, False if the user clicks Cancel or closes the dialog.

        #### Note:
        - This method is designed to be used in situations where a human needs to intervene, such as navigating through CAPTCHA or other login barriers that may require human interaction.
        - It assumes that the tkinter and messagebox modules are imported properly.
        - Ensure that the application calling this method has the proper permissions to create GUI components if running in a restricted environment.
        """

        root = tkinter.Tk()
        root.withdraw()
        print("Waiting for Login confirmation...")
        result = messagebox.askokcancel(
            "Confirmation", "Wait until the Login process is finished, close any popups and press OK")
        root.destroy()
        return result

    def click_100_views_button(self):
        """
        ## Clicks the button to display 100 views on a web page.
        #### This method is part of a class that uses Selenium WebDriver to interact with web elements. It finds a specific button with the given XPATH that corresponds to displaying 100 views and clicks it.

        - return: True if the button is successfully clicked, False if an exception occurs (such as the button not being found).

        #### Note:
        - Ensure that the WebDriver is correctly initialized and configured before calling this method.
        - This method assumes that the web page is loaded and the button to display 100 views is present on the page.
        """
        try:
            timeout = 20  # Set the timeout to 20 seconds
            xpath = '//button[@type="button" and @ng-click="params.count(100)"]'
            full_xpath = "/html/body/div/div[2]/div/div[5]/div[2]/div/div[2]/div/ul/li[12]/div/button[4]"
            button = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (By.XPATH, full_xpath))
            )
            button.click()
            return True
        except TimeoutException:
            print("Error @ 'click_100_views_button': Timed out waiting for the button to be clickable")
            return False
        except Exception as e:
            print(f"Error: Button not found or unable to click\n{e}")
            return False

    def click_next_page_button(self):
        """
        ## Clicks the button to navigate to the next page on a web page.
        #### This method is part of a class that uses Selenium WebDriver to interact with web elements. It waits for the presence of a specific "next page" button and clicks it to navigate to the next page.

        - return: True if the button is successfully clicked, False if the button is not found or an exception occurs during the process.

        #### Note:
        - Ensure that the WebDriver is correctly initialized and configured before calling this method.
        - This method assumes that the web page is loaded and the "next page" button is present on the page.
        - It will wait for a maximum of 10 seconds for the "next page" button to become present.
        - If a TimeoutException occurs, it is assumed that the last page has been reached.
        """
        try:
            next_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//li[contains(@class, "next")]/a')))
            next_button.click()
            return True
        except TimeoutException as e:
            print(
                f"Info: No next page button found. It seems we've reached the end of the pages.\n{e}")
            return False
        except Exception as e:
            print(f"Error: Next page button not found\n{e}")
            return False

    def select_site(self, site_name):
        """
        ## Selects a specific site from a dropdown menu on a webpage.
        #### This method is part of a class that uses Selenium WebDriver to interact with web elements. It waits for the presence of an iframe, switches to it, and then selects a site from a dropdown menu by its visible text.

        - param site_name: String representing the visible text of the option to be selected from the dropdown menu.

        - return: True if the site is successfully selected, False if an exception occurs during the process.

        #### Note:
        - `self.xpath_iframe_complete` should be defined as an instance variable of the class, containing the XPATH
        for the iframe to be selected.
        - This method assumes that the relevant web page has been loaded, and the iframe and dropdown are present
        on the page.
        """
        # /html/body/div/div[2]/div/div[4]/div[2]/div/div[3]/select
        try:
            # Switch to iframe
            WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located((By.XPATH, self.xpath_iframe_complete)))
            iframe = self.driver.find_element(
                By.XPATH, self.xpath_iframe_complete)
            self.driver.switch_to.frame(iframe)
        except Exception as e:
            print("Exception @ select_site @ Switch to iframe")
            print(e)

        try:
            # get the select element
            select_xpath = "/html/body/div/div[2]/div/div[4]/div[2]/div/div[3]/select"
            select_xpath = "/html/body/div/div[2]/div/div[4]/div[2]/div/div[3]/select"
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "select.ng-pristine.ng-valid.ng-touched")))

            dropdown = Select(self.driver.find_element(
                By.CSS_SELECTOR, "select.ng-pristine.ng-valid.ng-touched"))
            dropdown.select_by_visible_text(site_name)

            # Handle geolocation alert if it occurs
            # try:
            #     alert = self.driver.switch_to.alert
            #     alert_text = alert.text
            #     print(f"Alert Text: {alert_text}")
            #     alert.accept()
            # except NoAlertPresentException:
            #     pass

            time.sleep(2)
        except Exception as e:
            print("Exception @ select_site when trying to get the select element")
            print(e)
            return False

        print(f"Site {site_name} selected successfully!")
        return True


    def fetch_site_data(self, site_name):
        to_report = {
            "site": site_name,
            "function_name": "fetch_site_data",
            "status": "",
        }
        table_data = []
        self.click_100_views_button()
        while True:
            try:
                page_data = self.get_table_data()
                for row in page_data:
                    address = row.get('Address')
                    if address:
                        parts = address.split()
                        number = parts[0]
                        street_name = ' '.join(parts[1:])
                        row['Number'] = number
                        row['Street Name'] = street_name
                        table_data.append(row)
            except Exception as e:
                message = f'\nNot able to fetch data from site: {site_name}\n{e}'
                to_report["status"] = message

                self.fetch_report.append(to_report)
                print(message)
                break
            try:
                next_buttons = self.driver.find_element(
                    By.XPATH, '//li[contains(@class, "next")]/a')
                next_buttons.click()
                time.sleep(2)
            except Exception as e:
                print(
                    f"Info: No next page button found. It seems we've reached the end of the pages.\n{e}")
                break
            message = f'\nFetched data from site: {site_name} successfully\n'
            to_report["status"] = message
            self.fetch_report.append(to_report)

        return table_data


    def update_site(self, data):
        """
        ... (method docstring) ...
        """
        try:
            # Check and set default phone number
            phone_data = data.get("phone")
            if not phone_data or phone_data == "None" or phone_data == " ":
                phone_data = "0000000000"

            # Clear and fill fields
            fields = {
                "name": "/html/body/div/div[2]/div/div/form/div[3]/div[3]/input[1]",
                "lastName": "/html/body/div/div[2]/div/div/form/div[3]/div[3]/input[2]",
                "email": "/html/body/div/div[2]/div/div/form/div[6]/div[3]/input",
                "phone": "/html/body/div/div[2]/div/div/form/div[5]/div[3]/input"
            }

            for field_name, xpath in fields.items():
                field = self.driver.find_element(By.XPATH, xpath)
                field.clear()
                field.send_keys(data.get(field_name, ""))

            # Select Language
            language_select = self.driver.find_element(By.NAME, "language")
            language_options = language_select.find_elements(By.TAG_NAME, "option")
            for option in language_options:
                if option.text.strip() == "English":
                    option.click()
                    break

            # Select Feed
            feed_options = self.driver.find_elements(By.NAME, "feed")
            for option in feed_options:
                if option.get_attribute("value") == "Aerial":
                    option.click()
                    break

            # Select Installation Type
            installation_type_select = self.driver.find_element(By.NAME, "installationType")
            installation_type_options = installation_type_select.find_elements(By.TAG_NAME, "option")
            for option in installation_type_options:
                if option.text.strip() == data.get("type", ""):
                    option.click()
                    break

            # Select Status and Consent
            status_select = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/form/div[13]/div[3]/select")
            status_options = status_select.find_elements(By.TAG_NAME, "option")
            for option in status_options:
                status_attempt = data.get('statusAttempt', "")
                if option.text.strip() == status_attempt and status_attempt != "Consent Final":
                    option.click()
                    break
                elif option.text.strip() == status_attempt and status_attempt == "Consent Final":
                    option.click()

                    consent_select = self.driver.find_element(By.NAME, "Consent")
                    consent_options = consent_select.find_elements(By.TAG_NAME, "option")
                    for consent_option in consent_options:
                        if consent_option.text.strip() == data.get("consent", ""):
                            consent_option.click()
                            break
                    break

            # Submit the form
            time.sleep(2)
            submit_button = WebDriverWait(self.driver, 120).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/div[3]/div[2]/button[5]")))
            submit_button.click()

            return True

        except Exception as e:
            print("Error:", e)
            return False


    def find_matching_addresses_from_table(self, data):
        """
        ## Search for multiple addresses within a web page table
        ### Click the "Go To" button next to each matching address.

        - param data: List of dictionaries, where each dictionary contains 'streetNumber' and 'streetName' keys
        - return: True if the method executes without exception, False otherwise
        """

        # Iterate through each address item in the data
        for item in data:
            # Combine street number and street name to form the address
            address = str(item['streetNumber']) + ' ' + item['streetName']
            address_to_update = address.upper()

            # Click to change view or any initial action required
            self.click_100_views_button()
            print(f'Address to be updated: {address_to_update}')

            while True:  # Keep looping until address is found or no more pages
                try:
                    # Wait for page to load
                    time.sleep(1)

                    # Get all table rows
                    rows = self.driver.find_elements(By.TAG_NAME, 'tr')
                    address_found = False

                    # Iterate through rows
                    for row in rows:
                        row_dict = {}

                        # Get all cells within the row
                        cells = row.find_elements(By.TAG_NAME, 'td')

                        # Build dictionary from cell data
                        for cell in cells:
                            key = cell.get_attribute('data-title-text')
                            value = cell.text
                            row_dict[key] = value

                        # Check if address matches
                        if address_to_update in row_dict.get("Address", ""):
                            # Click the "Go To" button if address matches
                            go_to_button = row.find_element(
                                By.XPATH, "td//button[contains(text(), 'Go To')]")
                            go_to_button.click()
                            print(f'Found matching address:\n{row_dict}')
                            address_found = True
                            break  # Exit the for loop

                    if address_found:
                        break  # Exit the while loop if the address was found

                    # If address not found on this page, click next and continue loop
                    if not self.click_next_page_button():
                        print(f"Address {address_to_update} not found")
                        break  # Exit the while loop and continue with the next address in data

                except Exception as e:
                    # Print exception and return False
                    print("Error:", e)
                    return False

        # Return True if function executed without exception
        return True

    def find_matching_address_from_table(self, data, max_attempts=100):
        """
        ## Search for a single address
        ### Click the "Go To" button next to the matching address.

        - data: Dictionary containing 'streetNumber' and 'streetName' keys
        - max_attempts: Maximum number of pages to search through (default is 10)
        - return: True if the address is found and method executes without exception, False otherwise
        """

        # Combine street number and street name to form the address
        address = str(data['streetNumber']) + ' ' + data['streetName']
        address_to_update = address.upper()

        # Click to change view or any initial action required
        # self.click_100_views_button()
        print(f'Address to be updated: {address_to_update}')

        # Loop through pages.  '_' is a throwaway variable used to count the number of iterations
        for _ in range(max_attempts):
            try:
                # Wait for the table rows to be present
                wait = WebDriverWait(self.driver, 10)
                rows = wait.until(
                    EC.presence_of_all_elements_located((By.TAG_NAME, 'tr')))
                address_found = False

                # Iterate through rows
                for row in rows:
                    print(f"Current Function: find_matching_address_from_table\nCurrent row:{row}")
                    row_dict = {}

                    # Get all cells within the row
                    cells = row.find_elements(By.TAG_NAME, 'td')

                    # Build dictionary from cell data
                    for cell in cells:
                        key = cell.get_attribute('data-title-text')
                        value = cell.text
                        row_dict[key] = value

                    # Check if address matches
                    if address_to_update in row_dict.get("Address", ""):
                        # Click the "Go To" button if address matches
                        go_to_button = row.find_element(
                            By.XPATH, "td//button[contains(text(), 'Go To')]")
                        go_to_button.click()
                        print(f'Found matching address:\n{row_dict}')
                        address_found = True
                        break  # Exit the for loop

                if address_found:
                    print("Function: find_matching_address_from_table\nAddress found in table")
                    return True  # Return True if the address was found

                # If address not found on this page, click next and continue loop
                if not self.click_next_page_button():
                    print(
                        f"Address {address_to_update} not found after {max_attempts} attempts")
                    # return False  # Return False if address not found

            except Exception as e:
                # Print exception and return False
                print("Error:", e)
                return False

        # If the function has not returned by now, the address was not found in the given max_attempts
        print(
            f"Address {address_to_update} not found after {max_attempts} attempts")
        return False

    def process_csv_to_dict(self, file_path: str) -> list:
        """
        ## Read CSV file and processes its content into list of dictionaries.
        ### Each dictionary contains a property detail object.

        Parameters:
        file_path (str): The path to the CSV file to read.

        Returns:
        list[dict]: A list of dictionaries, each containing information about a person.

        CSV file format:
        The CSV file should have the following headers:
        - streetNumber: The street number
        - street: The street name
        - name: The person's first name
        - lastName: The person's last name
        - phone: The phone number
        - email: The email address
        - type: The type or category
        - consent: The consent status
        - location: The location (if applicable)
        """
        dataList = []
        with open(file_path, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data = {
                    'streetNumber': row['streetNumber'],
                    'streetName': row['street'],
                    'name': row['name'],
                    'lastName': row['lastName'],
                    'phone': row['phone'],
                    'email': row['email'],
                    'type': row['type'],
                    'statusAttempt': row['statusAttempt'],
                    'consent': row['consent'],
                    'location': row['location'],
                }
                dataList.append(data)
        return dataList

    def switch_to_forms_iframe(self):
        """
        ## Switch to the iframe containing the form.

        - return: True if the iframe is successfully selected, False if an exception occurs during the process.

        #### Note:
        - `self.form_iframe_xpath` should be defined as an instance variable of the class, containing the XPATH
        for the iframe to be selected.
        - This method assumes that the relevant web page has been loaded, and the iframe is present
        on the page.
        """
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.form_iframe_xpath)))
            iframe = driver.find_element(By.XPATH, self.form_iframe_xpath)
            # switch to selected iframe
            self.driver.switch_to.frame(iframe)
            return True
        except Exception as e:
            print(e)
            return False

    def check_if_form_2_required(self):
        """
        ## Check if form 2 is required.

        - return: True if the form 2 is required, False if an exception occurs during the process.

        """
        try:
            canvas_button = self.driver.find_element(
                By.XPATH, self.canvas_iframe_xpath)
            return True
        except Exception as e:
            print(e)
            print("\nForm 2 is not required")
            return False

    def switch_to_second_form_iframe(self):
        """
        ## Switch to the iframe containing the form.

        - return: True if the iframe is successfully selected, False if an exception occurs during the process.

        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.second_form_iframe_xpath)))
            iframe = self.driver.find_element(
                By.XPATH, self.second_form_iframe_xpath)
            # switch to selected iframe
            self.driver.switch_to.frame(iframe)
            return True
        except Exception as e:
            print(e)
            return False

    def draw_signature(self):
        """
        ## Draw signature on the canvas. save the signature and close the form.

        - return: True if the signature is successfully drawn, False if an exception occurs during the process.
        """
        try:
            canvas = self.driver.find_element(
                By.XPATH, self.canvas_iframe_xpath)
            self.driver.execute_script(self.draw_script, canvas)
            time.sleep(2)
            save_button = self.driver.find_element(
                By.XPATH, "/html/body/div/div[2]/div/div/form/div[7]/div[2]/button[3]")
            save_button.click()
            return True
        except Exception as e:
            print(e)
            return False


if __name__ == "__main__":
    bot = FetcherBot()
    # bot.go_to_url("https://bellconsent.my.salesforce.com/?ec=302&startURL=%2Fvisualforce%2Fsession%3Furl%3Dhttps%253A%252F%252Fbellconsent.lightning.force.com%252Flightning%252Fn%252FBell")

