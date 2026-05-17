from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

ACCOUNT_EMAIL = "bshshsshushs2@gmail.com"
ACCOUNT_PASSWORD = "mancity11223344"
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "Day-49/chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

wait = WebDriverWait(driver, 5)

# login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
# login_button.click()

# email_input = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
# email_input.send_keys(ACCOUNT_EMAIL)

# password_input = driver.find_element(By.ID, "password-input")
# password_input.send_keys(ACCOUNT_PASSWORD)

# submit_button = driver.find_element(By.ID, "submit-button")
# submit_button.click()

# all_classes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[id^='class-card-']")))

# booked_count = 0
# waitlist_join_count = 0
# already_count = 0
# processed_count = 0


# detailed_list = []

# for available_class in all_classes:
#     date = available_class.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
#     day = date.find_element(By.TAG_NAME, "h2").text

#     if "Tue" in day or "Thu" in day:
#         class_time = available_class.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text

#         if "6:00 PM" in class_time:
#             class_name = available_class.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

#             button = available_class.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
#             button_text = button.text

#             if button_text == "Booked":
#                 already_count += 1
#                 detailed_list.append(f"[Already Booked] {class_name} on {day}")
#                 print(f"✓ Already booked: {class_name} on {day}")
#             elif button_text == "Waitlisted":
#                 already_count += 1
#                 detailed_list.append(f"[Already Waitlisted] {class_name} on {day}")
#                 print(f"✓ Already on waitlist: {class_name} on {day}")
#             elif button_text == "Join Waitlist":
#                 waitlist_join_count += 1
#                 detailed_list.append(f"[Joined Waitlist] {class_name} on {day}")
#                 button.click()
#                 print(f"✓ Joined waitlist for: {class_name} on {day}")
#             else:
#                 button.click()
#                 detailed_list.append(f"[New Booking] {class_name} on {day}")
#                 booked_count += 1
#                 print(f"✓ Booked: {class_name} on {day}")

        
#             processed_count += 1

# my_bookings_link = wait.until(
#     EC.element_to_be_clickable((By.LINK_TEXT, "My Bookings"))
# )
# my_bookings_link.click()

# my_bookings_page = wait.until(
#     EC.presence_of_element_located((By.ID, "my-bookings-page"))
# )

# confirmed_count = int(my_bookings_page.get_attribute("data-bookings-count"))
# waitlist_count = int(my_bookings_page.get_attribute("data-waitlist-count"))

# found_count = confirmed_count + waitlist_count
# expected_count = processed_count

# print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")
# print(f"Confirmed bookings: {confirmed_count}")
# print(f"Waitlist entries: {waitlist_count}")

# print("\n--- VERIFICATION RESULT ---")
# print(f"Expected: {expected_count}")
# print(f"Found: {found_count}")

# if found_count == expected_count:
#     print("SUCCESS: All bookings verified!")
# else:
#     print(f"MISMATCH: Missing {expected_count - found_count} booking(s)")


# print("")
# print("---BOOKING SUMMARY---")
# print(f"Classes booked: {booked_count}")
# print(f"Waitlists joined: {waitlist_join_count}")
# print(f"Already booked/waitlisted: {already_count}")
# print(f"Total Tuesday and Thursday 6pm classes processed: {processed_count}")
# print("")

# print("---DETAILED CLASS LIST---")
# for details in detailed_list:
#     print(f"-{details}")



    
def login():
    

    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

    email_input = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = driver.find_element(By.ID, "password-input")
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    submit_button = driver.find_element(By.ID, "submit-button")
    submit_button.click()

    wait.until(
    EC.presence_of_element_located((By.ID, "schedule-page"))
    )


            


def process_classes():
    all_classes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[id^='class-card-']")))

    booked_count = 0
    waitlist_join_count = 0
    already_count = 0
    processed_count = 0


    detailed_list = []

    for available_class in all_classes:
        date = available_class.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
        day = date.find_element(By.TAG_NAME, "h2").text

        if "Tue" in day or "Thu" in day:
            class_time = available_class.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text

            if "6:00 PM" in class_time:
                class_name = available_class.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

                button = available_class.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
                button_text = button.text

                if button_text == "Booked":
                    detailed_list.append(f"[Already Booked] {class_name} on {day}")
                    print(f"✓ Already booked: {class_name} on {day}")
                    already_count += 1
                elif button_text == "Waitlisted":
                    detailed_list.append(f"[Already Waitlisted] {class_name} on {day}")
                    print(f"✓ Already on waitlist: {class_name} on {day}")
                    already_count += 1
                elif button_text == "Join Waitlist":
                    detailed_list.append(f"[Joined Waitlist] {class_name} on {day}")
                    button.click()
                    wait.until(lambda d: button.text == "Waitlisted")
                    print(f"✓ Joined waitlist for: {class_name} on {day}")
                    waitlist_join_count += 1
                else:
                    button.click()
                    wait.until(lambda d: button.text == "Booked")
                    detailed_list.append(f"[New Booking] {class_name} on {day}")
                    print(f"✓ Booked: {class_name} on {day}")
                    booked_count += 1

            
                processed_count += 1

    return booked_count, waitlist_join_count, already_count, processed_count, detailed_list

def verify_bookings(booked_count, waitlist_join_count, already_count, processed_count, detailed_list):


    my_bookings_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "My Bookings"))
    )
    my_bookings_link.click()

    my_bookings_page = wait.until(
        EC.presence_of_element_located((By.ID, "my-bookings-page"))
    )

    confirmed_count = int(my_bookings_page.get_attribute("data-bookings-count"))
    waitlist_count = int(my_bookings_page.get_attribute("data-waitlist-count"))

    found_count = confirmed_count + waitlist_count
    expected_count = processed_count

    print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")
    print(f"Confirmed bookings: {confirmed_count}")
    print(f"Waitlist entries: {waitlist_count}")

    print("\n--- VERIFICATION RESULT ---")
    print(f"Expected: {expected_count}")
    print(f"Found: {found_count}")

    if found_count == expected_count:
        print("SUCCESS: All bookings verified!")
    else:
        raise Exception(f"Mismatch: Missing {expected_count - found_count} booking(s)")


    print("")
    print("---BOOKING SUMMARY---")
    print(f"Classes booked: {booked_count}")
    print(f"Waitlists joined: {waitlist_join_count}")
    print(f"Already booked/waitlisted: {already_count}")
    print(f"Total Tuesday and Thursday 6pm classes processed: {processed_count}")
    print("")

    print("---DETAILED CLASS LIST---")
    for details in detailed_list:
        print(f"-{details}")





def retry(func, retries=7, description=""):

    success = False

    for attempt in range(1, retries + 1):

        try:
            print(f"Trying {description}. Attempt: {attempt}")

            result = func()

            print(f"{description} successful!")
            success = True
            return result
        
            
            

        except Exception as error:
            print(f"{description} failed: {error}")

    if success == False:
        raise Exception(f"{description} failed after {retries} retries")



retry(login, description="Login")
booked_count, waitlist_join_count, already_count, processed_count, detailed_list = retry(
    process_classes,
    description="process_classes"
)
retry(
    lambda: verify_bookings(booked_count, waitlist_join_count, already_count, processed_count, detailed_list),
    description="verify_bookings"
)

