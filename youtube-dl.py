try:
    from pytube import YouTube
    import tkinter
except NameError:
    print("Error! Module(s) not found!")


class Program(tkinter.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.create_link_entry()
        self.create_audio_button()
        self.create_video_button()
        self.create_exit_button()

    def create_audio_button(self):
        audio_button = tkinter.Button(text="Audio", command=self.audio_download)
        audio_button.pack()

    def create_video_button(self):
        video_button = tkinter.Button(text="Video", command=self.video_download)
        video_button.pack()

    def create_exit_button(self):
        exit_button = tkinter.Button(text="Exit", command=self.master.destroy)
        exit_button.pack()

    def create_link_entry(self):
        self.link_entry = tkinter.Entry(width=75)
        self.link_entry.pack()

    def audio_download(self):
        video_url = str(self.link_entry.get())
        YouTube(video_url).streams.filter(only_audio=True).order_by("abr").desc().first().download(output_dir)

    def video_download(self):
        video_url = str(self.link_entry.get())
        YouTube(video_url).streams.filter(subtype="mp4").order_by("resolution").desc().first().download(output_dir)

link = "https://www.youtube.com/watch?v=2lAe1cqCOXo&t"
output_dir = "C:\Output"
root = tkinter.Tk()
root.geometry("500x500")
window = Program(master=root)
window.mainloop()
