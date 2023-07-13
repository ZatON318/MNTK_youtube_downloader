import tkinter
import customtkinter
import yt_dlp
import os

from tkinter import filedialog
from tkinter import font
from tkinter import ttk
import xml
import xml.etree
import xml.etree.ElementTree
import http.cookies
import html.parser
import uuid
import fileinput

def startDownload():
    output_dir = "stiahnute" 
    url = link_var.get()
    selected_option = optionmenu_var.get()
    print(selected_option)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
    }
    
    if selected_option == "mp3":
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    elif selected_option == "mp4 - 1080p":
        ydl_opts['format'] = 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080]'
    elif selected_option == "mp4 - 720p":
        ydl_opts['format'] = 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720]'


    print(ydl_opts)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        lbl_download_finished.configure(text="Stiahnute úspešne, jeej!")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("600x250")
app.title("MNTK YouTube Downloader - 1.0")
app.resizable(False, False)

# UI
title = customtkinter.CTkLabel(app, text="Tu vlož svoj youtube link (ak to je link na playlist stiahne ho to celý)")
title.pack(padx=10, pady=10)

link_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=400, height=40, textvariable=link_var)
link.pack(padx=10, pady=10)

btn_download = customtkinter.CTkButton(app, text="Stiahnuť", command=startDownload)
btn_download.pack()

optionmenu_var = customtkinter.StringVar(value="mp3")
optionmenu = customtkinter.CTkOptionMenu(app, values=["mp3", "mp4 - 1080p", "mp4 - 720p"], variable=optionmenu_var)
optionmenu.pack(padx=10, pady=10)

lbl_download_finished = customtkinter.CTkLabel(app, text="")
lbl_download_finished.pack()

app.mainloop()
