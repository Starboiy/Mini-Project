from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import PIL

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1430x690+0+0")
        self.root.title("Face Recognition System")

       #First image 
        img = Image.open(r"C:\Users\Simon\Desktop\Face Recognition System\images\scan.png")
        img = img.resize((400, 130),PIL.Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        #Second image
        img1 = Image.open(r"C:\Users\Simon\Desktop\Face Recognition System\images\college.jpeg")
        img1 = img1.resize((400, 130),PIL.Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=400, y=0, width=500, height=130)

        #Third image
        img2 = Image.open(r"C:\Users\Simon\Desktop\Face Recognition System\images\face.webp")
        img2 = img2.resize((400, 130),PIL.Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=800, y=0, width=500, height=130)

         #bg image
        img3 = Image.open(r"C:\Users\Simon\Desktop\Face Recognition System\images\bg.jpg")
        img3 = img3.resize((1430,690),PIL.Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1430, height=690)

        title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1430,height=45)

        #Student button
        img4 = Image.open(r"C:\Users\Simon\Desktop\Face Recognition System\images\smart.webp")
        img4 = img4.resize((220,220),PIL.Image.LANCZOS)
        self.photoimg4= ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=100,y=100,width=220,height=200)

        b1_1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=300,width=220,height=40)

        #Detect Face button
        img5 = Image.open(r"C:\Users\Simon\Desktop\Face Recognition System\images\man.jpeg")
        img5 = img5.resize((220,220),PIL.Image.LANCZOS)
        self.photoimg5= ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=400,y=100,width=220,height=200)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=300,width=220,height=40)

        #Attendence Face button
        img6 = Image.open(r"C:\Users\Simon\Desktop\Face Recognition System\images\3p.jpg")
        img6 = img6.resize((220,220),PIL.Image.LANCZOS)
        self.photoimg6= ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=700,y=100,width=220,height=200)

        b1_1=Button(bg_img,text="Attendence",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=300,width=220,height=40)

        #Help button
        img7 = Image.open(r"C:\Users\Simon\Desktop\Face Recognition System\images\bg.jpg")
        img7 = img7.resize((220,220),PIL.Image.LANCZOS)
        self.photoimg7= ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1000,y=100,width=220,height=200)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=300,width=220,height=40)

        #Train Face button
        img8 = Image.open(r"C:\Users\Simon\Desktop\Face Recognition System\images\fin.webp")
        img8 = img8.resize((220,220),PIL.Image.LANCZOS)
        self.photoimg8= ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=100,y=350,width=220,height=200)

        b1_1=Button(bg_img,text="Train the Model",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=550,width=220,height=40)



if __name__ == "__main__":
    root = Tk() 
    obj = Face_Recognition_System(root)
    root.mainloop()
