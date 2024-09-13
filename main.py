import freecurrencyapi
import tkinter as tk

client = freecurrencyapi.Client('fca_live_zhgKbiCo5Jq57Enxbfl2OwlfTHfNoSmvcHBa4Noo')

def get_currency_names():
    result = client.latest()
    data = result['data']
    names = []
    for key in data:
        names.append(key)
    return names

def dropdown_from_currency_changed(var, index, mode):
    print("dropdown_from_currency_changed")

def dropdown_to_currency_changed(var, index, mode):
    print("dropdown_to_currency_changed")


# Funktion zum validieren der Eingaben
def validate_input(P):
    if str.isdigit(P) or str(P) == "" or str(P) == ".":
        return True
    else:
        return False


# Main Window Ui Stuff
mainWindow = tk.Tk()
mainWindow.title('Währungsrechner')
mainWindow.geometry('300x300')

vcmd = (mainWindow.register(validate_input))

# Die Optionen für die Dropdowns
options = get_currency_names()

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
input_from_currency = tk.Entry(mainWindow, validate='all', validatecommand=(vcmd, '%P'))
input_from_currency.grid(row=1, column=0)



# Zweites Eingabefeld
input_to_currency = tk.Entry(mainWindow , validate='all', validatecommand=(vcmd, '%P'))
input_to_currency.grid(row=1, column=2)

# Start Main Loop
mainWindow.mainloop()
