
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import PIL

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1430x690+0+0")
        self.root.title("Face Recognition System")

         #First image 
        img = Image.open(r"C:\Users\Simon\Desktop\Face Recognition System\images\student.jpg")
        img = img.resize((400, 130),PIL.Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        #Second image
        img1 = Image.open(r"C:\Users\Simon\Desktop\Face Recognition System\images\student2.jpg")
        img1 = img1.resize((400, 130),PIL.Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=400, y=0, width=500, height=130)

        #Third image
        img2 = Image.open(r"C:\Users\Simon\Desktop\Face Recognition System\images\student1.jpg")
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

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1430,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=2,y=50,width=1260,height=600)

        #Left Label frame
        Left_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=600,height=530)

        img_Left = Image.open(r"C:\Users\Simon\Desktop\Face Recognition System\images\stud1.jpg")
        img_Left = img_Left.resize((680, 130),PIL.Image.LANCZOS)
        self.photoimg_Left = ImageTk.PhotoImage(img_Left)

        f_lbl = Label(Left_frame,image=self.photoimg_Left)
        f_lbl.place(x=2, y=0, width=680, height=130)

        #Current Course
        current_course_frame=LabelFrame(Left_frame,bg="white",bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=2,y=135,width=590,height=115)

        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",13,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,font=("times new roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        Semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,font=("times new roman",13,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","Sem-1","Sem-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class Student Course
       # class_student_frame=LabelFrame(Left_frame,bg="white",bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
       # class_student_frame.place(x=2,y=135,width=590,height=115)









        #Right Label frame
        Right_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=650,y=10,width=600,height=530)








        






if __name__ == "__main__":
    root = Tk() 
    obj = Student(root)
    root.mainloop()
