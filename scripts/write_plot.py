import pandas as pd
import matplotlib.pyplot as plt

def write_to_file(N, moves_history, T, n):
    if N<=1000:
        f = open('small_'+ str(T) + '_' + str(n) + '.txt', 'w')
    else:
        f = open('large_'+ str(T) + '_' + str(n) + '.txt', 'w')
    f.write(str(N))
    f.write("\n")
    for i in range(len(moves_history)):
        f.write(moves_history.loc[[i]]['date'].values[0])
        f.write(' ')
        f.write(moves_history.loc[[i]]['move'].values[0])
        f.write(' ')
        f.write(moves_history.loc[[i]]['stock'].values[0])
        f.write(' ')
        f.write(str(int(moves_history.loc[[i]]['Xvolume'].values[0])))
        f.write('\n')
    f.close()
    

def plot_profit_balance(profit,bal):
    del bal['date']   
    df_merged = pd.concat([profit, bal], axis=1)
    df_merged['date'] = pd.DatetimeIndex(df_merged['date']).year
    ax = df_merged.set_index('date').plot(figsize=(10,5), grid=True, kind= 'area',legend=True , stacked=True, title = 'Diagram of my profit and balance')
    ax.margins(0,0)
    plt.savefig('profit_balance.png', dpi=100)
    plt.show()