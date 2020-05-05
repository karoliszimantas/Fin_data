import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# ratios
def days_sales_outstanding():
    return int(t_receivables / rev * 365)


def days_payable_outstanding():
    return int(t_payables / cogs * 365)


def days_inventory_outstanding():
    return int(inventory / cogs * 365)


def roa_percentage():
    return int(100 * (tot_assets / net_income))


def roa():
    return int(100 - roa_percentage())


def operating_profit_percetenge():
    return int(100 * (ebit / rev))


def operating_profit():
    return int(100 - operating_profit_percetenge())


def roe_percetange():
    return int(100 * (tot_equity / net_income))


def roe():
    return int(100 - roe_percetange())


def current_ratio():
    return int(short_assets / short_liabl)


# graphics

def current_ratio_pic():
    plt.xkcd()
    plt.text(0.8, 3.1, "Underperformance", fontsize=20)
    plt.text(1, 0.5, "Risk", fontsize=20)
    plt.ylabel("Current ratio")
    plt.xticks([])
    plt.bar(1, current_ratio(), label="Current ratio is {}".format(current_ratio()))
    plt.legend(loc=8)
    plt.axhspan(0, 1, facecolor='red', alpha=0.5)
    plt.axhspan(3,5, facecolor='yellowgreen', alpha=0.5)
    plt.show()


def capital_structure():
    plt.xkcd()
    plt.pie([tot_liabl, tot_equity],
            labels=["Liabilities", "Equity"],
            autopct='%1.1f%%',
            startangle=90,
            explode=(0, 0.1))
    plt.legend(loc=3)
    plt.title("Capital structure")
    plt.show()


def cash_conversion_cycle():
    plt.xkcd()
    fig, ax = plt.subplots(1, 1)
    ax.bar(1, days_inventory_outstanding(), label="Inventory")
    ax.bar(1, days_sales_outstanding(), bottom=days_inventory_outstanding(), label="sale")
    ax.bar(1, days_payable_outstanding(), bottom=days_inventory_outstanding() + days_sales_outstanding(),
           label="payable")
    ax.set_xlim(0, 1)
    plt.ylabel('Days')
    plt.xticks([])
    plt.legend()
    plt.show()


def profitability():
    gs = gridspec.GridSpec(2, 2)
    plt.figure()

    ax1 = plt.subplot(gs[0, 0])
    plt.pie([roa(), roa_percentage()],
            autopct='%1.1f%%',
            startangle=90,
            colors=["white", "red"])
    plt.title("Return on assets")
    circle = plt.Circle((0, 0), 0.8, fc="white")
    fig = plt.gcf()
    fig.gca().add_artist(circle)

    ax2 = plt.subplot(gs[0, 1])
    plt.pie([operating_profit(), operating_profit_percetenge()],
            autopct='%1.1f%%',
            startangle=90,
            colors=["white", "red"])
    plt.title("Operating profit margin")
    circle = plt.Circle((0, 0), 0.8, fc="white")
    fig = plt.gcf()
    fig.gca().add_artist(circle)

    ax3 = plt.subplot(gs[1, :])
    plt.pie([roe(), roe_percetange()],
            autopct='%1.1f%%',
            startangle=90,
            colors=["white", "red"])
    plt.title("Return on equity")
    circle = plt.Circle((0, 0), 0.8, fc="white")
    fig = plt.gcf()
    fig.gca().add_artist(circle)
    plt.show()
