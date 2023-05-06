import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# create lists from .csv
data = pd.read_csv('C:\\Users\\Andrii\\Downloads\\company_sales_data.csv')
month_list = data['month_number'].tolist()
facecream_list = data['facecream'].tolist()
facewash_list = data['facewash'].tolist()
toothpaste_list = data['toothpaste'].tolist()
bathingsoap_list = data['bathingsoap'].tolist()
shampoo_list = data['shampoo'].tolist()
moisturizer_list = data['moisturizer'].tolist()
units_list = data['total_units'].tolist()
profit_list = data['total_profit'].tolist()

# task 1
fig1, ax1 = plt.subplots()
ax1.plot(month_list, profit_list)
ax1.set_title('Company profit per month')
ax1.set_xlabel('Month number')
ax1.set_ylabel('Profit')
plt.xticks(month_list)
plt.yticks([100000, 200000, 300000, 400000, 500000])

# task 2
fig2, ax2 = plt.subplots()
ax2.plot(month_list, profit_list, ls='--', color='red', lw=3, marker='o', markerfacecolor='black',
         label='Profit data of last year')
ax2.set_title('Company Sales data of last year')
ax2.set_xlabel('Month number')
ax2.set_ylabel('Sold units number')
plt.xticks(month_list)
plt.yticks([100000, 200000, 300000, 400000, 500000])
ax2.legend(loc=4)

# task 3
fig3, ax3 = plt.subplots()
ax3.set_title('Sales data')
ax3.plot(month_list, facecream_list, ls='-', color='#FF0000', lw=3,
         marker='o', label='Face cream Sales Data')
ax3.plot(month_list, facewash_list, ls='-', color='#00CC00', lw=3,
         marker='o', label='Face wash Sales Data')
ax3.plot(month_list, toothpaste_list, ls='-', color='#0080FF', lw=3,
         marker='o', label='Toothpaste Sales Data')
ax3.plot(month_list, bathingsoap_list, ls='-', color='#B266FF', lw=3,
         marker='o', label='Bathing soap Sales Data')
ax3.plot(month_list, shampoo_list, ls='-', color='#FF8000', lw=3,
         marker='o', label='Shampoo Sales Data')
ax3.plot(month_list, moisturizer_list, ls='-', color='#660000', lw=3,
         marker='o', label='Moisturizer Sales Data')
ax3.set_xlabel('Month number')
ax3.set_ylabel('Sales units in number')
plt.xticks(month_list)
task3_list_number = [1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000]
plt.yticks(task3_list_number)
ax3.legend(loc=2)

# task 4
fig4, ax4 = plt.subplots()
ax4.set_title('Tooth paste Sales data')
ax4.plot(month_list, toothpaste_list, ls=' ', color='#0080FF', lw=3,
         marker='o', label='Tooth paste Sales Data')
ax4.grid(ls='--')
ax4.set_xlabel('Month number')
ax4.set_ylabel('Number of units Sold')
plt.xticks(month_list)
task4_list_number = np.arange(4500, 8001, 500)
plt.yticks(task4_list_number)
ax4.legend(loc=2)

# task 5
fig5, ax5 = plt.subplots()
ax5.set_title('Facewash and facecream sales data')
ax5.bar([x - 0.25 for x in month_list], facecream_list, width=0.25, align='edge', color='#0066CC',
        label='Face Cream sales data')
ax5.bar([x + 0.25 for x in month_list], facewash_list, width=-0.25, align='edge', color='#FF8000',
        label='Face Wash sales data')
ax5.grid(ls='--')
ax5.set_xlabel('Month number')
ax5.set_ylabel('Sales units in number')
plt.xticks(month_list)
task5_list_number = np.arange(500, 3501, 500)
plt.yticks(task5_list_number)
ax5.legend(loc=2)

# task 6
fig6, ax6 = plt.subplots()
ax6.set_title('bathing soap sales data')
ax6.bar(month_list, bathingsoap_list, color='#0066CC')
ax6.grid(ls='--')
ax6.set_xlabel('Month number')
ax6.set_ylabel('Sales units in number')
plt.xticks(month_list)
task6_list_number = np.arange(2000, 14001, 2000)
plt.yticks(task6_list_number)

# task 7
fig7, ax7 = plt.subplots()
ax7.set_title('Profit data')
profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
ax7.hist(profit_list, profit_range, color='#0066CC', label='Profit data')
ax7.set_xlabel('profit range in dollar')
ax7.set_ylabel('Actual Profit in dollar')
plt.xticks(profit_range)
plt.yticks(np.arange(0, 6, 1))
ax7.legend(loc=2)

# task 8
fig8, ax8 = plt.subplots()
ax8.set_title('Sales data')
labels = ['Facecream', 'Facewash', 'Toothpaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
sales_data = [data['facecream'].sum(), data['facewash'].sum(),
              data['toothpaste'].sum(), data['bathingsoap'].sum(),
              data['shampoo'].sum(), data['moisturizer'].sum()]
ax8.pie(sales_data, labels=labels, autopct='%1.1f%%')
ax8.legend(loc=4)

# task 9
fig9, ax9 = plt.subplots(2)
ax9[0].plot(month_list, bathingsoap_list, color='#000000', marker='o', lw=3,
            label='Bathingsoap Sales Data')
ax9[0].set_title('Sales data of a Bathingsoap')
ax9[1].plot(month_list, facewash_list, color='#FF0000', marker='o', lw=3,
            label='Face wash Sales Data')
ax9[1].set_title('Sales data of a facewash')

plt.xticks(month_list)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')

# task 10
fig10, ax10 = plt.subplots()
ax10.plot([], [], color='m', label='face cream', linewidth=4)
ax10.plot([], [], color='c', label='face wash', linewidth=4)
ax10.plot([], [], color='r', label='toothpaste', linewidth=4)
ax10.plot([], [], color='k', label='bathing soap', linewidth=4)
ax10.plot([], [], color='g', label='shampoo', linewidth=4)
ax10.plot([], [], color='y', label='moisturizer', linewidth=4)

ax10.stackplot(month_list, facecream_list, facewash_list, toothpaste_list, bathingsoap_list,
               shampoo_list, moisturizer_list, colors=['m', 'c', 'r', 'k', 'g', 'y'])
ax10.set_xlabel('Month number')
ax10.set_ylabel('Sales units in Number')
ax10.set_title('All product sales data using stack plot')
ax10.legend(loc=2)

plt.show()
