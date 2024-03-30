from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk #pip install pillow


class BILL_Application:   #(help to simplify the code)
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")   #(show the width and height of window)
        self.root.title("Billing Software")
        
        #product category list
        self.product_category_List = ["Select Category","Clothing","Lifestyle","Footwear"]
        
        #product sub category clothing list
        self.product_subcategory_clothing_List = ["T-shirts","Trousers","Jackets","shirt"]
        #for tshirt
        self.tshirts=["nike","adidas","puma","reebok"]
        self.price_nike=[1000,2000,3000,4000,5000]
        self.price_adidas=[1000,2000,3000,4000,5000]
        self.price_puma=[1000,2000,3000,4000,5000]
        self.price_reebok=[1000,2000,3000,4000,5000]
        #for trousers
        self.trousers=["levis","armani","gap","pepe jeans","wrangler","puma","reebok","nike","adidas"]
        self.price_levis=[1000,2000,3000,4000,5000]
        self.price_armani=[1000,2000,3000,4000,5000]
        self.price_gap=[1000,2000,3000,4000,5000]
        self.price_pepe_jeans=[1000,2000,3000,4000,5000]
        self.price_wrangler=[1000,2000,3000,4000,5000]
        self.price_puma=[1000,2000,3000,4000,5000]
        self.price_reebok=[1000,2000,3000,4000,5000]
        self.price_nike=[1000,2000,3000,4000,5000]
        self.price_adidas=[1000,2000,3000,4000,5000]
        #for jacket
        self.jacket=["levis","armani","gap","puma","nike","adidas","reebok","prada","versace","jockey","converse",]
        self.price_levis=["1000","2000","3000","4000","5000"]
        self.price_armani=["1000","2000","3000","4000","5000"]
        self.price_gap=["1000","2000","3000","4000","5000"]
        self.price_puma=["1000","2000","3000","4000","5000"]
        self.price_nike=["1000","2000","3000","4000","5000"]
        self.price_adidas=["1000","2000","3000","4000","5000"]
        self.price_reebok=["1000","2000","3000","4000","5000"]
        self.price_prada=["1000","2000","3000","4000","5000"]
        self.price_versace=["1000","2000","3000","4000","5000"]
        self.price_jockey=["1000","2000","3000","4000","5000"]
        self.price_converse=["1000","2000","3000","4000","5000"]
        #for shirt
        self.shirt=["levis","armani","gap","puma","nike","adidas","reebok","prada","versace","jockey","converse"]
        self.price_levis=["1000","2000","3000","4000","5000"]
        self.price_armani=["1000","2000","3000","4000","5000"]
        self.price_gap=["1000","2000","3000","4000","5000"]
        self.price_puma=["1000","2000","3000","4000","5000"]
        self.price_nike=["1000","2000","3000","4000","5000"]
        self.price_adidas=["1000","2000","3000","4000","5000"]
        self.price_reebok=["1000","2000","3000","4000","5000"]
        self.price_prada=["1000","2000","3000","4000","5000"]
        self.price_versace=["1000","2000","3000","4000","5000"]
        self.price_jockey=["1000","2000","3000","4000","5000"]
        self.price_converse=["1000","2000","3000","4000","5000"]
        
        
        #product sub category lifestyle list
        self.product_subcategory_lifestyle_List = ["hair oil","shampoo","face cream","face wash","bodylotion","bodysoap","deodrant","face pack","lipstick"]
        #for hair oil
        self.hair_oil=["keshkanti","lakme","redington","maybelline","hada labo","pureology","himalayaa"]
        self.price_keshkanti=["100","200","300"]
        self.price_lakme=["100","200","300"]
        self.price_redington=["100","200","300"]
        self.price_maybelline=["100","200","300"]
        self.price_hada_labo=["100","200","300"]
        self.price_pureology=["100","200","300"]
        self.price_himalayaa=["100","200","300"]
        #for shampoo
        self.shampoo=["sunsilk","taj","nivea","lifeboy","lakme","redington","maybelline","himalaya","huda","kamas"]
        self.price_sunsilk=["130","250"]
        self.price_taj=["130","250"]
        self.price_nivea=["130","250"]
        self.price_lifeboy=["130","250"]
        self.price_lakme=["130","250"]
        self.price_redington=["130","250"]
        self.price_maybelline=["130","250"]
        self.price_himalaya=["130","250"]
        self.price_huda=["130","250"]
        self.price_kamas=["130","250"]  
        #for face cream
        self.face_cream=["fairhandsome","lakme","vaslline"]
        self.price_fairhandsome=["50","100","150"]
        self.price_lakme=["150","250","350"]
        self.price_vaslline=["50","100","150"]
        #for face wash
        self.face_wash=["breado","garnier","lakme"]
        self.price_breado=["50","100","150"]
        self.price_garnier=["50","100","150"]
        self.price_lakme=["50","100","150"]
        #for bodylotion
        self.bodylotion=["vaslline","lakme"]
        self.price_vaslline=["50","100","150"]
        self.price_lakme=["50","180","250"]
        #for bodysoap
        self.bodysoap=["lifeboy","dove","dettol","pears","lakme"]
        self.price_lifeboy=["50","100"]
        self.price_dove=["50","120"]
        self.price_dettol=["50","120"]
        self.price_pears=["50","120"]
        self.price_lakme=["50","120"]
        #for face pack
        self.face_pack=["fairhandsome","lakme","vaslline"]
        self.price_fairhandsome=["50","100","150"]
        self.price_lakme=["150","250","350"]
        self.price_vaslline=["50","100","150"]
        #for lipstick
        self.lipstick=["lakme","maybelline"]
        self.price_lakme=["50","100","150"]
        self.price_maybelline=["50","100","150"]
        #for deodrant
        self.deodrant=["denver","fogg"]
        self.price_denver=["250","450"]
        self.price_fogg=["250","450"]
        
        #product sub category footwear list
        self.product_subcategory_footwear_List = ["sneakers","formal","casual","sports","boots","heels","sandals","flipflops","slippers"]
        #for sneaker
        self.sneakers=["nike","adidas","puma","reebok"]
        self.price_nike=[1000,2000,3000,4000,5000]
        self.price_adidas=[1000,2000,3000,4000,5000]
        self.price_puma=[1000,2000,3000,4000,5000]
        self.price_reebok=[1000,2000,3000,4000,5000]
        #for formal
        self.formal=["nike","adidas","puma","reebok"]
        self.price_nike=[1000,2000,3000,4000,5000]
        self.price_adidas=[1000,2000,3000,4000,5000]
        self.price_puma=[1000,2000,3000,4000,5000]
        self.price_reebok=[1000,2000,3000,4000,5000]
        #for casual
        self.casual=["nike","adidas","puma","reebok",]
        self.price_nike=[1000,2000,3000,4000,5000]
        self.price_adidas=[1000,2000,3000,4000,5000]
        self.price_puma=[1000,2000,3000,4000,5000]
        self.price_reebok=[1000,2000,3000,4000,5000]
        #for sports
        self.sports=["nike","adidas","puma","reebok","under armour"]
        self.price_nike=[1000,2000,3000,4000,5000]
        self.price_adidas=[1000,2000,3000,4000,5000]
        self.price_puma=[1000,2000,3000,4000,5000]
        self.price_reebok=[1000,2000,3000,4000,5000]
        self.price_under_armour=[1000,2000,3000,4000,5000]  
        #for boots
        self.boots=["nike","adidas","puma","reebok"]
        self.price_nike=[1000,2000,3000,4000,5000]
        self.price_adidas=[1000,2000,3000,4000,5000]
        self.price_puma=[1000,2000,3000,4000,5000]
        self.price_reebok=[1000,2000,3000,4000,5000]
        #for heels
        self.heels=["louis vuitton","gucci","chanel","prada","stella mccartney"]
        self.price_louis_vuitton=["1000","2000","3000","4000","5000"]
        self.price_gucci=["1000","2000","3000","4000","5000"]
        self.price_chanel=["1000","2000","3000","4000","5000"]
        self.price_prada=["1000","2000","3000","4000","5000"]
        self.price_stella_mccartney=["1000","2000","3000","4000","5000"]
        #for sandals
        self.sandals=["nike","adidas","puma","reebok","wildcraft"]
        self.price_nike=[1000,2000,3000,4000,5000]
        self.price_adidas=[1000,2000,3000,4000,5000]
        self.price_puma=[1000,2000,3000,4000,5000]
        self.price_reebok=[1000,2000,3000,4000,5000]
        self.price_wildcraft=[1000,2000,3000,4000,5000]
        #for flipflops
        self.flipflops=["nike","adidas","puma","reebok","salomon"]
        self.price_nike=[1000,2000,3000,4000,5000]
        self.price_adidas=[1000,2000,3000,4000,5000]
        self.price_puma=[1000,2000,3000,4000,5000]
        self.price_reebok=[1000,2000,3000,4000,5000]
        self.price_salomon=[1000,2000,3000,4000,5000]   
        #forslipper
        self.slipper=["nike","adidas","puma","reebok","salomon","bata"]
        self.price_nike=[1000,2000,3000,4000,5000]
        self.price_adidas=[1000,2000,3000,4000,5000]
        self.price_puma=[1000,2000,3000,4000,5000]
        self.price_reebok=[1000,2000,3000,4000,5000]
        self.price_salomon=[1000,2000,3000,4000,5000] 
        
        
        """#IMAGE-1
        img=Image.open("images/a1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)   #(antialias is used to make image smooth means convert high level image to low level image)
        self.photoimg=ImageTk.PhotoImage(img)  #(convert image into tkinter photoimage)
        
        lbl1=Label(self.root,image=self.photoimg)
        lbl1.place(x=0,y=0,width=500,height=130)
         
        #IMAGE-2
        img1=Image.open("images/a2.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)   #(antialias is used to make image smooth means convert high level image to low level image)
        self.photoimg1=ImageTk.PhotoImage(img1)  #(convert image into tkinter photoimage)
        
        lbl2=Label(self.root,image=self.photoimg1)
        lbl2.place(x=500,y=0,width=500,height=130)
        
        #IMAGE-3
        img2=Image.open("images/a3.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)   #(antialias is used to make image smooth means convert high level image to low level image)
        self.photoimg2=ImageTk.PhotoImage(img2)  #(convert image into tkinter photoimage)
        
        lbl3=Label(self.root,image=self.photoimg2)
        lbl3.place(x=1000,y=0,width=550,height=130)"""
        
        
        lbl_title = Label(self.root,text="BILLING SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=0,width=1530,height=80)
        
        #main frame
        main_frame = Frame(self.root,bd=5,relief=GROOVE) #(bd is border) #(relief is border line) #(frame is a box)
        main_frame.place(x=0,y=80,width=1530,height=575)
        
        #customer frame
        customer_frame = LabelFrame(main_frame,bd=5,relief=GROOVE,text="Customer Details",font=("times new roman",12,"bold"),fg="red",bg="white")
        customer_frame.place(x=15,y=5,width=400,height=170)
        
        #customer mobile details
        self.lbl_mob = Label(customer_frame,text="Mobile Number:",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)    #(sticky=W is used for left side or right side)
        
        self.txt_mob = ttk.Entry(customer_frame,font=("times new roman",10,"bold"),width=30)  #(for taking entry)
        self.txt_mob.grid(row=0,column=1,padx=5,pady=2,sticky=W)    #(pad shows the padding)
        
        #customer name details
        self.lbl_name = Label(customer_frame,text="Customer Name:",font=("arial",12,"bold"),bg="white",bd=5)
        self.lbl_name.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        
        self.txt_name = ttk.Entry(customer_frame,font=("arial",10,"bold"),width=30)
        self.txt_name.grid(row=1,column=1,padx=5,pady=2,sticky=W)
        
        #customer email details
        self.lbl_email = Label(customer_frame,text="Email:",font=("arial",12,"bold"),bg="white",bd=5)
        self.lbl_email.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        
        self.txt_email = ttk.Entry(customer_frame,font=("arial",10,"bold"),width=30)
        self.txt_email.grid(row=2,column=1,padx=5,pady=2,sticky=W)
        
        #customer address details
        self.lbl_address = Label(customer_frame,text="Address:",font=("arial",12,"bold"),bg="white",bd=5)
        self.lbl_address.grid(row=3,column=0,sticky=W,padx=5,pady=2)
        
        self.txt_address = ttk.Entry(customer_frame,font=("arial",10,"bold"),width=30)
        self.txt_address.grid(row=3,column=1,padx=5,pady=2,sticky=W)
        
        #product frame
        product_frame = LabelFrame(main_frame,bd=5,relief=GROOVE,text="Product Details",font=("times new roman",12,"bold"),fg="red",bg="white")
        product_frame.place(x=430,y=5,width=490,height=220)
        
        #product category details
        self.product_category = Label(product_frame,text="Product Category:",font=("arial",12,"bold"),bg="white",bd=5)
        self.product_category.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        
        self.txt_product_category = ttk.Combobox(product_frame,value=self.product_category_List ,font=("arial",10,"bold"),width=30,state="readonly")
        self.txt_product_category.current(0)
        self.txt_product_category.grid(row=0,column=1,padx=5,pady=2,sticky=W)
        self.txt_product_category.bind("<<ComboboxSelected>>",self.categories)
        
        #product sub category details
        self.product_subcategory = Label(product_frame,text="Product Sub Category:",font=("arial",12,"bold"),bg="white",bd=5)
        self.product_subcategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        
        self.txt_product_subcategory = ttk.Combobox(product_frame,values=[""],font=("arial",10,"bold"),width=30,state="readonly")
        self.txt_product_subcategory.grid(row=1,column=1,padx=5,pady=2,sticky=W)
        self.txt_product_subcategory.bind("<<ComboboxSelected>>",self.product_add)
        
        #product name details
        self.lbl_product_name = Label(product_frame,text="Product Name:",font=("arial",12,"bold"),bg="white",bd=5)
        self.lbl_product_name.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        
        self.txt_product_name = ttk.Combobox(product_frame,font=("arial",10,"bold"),width=30,state="readonly")
        self.txt_product_name.grid(row=2,column=1,padx=5,pady=2,sticky=W)
        
        #product price details
        self.lbl_price = Label(product_frame,text="Price:",font=("arial",12,"bold"),bg="white",bd=5)
        self.lbl_price.grid(row=3,column=0,sticky=W,padx=5,pady=2)
        
        self.txt_price = ttk.Combobox(product_frame,font=("arial",10,"bold"),width=30) 
        self.txt_price.grid(row=3,column=1,padx=5,pady=2,sticky=W)
        
        #product quantity details
        self.lbl_quantity = Label(product_frame,text="Quantity:",font=("arial",12,"bold"),bg="white",bd=5)
        self.lbl_quantity.grid(row=4,column=0,sticky=W,padx=5,pady=2)
        
        self.txt_quantity = ttk.Entry(product_frame,font=("arial",10,"bold"),width=30)
        self.txt_quantity.grid(row=4,column=1,padx=5,pady=2,sticky=W)
        
         #frequently customer frame
        frequently_customer_frame = LabelFrame(main_frame,bd=5,relief=GROOVE,text="Frequently Customer",font=("times new roman",12,"bold"),fg="red",bg="white")
        frequently_customer_frame.place(x=15,y=185,width=400,height=110)
        
        #check customer frequently come or not
        self.chk_frequent = Label(frequently_customer_frame,text="Frequent Customer:",font=("times new roman",12,"bold"),bg="white",bd=5,)
        self.chk_frequent.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        
        self.chk_frequent = ttk.Combobox(frequently_customer_frame,font=("times new roman",10,"bold"),width=25)
        self.chk_frequent.grid(row=0,column=1,padx=5,pady=2,sticky=W)
        
        #if yes then regular id 
        self.id_regular = Label(frequently_customer_frame,text="Regular Customer id:",font=("times new roman",12,"bold"),bg="white",bd=5,)
        self.id_regular.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        
        self.id_regular = ttk.Entry(frequently_customer_frame,font=("times new roman",10,"bold"),width=25)
        self.id_regular.grid(row=1,column=1,padx=5,pady=2,sticky=W)
        
        #bill area frame in right side
        RIGHT_frame = LabelFrame(main_frame,bd=5,relief=GROOVE,text="Bill Area",font=("times new roman",12,"bold"),fg="red",bg="white")
        RIGHT_frame.place(x=940,y=5,width=570,height=545)
        
        SCROLL_Y = Scrollbar(RIGHT_frame,orient=VERTICAL)
        self.txtarea = Text(RIGHT_frame,yscrollcommand=SCROLL_Y.set,bg="white",fg="black",font=("times new roman",12,"bold"))
        SCROLL_Y.pack(side=RIGHT,fill=Y)
        SCROLL_Y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
         # bill search frame
        s_customer_frame = LabelFrame(main_frame,bd=5,relief=GROOVE,text="Bill Search",font=("times new roman",12,"bold"),fg="red",bg="white")
        s_customer_frame.place(x=430,y=460,width=490,height=87)
        
        self.search_frame = Label(s_customer_frame,text="Bill Number:",font=("times new roman",12,"bold"),fg="black",bg="white")
        self.search_frame.grid(row=0,column=0,sticky=W,padx=5,pady=3)
        
        self.txt_search = ttk.Entry(s_customer_frame,width=30,font=("times new roman",10,"bold"))
        self.txt_search.grid(row=0,column=1,padx=5,pady=3,sticky=W)
        
        #search button
        self.btn_search = Button(s_customer_frame,text="Search",font=("times new roman",13,"bold"),bg="red",fg="white",width=12 ,cursor="hand2")
        self.btn_search.grid(row=0,column=2,padx=3,pady=2,sticky=W)
        
        
        #bill counter label frame
        bill_counter_frame = LabelFrame(main_frame,bd=5,relief=GROOVE,text="Bill Counter",font=("times new roman",12,"bold"),fg="red",bg="white")
        bill_counter_frame.place(x=430,y=240,width=490,height=200)
        
        # for sub-total frame
        self.lbl_sub_total = Label(bill_counter_frame,text="Sub Total:",font=("times new roman",12,"bold"),bg="white",bd=5,)
        self.lbl_sub_total.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        
        self.txt_sub_total = ttk.Entry(bill_counter_frame,font=("times new roman",10,"bold"),width=30)
        self.txt_sub_total.grid(row=0,column=1,padx=5,pady=2,sticky=W)
        
        #for tax frame
        self.lbl_tax = Label(bill_counter_frame,text="Goverment Tax:",font=("times new roman",12,"bold"),bg="white",bd=5,)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        
        self.txt_tax = ttk.Entry(bill_counter_frame,font=("times new roman",10,"bold"),width=30)
        self.txt_tax.grid(row=1,column=1,padx=5,pady=2,sticky=W)
        
        #for total amount frame
        self.lbl_total_amount = Label(bill_counter_frame,text="Total Amount:",font=("times new roman",12,"bold"),bg="white",bd=5,)
        self.lbl_total_amount.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        
        self.txt_total_amount = ttk.Entry(bill_counter_frame,font=("times new roman",10,"bold"),width=30)
        self.txt_total_amount.grid(row=2,column=1,padx=5,pady=2,sticky=W)
        
        #type of payment frame
        self.lbl_type_of_payment = Label(bill_counter_frame,text="Type of Payment:",font=("times new roman",12,"bold"),bg="white",bd=5,)
        self.lbl_type_of_payment.grid(row=3,column=0,sticky=W,padx=5,pady=2)
        
        self.txt_type_of_payment = ttk.Combobox(bill_counter_frame,font=("times new roman",10,"bold"),width=30)
        self.txt_type_of_payment.grid(row=3,column=1,padx=5,pady=2,sticky=W)
       
        #button frame for add to cart
        b_frame = Frame(main_frame,bd=5,bg="white",relief=GROOVE)
        b_frame.place(x=15,y=310,width=175,height=73)
        
        self.btn_submit = Button(b_frame,text="Add to cart",font=("times new roman",20,"bold"),bd=5,bg="red",fg="white",cursor="hand2")
        self.btn_submit.grid(row=0,column=0)
        
        #button frame for generate bill
        g_frame = Frame(main_frame,bd=5,bg="white",relief=GROOVE)
        g_frame.place(x=15,y=395,width=198,height=74)
        
        self.btn_generate = Button(g_frame,text="Generate Bill",font=("times new roman",20,"bold"),bd=5,bg="red",fg="white",cursor="hand2")
        self.btn_generate.grid(row=0,column=0)
        
        #for save bill
        s_frame = Frame(main_frame,bd=5,bg="white",relief=GROOVE)
        s_frame.place(x=15,y=480,width=147,height=72)
        
        self.btn_save = Button(s_frame,text="Save Bill",font=("times new roman",20,"bold"),bd=5,bg="red",fg="white",cursor="hand2")
        self.btn_save.grid(row=0,column=0)
        
        #for print bill
        p_frame = Frame(main_frame,bd=5,bg="white",relief=GROOVE)
        p_frame.place(x=240,y=310,width=153,height=73)
        
        self.btn_print = Button(p_frame,text="Print Bill",font=("times new roman",20,"bold"),bd=5,bg="red",fg="white",cursor="hand2")
        self.btn_print.grid(row=0,column=0)
        
        #for clear bill
        c_frame = Frame(main_frame,bd=5,bg="white",relief=GROOVE)
        c_frame.place(x=240,y=395,width=157,height=74)
        
        self.btn_clear = Button(c_frame,text="Clear Bill",font=("times new roman",20,"bold"),bd=5,bg="red",fg="white",cursor="hand2")
        self.btn_clear.grid(row=0,column=0)
        
        #for exit bill
        e_frame = Frame(main_frame,bd=5,bg="white",relief=GROOVE)
        e_frame.place(x=240,y=480,width=150,height=72)
        
        self.btn_exit = Button(e_frame,text="Exit Bill",font=("times new roman",20,"bold"),bd=5,bg="red",fg="white",cursor="hand2")
        self.btn_exit.grid(row=0,column=0)
        
    def categories(self, event=""):
        if self.txt_product_category.get() == "Clothing":
            self.txt_product_subcategory.config(values = self.product_subcategory_clothing_List)
            self.txt_product_subcategory.current(0)
        
        if self.txt_product_category.get() == "Lifestyle":
            self.txt_product_subcategory.config(values = self.product_subcategory_lifestyle_List)
            self.txt_product_subcategory.current(0)
            
        if self.txt_product_category.get() == "Footwear":
            self.txt_product_subcategory.config(values = self.product_subcategory_footwear_List)
            self.txt_product_subcategory.current(0)
            
    def product_add(self, event=""):
        """if self.txt_product_subcategory.get() == "T-Shirts":
             self.txt_product_name.config(values = self.tshirts)
             self.txt_product_name.current(0)"""
            
        if self.txt_product_subcategory.get() == "Trousers":
             self.txt_product_name.config(values = self.trousers)
             self.txt_product_name.current(0)
        
        if self.txt_product_subcategory.get() == "Jackets":
             self.txt_product_name.config(values = self.jacket)
             self.txt_product_name.current(0)
             
        """if self.txt_product_subcategory.get() == "Shirt":
             self.txt_product_name.config(values = self.shirt) 
             self.txt_product_name.current(0)"""
        
        if self.txt_product_subcategory.get() == "hair oil":
            self.txt_product_name.config(values = self.hair_oil)
            self.txt_product_name.current(0)
            
        if self.txt_product_subcategory.get() == "shampoo":
            self.txt_product_name.config(values = self.shampoo)
            self.txt_product_name.current(0)
        
        if self.txt_product_subcategory.get() == "face cream":
            self.txt_product_name.config(values = self.face_cream)
            self.txt_product_name.current(0)
        
        if self.txt_product_subcategory.get() == "face wash":
            self.txt_product_name.config(values = self.face_wash)
            self.txt_product_name.current(0)
            
        if self.txt_product_subcategory.get() == "bodylotion":
            self.txt_product_name.config(values = self.bodylotion)
            self.txt_product_name.current(0)
        
        if self.txt_product_subcategory.get() == "bodysoap":
            self.txt_product_name.config(values = self.bodysoap)
            self.txt_product_name.current(0)
            
        if self.txt_product_subcategory.get() == "deodrant":
            self.txt_product_name.config(values = self.deodrant)
            self.txt_product_name.current(0)
            
        if self.txt_product_subcategory.get() == "face pack":
            self.txt_product_name.config(values = self.face_pack)
            self.txt_product_name.current(0)
            
        if self.txt_product_subcategory.get() == "lipstick":
            self.txt_product_name.config(values = self.lipstick)
            self.txt_product_name.current(0)
            
        if self.txt_product_subcategory.get() == "sneakers":
            self.txt_product_name.config(values = self.sneakers)
            self.txt_product_name.current(0)
            
        if self.txt_product_subcategory.get() == "formal":
            self.txt_product_name.config(values = self.formal)
            self.txt_product_name.current(0)
            
        if self.txt_product_subcategory.get() == "casual":
            self.txt_product_name.config(values = self.casual)
            self.txt_product_name.current(0)
            
        if self.txt_product_subcategory.get() == "sports":
            self.txt_product_name.config(values = self.sports)
            self.txt_product_name.current(0)
        
        if self.txt_product_subcategory.get() == "boots":
            self.txt_product_name.config(values = self.boots)
            self.txt_product_name.current(0)
            
        if self.txt_product_subcategory.get() == "heels":
            self.txt_product_name.config(values = self.heels)
            self.txt_product_name.current(0)
        
        if self.txt_product_subcategory.get() == "sandals":
            self.txt_product_name.config(values = self.sandals)
            self.txt_product_name.current(0)
            
        if self.txt_product_subcategory.get() == "flipflops":
            self.txt_product_name.config(values = self.flipflops)
            self.txt_product_name.current(0)
            
        if self.txt_product_subcategory.get() == "slippers":
            self.txt_product_name.config(values = self.slipper)
            self.txt_product_name.current(0)
                        
            
            
            
            
            
            
            
            
            
        
if __name__ == "__main__":
    root = Tk()
    obj = BILL_Application(root)
    root.mainloop()    #(main loop work upto till when we close the window or program)
