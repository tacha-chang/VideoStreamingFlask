import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def Privacy():
    tk.Tk().withdraw()
    messagebox.showinfo(title="Privacy Notice",message=" thus, we provide this privacy notice to inform our customers of our policy in relation to the collection, use and disclosure of personal data of individual (“you”) in accordance with the Personal Data Protection Act B.E. 2562 (“PDPA”), relevant laws and regulations. This privacy notice informs you of how we collect, use or disclose your personal data, what and why we collect, use or disclose your personal data, how long we hold it, who we disclose it to, your rights, what steps we will take to make sure your personal data stays private and secure, and how you can contact us.")
def popupmsg():
    msg = " thus, we provide this privacy notice to inform our customers of our policy in relation to the collection,\n use and disclosure of personal data of individual (“you”) in accordance with the Personal Data Protection Act B.E. 2562 (“PDPA”),\n relevant laws and regulations. This privacy notice informs you of how we collect, use or disclose your personal data,\n what and why we collect, use or disclose your personal data, how long we hold it, who we disclose it to, your rights,\n what steps we will take to make sure your personal data stays private and secure, and how you can contact us."
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="CONFIRM", command = popup.destroy)
    B1.pack()
    popup.mainloop()
