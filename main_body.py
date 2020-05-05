import numpy as np
import matplotlib.pyplot as plt
import sys


class Year:
    def __init__(self, rev, cogs, assets, liab, equity, net):
        self.rev = rev
        self.cogs = cogs
        self.assets = assets
        self.liab = liab
        self.equity = equity
        self.net = net


def input_attrs(initial_string):
    print(initial_string)
    rev = input("Revenues")
    cogs = input("Costs of goods")
    assets = input("Total assets")
    liab = input("Total liabilities")
    equity = input("Equity")
    net = input("Net income")
    return rev, cogs, assets, liab, equity, net

def plot_plots(years, ylabel, attribute):
    plt.tight_layout()
    plt.style.use("bmh")
    x_axis = np.arange(1, len(years) + 1)
    labels = [int(getattr(year, attribute)) for year in years]
    plt.plot(x_axis, labels)
    plt.xlabel('Periods')
    plt.ylabel(ylabel)
    plt.xticks(x_axis, x_axis)
    plt.show()

def plot_balance(years):
    fig, ax1 = plt.subplots()
    width = 0.22
    x_axis = np.arange(1, len(years) + 1)
    t_asset_labels = [int(getattr(year, 'assets')) for year in years]
    t_liabl_labels = [int(getattr(year, 'liab')) for year in years]
    ax1.bar(x_axis - width/2 ,t_asset_labels, width, label='Total assets')
    ax1.bar(x_axis + width/2, t_liabl_labels, width, label='Total liabilities')
    ax1.set_xlabel('Periods')
    ax1.legend()

    ax2 = ax1.twinx()

    debt_assets = [a / b * 100 for a, b in zip(t_liabl_labels, t_asset_labels)]
    ax2.plot(x_axis,debt_assets, color='red', label='Debt to Assets', lw=3)
    ax2.set_ylabel('%')
    ax2.legend(loc=2)

    plt.xticks(x_axis, x_axis)
    fig.tight_layout()
    plt.show()

def plot_income(years):
    fig, ax1 = plt.subplots()
    width = 0.22
    x_axis = np.arange(1, len(years) + 1)
    rev_labels = [int(getattr(year, 'rev', )) for year in years]
    net_labels = [int(getattr(year, 'net', )) for year in years]
    ax1.bar(x_axis - width / 2, rev_labels, width, label='Revenue')
    ax1.bar(x_axis + width / 2, net_labels, width, label='Net income')
    ax1.set_xlabel('Periods')
    ax1.legend()

    ax2 = ax1.twinx()

    profit_margin = [a / b * 100 for a, b in zip(net_labels, rev_labels)]
    ax2.plot(x_axis, profit_margin, color='red', label='Profit margin', lw=3)
    ax2.set_ylabel('%')
    ax2.legend(loc=2)

    plt.xticks(x_axis, x_axis)
    fig.tight_layout()
    plt.show()


def horizontal_analysis():
    while True:
        select_h_main = int(input("Enter the number of comparative periods\n 2 year\n 3 year\n 4 year: "))
        years = []
        for year_id in range(select_h_main):
            attrs = input_attrs('Enter ' + str(year_id + 1) + ' period data: ')
            year = Year(*attrs)
            years.append(year)

        while True:
            print("please select\n 1 - revenues\n 2 - cogs\n 3 - assets\n"
                  " 4 - liabilities\n 5 - equity\n 6 - net income")

            select_h_2 = int(input("Please enter selection"))

            if select_h_2 == 1:
                plot_plots(years, 'Revenue', 'rev')
            elif select_h_2 == 2:  # cogs
                plot_plots(years, 'Cost of goods', 'cogs')
            elif select_h_2 == 3:  # assets
                plot_plots(years, 'Assets', 'cogs')
            elif select_h_2 == 4:  # liabilities
                plot_plots(years, 'Liabilities', 'liab')
            elif select_h_2 == 5:  # equity
                plot_plots(years, 'Equity', 'equity')
            elif select_h_2 == 6:  # income
                plot_plots(years, 'Net income', 'net')
            else:
                print('Bad input, try again')
            end = input('Press any key to go back. If you want to quit, please enter "Q"')

            if end in ['q', 'Q']:
                sys.exit()


def vertical_analysis(manual_data_input):
    while True:
        if manual_data_input is True:
            import manual_input
            import functions_ratios
        else:
            import yahoo_finance
            import functions_ratios
        print(
            "please select pics\n 1 - current ratio analysis\n 2 - capital structure\n "
            "3 - cash conversion\n 4 - profitability")
        select_h_main = int(input("Please enter selection"))
        if select_h_main == 1:
            functions_ratios.current_ratio_pic()
        if select_h_main == 2:
            functions_ratios.capital_structure()
        if select_h_main == 3:
            functions_ratios.cash_conversion_cycle()
        if select_h_main == 4:
            functions_ratios.profitability()
        end = input('Enter "Q" if you wat to go back.\n Enter any key to select other option')
        if end in ('Q', 'q'):
            sys.exit()


def main_loop():
    while True:
        print("Welcome to financial analysis. This project will help you to visualise financial data. "
              "You can choose to compare historical data over a number of accounting periods (horizontal analysis) "
              "or analyse single reporting period (vertical analysis)")
        select_menu = int(input("Please enter\n1 (vertical analysis) \n2 (horizontal analysis) \n3 income statement\n4 balance sheet\n5 extract data from yahoo finance webpage"))
        if select_menu in [1, 2, 3, 4, 5]:
            if select_menu == 1:
                vertical_analysis(manual_data_input = True)
            elif select_menu == 2:
                horizontal_analysis()
            elif select_menu == 3:
                while True:
                    select_h_main = int(input("Enter the number of comparative periods\n 2 year\n 3 year\n 4 year: "))
                    years = []
                    for year_id in range(select_h_main):
                        attrs = input_attrs('Enter ' + str(year_id + 1) + ' period data: ')
                        year = Year(*attrs)
                        years.append(year)
                    plot_income(years)
                    end = input('Enter "Q" if you wat to go back.\n Enter any key to re enter periods')
                    if end in ('Q', 'q'):
                        sys.exit()
            elif select_menu == 4:
                while True:
                    select_h_main = int(input("Enter the number of comparative periods\n 2 year\n 3 year\n 4 year: "))
                    years = []
                    for year_id in range(select_h_main):
                        attrs = input_attrs('Enter ' + str(year_id + 1) + ' period data: ')
                        year = Year(*attrs)
                        years.append(year)
                    plot_balance(years)
            elif select_menu == 5:
                vertical_analysis(manual_data_input = False)
                import functions_ratios
            else:
                print("Wrong choice")
        end = input('Enter "Q" if you want to exit.\n Enter any key to select other option: ')
        if end in ['q', 'Q']:
            return


if __name__ == '__main__':
    main_loop()
