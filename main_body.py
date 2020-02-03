import numpy as np
import matplotlib.pyplot as plt


# Objective-oriented programming
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


def delta_1_year(year_1, year_2):
    delta = (int(year_2.rev) - int(year_1.rev)) / int(year_1.rev) * 100
    return round(delta, 2)


def plot_plots(years, ylabel, attribute):
    plt.style.use("bmh")  # revenue
    x_axis = np.arange(1, len(years) + 1)
    labels = [int(getattr(year, attribute)) for year in years]
    plt.bar(x_axis, labels)
    # plt.text(2, int(year2.rev) + .25, str(Delta_1_year()) + '%', color=Colo)
    # Under development. Associated with Delta and Color_change f-tions.
    plt.xlabel('Periods')
    plt.ylabel(ylabel)
    plt.xticks(x_axis, x_axis)
    plt.show()


def vertical_analysis():
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
                return


def horizontal_analysis():
    import functions
    # Under development. Target: differentiate colors regarding the value
    # def Second_color():
    #     if roe_percetange() or operating_profit_percetenge() or roa_percentage() < 5:
    #         return "red"
    #     elif roe_percetange or operating_profit_percetenge() or roa_percentage() > 5 and
    #     roe_percetange or operating_profit_percetenge() or roa_percentage() < 10:
    #         return "yellow"
    #     else:
    #         return "green"
    # pie_chart_colors = ['white', Second_color()]
    while True:
        print(
            "please select pics\n 1 - current ratio analysis\n 2 - capital structure\n "
            "3 - cash conversion\n 4 - profitability")
        select_h_main = int(input("Please enter selection"))
        if select_h_main == 1:
            functions.current_ratio_pic()
        if select_h_main == 2:
            functions.capital_structure()
        if select_h_main == 3:
            functions.cash_conversion_cycle()
        if select_h_main == 4:
            functions.profitability()
        end = input('Enter "Q" if you wat to go back.\n Enter any key to select other option')
        if end in ('Q', 'q'):
            return


def main_loop():
    while True:
        print("Welcome to financial analysis. This project will help you to visualise financial data. "
              "You can choose to compare historical data over a number of accounting periods (horizontal analysis) "
              "or analyse single reporting period (vertical analysis)")
        select_menu = int(input("Please enter 1 (vertical analysis) or 2 (horizontal analysis): "))
        if select_menu in [1, 2]:
            if select_menu == 1:
                # under development. Target: to identify delta between values and diferiancate color of text according to output
                # class Features:
                #      def Delta_1_year(self, delta):
                #          self.delta = (int(year2.rev) - int(year1.rev)) / int(year1.rev) * 100
                #          return round(self.delta, 2)
                #
                #      def Color_change(self):
                #          if self.delta < 0:
                #              Colo = 'r'
                #          elif self.delta > 0:
                #              Colo = 'g'
                vertical_analysis()

            elif select_menu == 2:
                # Functional programing
                horizontal_analysis()
            else:
                print("Wrong choice")
        end = input('Enter "Q" if you want to exit.\n Enter any key to select other option: ')
        if end in ['q', 'Q']:
            return


if __name__ == '__main__':
    main_loop()
