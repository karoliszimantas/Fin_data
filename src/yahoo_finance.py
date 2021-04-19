from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

company = input('enter companies abbreviation: ')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
wd = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', options=chrome_options)

DELAY = 25

wd.maximize_window()

wd.get('https://finance.yahoo.com/quote/' + company + '/financials/')

#pop_up
try:
    btn = WebDriverWait(wd, DELAY).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consent-page"]/div/div/div/form/div[2]/div[2]/button')))
    wd.execute_script("arguments[0].scrollIntoView();", btn)
    wd.execute_script("arguments[0].click();", btn)
except:
    pass

results = WebDriverWait(wd, DELAY).until(EC.presence_of_element_located((By.ID, 'Col1-1-Financials-Proxy')))

soup_income = BeautifulSoup(results.get_attribute('innerHTML'), 'html.parser')

revenue_element = soup_income.find('span', string='Total Revenue').find_next('span').text
cogs_element = soup_income.find('span', string='Cost of Revenue').find_next('span').text
ebit_element = soup_income.find('span', string='Operating Income').find_next('span').text
net_element = soup_income.find('span', string='Pretax Income').find_next('span').text

wd.get('https://finance.yahoo.com/quote/' + company + '/balance-sheet/')

results = WebDriverWait(wd, DELAY).until(EC.presence_of_element_located((By.ID, 'Col1-1-Financials-Proxy')))

btn = WebDriverWait(wd, DELAY).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="Col1-1-Financials-Proxy"]/section/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button/svg/path')))
wd.execute_script("arguments[0].scrollIntoView();", btn)
wd.execute_script("arguments[0].click();", btn)

btn = WebDriverWait(wd, DELAY).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="Col1-1-Financials-Proxy"]/section/div[4]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button/svg/path')))
wd.execute_script("arguments[0].scrollIntoView();", btn)
wd.execute_script("arguments[0].click();", btn)

soup_balance = BeautifulSoup(results.get_attribute('innerHTML'), 'html.parser')

short_assets_element = soup_balance.find('span', string='Current Assets').find_next('span').text
inventory_element = soup_balance.find('span', string='Inventory').find_next('span').text
tot_assets_element = soup_balance.find('span', string='Total Assets').find_next('span').text
t_payables_element = soup_balance.find('span', string='Total Current Assets').find_next('span').text
short_liabl_element = soup_balance.find('span', string='Accounts Payable').find_next('span').text
tot_liab_element = soup_balance.find('span', string='Total Liabilities').find_next('span').text
tot_equity_element = soup_balance.find('span', string="Total stockholders' equity").find_next('span').text

wd.quit()

