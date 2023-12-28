import tkinter as tk
import joblib
import ttkbootstrap as ttk

regression_tree = joblib.load('trained_model.joblib')
label_encoder = joblib.load('label_encoder.joblib')


def predictor(input_car_name, input_car_year, input_car_mileage, input_car_accident, input_car_owner):
    try:
        input_car_name_encoded = label_encoder.transform([input_car_name])[0]
        predicted_price = regression_tree.predict(
            [[input_car_name_encoded, input_car_year, input_car_mileage, input_car_accident, input_car_owner]])
        return predicted_price
    except ValueError:
        output_str.set('It is not availabe')


def on_entry_click(event, entry):
    entry.delete(0, "end")


def convert():
    input_car_name = entry1.get().strip().lower().replace(' ', '')
    input_car_year = entry2.get()
    input_car_mileage = entry3.get()
    input_car_accident = entry4.get()
    input_car_owner = entry5.get()

    predicted_price = predictor(input_car_name, input_car_year,
                                input_car_mileage, input_car_accident, input_car_owner)
    result = str(predicted_price)
    result = result.replace('[', '').replace(']', '').replace('.', '')

    result = "$ " + str(result)
    # print(result)

    if result != '$ None':
        output_str.set(result)


window = ttk.Window(themename='journal')
window.title('AI')
window.geometry('280x370')

title_label = ttk.Label(
    master=window, text="Enter car's properties", font='kalameh 10')
title_label.pack()

input_frame = ttk.Frame(master=window)

entry1_string = tk.StringVar()
entry2_int = tk.StringVar()
entry3_int = tk.StringVar()
entry4_int = tk.StringVar()
entry5_int = tk.StringVar()


def on_entry_click(event, entry, default_text):
    if entry.get() == default_text:
        entry.delete(0, "end")
    entry.config(foreground="black")


def on_focus_out(event, entry, default_text):
    if not entry.get():
        entry.insert(0, default_text)
        entry.config(foreground="light gray")


entry1 = ttk.Entry(master=input_frame)
entry1.insert(0, 'Enter car name')
entry1.config(foreground="light gray")
entry1.bind("<FocusIn>", lambda event, entry=entry1,
            default_text='Enter car name': on_entry_click(event, entry, default_text))
entry1.bind("<FocusOut>", lambda event, entry=entry1,
            default_text='Enter car name': on_focus_out(event, entry, default_text))
entry1.bind("<Button-1>", lambda event, entry=entry1,
            default_text='Enter car name': on_entry_click(event, entry, default_text))

entry2 = ttk.Entry(master=input_frame)
entry2.insert(0, 'Enter car year')
entry2.config(foreground="light gray")
entry2.bind("<FocusIn>", lambda event, entry=entry2,
            default_text='Enter car year': on_entry_click(event, entry, default_text))
entry2.bind("<FocusOut>", lambda event, entry=entry2,
            default_text='Enter car year': on_focus_out(event, entry, default_text))
entry2.bind("<Button-1>", lambda event, entry=entry2,
            default_text='Enter car year': on_entry_click(event, entry, default_text))

entry3 = ttk.Entry(master=input_frame)
entry3.insert(0, 'Enter car mileage')
entry3.config(foreground="light gray")
entry3.bind("<FocusIn>", lambda event, entry=entry3,
            default_text='Enter car mileage': on_entry_click(event, entry, default_text))
entry3.bind("<FocusOut>", lambda event, entry=entry3,
            default_text='Enter car mileage': on_focus_out(event, entry, default_text))
entry3.bind("<Button-1>", lambda event, entry=entry3,
            default_text='Enter car mileage': on_entry_click(event, entry, default_text))

entry4 = ttk.Entry(master=input_frame)
entry4.insert(0, 'Enter car accident(s)')
entry4.config(foreground="light gray")
entry4.bind("<FocusIn>", lambda event, entry=entry4,
            default_text='Enter car accident(s)': on_entry_click(event, entry, default_text))
entry4.bind("<FocusOut>", lambda event, entry=entry4,
            default_text='Enter car accident(s)': on_focus_out(event, entry, default_text))
entry4.bind("<Button-1>", lambda event, entry=entry4,
            default_text='Enter car accident(s)': on_entry_click(event, entry, default_text))

entry5 = ttk.Entry(master=input_frame)
entry5.insert(0, 'Enter car owner(s)')
entry5.config(foreground="light gray")
entry5.bind("<FocusIn>", lambda event, entry=entry5,
            default_text='Enter car owner(s)': on_entry_click(event, entry, default_text))
entry5.bind("<FocusOut>", lambda event, entry=entry5,
            default_text='Enter car owner(s)': on_focus_out(event, entry, default_text))

button = ttk.Button(master=input_frame, text='predict', command=convert)

entry1.pack()
entry2.pack()
entry3.pack()
entry4.pack()
entry5.pack()

button.pack(pady=20, padx=20,)
input_frame.pack()

output_str = tk.StringVar()
output_label = ttk.Label(master=input_frame, textvariable=output_str)
output_label.pack()

window.mainloop()
