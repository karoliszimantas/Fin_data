from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from bs4 import BeautifulSoup


company = input('enter companies abbreviation')
income_page = 'https://finance.yahoo.com/quote/' + company + '/financials/'
balance_page = 'https://finance.yahoo.com/quote/' + company + '/balance-sheet/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
wd = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe', options=chrome_options)

wd.get('https://finance.yahoo.com/quote/' + company + '/financials/')
DELAY = 15

wd.maximize_window()

wd.get('https://finance.yahoo.com/quote/' + company + '/financials/')

try:
    btn = WebDriverWait(wd, DELAY).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consent-page"]/div/div/div/div[2]/div[2]/form/button')))
    wd.execute_script("arguments[0].scrollIntoView();", btn)
    wd.execute_script("arguments[0].click();", btn)
except:
    pass

ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)

results_income = WebDriverWait(wd, DELAY).until(EC.presence_of_element_located((By.ID, 'Col1-1-Financials-Proxy')))
#soup_income = BeautifulSoup(results_income.get_attribute('innerHTML'), 'html.parser')

results_balance = results_income.find_element(By.XPATH, '//*[@id="Col1-1-Financials-Proxy"]/section/div[1]/div[1]/div/a[1]/div/span').click()
#soup_balance = BeautifulSoup(results_income.get_attribute('innerHTML'), 'html.parser')

revenue_element = soup_income.find('span', string='Total Revenue').find_next('span').text
cogs_element = soup_income.find('span', string='Cost of Revenue').find_next('span').text
ebit_element = soup_income.find('span', string='Operating Income').find_next('span').text
net_element = soup_income.find('span', string='Pretax Income').find_next('span').text
short_assets_element = soup_balance.find('span', string='Current Assets').find_next('span').text
inventory_element = soup_balance.find('span', string='Inventory').find_next('span').text

wd.quit()

revenue_element = soup_income.find('span', string='Total Revenue').find_next('span').text
cogs_element = soup_income.find('span', string='Cost of Revenue').find_next('span').text
ebit_element = soup_income.find('span', string='Operating Income or Loss').find_next('span').text
net_element = soup_income.find('span', string='Net Income').find_next('span').text
t_receivables_element = soup_balance.find('span', string='Net Receivables').find_next('span').text
inventory_element = soup_balance.find('span', string='Inventory').find_next('span').text
short_assets_element = soup_balance.find('span', string='Total Current Assets').find_next('span').text
tot_assets_element = soup_balance.find('span', string='Total Assets').find_next('span').text
t_payables_element = soup_balance.find('span', string='Total Current Assets').find_next('span').text
short_liabl_element = soup_balance.find('span', string='Accounts Payable').find_next('span').text
tot_liab_element = soup_balance.find('span', string='Total Liabilities').find_next('span').text
tot_equity_element = soup_balance.find('span', string="Total stockholders' equity").find_next('span').text


rev = int(revenue_element.replace(',', ''))
cogs = int(cogs_element.replace(',', ''))
ebit = int(ebit_element.replace(',', ''))
net_income = int(net_element.replace(',', ''))
t_receivables = int(t_receivables_element.replace(',', ''))
inventory = int(inventory_element.replace(',', ''))
short_assets = int(short_assets_element.replace(',', ''))
tot_assets =int(tot_assets_element.replace(',', ''))
t_payables = int(t_payables_element.replace(',', ''))
short_liabl = int(short_liabl_element.replace(',', ''))
tot_liab =int(tot_liab_element.replace(',', ''))
tot_equity =int(tot_equity_element.replace(',', ''))
