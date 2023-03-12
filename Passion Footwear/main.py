from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
import math,random,os
from PIL import Image, ImageTk

class Passion_footwear:
    def __init__(self,root):
        self.root = root
        self.root.state('zoomed')
        self.root.geometry("1500x775")
        self.root.minsize(1500,775)
        # self.root.resizable(0, 0)
        self.root.title("PASSION FOOTWEAR")
        bg_color = "#283747"
        title = Label(self.root,text="PASSION FOOTWEAR", bd=0,relief=SOLID,fg="white",bg=bg_color,font=("times new roman",30,"bold"),pady=2).pack(fill=X)


        #==========================================Variables=================
        self.karigar_name, self.remark, self.date = StringVar(), StringVar(), StringVar()
        self.party_no, self.rate = IntVar(), IntVar()

        #=========================================colors and size==============

        self.colors_a, self.colors_b, self.colors_c, self.colors_d, self.colors_e = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
        sizes = []
        for letter in "abcde":
            for i in range(1, 11):
                sizes.append(IntVar())
                setattr(self, f"size_{letter}{i}", sizes[-1])
   

        #==========================================Total===================
        self.size_a,self.size_b, self.size_c, self.size_d, self.size_e, self.art_no = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
        
        #==========Search Frame=============
        F1 = LabelFrame(self.root,bd=0,relief=SOLID, font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=53,relwidth=1)

        karigar_name_lbl = Label(F1,text="Name:", font=("Times new roma",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=7,pady=5)
        karigar_name_txt = Entry(F1,width=20,font="arial 15",textvariable=self.karigar_name,bd=7,relief=GROOVE).grid(row=0,column=1,pady=5,padx=10)
        
        party_no_lbl = Label(F1,text="    Party no.", font=("Times new roma",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=2,padx=10,pady=5)
        Party_no_txt = Entry(F1,width=5,font="arial 15",textvariable=self.party_no,bd=7,relief=GROOVE).grid(row=0,column=3,pady=5,padx=0)
        
        art_no_lbl = Label(F1,text="   Art No.", font=("Times new roma",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=4,padx=10,pady=5)
        art_no_txt = Entry(F1,width=10,font="arial 15",textvariable=self.art_no,bd=7,relief=GROOVE).grid(row=0,column=5,pady=5,padx=0)

        rate_lbl = Label(F1,text="Rate:",font=("Times new roma",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=6,padx=10,pady=5)
        rate_txt = Entry(F1,width=10,font="arial 15",textvariable=self.rate,bd=7,relief=GROOVE).grid(row=0,column=7,pady=5,padx=0)

        date_lbl = Label(F1,text="    Date:",font=("Times new roma",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=8,padx=10,pady=5)
        date_txt = Entry(F1,width=10,font="arial 15",textvariable=self.date,bd=7,relief=GROOVE).grid(row=0,column=9,pady=5,padx=0)
        
        search_btn=Button(F1,text="Search",command=self.find_of,width=13,bd=7,font="arial 12 bold").grid(row=0,column=10,padx=55,pady=10)


        #=======input Order_form Frame========= 
        F2 = LabelFrame(self.root,bd=0,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=0,y=120,width=660,height=235)

        colour_lbl=Label(F2,text="   COLOUR", font=("Times new roma",14,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=7,pady=10,sticky="w")
        colour_a_txt=Entry(F2,width=10,textvariable=self.colors_a,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=1,column=0,padx=10,pady=0)

        size1_lbl=Label(F2,text=" 4/35", font=("Times new roma",14,"bold"),bg=bg_color,fg="white").grid(row=0,column=1,padx=0,pady=0,sticky="w")
        size_a1_txt=Entry(F2,width=3,textvariable=self.size_a1,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=1,column=1,padx=0,pady=0)
        
        size2_lbl=Label(F2,text=" 5/36", font=("Times new roma",14,"bold"),bg=bg_color,fg="white").grid(row=0,column=2,padx=0,pady=0,sticky="w")
        size_a2_txt=Entry(F2,width=3,textvariable=self.size_a2,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=1,column=2,padx=0,pady=0)

        size3_lbl=Label(F2,text=" 6/37", font=("Times new roma",14,"bold"),bg=bg_color,fg="white").grid(row=0,column=3,padx=0,pady=0,sticky="w")
        size_a3_txt=Entry(F2,width=3,textvariable=self.size_a3,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=1,column=3,padx=0,pady=0)
        
        size4_lbl=Label(F2,text=" 7/38", font=("Times new roma",14,"bold"),bg=bg_color,fg="white").grid(row=0,column=4,padx=0,pady=0,sticky="w")
        size_a4_txt=Entry(F2,width=3,textvariable=self.size_a4,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=1,column=4,padx=0,pady=0)

        size5_lbl=Label(F2,text=" 8/39", font=("Times new roma",14,"bold"),bg=bg_color,fg="white").grid(row=0,column=5,padx=0,pady=0,sticky="w")
        size_a5_txt=Entry(F2,width=3,textvariable=self.size_a5,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=1,column=5,padx=0,pady=0)
        
        size6_lbl=Label(F2,text=" 9/40", font=("Times new roma",14,"bold"),bg=bg_color,fg="white").grid(row=0,column=6,padx=0,pady=0,sticky="w")
        size_a6_txt=Entry(F2,width=3,textvariable=self.size_a6,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=1,column=6,padx=0,pady=0)

        size7_lbl=Label(F2,text="10/41", font=("Times new roma",14,"bold"),bg=bg_color,fg="white").grid(row=0,column=7,padx=0,pady=0,sticky="w")
        size_a7_txt=Entry(F2,width=3,textvariable=self.size_a7,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=1,column=7,padx=0,pady=0)
        
        size8_lbl=Label(F2,text="11/42", font=("Times new roma",14,"bold"),bg=bg_color,fg="white").grid(row=0,column=8,padx=0,pady=0,sticky="w")
        size_a8_txt=Entry(F2,width=3,textvariable=self.size_a8,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=1,column=8,padx=0,pady=0)

        size9_lbl=Label(F2,text="12/43", font=("Times new roma",14,"bold"),bg=bg_color,fg="white").grid(row=0,column=9,padx=0,pady=0,sticky="w")
        size_a9_txt=Entry(F2,width=3,textvariable=self.size_a9,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=1,column=9,padx=0,pady=0)
        
        size10_lbl=Label(F2,text="13/44", font=("Times new roma",14,"bold"),bg=bg_color,fg="white").grid(row=0,column=10,padx=0,pady=0,sticky="w")
        size_a10_txt=Entry(F2,width=3,textvariable=self.size_a10,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=1,column=10,padx=0,pady=0)

        #===========================================second line==================================================
        colour_b_txt=Entry(F2,width=10,textvariable=self.colors_b,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=2,column=0,padx=0,pady=0)
        size_b1_txt=Entry(F2,width=3,textvariable=self.size_b1,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=2,column=1,padx=0,pady=10)
        size_b2_txt=Entry(F2,width=3,textvariable=self.size_b2,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=2,column=2,padx=0,pady=10)
        size_b3_txt=Entry(F2,width=3,textvariable=self.size_b3,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=2,column=3,padx=0,pady=10)
        size_b4_txt=Entry(F2,width=3,textvariable=self.size_b4,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=2,column=4,padx=0,pady=10)
        size_b5_txt=Entry(F2,width=3,textvariable=self.size_b5,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=2,column=5,padx=0,pady=10)
        size_b6_txt=Entry(F2,width=3,textvariable=self.size_b6,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=2,column=6,padx=0,pady=10)
        size_b7_txt=Entry(F2,width=3,textvariable=self.size_b7,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=2,column=7,padx=0,pady=10)
        size_b8_txt=Entry(F2,width=3,textvariable=self.size_b8,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=2,column=8,padx=0,pady=10)
        size_b9_txt=Entry(F2,width=3,textvariable=self.size_b9,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=2,column=9,padx=0,pady=10)
        size_b10_txt=Entry(F2,width=3,textvariable=self.size_b10,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=2,column=10,padx=0,pady=10)

        #============================================third line===============================================================
        colour_c_txt=Entry(F2,width=10,textvariable=self.colors_c,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=3,column=0,padx=0,pady=0)
        size_c1_txt=Entry(F2,width=3,textvariable=self.size_c1,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=3,column=1,padx=0,pady=0)
        size_c2_txt=Entry(F2,width=3,textvariable=self.size_c2,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=3,column=2,padx=0,pady=0)
        size_c3_txt=Entry(F2,width=3,textvariable=self.size_c3,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=3,column=3,padx=0,pady=0)
        size_c4_txt=Entry(F2,width=3,textvariable=self.size_c4,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=3,column=4,padx=0,pady=0)
        size_c5_txt=Entry(F2,width=3,textvariable=self.size_c5,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=3,column=5,padx=0,pady=0)
        size_c6_txt=Entry(F2,width=3,textvariable=self.size_c6,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=3,column=6,padx=0,pady=0)
        size_c7_txt=Entry(F2,width=3,textvariable=self.size_c7,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=3,column=7,padx=0,pady=0)
        size_c8_txt=Entry(F2,width=3,textvariable=self.size_c8,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=3,column=8,padx=0,pady=0)
        size_c9_txt=Entry(F2,width=3,textvariable=self.size_c9,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=3,column=9,padx=0,pady=0)
        size_c10_txt=Entry(F2,width=3,textvariable=self.size_c10,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=3,column=10,padx=0,pady=0)

        #============================================fourth line=================================================================
        colour_d_txt=Entry(F2,width=10,textvariable=self.colors_d,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=4,column=0,padx=0,pady=0)
        size_d1_txt=Entry(F2,width=3,textvariable=self.size_d1,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=4,column=1,padx=0,pady=10)
        size_d2_txt=Entry(F2,width=3,textvariable=self.size_d2,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=4,column=2,padx=0,pady=10)
        size_d3_txt=Entry(F2,width=3,textvariable=self.size_d3,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=4,column=3,padx=0,pady=10)
        size_d4_txt=Entry(F2,width=3,textvariable=self.size_d4,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=4,column=4,padx=0,pady=10)
        size_d5_txt=Entry(F2,width=3,textvariable=self.size_d5,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=4,column=5,padx=0,pady=10)
        size_d6_txt=Entry(F2,width=3,textvariable=self.size_d6,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=4,column=6,padx=0,pady=10)
        size_d7_txt=Entry(F2,width=3,textvariable=self.size_d7,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=4,column=7,padx=0,pady=10)
        size_d8_txt=Entry(F2,width=3,textvariable=self.size_d8,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=4,column=8,padx=0,pady=10)
        size_d9_txt=Entry(F2,width=3,textvariable=self.size_d9,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=4,column=9,padx=0,pady=10)
        size_d10_txt=Entry(F2,width=3,textvariable=self.size_d10,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=4,column=10,padx=0,pady=10)

        #==============================================fifth line==========================================================
        colour_e_txt=Entry(F2,width=10,textvariable=self.colors_e,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=5,column=0,padx=0,pady=0)
        size_e1_txt=Entry(F2,width=3,textvariable=self.size_e1,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=5,column=1,padx=0,pady=0)
        size_e2_txt=Entry(F2,width=3,textvariable=self.size_e2,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=5,column=2,padx=0,pady=0)
        size_e3_txt=Entry(F2,width=3,textvariable=self.size_e3,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=5,column=3,padx=0,pady=0)
        size_e4_txt=Entry(F2,width=3,textvariable=self.size_e4,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=5,column=4,padx=0,pady=0)
        size_e5_txt=Entry(F2,width=3,textvariable=self.size_e5,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=5,column=5,padx=0,pady=0)
        size_e6_txt=Entry(F2,width=3,textvariable=self.size_e6,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=5,column=6,padx=0,pady=0)
        size_e7_txt=Entry(F2,width=3,textvariable=self.size_e7,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=5,column=7,padx=0,pady=0)
        size_e8_txt=Entry(F2,width=3,textvariable=self.size_e8,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=5,column=8,padx=0,pady=0)
        size_e9_txt=Entry(F2,width=3,textvariable=self.size_e9,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=5,column=9,padx=0,pady=0)
        size_e10_txt=Entry(F2,width=3,textvariable=self.size_e10,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=5,column=10,padx=0,pady=0)


        total_frame = Label(self.root,bd=0,font=("times new roman",15,"bold"),relief=GROOVE,fg="gold",bg="#283747")
        total_frame.place(x=0,y=360,width=140,height=220)
        total_lbl=Label(total_frame,text="   TOTAL", font=("Times new roma",14,"bold"),bg="#283747",fg="white").grid(row=0,column=0,padx=7,pady=5,sticky="w")
        total_a_txt=Entry(total_frame,textvariable=self.size_a,width=10,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=1,column=0,padx=10,pady=0)
        total_b_txt=Entry(total_frame,textvariable=self.size_b,width=10,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=2,column=0,padx=10,pady=10)
        total_c_txt=Entry(total_frame,textvariable=self.size_c,width=10,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=3,column=0,padx=10,pady=0)
        total_d_txt=Entry(total_frame,textvariable=self.size_d,width=10,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=4,column=0,padx=10,pady=10)
        total_e_txt=Entry(total_frame,textvariable=self.size_e,width=10,justify=CENTER,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=5,column=0,padx=10,pady=0)

        frm = LabelFrame(root,bd=0,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        frm.place(x=0,y=585)
        search_btn=Button(frm,text="Browse",command=self.image_search,width=11,bd=3,bg="cadetblue",fg="white",font="arial 12 bold").grid(row=0,column=0,padx=0,pady=0)
        remark_lbl = Label(frm,text="   Remark:", font=("Times new roma",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=1,padx=0,pady=0)
        remark_txt=Entry(frm,width=38,textvariable=self.remark,font=("times new roman",16,"bold"),bd=0,relief=SUNKEN).grid(row=0,column=2,padx=2,pady=0)
        remark_lbl = Label(frm,text="", font=("Times new roma",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=3,padx=0,pady=0)

#===================================Text Area=========================================================================

        F3 = Frame(self.root,bd=3,relief=GROOVE)
        F3.place(x=665,y=120,width=870,height=502)
        bill_title =Label(F3,text="Order Form",font="arial 15 bold",bd=3,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F3,orient=VERTICAL)
        self.txtarea=Text(F3,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #===============Button Frame=================================

        F4 = LabelFrame(self.root,bd=7,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=0,y=632,relwidth=1,height=170)
        total_btn=Button(F4,text="Total",command=self.total, bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 14 bold").grid(row=0,column=0,padx=15,pady=50)
        generate_btn=Button(F4,text="Genrate Form",command=self.order_form, bg="cadetblue",fg="white",bd=2,pady=15,width=12,font="arial 14 bold").grid(row=0,column=1,padx=15,pady=5)
        print_btn=Button(F4,text="Print", bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 14 bold").grid(row=0,column=2,padx=15,pady=5)
        show_details_btn=Button(F4,text="Show Details", bg="cadetblue",fg="white",bd=2,pady=15,width=12,font="arial 14 bold").grid(row=0,column=3,padx=15,pady=5)
        Clear_btn=Button(F4,text="Clear",command=self.clear_data, bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 14 bold").grid(row=0,column=4,padx=15,pady=5)
        Exit_btn=Button(F4,text="Exit",command=self.exit_app, bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 14 bold").grid(row=0,column=5,padx=15,pady=5)
        self.welcome_bill()


#==============================================Functions============================

    # def total(self):
    #     self.s_a1, self.s_a2, self.s_a3, self.s_a4, self.s_a5, self.s_a6, self.s_a7, self.s_a8, self.s_a9, self.s_a10 =  self.size_a1.get(), self.size_a2.get(), self.size_a3.get(), self.size_a4.get(), self.size_a5.get(), self.size_a6.get(), self.size_a7.get(), self.size_a8.get(), self.size_a9.get(), self.size_a10.get()
    #     self.total_size_a = float(self.s_a1 + self.s_a2 + self.s_a3 + self.s_a4 + self.s_a5 + self.s_a6 + self.s_a7 + self.s_a8 + self.s_a9 + self.s_a10)
    #     self.size_a.set(str(self.total_size_a))

    #     self.s_b1, self.s_b2, self.s_b3, self.s_b4, self.s_b5, self.s_b6, self.s_b7, self.s_b8, self.s_b9, self.s_b10 =  self.size_b1.get(), self.size_b2.get(), self.size_b3.get(), self.size_b4.get(), self.size_b5.get(), self.size_b6.get(), self.size_b7.get(), self.size_b8.get(), self.size_b9.get(), self.size_b10.get()
    #     self.total_size_b = float(self.s_b1 + self.s_b2 + self.s_b3 + self.s_b4 + self.s_b5 + self.s_b6 + self.s_b7 + self.s_b8 + self.s_b9 + self.s_b10)
    #     self.size_b.set(str(self.total_size_b))

    #     self.s_c1, self.s_c2, self.s_c3, self.s_c4, self.s_c5, self.s_c6, self.s_c7, self.s_c8, self.s_c9, self.s_c10 =  self.size_c1.get(), self.size_c2.get(), self.size_c3.get(), self.size_c4.get(), self.size_c5.get(), self.size_c6.get(), self.size_c7.get(), self.size_c8.get(), self.size_c9.get(), self.size_c10.get()
    #     self.total_size_c = float(self.s_c1 + self.s_c2 + self.s_c3 + self.s_c4 + self.s_c5 + self.s_c6 + self.s_c7 + self.s_c8 + self.s_c9 + self.s_c10)
    #     self.size_c.set(str(self.total_size_c))

    #     self.s_d1, self.s_d2, self.s_d3, self.s_d4, self.s_d5, self.s_d6, self.s_d7, self.s_d8, self.s_d9, self.s_d10 =  self.size_d1.get(), self.size_d2.get(), self.size_d3.get(), self.size_d4.get(), self.size_d5.get(), self.size_d6.get(), self.size_d7.get(), self.size_d8.get(), self.size_d9.get(), self.size_d10.get()
    #     self.total_size_d = float(self.s_d1 + self.s_d2 + self.s_d3 + self.s_d4 + self.s_d5 + self.s_d6 + self.s_d7 + self.s_d8 + self.s_d9 + self.s_d10)
    #     self.size_d.set(str(self.total_size_d))

    #     self.s_e1, self.s_e2, self.s_e3, self.s_e4, self.s_e5, self.s_e6, self.s_e7, self.s_e8, self.s_e9, self.s_e10 =  self.size_e1.get(), self.size_e2.get(), self.size_e3.get(), self.size_e4.get(), self.size_e5.get(), self.size_e6.get(), self.size_e7.get(), self.size_e8.get(), self.size_e9.get(), self.size_e10.get()
    #     self.total_size_e = float(self.s_e1 + self.s_e2 + self.s_e3 + self.s_e4 + self.s_e5 + self.s_e6 + self.s_e7 + self.s_e8 + self.s_e9 + self.s_e10)
    #     self.size_e.set(str(self.total_size_e))

    def total(self):
        size_dict = {
            'a': self.size_a,
            'b': self.size_b,
            'c': self.size_c,
            'd': self.size_d,
            'e': self.size_e
        }
        for key, size in size_dict.items():
            total_size = 0
            for i in range(1, 11):
                size_i = getattr(self, f'size_{key}{i}').get()
                total_size += float(size_i)
            size.set(str(total_size))




    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,f"\n=========================================================================================================")
        self.txtarea.insert(END,f"\n Name:{self.karigar_name.get()}\t\t\t")
        self.txtarea.insert(END,f"Party No. :{self.party_no.get()}\t\t\t")
        self.txtarea.insert(END,f"Date:{self.date.get()}\t\t\t")
        self.txtarea.insert(END,f"ART No.:{self.art_no.get()}\t\t")
        self.txtarea.insert(END,f"Rate:{self.rate.get()}")
        self.txtarea.insert(END,f"\n=========================================================================================================")
        self.txtarea.insert(END,f"\nCOLOUR\t")
        self.txtarea.insert(END,f"4/35\t5/36\t6/37\t7/38\t8/39\t9/40\t10/41\t11/42\t12/43\t13/44")
        self.txtarea.insert(END,f"\tTOTAL")
        
    def image_search(self):
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="select Image File",filetypes=(("All Files","*.*"),("JPEG File","*.jpeg"),("JPG File","*.jpg"),("PNG file","*.png")))
        img = Image.open(fln)
        img.thumbnail((250,250))
        img = ImageTk.PhotoImage(img)
        lbl.configure(image=img)
        lbl.image = img 

    # def order_form(self):
    #     if self.karigar_name.get()=="" or self.party_no.get()=="" or self.art_no.get()=="" or self.date.get()=="":
    #         messagebox.showerror("Error","Oops, Credential data is missing")
    #     elif self.colors_a.get()=="" and self.colors_b.get()=="" and self.colors_c.get()=="" and self.colors_d.get()=="" and self.colors_e.get()=="":
    #         messagebox.showerror("Error","Enter the colour")
    #     elif self.size_a.get()=="0.0" and self.size_b.get()=="0.0" and self.size_c.get()=="0.0" and self.size_d.get()=="0.0" and self.size_e.get()=="0.0":
    #         messagebox.showerror("Error","Enter the size")
    #     else:
    #         self.welcome_bill()
    #         #==========================Size-L1========================
    #         if self.colors_a.get()!="":
    #             self.txtarea.insert(END,f"{self.colors_a.get()}")
    #         if self.size_a1.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_a1.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_a2.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_a2.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_a3.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_a3.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_a4.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_a4.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_a5.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_a5.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_a6.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_a6.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_a7.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_a7.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_a8.get()!=0:
    #             self.txtarea.insert(END,f"      {self.size_a8.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_a9.get()!=0:
    #             self.txtarea.insert(END,f"      {self.size_a9.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_a10.get()!=0:
    #             self.txtarea.insert(END,f"      {self.size_a10.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_a11.get()!=0:
    #             self.txtarea.insert(END,f"    {self.size_a11.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_a12.get()!=0:
    #             self.txtarea.insert(END,f"  {self.size_a12.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_a13.get()!=0:
    #             self.txtarea.insert(END,f"  {self.size_a13.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_a.get()!=0:
    #             self.txtarea.insert(END,f"   {self.size_a.get()}")


    #         #==========================Size-L2========================
    #         if self.colors_b.get()!="":
    #             self.txtarea.insert(END,f"\n{self.colors_a.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_b1.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_b1.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_b2.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_b2.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_b3.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_b3.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_b4.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_b4.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_b5.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_b5.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_b6.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_b6.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_b7.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_b7.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_b8.get()!=0:
    #             self.txtarea.insert(END,f"      {self.size_b8.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_b9.get()!=0:
    #             self.txtarea.insert(END,f"      {self.size_b9.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_b10.get()!=0:
    #             self.txtarea.insert(END,f"      {self.size_b10.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_b11.get()!=0:
    #             self.txtarea.insert(END,f"    {self.size_b11.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_b12.get()!=0:
    #             self.txtarea.insert(END,f"  {self.size_b12.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_b13.get()!=0:
    #             self.txtarea.insert(END,f"  {self.size_b13.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")

    #         #==========================Size-L3========================
    #         if self.colors_c.get()!="":
    #             self.txtarea.insert(END,f"\n{self.colors_c.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_c1.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_c1.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_c2.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_c2.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_c3.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_c3.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_c4.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_c4.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_c5.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_c5.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_c6.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_c6.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_c7.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_c7.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_c8.get()!=0:
    #             self.txtarea.insert(END,f"      {self.size_c8.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_c9.get()!=0:
    #             self.txtarea.insert(END,f"      {self.size_c9.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_c10.get()!=0:
    #             self.txtarea.insert(END,f"      {self.size_c10.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_c11.get()!=0:
    #             self.txtarea.insert(END,f"    {self.size_c11.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_c12.get()!=0:
    #             self.txtarea.insert(END,f"  {self.size_c12.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_c13.get()!=0:
    #             self.txtarea.insert(END,f"  {self.size_c13.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")

    #         #==========================Size-L4========================
    #         if self.colors_d.get()!="":
    #             self.txtarea.insert(END,f"\n{self.colors_a.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_d1.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_d1.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_d2.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_d2.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_d3.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_d3.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_d4.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_d4.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_d5.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_d5.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_d6.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_d6.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_d7.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_d7.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_d8.get()!=0:
    #             self.txtarea.insert(END,f"      {self.size_d8.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_d9.get()!=0:
    #             self.txtarea.insert(END,f"      {self.size_d9.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_d10.get()!=0:
    #             self.txtarea.insert(END,f"      {self.size_d10.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_d11.get()!=0:
    #             self.txtarea.insert(END,f"    {self.size_d11.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_d12.get()!=0:
    #             self.txtarea.insert(END,f"  {self.size_d12.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_d13.get()!=0:
    #             self.txtarea.insert(END,f"  {self.size_d13.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")

    #         #==========================Size-L2========================
    #         if self.colors_e.get()!="":
    #             self.txtarea.insert(END,f"\n{self.colors_a.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_e1.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_e1.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_e2.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_e2.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_e3.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_e3.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_e4.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_e4.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_e5.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_e5.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_e6.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_e6.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_e7.get()!=0:
    #             self.txtarea.insert(END,f"     {self.size_e7.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_e8.get()!=0:
    #             self.txtarea.insert(END,f"      {self.size_e8.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_e9.get()!=0:
    #             self.txtarea.insert(END,f"      {self.size_e9.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_e10.get()!=0:
    #             self.txtarea.insert(END,f"      {self.size_e10.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_e11.get()!=0:
    #             self.txtarea.insert(END,f"    {self.size_e11.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_e12.get()!=0:
    #             self.txtarea.insert(END,f"  {self.size_e12.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")
    #         if self.size_e13.get()!=0:
    #             self.txtarea.insert(END,f"  {self.size_e13.get()}")
    #         else:
    #             self.txtarea.insert(END,f"     -")


        #===============================Optimized order_form ==========================
    def order_form(self):
        if not all([self.karigar_name.get(), self.party_no.get(), self.art_no.get(), self.date.get()]):
            messagebox.showerror("Error","Oops, Credential data is missing")
        elif not any([self.colors_a.get(), self.colors_b.get(), self.colors_c.get(), self.colors_d.get(), self.colors_e.get()]):
            messagebox.showerror("Error","Enter the colour")
        elif not any([self.size_a.get(), self.size_b.get(), self.size_c.get(), self.size_d.get(), self.size_e.get()]):
            messagebox.showerror("Error","Enter the size")
        else:
            self.welcome_bill()
            for color, size in [("colors_a", "size_a"),
                                ("colors_b", "size_b"),
                                ("colors_c", "size_c"),
                                ("colors_d", "size_d"),
                                ("colors_e", "size_e")]:
                if getattr(self, color).get():
                    self.txtarea.insert(END, f"\n{getattr(self, color).get()}\t")
                    for i in range(1, 11):
                        size_i = getattr(self, f'{size}{i}').get()
                        if size_i != 0:
                            self.txtarea.insert(END, f"{size_i}\t")
                        else:
                            self.txtarea.insert(END, "-\t")
                    self.txtarea.insert(END, f"{getattr(self, size).get()}")
            if self.remark.get():
                self.txtarea.insert(END, f"\n\nREMARK: {self.remark.get()}")
            self.save_order_form()

            
    def save_order_form(self):
        op=messagebox.askyesno("Save Order Form","Do you want to save the order form")
        if op>0:
            self.of_data=self.txtarea.get("1.0",END)
            f1=open("./Passion Footwear/order_form/"+str(self.art_no.get())+".txt","w")
            f1.write(self.of_data)
            f1.close
            messagebox.showinfo("Saved",f"Art No. : {self.art_no.get()} saved successfully")
        else:
            return
    
    def find_of(self):
        present ="no"
        for i in os.listdir("./Passion Footwear/order_form/"):
            if i.split('.')[0]==self.art_no.get():
                f1=open(f"./Passion Footwear/order_form/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
                messagebox.showerror("Error","Invalid bill number")

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to Clear?")
        if op>0:       
            #==========================================Variables=================
            self.karigar_name.set("")
            self.party_no.set(0)
            self.rate.set(0)
            self.date.set("")
            self.remark.set("")

            #=========================================colors and size==============
            # self.colors_a.set("")
            # self.colors_b.set("")
            # self.colors_c.set("")
            # self.colors_d.set("")
            # self.colors_e.set("")
            # self.size_a1.set(0)
            # self.size_a2.set(0)
            # self.size_a3.set(0)
            # self.size_a4.set(0)
            # self.size_a5.set(0)
            # self.size_a6.set(0)
            # self.size_a7.set(0)
            # self.size_a8.set(0)
            # self.size_a9.set(0)
            # self.size_a10.set(0)
            # self.size_b1.set(0)
            # self.size_b2.set(0)
            # self.size_b3.set(0)
            # self.size_b4.set(0)
            # self.size_b5.set(0)
            # self.size_b6.set(0)
            # self.size_b7.set(0)
            # self.size_b8.set(0)
            # self.size_b9.set(0)
            # self.size_b10.set(0)
            # self.size_c1.set(0)
            # self.size_c2.set(0)
            # self.size_c3.set(0)
            # self.size_c4.set(0)
            # self.size_c5.set(0)
            # self.size_c6.set(0)
            # self.size_c7.set(0)
            # self.size_c8.set(0)
            # self.size_c9.set(0)
            # self.size_c10.set(0)
            # self.size_d1.set(0)
            # self.size_d2.set(0)
            # self.size_d3.set(0)
            # self.size_d4.set(0)
            # self.size_d5.set(0)
            # self.size_d6.set(0)
            # self.size_d7.set(0)
            # self.size_d8.set(0)
            # self.size_d9.set(0)
            # self.size_d10.set(0)
            # self.size_e1.set(0)
            # self.size_e2.set(0)
            # self.size_e3.set(0)
            # self.size_e4.set(0)
            # self.size_e5.set(0)
            # self.size_e6.set(0)
            # self.size_e7.set(0)
            # self.size_e8.set(0)
            # self.size_e9.set(0)
            # self.size_e10.set(0)

            # #==========================================Total===================
            # self.size_a.set("")
            # self.size_b.set("")
            # self.size_c.set("")
            # self.size_d.set("")
            # self.size_e.set("")

            # creating lists of size variables and color variables for each row
            size_vars = [getattr(self, f'size_{row}{i}') for row in 'abcde' for i in range(1, 11)]
            color_vars = [getattr(self, f'colors_{row}') for row in 'abcde']

            # set all size variables to 0
            for var in size_vars:
                var.set(0)

            # set all color variables to an empty string
            for var in color_vars:
                var.set("")

            # set art_no variable to an empty string
            self.art_no.set("")

            self.welcome_bill()
        

    
    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()


            


root=Tk()
# root.resizable(True,True)
lbl = Label(root,bd=0,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg="#283747")
lbl.place(x=140,y=360,width=520,height=220)
obj  = Passion_footwear(root)
root.mainloop()
