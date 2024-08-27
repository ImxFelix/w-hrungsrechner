import freecurrencyapi
import tkinter as tk

client = freecurrencyapi.Client('fca_live_zhgKbiCo5Jq57Enxbfl2OwlfTHfNoSmvcHBa4Noo')

def get_exchange_rate(cur_name):
    result = client.latest()
    exchange_rate = result['data'][cur_name]
    return exchange_rate



def button_click():
    l2.config(text=get_exchange_rate(e1.get()))

mainWindow = tk.Tk()
mainWindow.title('Währungsrechner')

l1 = tk.Label(mainWindow, text="Währung: ")
l1.grid(row=0, column=0)

l2 = tk.Label(mainWindow, text="0")
l2.grid(row=0, column=1)


e1 = tk.Entry(mainWindow)
e1.grid(row=1, column=1)

button = tk.Button(mainWindow, text="Umrechnen", command=button_click)
button.grid()

mainWindow.mainloop()
