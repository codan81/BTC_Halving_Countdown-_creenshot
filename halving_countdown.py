

import time
from datetime import datetime
import os
import subprocess
import pyautogui
import schedule

def capture_screenshot_at_specific_time():
    screenshot_path = None  # Initialize with None
    try:
        # Open Safari in the background
        subprocess.Popen(['open', '-g', '-a', 'Safari', 'https://coinmarketcap.com/events/bitcoin-halving/'])

        # Wait for Safari to open (adjust as needed)
        time.sleep(5)

        # Use JavaScript to retrieve the text content of the countdown timer element
        countdown_time = pyautogui.press('command+shift+4', interval=1)

        if countdown_time == '0 days 0 hours 0 minutes 0 seconds':
            print('Bitcoin halving has occurred!')

            # Capture a screenshot of the halving countdown clock
            current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            screenshot_path = f'./btc_halving_clock/btc_halving_{current_time}.png'
            pyautogui.screenshot(screenshot_path)
            print(f'Screenshot saved at 0 days and 0 hours: {screenshot_path}')
        else:
            print('Countdown clock has not reached the halving yet.')

        # Minimize Safari window
        pyautogui.hotkey('command', 'm')

        # Wait for Safari window to minimize
        time.sleep(1)
        
    except Exception as e:
        print(f"Error occurred: {e}")

    return screenshot_path  # Return the path of the saved screenshot, if any

# Create the folder to store the screenshots
    if not os.path.exists('btc_halving_clock'):
        try:
            os.makedirs('btc_halving_clock')
        except OSError as e:
            print(f'Error creating directory: {e}')

# Main program execution
def main():
     # Check if the current time is past 5:45 PM
    if datetime.now().time() >= datetime.strptime("17:30", "%H:%M").time():
        # If it is, then execute the script
        while True:
            screenshot_path = capture_screenshot_at_specific_time()
            if screenshot_path:
                print(f'Screenshot saved at: {screenshot_path}')
                break  # Stop the loop after taking the screenshot
            else:
                print('No screenshot saved.')
                time.sleep(60)  # Check every 60 seconds
    else:
        print("It's not yet time to run the script.")

# Schedule the main function to run every day at 5:45 PM
schedule.every().day.at("17:30").do(main)

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
    main()
