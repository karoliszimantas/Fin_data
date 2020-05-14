import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# ratios
def days_sales_outstanding(financials):
    return int(financials['t_receivables'] / financials['rev'] * 365)


def days_payable_outstanding(financials):
    return int(financials['t_payables'] / financials['cogs'] * 365)


def days_inventory_outstanding(financials):
    return int(financials['inventory'] / financials['cogs'] * 365)


def roa_percentage(financials):
    return int(100 * (financials['tot_assets'] / financials['net_income']))


def roa(financials):
    return int(100 - roa_percentage(financials))


def operating_profit_percetenge(financials):
    return int(100 * (financials['ebit'] / financials['rev']))


def operating_profit(financials):
    return int(100 - operating_profit_percetenge(financials))


def roe_percetange(financials):
    return int(100 * (financials['tot_equity'] / financials['net_income']))


def roe(financials):
    return int(100 - roe_percetange(financials))


def current_ratio(financials):
    return int(financials['short_assets'] / financials['short_liabl'])


# graphics

def current_ratio_pic(financials):
    plt.xkcd()
    plt.text(0.8, 3.1, "Underperformance", fontsize=20)
    plt.text(1, 0.5, "Risk", fontsize=20)
    plt.ylabel("Current ratio")
    plt.xticks([])
    plt.bar(1, current_ratio(financials), label="Current ratio is {}".format(current_ratio(financials)))
    plt.legend(loc=8)
    plt.axhspan(0, 1, facecolor='red', alpha=0.5)
    plt.axhspan(3,5, facecolor='yellowgreen', alpha=0.5)
    plt.show()


def capital_structure(financials):
    plt.xkcd()
    plt.pie([financials['tot_liabl'], financials['tot_equity']],
            labels=["Liabilities", "Equity"],
            autopct='%1.1f%%',
            startangle=90,
            explode=(0, 0.1))
    plt.legend(loc=3)
    plt.title("Capital structure")
    plt.show()


def cash_conversion_cycle(financials):
    plt.xkcd()
    fig, ax = plt.subplots(1, 1)
    ax.bar(1, days_inventory_outstanding(financials), label="Inventory")
    ax.bar(1, days_sales_outstanding(financials), bottom=days_inventory_outstanding(financials), label="sale")
    ax.bar(1, days_payable_outstanding(financials), bottom=days_inventory_outstanding(financials) + days_sales_outstanding(financials),
           label="payable")
    ax.set_xlim(0, 1)
    plt.ylabel('Days')
    plt.xticks([])
    plt.legend()
    plt.show()


def profitability(financials):
    gs = gridspec.GridSpec(2, 2)
    plt.figure()

    ax1 = plt.subplot(gs[0, 0])
    plt.pie([roa(financials), roa_percentage(financials)],
            labels=['',str(roa_percentage(financials))+'%'],
            startangle=90,
            colors=["white", "red"])
    plt.title("Return on assets")
    circle = plt.Circle((0, 0), 0.8, fc="white")
    fig = plt.gcf()
    fig.gca().add_artist(circle)

    ax2 = plt.subplot(gs[0, 1])
    plt.pie([operating_profit(financials), operating_profit_percetenge(financials)],
            labels=['',str(operating_profit_percetenge(financials))+'%'],
            startangle=90,
            colors=["white", "red"])
    plt.title("Operating profit margin")
    circle = plt.Circle((0, 0), 0.8, fc="white")
    fig = plt.gcf()
    fig.gca().add_artist(circle)

    ax3 = plt.subplot(gs[1, :])
    plt.pie([roe(financials), roe_percetange(financials)],
            labels=['',str(roe_percetange(financials))+'%'],
            startangle=90,
            colors=["white", "red"])
    plt.title("Return on equity")
    circle = plt.Circle((0, 0), 0.8, fc="white")
    fig = plt.gcf()
    fig.gca().add_artist(circle)
    plt.show()
