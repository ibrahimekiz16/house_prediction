import tkinter as tk
def butona_tıkla():
    etiket.config(text="saol king", bg = "LightGreen")

pencere = tk.Tk()
pencere.title("saol naber kingo")
pencere.geometry("640x480")

etiket = tk.Label(pencere ,text="tıkla")
etiket.pack(pady=180)

buton = tk.Button(pencere ,text=" tıkla kardeş", command=butona_tıkla)
buton.pack(pady=10)

pencere.mainloop()
