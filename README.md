# Bitcoin Halving Countdown Screenshot Script

## Overview
This Python script captures a screenshot of the Bitcoin halving countdown clock from the CoinMarketCap website. It uses Selenium to automate the process of opening a web browser, navigating to the countdown page, and capturing the screenshot when the countdown reaches 0 days, 0 hours, 0 minutes, and 0 seconds.

## Requirements
- Python 3.x
- Selenium
- Safari WebDriver
- PyAutoGUI (only required for specific implementation)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/bitcoin-halving-countdown.git

## Install dependencies
2.  pip install -r requirements.txt

## Usage
1. Navigate to the project directory:
   ```bash
   cd bitcoin-halving-countdown

2. Run the script:
   ``` bash
   python halving_countdown.py

3. The script will continuously monitor the Bitcoin halving countdown. When the countdown reaches 0 days, 0 hours, 0 minutes, and 0 seconds, it will capture a screenshot and save it to the btc_halving_clock folder.

## Configuration
You can modify the script to change the browser used (e.g., Chrome, Firefox) by adjusting the WebDriver initialization code.
Adjust the countdown check interval and other parameters as needed.

## Credits
Inspired by the idea of capturing Bitcoin halving countdown screenshots.
Developed by codan_81.

## License
This project is licensed under the MIT License.

