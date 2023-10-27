#code by Richard Neumann (Energy Neumann)

import pyautogui
import time
import customtkinter

#failsafe to give you security, if you need to break the code
pyautogui.FAILSAFE = True
time.sleep(2)

#button function
def getDates():
    adc_number = int(entry_adc_number.get())
    for i in range(0, 31):
        time.sleep(3)
        pyautogui.click(x=564, y=46)
        pyautogui.write(str(i) * adc_number)
        pyautogui.press('enter')

#window
window = customtkinter.CTk()
window.geometry("500x300")

texto = customtkinter.CTkLabel(window, text="Do you want to add how many more units to the number, \n so that the search is not the same as the previous day? \n (Enter 0 if none)")
texto.pack(padx=10, pady=10)

entry_adc_number = customtkinter.CTkEntry(window)
entry_adc_number.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(window, text="Proceed", command=getDates)
botao.pack(padx=10, pady=10)

window.mainloop()


