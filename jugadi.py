from tkinter import *
from PIL import ImageTk, Image

class GraphicalPasswordAuthentication:
    def __init__(self, master):
        self.master = master
        master.title("Graphical Password Authentication")

        self.password = []

        self.img1 = ImageTk.PhotoImage(Image.open("E:\Programming Projects\Python Projects\JugadiNotepadimg.jpg"))
        self.img2 = ImageTk.PhotoImage(Image.open("E:\Programming Projects\Python Projects\JugadiNotepad\img2.jpg"))
        self.img3 = ImageTk.PhotoImage(Image.open("E:\Programming Projects\Python Projects\JugadiNotepad\img3.jpg"))
        self.img4 = ImageTk.PhotoImage(Image.open("E:\Programming Projects\Python Projects\JugadiNotepad\img4.jpg"))
        self.img5 = ImageTk.PhotoImage(Image.open("E:\Programming Projects\Python Projects\JugadiNotepad\img5.jpg"))
        self.img6 = ImageTk.PhotoImage(Image.open("E:\Programming Projects\Python Projects\JugadiNotepad\img6.jpg"))
        # self.img7 = ImageTk.PhotoImage(Image.open("image7.jpg"))
        # self.img8 = ImageTk.PhotoImage(Image.open("image8.jpg"))
        # self.img9 = ImageTk.PhotoImage(Image.open("image9.jpg"))

        self.img_list = [self.img1, self.img2, self.img3, self.img4, self.img5, self.img6]

        self.img_btn1 = Button(master, image=self.img1, command=lambda: self.select_image(self.img1))
        self.img_btn2 = Button(master, image=self.img2, command=lambda: self.select_image(self.img2))
        self.img_btn3 = Button(master, image=self.img3, command=lambda: self.select_image(self.img3))
        self.img_btn4 = Button(master, image=self.img4, command=lambda: self.select_image(self.img4))
        self.img_btn5 = Button(master, image=self.img5, command=lambda: self.select_image(self.img5))
        self.img_btn6 = Button(master, image=self.img6, command=lambda: self.select_image(self.img6))
        # self.img_btn7 = Button(master, image=self.img7, command=lambda: self.select_image(self.img7))
        # self.img_btn8 = Button(master, image=self.img8, command=lambda: self.select_image(self.img8))
        # self.img_btn9 = Button(master, image=self.img9, command=lambda: self.select_image(self.img9))

        self.img_btn_list = [self.img_btn1, self.img_btn2, self.img_btn3, self.img_btn4, self.img_btn5, self.img_btn6]

        for img_btn in self.img_btn_list:
            img_btn.pack(side=LEFT, padx=10, pady=10)

    def select_image(self, img):
        self.password.append(img)

        if len(self.password) == 3:
            if self.password[0] == self.password[1] == self.password[2]:
                print("Password accepted!")
            else:
                print("Invalid password!")
            self.password = []

root = Tk()
gp_auth = GraphicalPasswordAuthentication(root)
root.mainloop()
