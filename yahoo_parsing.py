import urllib.request as url
from bs4 import BeautifulSoup


company = input('enter companies abbreviation')
income_page = 'https://finance.yahoo.com/quote/' + company + '/financials/'
balance_page = 'https://finance.yahoo.com/quote/' + company + '/balance-sheet/'
set_income_page = url.urlopen(income_page).read()
set_balance_page = url.urlopen(balance_page).read()
soup_income = BeautifulSoup(set_income_page, 'html.parser')
soup_balance = BeautifulSoup(set_balance_page, 'html.parser')

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
