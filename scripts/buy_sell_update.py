import pandas as pd
#possible buy stocks
def to_buy(df, profit, datetrack, daterange):
    mask = (df['Date'] > datetrack)
    df_buy =  df[mask]
    df_buy = df_buy[df_buy['Date'] <= str(daterange[-1]).split()[0]]
    df_buy = df_buy[df_buy['Low'] <= profit['profit'].iloc[-1]]
    return df_buy

#possible sell stocks
def to_sell(df, stocks_bought, datetrack, daterange):
    if not(stocks_bought.empty):
        mask = (df['Date'] > datetrack) 
        df_sell = df[mask]
        df_sell = df_sell[df_sell['Date'] <= str(daterange[-1]).split()[0]]
        df_sell = df_sell[df_sell['Stock'].isin(list(stocks_bought['stocks'].values))]
        return df_sell
        
    else:       
        return pd.DataFrame()


def decide(df, profit, stocks_bought, datetrack, daterange):
    df_buy = to_buy(df, profit, datetrack, daterange)
    df_sell = to_sell(df, stocks_bought, datetrack, daterange)
    
    if df_buy.empty and df_sell.empty: return 'stop', pd.DataFrame()
    temp_dfs = []
    if df_buy.empty:
        for stock in list(df_sell.Stock.unique()):
            temp = df_sell.loc[df_sell['Stock'] == stock]
            volume_bought = stocks_bought.loc[stocks_bought['stocks'] == stock]['volume'].values[0]
            pricepaid = stocks_bought.loc[stocks_bought['stocks'] == stock]['pricepaid'].values[0]
            temp.loc[temp['Volume'] >= volume_bought, 'VolumeToSell'] = volume_bought
            temp.loc[temp['Volume'] < volume_bought, 'VolumeToSell'] = temp['Volume']

            temp['difference'] =  (temp['High'] * temp['VolumeToSell'] ) - pricepaid 
            temp['earning'] =  temp['High'] * temp['VolumeToSell']
            temp = temp.loc[temp['difference'] > 0]
            temp_dfs.append(temp)
        if(len(temp_dfs)!=0):
            result = pd.concat(temp_dfs, ignore_index = True)
            result = result.sort_values(by =['Date'])
            return 'sell', result
        else:
            return 'stop', pd.DataFrame() 
    else:
        return 'buy', df_buy


def buy_low(dcion_df):
    dcion_df['variance'] = dcion_df['High'] / dcion_df['Low']
    groupby = dcion_df.groupby(['Stock'])['variance'].mean()
    groupby = groupby.sort_values(ascending=False)
    a = groupby.idxmax() # stock i want!
    stock_interested = dcion_df[dcion_df['Stock'] == a]
    
    return stock_interested.loc[stock_interested['Low'].idxmin()]
 
def sell_high(dcion_df):
    return dcion_df.loc[dcion_df['difference'].idxmax()]

def update_balance(df,stocks_bought,datetrack, profit):
    balance_sum = profit
    mystocks = list(stocks_bought.stocks.unique()) 
    myvolume = list(stocks_bought.volume.unique()) 
    myStockVol = zip(mystocks,myvolume)            
    
    for i,vol in myStockVol:
        myrow = df.loc[(df['Date'] == datetrack) & (df['Stock']== i)]
        if not(myrow.empty):
            close_price = myrow['Close'].values[0]
            balance_sum += vol * close_price
        else:
            continue

    return  balance_sum