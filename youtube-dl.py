try:
    from pytube import YouTube
    import tkinter as tk
    import requests
    from tkinter import messagebox

except NameError:
    print("Error! Module(s) not found!")


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Audio Button
        self.audio = tk.Button(text="Audio",command=self.audio_download)
        self.audio.place(x=200, y=300)
        # Video Button
        self.video = tk.Button(text="Video", command=self.video_download)
        self.video.place(x=275, y=300)
        # Link Input
        url_x = 50
        url_y = 150
        self.url_textbox = tk.Entry(width=50)
        self.url = tk.Label(text="URL:").place(x=url_x, y=url_y)
        self.url_textbox.insert(0,"https://")
        self.url_textbox.place(x=url_x+91, y=url_y)
        # Output Directory
        output_x = 50
        output_y = 200
        self.output_directory_textbox = tk.Entry(width=50)
        self.output_directory = tk.Label(text="Output: ").place(x=output_x, y=output_y)
        self.output_directory_textbox.insert(0, "C:/Output")
        self.output_directory_textbox.place(x=output_x+91, y=output_y)
        # Exit Button
        self.exit = tk.Button(text="Exit", command=self.master.destroy)
        self.exit.place(x=450,y=350)

    def link_is_valid(self):
        try:
            link = requests.get(str(self.url_textbox.get()))
            if "Video unavailable" in link.text:
                messagebox.showerror(title="Error", message="Invalid Link! Please try again.")
            else:
                return True
        except:
            messagebox.showerror(title="Error", message="Invalid link! Please try again.")

    def audio_download(self):
        if self.link_is_valid():
            YouTube(self.url_textbox.get()).streams.filter(only_audio=True).order_by("abr").desc().first().download(self.output_directory_textbox.get())
            messagebox.showinfo(title="Success", message="Audio successfully downloaded!")

    def video_download(self):
        if self.link_is_valid():
            YouTube(self.url_textbox.get()).streams.filter(subtype="mp4").order_by("resolution").desc().first().download(self.output_directory_textbox.get())
            messagebox.showinfo(title="Success", message="Video successfully downloaded!")


test_link = "https://www.youtube.com/watch?v=2lAe1cqCOXo&t"
root = tk.Tk()
root.geometry("500x400")
root.resizable(False,False)
app = Application(master=root)
app.mainloop()
