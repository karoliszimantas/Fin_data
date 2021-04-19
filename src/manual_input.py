financials = {}

def read_information_input():
    print('Enter income statement information')
    financials['rev'] = float(input("Enter revenues"))
    financials['cogs'] = float(input("Enter costs of goods"))
    financials['ebit'] = float(input("Enter EBIT/operating profit"))
    financials['net_income'] = float(input("Enter net income"))
    print("Enter balance sheet information")
    financials['t_receivables'] = float(input("Enter trades receivables"))
    financials['inventory'] = float(input("Enter inventory"))
    financials['short_assets'] = float(input("Enter current assets"))
    financials['tot_assets'] = float(input("Enter total assets"))
    financials['t_payables'] = float(input("Enter trades payables"))
    financials['short_liabl'] = float(input("Enter current liabilities"))
    financials['tot_liabl'] = float(input("Enter total liabilities"))
    financials['tot_equity'] = float(input("Enter total equity"))
