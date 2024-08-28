import freecurrencyapi
import tkinter as tk

client = freecurrencyapi.Client('fca_live_zhgKbiCo5Jq57Enxbfl2OwlfTHfNoSmvcHBa4Noo')

def get_exchange_rate(cur_name):
    result = client.latest()
    exchange_rate = result['data'][cur_name]
    return exchange_rate


def dropdown_from_currency_changed(var, index, mode):
    print("dropdown_from_currency_changed")

def dropdown_to_currency_changed(var, index, mode):
    print("dropdown_to_currency_changed")




def callback(self, P):
    if str.isdigit(P) or P == "" or P == ".":
        return True
    else:
        return False

def button_click():
    l2.config(text=get_exchange_rate(e1.get()))

mainWindow = tk.Tk()
mainWindow.title('Währungsrechner')
mainWindow.geometry('300x300')

vcmd = (mainWindow.register(callback))


# Erstes Dropdown
dropdown_from_currency_clicked = tk.StringVar()
dropdown_from_currency_clicked.set(options[8])
dropdown_from_currency_clicked.trace_add("write", dropdown_from_currency_changed)
dropdown_from_currency = tk.OptionMenu(mainWindow, dropdown_from_currency_clicked, *options)
dropdown_from_currency.grid(row=0, column=0)

# Zweites Dropdown
dropdown_to_currency_clicked = tk.StringVar()
dropdown_to_currency_clicked.set(options[31])
dropdown_to_currency_clicked.trace_add("write", dropdown_to_currency_changed)
dropdown_to_currency = tk.OptionMenu(mainWindow, dropdown_to_currency_clicked, *options)
dropdown_to_currency.grid(row=0, column=2)

# Erstes Eingabefeld
input_from_currency = tk.Entry(mainWindow)
input_from_currency.grid(row=1, column=0)


# Zweites Eingabefeld
input_to_currency = tk.Entry(mainWindow , validate='all', validatecommand=(vcmd, '%P'))

input_to_currency.grid(row=1, column=2)

mainWindow.mainloop()
