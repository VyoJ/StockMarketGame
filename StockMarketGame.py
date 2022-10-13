import tkinter as tk
import random

name = "Stock name"
price_bought, number = 0, "Number of stocks bought"
stock = [["Apple Inc.", 499.3, 60], ["TATA Consumer Products Ltd.", 550.45, 8],
         ["Microsoft", 216.47, 12], ["Reliance Industries Ltd.", 208.77, 31.2],
         ["Jindal Steel & Power Ltd.", 199, 5], ["Airtel Ltd.", 514.65, 55],
         ["Cipla Ltd.", 728.6, 9], ["Bajaj Finance Ltd.", 670, 97],
         ["Intel Corporation", 277.25, 7],
         ["Apollo Hospitals Enterprises Ltd.", 103.9, 19.5],
         ["Amazon.com Inc.", 191.30, 6.5],
         ["Alphabet Inc. (Google)", 177.7, 3.5]]
transactions=[]     #[(day_num, buy/sell, name, price_bought, number)]
stock_bought = {}
money = 5000
daynum = 1
flag1, flag2, flag3 = 0, 0, 0

# Stock Price Variability Function
def rnge(start, stop):
    ''''
    Function to vary the price of a stock along with decimal variation
    Parameters:
    start- lower bound for increase/decrease in price
    stop- upper bound for increase/decrease in price
    Returns a value with variation in initial price
    '''
    dec_part1 = start % 1
    dec_part2 = stop % 1
    int_part1 = int(start - dec_part1)
    int_part2 = int(stop - dec_part2)
    dec_part1 = round(dec_part1 * 10)
    dec_part2 = round(dec_part2 * 10)
    int_random = random.randrange(int_part1, int_part2 + 1)
    dec_random = random.randrange(dec_part1, dec_part2 + 1)
    s = str(int_random) + "." + str(dec_random)
    return eval(s)


# Function to increase or decrease stock prices
def inc_dec():
    for i in range(len(stock)):
        if random.randrange(1, 3) > 1:
            # increase in price
            inc(stock, i)
        else:
            # decrease in price
            dec(stock, i)


# increase in price
def inc(a, i):
    a[i][1] = a[i][1] + rnge(0, a[i][2])


# decrease in price
def dec(b, i):
    b[i][1] = b[i][1] - rnge(0, b[i][2])


# Function to display stocks in a defined format.
def goodprinting(stock):
    stock_avail = ""
    for i in range(len(stock)):
        stock_avail = stock_avail + str(i + 1) + ": " + str(
            stock[i][0]) + ' : ' + str(stock[i][1]) + "\n"
    return stock_avail


#Function to create buttons of all stocks' names.
def buyWindow1():
    buy_root = tk.Tk()
    buy_root.configure(bg="#000000")

    def Button_Create(name, price):
        Button_new = tk.Button(
            buy_root,
            bg="#FFFFFF",
            fg="#000000",
            text=name + ": " + str(price),
            command=lambda: buyWindow2(name, price, 'Enter number of stocks to be bought:') or buy_root.destroy())
        Button_new.pack()

    for i in stock:
        Button_Create(i[0], i[1])
    buy_root.mainloop()


#Function to take input about which stock is to be bought.
def buyWindow2(name, price, Text):
    Window = tk.Tk()
    label = tk.Label(master=Window, text=Text)
    label.grid(row=0, column=0)

    entry = tk.Entry(master=Window, bg="#FFFFFF")
    entry.grid(row=0, column=1)

    button = tk.Button(
        master=Window,
        text="Submit",
        command=lambda: buy(name, entry.get(), price) or Window.destroy())
    button.grid(row=1, column=1)


#Function to buy the stock and add it to the gamer's portfolio.
def buy(name, numberofstocksbought, price):
    global money
    if int(numberofstocksbought) <= 0 or not (numberofstocksbought.isdigit(
    )) or money < int(numberofstocksbought) * price:
        buyWindow2(name, price, "Enter valid number of stocks to be bought")
    elif money > int(numberofstocksbought) * price:
        if len(stock_bought) > 0 and (name in stock_bought.keys()):
            stock_bought[name] += int(numberofstocksbought)
            money -= int(numberofstocksbought) * price
        else:
            stock_bought[name] = int(numberofstocksbought)
            money -= int(numberofstocksbought) * price
        events.insert(
            tk.END, "You have " + str(money) + " units of money." + "\n\n")
        events.see(tk.END)
        transactions.append((str(daynum),"BOUGHT",name,str(price),str(numberofstocksbought)))


def sellWindow1():
    sell_root = tk.Tk()
    sell_root.configure(bg="#000000")

    def Button_Create(name, price, number):
        Button_new = tk.Button(
            sell_root,
            bg="#FFFFFF",
            fg="#000000",
            text=name + ": " + str(price) + " No.: " + str(number),
            command=lambda: sellWindow2(name, price, 'Enter number of stocks to be sold:') or sell_root.destroy())
        Button_new.pack()

    p = 0
    for i in stock_bought:
        for j in stock:
            if i in j:
                p = j[1]
        if len(stock_bought) > 0:
            Button_Create(i, p, stock_bought[i])


def sellWindow2(name, price, Text):
    Window = tk.Tk()
    label = tk.Label(master=Window, text=Text)
    label.grid(row=0, column=0)

    entry = tk.Entry(master=Window, bg="#FFFFFF")
    entry.grid(row=0, column=1)

    button = tk.Button(
        master=Window,
        text="Submit",
        command=lambda: sell(name, entry.get(), price) or Window.destroy())
    button.grid(row=1, column=1)


def sell(name, number, price):
    global money
    if int(number) <= 0 or not (number.isdigit()) or int(number) > stock_bought[name]:
        sellWindow2(name, price, "Enter a valid number of stocks to be sold.")
    elif stock_bought[name] >= int(number):
        stock_bought[name] -= int(number)
        money += int(number) * price
        events.insert(tk.END, "You have " + str(money) + " units of money." + "\n\n")
        events.see(tk.END)
        transactions.append((str(daynum),"SOLD",name,str(price),str(number)))


def portfolio():
    
    global daynum
    global transactions
    displaystock = ""
    
    portfolio_root = tk.Tk()
    portfolio_root.geometry("600x600")

    labelHead = tk.Label(portfolio_root,
                         bg="#000000",
                         fg="#EAECEE",
                         text='Daily Portfolio',
                         font="Helvetica 13 bold",
                         pady=5)
    labelHead.place(relwidth=1)

    for i in stock_bought:
        if len(stock_bought) > 0:
            displaystock = displaystock + i + ": " + str(
                stock_bought[i]) + "\n"
        else:
            displaystock = "None"

    port_text = tk.Text(portfolio_root,
                       height=2,
                       bg="#000000",
                       fg="#EAECEE",
                       font="Helvetica 14",
                       padx=5,
                       pady=5)
    port_text.place(relheight=0.8, relwidth=1, rely=0.045)
    port_text.insert(tk.END, 'Your stocks: \n')
    port_text.insert(tk.END, displaystock + '\n\n')

    port_text.insert(tk.END, 'Your transaction history: \n')
    if bool(transactions):
        for i in transactions:
            port_text.insert(tk.END, ("Day Number: " + i[0] + ": " + i[1] + " " + i[4] + " stocks of " + i[2] + " for " + i[3] + " units \n"))
        port_text.insert(tk.END, '\n')
    port_text.see(tk.END)
    
    labelBottom = tk.Label(portfolio_root, bg="#000000", height=80)
    labelBottom.place(relwidth=1, rely=0.825)


def nextday():
    global daynum
    global money
    daynum += 1
    inc_dec()
    rand_events()
    events.insert(tk.END, "Day number " + str(daynum) + "\n\n")
    button_buy['state'] = tk.NORMAL
    
    if money < 1000 and money > 0:
        events.insert(tk.END, "Warning! You have only " + str(money) + " units left." + "\n\n")
    elif money <= 0:
        events.insert(tk.END, "You have spent all your units of money. You will be unable to buy anymore stocks\
 till you sell some stocks or get a bonus. \n\n")
        money = 0
        button_buy['state'] = tk.DISABLED

    if daynum == 20:
        events.insert(tk.END, "Your uncle is almost back! Maximise profits. \n\n")
    elif daynum == 28:
        events.insert(
            tk.END,
            "Your uncle is almost there gamer! You've done well. Keep up the hardwork, just a couple more days.\
 When your uncle comes back, he shall evaluate you based on your profit earned and the amount you currently have invested."
            + "\n\n")
    elif daynum == 29:
        events.insert(tk.END, "Hello Gamer. Your uncle will review your file in a while now. Make your final transactions\
 NOW! \n\n")
    elif daynum >= 30:
        events.insert(tk.END, "Your uncle has returned! Here is your game summary. \n\n")
        summary()
        button_buy['state'] = tk.DISABLED
        button_sell['state'] = tk.DISABLED
        button_portfolio['state'] = tk.DISABLED
        button_next['state'] = tk.DISABLED
    events.see(tk.END)


def summary():
    global money
    total = 0
    events.insert(tk.END, "Here is your remaining balance: " + str(money) + "\n")
    events.see(tk.END)
    cost = 1
    for i in stock_bought:
        for j in stock:
            if i in j:
                cost = j[1]
        total += cost * stock_bought[i]
    events.insert(tk.END, "The total amount of money (after selling your stocks) you have is " +
                  str(total + money) + "\n")
    events.see(tk.END)
    if (total + money) > 5000:
        events.insert(tk.END, "Congratulations! You have earned " + str((total+money) - 5000) +
            " units of money. You are a natural stockbroker.")
    elif (total + money) <= 5000:
        events.insert(tk.END, "You did not make any profit. Better luck next time!")
    events.see(tk.END)


def endgame():
    end_window = tk.Tk()
    label = tk.Label(
        master=end_window,
        text='Are you sure you want to leave. Your progress will not be saved.'
    )
    label.grid(row=0, column=1)

    Confirm_button = tk.Button(
        master=end_window,
        text="YES",
        fg='#006400',
        command=lambda: end_window.destroy() or root.destroy())
    Confirm_button.grid(row=1, column=0)

    Return_button = tk.Button(master=end_window,
                              text="NO",
                              fg='#FF0000',
                              command=end_window.destroy)
    Return_button.grid(row=1, column=2)


# Function to create random events.
def rand_events():
    global money
    global stock_bought
    global stock
    global flag1 
    global flag2
    global flag3
    number = random.randint(1, 50)
    
    if number == 51:
        events.insert(tk.END,
            "Scandal! The stock market has plummeted due to the revelation of a huge Ponzi scheme. You have lost\
 a lot of your money and all your stocks. You have to start again from scratch. \n\n")
        if money >= 1000:
            money = 1000
        stock_bought = {}
        events.insert(tk.END, "You have " + str(money) + " units of money. \n\n")
        events.see(tk.END)
    elif (number == 10 or number == 20 or number == 30) and (flag1 < 4):
        events.insert(tk.END, "Good Fortune! Increased employment and investment has awarded you with 1000 units of money! \n\n")
        money += 1000
        flag1 += 1
        events.insert(tk.END, "You have " + str(money) + " units of money. \n\n")
        events.see(tk.END)
    elif number == 15:
        if flag2 == 1:
            pass
        else:
            flag2 += 1
            events.insert(tk.END, "A new and upcoming company has reached new heights! It is now available to trade.\
 The company is called: Tesla and the stock price is 50.00 \n\n")
            stock.append(['Tesla', 50.0, 2.5])
        events.see(tk.END)
    elif number == 40:
        if flag3 == 0:
            events.insert(tk.END, "Cipla Ltd. has gone bankrupt! It has been removed from the stock market and all\
 stocks owned by you for it have been removed. \n\n")
            for i in stock:
                if 'Cipla Ltd.' == i[0]:
                    stock.remove(i)
            if 'Cipla Ltd.' in stock_bought.keys():
                stock_bought.pop('Cipla Ltd.')
            flag3 += 1
            events.see(tk.END)
        else:
            pass
    elif number==39:
        events.insert(tk.END, "Congratulations! Apple Inc. has gifted you a stock. Check your portfolio to find the stock. \n\n")
        if "Apple Inc." in stock_bought.keys():
            stock_bought["Apple Inc."] += 1
        else:
            stock_bought["Apple Inc."] = 1
        events.see(tk.END)
    elif number == 3:
        if "Reliance Industries Ltd." in stock_bought:
            events.insert(tk.END,
            "You have been caught insider trading for the Reliance Industries Ltd. As a result, you have been ordered to\
 pay a criminal fine of 1000 units \n\n")
            if money >= 1000:
                money -= 1000
            elif money < 1000 and money!=0:
                money = 0
            events.insert(tk.END, "You have " + str(money) + " units of money. \n\n")


# Main Window GUI
root = tk.Tk()
root.title("Stock Market Game")
root.geometry("1080x720")
Header = tk.Label(root,
                  bg="#000000",
                  fg="#EAECEE",
                  text='Events',
                  font="Helvetica 13 bold",
                  pady=5)
Header.place(relwidth=1)

events = tk.Text(root,
                 height=2,
                 bg="#000000",
                 fg="#EAECEE",
                 font="Helvetica 14",
                 padx=5,
                 pady=5)
events.place(relheight=0.8, relwidth=1, rely=0.045)

labelBottom = tk.Label(root, bg="#ABB2B9", height=80)
labelBottom.place(relwidth=1, rely=0.85)

scrollbar = tk.Scrollbar(root, command=events.yview, width=8)
scrollbar.pack(side=tk.RIGHT, fill='y')

#In-game scenario.
events.insert(
    tk.END,
    "Hello Gamer! You have been chosen by your stock broker uncle to continue his business\
 while he goes on a much deserved holiday. He has appointed you as his chief stock broker for 30 days and you\
 are determined to prove to him that you are a worthy successor. Try to make as much money as possible in these\
 30 days and impress your uncle. Good Luck and I hope you enjoy the game! \n\n"
)

#Instructions for the gamer to understand how to play.
events.insert(
    tk.END, '''Here are the instructions on how to play:
1. Click on the buy button to buy stocks. It will display the stock name as ABC: 123 where ABC is the name of the stock and 123 is it's current price.
2. Click on the sell button to sell stocks you already own. The stocks will be displayed as ABC: 123 No.: X, where ABC is name of the stock, 123 is the current price of the stock and X shows how many stocks you own.
3. Click on the Portfolio button to see the stocks you own and how many are owned. It also shows the current day in the game.
4. The next day button will take you to the next day. Click it once you have finished buying or selling all the stocks you want at some steady price. By clicking next day, the current price of the stocks will either increase or decrease and you can make a profit by selling those stocks you bought at a lower price in the previous days and selling them at higher prices caused due to the fluctuation in prices.
5. The close button will allow you to quit the game before it ends.
6. The main window labelled Events (where you are reading this) is where the amount of money you currently have will be displayed. There will also be in game announcements on that window that can give you more money or take some away.
Best of luck gamer! We hope you enjoy.

''')

events.insert(tk.END, "You have " + str(money) + " units of money." + "\n\n")

#Buttons for each function: buying, selling and checking the portfolio
#To create button for buying stocks.
button_buy = tk.Button(labelBottom,
                       text="BUY",
                       font="Helvetica 10 bold",
                       width=20,
                       bg="#ABB2B9",
                       fg="#008000",
                       command=buyWindow1)
button_buy.place(relx=0, rely=0.008, relheight=0.06, relwidth=0.22)

#To create button for selling stocks.
button_sell = tk.Button(labelBottom,
                        text="SELL",
                        font="Helvetica 10 bold",
                        width=20,
                        bg="#ABB2B9",
                        fg="#FF0000",
                        command=sellWindow1)
button_sell.place(relx=0.25, rely=0.008, relheight=0.06, relwidth=0.22)

#To create button for showing gamer's portfolio.
button_portfolio = tk.Button(labelBottom,
                             text="PORTFOLIO",
                             font="Helvetica 10 bold",
                             width=20,
                             bg="#ABB2B9",
                             command=portfolio)
button_portfolio.place(relx=0.50, rely=0.008, relheight=0.06, relwidth=0.22)

#To create button for progressing the game to the next day.
button_next = tk.Button(labelBottom,
                        text="NEXT DAY",
                        font="Helvetica 10 bold",
                        width=20,
                        bg="#ABB2B9",
                        fg="#008000",
                        command=nextday)
button_next.place(relx=0.75, rely=0.008, relheight=0.06, relwidth=0.22)

#To create a button through which the game can be ended early.
button_exit = tk.Button(Header,
                        text="CLOSE X",
                        bg="#FF0000",
                        command=lambda: endgame())
button_exit.place(relx=0.94)
events.config(cursor="arrow")
