import tkinter as tk

main_window = tk.Tk()

def event_tekan():
    label2 = tk.Label(main_window, text = "aku disentuh ^_^")
    label2.pack()

label = tk.Label(main_window, text = "halo, saya adalah \nGUI sederhana dengan")
tombol = tk.Button(main_window, text = "tekan aku please", command = event_tekan)

label.pack()
tombol.pack()
main_window.mainloop()