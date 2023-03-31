import tkinter as tk
import fnmatch
import os
import pygame
from pygame import mixer

class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='blue')
        label = tk.Label(self,text = 'AUDIO AND VIDEO PLAYER',bg = 'black',fg = 'yellow',font = ('Nexa Rust Slab-Trial Black Shadow 3',55))
        label.pack(pady = 19)
        Button = tk.Button(self, text="Music Player", font=("Arial", 25), command=lambda: controller.show_frame(SecondPage))
        Button.place(x=350, y=450)
        Button = tk.Button(self, text="Video Player", font=("Arial", 25), command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=650, y=450)


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='black')
        rootpath = "C:\\Users\my pc\Desktop\music"
        pattern = "*.mp3"
        mixer.init()
        prev_img = tk.PhotoImage(file = "prev_img.png")
        stop_img = tk.PhotoImage(file = "stop_img.png")
        play_img = tk.PhotoImage(file = "play_img.png")
        pause_img = tk.PhotoImage(file = "pause_img.png")
        next_img = tk.PhotoImage(file = "next_img.png")
        def select():
            rootpath = "C:\\Users\my pc\Desktop\music"
            pattern = "*.mp3"
            mixer.init()
            label.config(text = listBox.get("anchor"))
            mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
            mixer.music.play()
        def stop():
            mixer.music.stop()
            listBox.select_clear('active')
        def play_next():
            rootpath = "C:\\Users\my pc\Desktop\music"
            next_song = listBox.curselection()
            next_song = next_song[0] + 1
            next_song_name = listBox.get(next_song)
            label.config (text = next_song_name)
            mixer.music.load(rootpath + "\\" + next_song_name)
            mixer.music.play()
            listBox.select_clear(0,'end')
            listBox.activate(next_song)
            listBox.select_set(next_song)
        def play_prev():
            rootpath = "C:\\Users\my pc\Desktop\music"
            next_song = listBox.curselection()
            next_song = next_song[0] - 1
            next_song_name = listBox.get(next_song)
            label.config (text = next_song_name)
            mixer.music.load(rootpath + "\\" + next_song_name)
            mixer.music.play()
            listBox.select_clear(0,'end')
            listBox.activate(next_song)
            listBox.select_set(next_song)
        def pause_song():
            if pauseButton["text"] == "Pause":
                mixer.music.pause()
                pauseButton["text"] = "Play"
            else:
                mixer.music.unpause()
                pauseButton["text"] = "Pause"
        listBox = tk.Listbox(self,fg = "cyan",bg = "black",width = 25,font = ('Lusiana',22))
        listBox.pack(padx = 130, pady = 150)
        label = tk.Label(self,text = '',bg = 'black',fg = 'yellow',font = ('Lusiana',22))
        label.pack(pady = 1)
        top = tk.Frame(self, bg = "black")
        top.pack(padx = 10,pady = 5, anchor = 'center')
        prevButton = tk.Button(self, text="Prev", font=("Arial", 15), command= play_prev)
        prevButton.place(x=400, y=750)
        stopButton = tk.Button(self, text="Stop", font=("Arial", 15), command= stop)
        stopButton.place(x=500, y=750)
        playButton = tk.Button(self, text="Play", font=("Arial", 15), command= select)
        playButton.place(x=600, y=750)
        pauseButton = tk.Button(self, text="Pause", font=("Arial", 15), command= pause_song)
        pauseButton.place(x=700, y=750)
        nextButton = tk.Button(self, text="Next", font=("Arial", 15), command= play_next)
        nextButton.place(x=800, y=750)
        
        for root, dirs, files in os.walk(rootpath):
            for filename in fnmatch.filter(files,pattern):
                listBox.insert('end',filename)

        Button = tk.Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=580, y=830)

class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='Tomato')
        f = tk.Frame(self,borderwidth = 1,relief="groove")
        l_menu=tk.Label(f,text = "Video Player",font = ("rockwell",18,"bold"),fg = 'black',bg = 'lightpink')
        l_menu.pack(pady = 5)
        f.pack(pady = 5)
        lb =tk.Listbox(self,width = 55,height = 15,font = ("Helvetica",15),bg = "wheat")
        lb.pack()

        def ffplay(event):
            if lb.curselection():
                file = lb.curselection()[0]
                os.startfile(lb.get(file))
        for file in os.listdir():
            if file.endswith(".mp4"):
                lb.insert(0,file)
        bstart = tk.Button(self, text = "Play Video",font = ("Arial",14),bg = "Tan")
        bstart.pack(fill = 'x',expand = 'no')
        bstart.bind("<ButtonPress-1>",ffplay)
        def top():
            root.destroy()

        bstop = tk.Button(self,text = "Close",font = ("Arial",14),bg = "Tan",command = top)
        bstop.pack(fill = 'x',expand = 'no')
        
        Button = tk.Button(self, text="Home", font=("Arial", 20), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=650, y=650)

        Button = tk.Button(self, text="Back", font=("Arial", 20), command=lambda: controller.show_frame(SecondPage))
        Button.place(x=450, y=650)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")


app = Application()
app.maxsize(1900, 2500)
app.mainloop()
