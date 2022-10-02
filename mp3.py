#pueden modificar la interfaz si desean, estare subiendo más proyectos en github
from tkinter import *
from pytube import YouTube
from moviepy.editor import *


root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("er Youtue Downloader")
root.configure(bg="#f2eee3")

Label(root, text='YouTube Video Downloader', font='arial 20 bold',bg="#f2eee3",fg="red").pack()

link = StringVar()
Label(root, text='Pega el link de YouTube aqui:', font='arial 15 bold',bg="#f2eee3").place(x=40, y=60)
link_enter = Entry(root, width=50, textvariable=link).place(x=32, y=90)


def dowloader():
	url = YouTube(str(link.get()))
	video = url.streams[1]
	video.download()
	Label(root, text='DOWLOADED',font='arial 15',bg="#f2eee3",fg="red").place(x=185, y=185)
	return video.download()

def converter():
	mp3_file = 'C:/Users/bioer/OneDrive/Escritorio/python mp3/Converted MP4.mp3'
	mp4_file = dowloader()
	videoclip =VideoFileClip(mp4_file)
	audioclip = videoclip.audio
	audioclip.write_audiofile(mp3_file)
	audioclip.close()
	videoclip.close()
	Label(root, text='CONVERTED',font='arial 15',bg="#f2eee3",fg="red").place(x=185, y=245)



dowload_mp4 = Button(root,
	text='DOWNLOAD',
	font='arial 15 bold',
	bg='pale violet red',
	padx=2,
	command=dowloader,
	fg="blue").place(x=180, y=150)




connvert_mp4 = Button(root,
       text='Convert to mp3',
       font='arial 15 bold',
       bg='pale violet red',
       padx=2,
       command=converter,
       fg="blue").place(x=180, y=210)

root.mainloop()

