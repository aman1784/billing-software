from tkinter import *
import math, random, os, time
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x700+0+0")
        self.root.config(bg="black")
        self.root.title("Bill Software")
        bg_color = "#074463"

        title = Label(self.root, text="Billing Software", bd="12", relief=GROOVE, bg=bg_color, fg="gold",
                      font=("times new roman", 37, "bold"), pady=2).pack(fill=X)
        # ===================variables==================================================================================
        # ===================Cosmetics==================================================================================
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.lotion = IntVar()
        # ==========================Grocery=============================================================================
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        # ==========================COLD DRINKS=========================================================================
        self.maza = IntVar()
        self.coke = IntVar()
        self.frooti = IntVar()
        self.thumbsup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        # =========================Total product and tax variables======================================================
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        # ================Customer======================================================================================
        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        # ===================================customer details frame=====================================================
        F1 = LabelFrame(self.root, text="Customer Details", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        bg=bg_color, fg="gold", pady=2)
        F1.place(x=0, y=83, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(
            row=0, column=0, padx=10, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, bd=7, relief=SUNKEN, font="arial 15").grid(row=0,
                                                                                                             column=1,
                                                                                                             pady=5,
                                                                                                             padx=10)

        cphn_lbl = Label(F1, text="Customer Phone No.", bg=bg_color, fg="white",
                         font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=10, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phon, bd=7, relief=SUNKEN, font="arial 15").grid(row=0,
                                                                                                            column=3,
                                                                                                            pady=5,
                                                                                                            padx=10)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(
            row=0, column=4, padx=10, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, bd=7, relief=SUNKEN, font="arial 15").grid(
            row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font="arial 12 bold").grid(row=0,
                                                                                                                column=6,
                                                                                                                padx=10,
                                                                                                                pady=10)
        # ===================================cosmetic frame=============================================================
        F2 = LabelFrame(self.root, text="Cosmetic", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        bg=bg_color, fg="gold", pady=2)
        F2.place(x=1, y=185, width=319, height=366)

        bath_lbl = Label(F2, text="Bath Soap", font=("times new roman", 16, "bold"), bg=bg_color,
                         fg="light green").grid(row=0, column=0, padx=10, pady=10, sticky="W")
        bath_txt = Entry(F2, width=10, textvariable=self.soap, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        Face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="light green").grid(row=3, column=0, padx=10, pady=10, sticky="W")
        Face_cream_txt = Entry(F2, width=10, textvariable=self.face_cream, font=("times new roman", 16, "bold"), bd=5,
                               relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        Face_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="light green").grid(row=4, column=0, padx=10, pady=10, sticky="W")
        Face_w_txt = Entry(F2, width=10, textvariable=self.face_wash, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        Hair_s_lbl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="light green").grid(row=5, column=0, padx=10, pady=10, sticky="W")
        Hair_s_txt = Entry(F2, width=10, textvariable=self.spray, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        Hair_g_lbl = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="light green").grid(row=6, column=0, padx=10, pady=10, sticky="W")
        Hair_g_txt = Entry(F2, width=10, textvariable=self.gell, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10)

        body_lbl = Label(F2, text="Body Lotion", font=("times new roman", 16, "bold"), bg=bg_color,
                         fg="light green").grid(row=7, column=0, padx=10, pady=10, sticky="W")
        body_txt = Entry(F2, width=10, textvariable=self.lotion, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=7, column=1, padx=10, pady=10)
        # ========================================Grocery===============================================================
        F3 = LabelFrame(self.root, text="Grocery", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        bg=bg_color, fg="gold", pady=2)
        F3.place(x=321, y=185, width=320, height=366)

        g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=0,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="W")
        g1_txt = Entry(F3, width=10, textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        g2_lbl = Label(F3, text="Food Oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(
            row=3, column=0, padx=10, pady=10, sticky="W")
        g2_txt = Entry(F3, width=10, textvariable=self.food_oil, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        g3_lbl = Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=4,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="W")
        g3_txt = Entry(F3, width=10, textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        g4_lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(
            row=5, column=0, padx=10, pady=10, sticky="W")
        g4_txt = Entry(F3, width=10, textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        g5_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(
            row=6, column=0, padx=10, pady=10, sticky="W")
        g5_txt = Entry(F3, width=10, textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10)

        g6_lbl = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=7,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="W")
        g6_txt = Entry(F3, width=10, textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=7, column=1, padx=10, pady=10)
        # ===================================cold drinks================================================================
        F4 = LabelFrame(self.root, text="Cold Drinks", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        bg=bg_color, fg="gold", pady=2)
        F4.place(x=641, y=185, width=321, height=366)

        c1_lbl = Label(F4, text="Maza", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=0,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="W")
        c1_txt = Entry(F4, width=10, textvariable=self.maza, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        c2_lbl = Label(F4, text="Coke", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=3,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="W")
        c2_txt = Entry(F4, width=10, textvariable=self.coke, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        c3_lbl = Label(F4, text="Frooti", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(
            row=4, column=0, padx=10, pady=10, sticky="W")
        c3_txt = Entry(F4, width=10, textvariable=self.frooti, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        c4_lbl = Label(F4, text="Thumbs Up", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(
            row=5, column=0, padx=10, pady=10, sticky="W")
        c4_txt = Entry(F4, width=10, textvariable=self.thumbsup, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        c5_lbl = Label(F4, text="Limca", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(
            row=6, column=0, padx=10, pady=10, sticky="W")
        c5_txt = Entry(F4, width=10, textvariable=self.limca, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10)

        c6_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(
            row=7, column=0, padx=10, pady=10, sticky="W")
        c6_txt = Entry(F4, width=10, textvariable=self.sprite, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=7, column=1, padx=10, pady=10)
        # =======================================Bill Area==============================================================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=963, y=185, width=390, height=366)
        bill_lbl = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        # ====================================Button Frame==============================================================
        F6 = LabelFrame(self.root, text="Bill Menu", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        bg=bg_color, fg="gold", pady=2)
        F6.place(x=0, y=550, relwidth=1, height=137)
        m1_lbl = Label(F6, text="Total Cosmetic Price", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=5, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable=self.cosmetic_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=5, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=1, padx=10, pady=2)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=3, column=0, padx=5, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drink_price, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=3, column=1, padx=10, pady=1)

        c1_lbl = Label(F6, text="Cosmetic Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=0, column=2, padx=5, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18, textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="Grocery Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=1, column=2, padx=5, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=3, padx=10, pady=2)

        c3_lbl = Label(F6, text="Cold Drinks Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=3, column=2, padx=5, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18, textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=3, column=3, padx=10, pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.config(bg="black")
        btn_F.place(x=690, y=0, width=635, height=103)

        total_btn = Button(btn_F, command=self.total, text="Total", bg="cadetblue", fg="white", foreground="black",
                           activebackground="sky blue", bd=5, pady=15, width=10, font="arial 15 bold").grid(row=0,
                                                                                                            column=0,
                                                                                                            padx=7,
                                                                                                            pady=13)
        GBill_btn = Button(btn_F, text="Generate Bill", command=self.bill_area, bg="cadetblue", fg="white",
                           foreground="black", activebackground="sky blue", bd=5, pady=15, width=12,
                           font="arial 15 bold").grid(row=0, column=1, padx=7, pady=13)
        Clear_btn = Button(btn_F, text="Clear", command=self.Clear_data, bg="cadetblue", fg="white", foreground="black",
                           activebackground="sky blue", bd=5, pady=15, width=10, font="arial 15 bold").grid(row=0,
                                                                                                            column=2,
                                                                                                            padx=7,
                                                                                                            pady=13)
        Exit_btn = Button(btn_F, text="Exit", command=self.Exit_app, bg="cadetblue", fg="white", foreground="black",
                          activebackground="sky blue", bd=5, pady=15, width=10, font="arial 15 bold").grid(row=0,
                                                                                                           column=3,
                                                                                                           padx=7,
                                                                                                           pady=13)
        self.welcome_bill()

    def total(self):
        self.c_s_p = self.soap.get() * 40
        self.c_fc_p = self.face_cream.get() * 120
        self.c_fw_p = self.face_wash.get() * 60
        self.c_hs_p = self.spray.get() * 180
        self.c_hg_p = self.gell.get() * 140
        self.c_bl_p = self.lotion.get() * 180

        self.total_cosmetic_price = float(
            self.c_s_p +
            self.c_fc_p +
            self.c_fw_p +
            self.c_hs_p +
            self.c_hg_p +
            self.c_bl_p
        )
        self.cosmetic_price.set("Rs. " + str(self.total_cosmetic_price))
        self.c_tax = round((self.total_cosmetic_price * 0.05), 2)
        self.cosmetic_tax.set("Rs. " + str(self.c_tax))

        self.g_r_p = self.rice.get() * 80
        self.g_f_p = self.food_oil.get() * 180
        self.g_d_p = self.daal.get() * 60
        self.g_w_p = self.wheat.get() * 240
        self.g_s_p = self.sugar.get() * 45
        self.g_t_p = self.tea.get() * 150

        self.total_grocery_price = float(
            self.g_r_p +
            self.g_f_p +
            self.g_d_p +
            self.g_w_p +
            self.g_s_p +
            self.g_t_p
        )
        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price * 0.1), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.d_m_p = self.maza.get() * 60
        self.d_c_p = self.coke.get() * 60
        self.d_f_p = self.frooti.get() * 50
        self.d_t_p = self.thumbsup.get() * 45
        self.d_l_p = self.limca.get() * 40
        self.d_s_p = self.sprite.get() * 60

        self.total_drinks_price = float(
            self.d_m_p +
            self.d_c_p +
            self.d_f_p +
            self.d_t_p +
            self.d_l_p +
            self.d_s_p
        )
        self.cold_drink_price.set("Rs. " + str(self.total_drinks_price))
        self.d_tax = round((self.total_drinks_price * 0.05), 2)
        self.cold_drink_tax.set("Rs. " + str(self.d_tax))

        self.Total_bill = float(
            self.total_cosmetic_price +
            self.total_grocery_price +
            self.total_drinks_price +
            self.c_tax +
            self.g_tax +
            self.d_tax
        )

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        name_ = {self.c_name.get()}
        self.txtarea.insert(END, f"\t\tWelcome {self.c_name.get()}\n")
        self.root.x = time.strftime("%d/%m/%Y")
        self.root.y = time.strftime('%H:%M:%S')
        self.txtarea.insert(END, f"\n Date : {self.root.x}")
        self.txtarea.insert(END, f"\n Time : {self.root.y}")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")

        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number : {self.c_phon.get()}")
        self.txtarea.insert(END, f"\n===========================================")
        self.txtarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END, f"\n===========================================")

    def bill_area(self):

        if self.c_name.get() == "" or self.c_phon.get() == "":
            messagebox.showerror("Error", "Customer details are must")
        elif self.cosmetic_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drink_price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
            # ========================cosmetics==========================================================================
            if self.soap.get() != 0:
                self.txtarea.insert(END, f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get() != 0:
                self.txtarea.insert(END, f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get() != 0:
                self.txtarea.insert(END, f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.spray.get() != 0:
                self.txtarea.insert(END, f"\n Spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")
            if self.gell.get() != 0:
                self.txtarea.insert(END, f"\n Hair Gell\t\t{self.gell.get()}\t\t{self.c_hg_p}")
            if self.lotion.get() != 0:
                self.txtarea.insert(END, f"\n Body Lotion\t\t{self.lotion.get()}\t\t{self.c_bl_p}")

            # =============================Grocery=======================================================================
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get() != 0:
                self.txtarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")

            # ================================Drinks=====================================================================
            if self.maza.get() != 0:
                self.txtarea.insert(END, f"\n Maza\t\t{self.maza.get()}\t\t{self.d_m_p}")
            if self.coke.get() != 0:
                self.txtarea.insert(END, f"\n Coke\t\t{self.coke.get()}\t\t{self.d_c_p}")
            if self.frooti.get() != 0:
                self.txtarea.insert(END, f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")
            if self.thumbsup.get() != 0:
                self.txtarea.insert(END, f"\n Thumbs Up\t\t{self.thumbsup.get()}\t\t{self.d_t_p}")
            if self.limca.get() != 0:
                self.txtarea.insert(END, f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")

            self.txtarea.insert(END, f"\n*******************************************")
            if self.cosmetic_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Cold Drink Tax\t\t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(END, f"\n Total Bill : \t\t\t Rs. {str(self.Total_bill)}")
            self.txtarea.insert(END, f"\n*******************************************")
            self.txtarea.insert(END, f"\n\t\tTHANK YOU ")
            self.txtarea.insert(END, f"\n\t\tVISIT AGAIN ")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save Bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            #f1 = open("C:/bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no. :{self.bill_no.get()} saved Successfully")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No.")

    def Clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear Data")
        if op > 0:
            # ===========================Cosmetics=======================================================================
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.lotion.set(0)
            # ===================================Grocery=================================================================
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            # ================================COLD DRINKS================================================================
            self.maza.set(0)
            self.coke.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            # ===========================Total product and tax variables================================================
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            # ===============================COSTUMER===================================================================
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit")
        if op > 0:
            self.root.destroy()


class a:
    def __init__(self2, root):
        def play():
            p = password_verify.get()
            print(p)
            if p == "root":
                obj = Bill_App(root)
                root.mainloop()
            else:
                messagebox.showinfo("ERROR", "WRONG PASSWORD")

        # filename=PhotoImage(file ="i.jpg")
        self2.root = root
        self2.root.geometry("1366x700+0+0")
        self2.root.config(bg="light blue",bd=7,relief=SUNKEN)
        self2.root.title("Bill Software Login Page")
        title = Label(self2.root, text="Billing Software Login System", bd="7", relief=FLAT, bg="lightslategrey", fg="black",
                      font=("times new roman", 50, "bold"), pady=2).place(x=200,y=50,height=100)
        login = Frame(self2.root, bd=7,relief=SUNKEN)
        login.config(bg="lightslategrey")
        login.place(x=400, y=165, width=500, height=410)
        Label(login, text="Please enter the login details below",bg="lightslategrey", fg="navy", bd=5,
              font=("times new roman", 20, "bold")).place(x=30,y=20,height=70)
        Label(login, text="").place()

        global username_verify
        global password_verify

        username_verify = StringVar()
        password_verify = StringVar()
        global username_login_entry
        global password_login_entry
        Label(login, text="Username * ", font=("times new roman", 20, "bold"), fg="black", bg="white").place(x=50,y=150)
        username_login_entry = Entry(login, textvariable=username_verify, font="arial 18 bold", bd=3, relief=SUNKEN)
        username_login_entry.place(x=210,y=150)
        Label(login, text="").place()
        Label(login, text="Password * ", font=("times new roman", 20, "bold"), fg="black", bg="white").place(x=50,y=220)
        password_login_entry = Entry(login, textvariable=password_verify, show='*', font="arial 18 bold", bd=3,
                                     relief=SUNKEN)
        password_login_entry.place(x=210,y=220)
        Label(login, text="").place()
        Button(login, text="Login", width=7, height=2, bg="cadetblue", fg="white", foreground="black",
               activebackground="sky blue", bd=5, font="arial 15 bold",command=play).place(x=200,y=300)


y = Tk()
o = a(y)
y.mainloop()



