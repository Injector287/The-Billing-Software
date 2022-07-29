#Import statements
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
import tkinter.ttk as ttk
import csv
import pandas as pd

# Window
k = tk.Tk()
k.geometry("450x250")
k.title("Server Entry")
k.configure(background='White')

# Non resizable window
k.resizable(0,0)


#Heading Tag
Bill=tk.Label(k, text="Bill Book", bg='White', fg='Black')
Bill.config(font=("Arial", 22))
Bill.pack()
Bill.place(x=200, y=10)


# UsernameTag
user=tk.Label(k, text="User ID:", bg='White', fg='Black')
user.config(font=("Arial", 15))
user.pack()
user.place(x=50, y=80)

# UsernameType
name=ttk.Entry(width=35)
name.pack()
name.place(x=150, y=85)

# PasswordTag
pas=tk.Label(k, text="Password:", bg='White',fg='Black')
pas.config(font=("Arial", 15))
pas.pack()
pas.place(x=50, y=120)

# PasswordType
word=ttk.Entry(k, show="*", width=35)
word.pack()
word.place(x=150, y=125)

# OpenNewWindow


def HomeScrn():
    k.withdraw()
    HMS=tk.Toplevel()
    HMS.geometry("200x150")
    HMS.title('Title')
    HMS.resizable(0,0)

    def KSAwin():
        HMS.withdraw()
        KSA=tk.Toplevel()
        KSA.geometry("350x300")
        KSA.title("Enter Values")
        o=open("stocks.csv",'a',newline="")
        x=csv.writer(o)
# ProductNumTag
        ProductNumTag=tk.Label(KSA,text="Product No.")
        ProductNumTag.pack()
        ProductNumTag.place(x=50, y=50)
# ProductNumEntry       
        ProductNumEntry=ttk.Entry(KSA,text="Product No.")
        ProductNumEntry.pack()
        ProductNumEntry.place(x=150,y=50)
# ProductNameTag
        ProductNameTag=tk.Label(KSA,text="Product Name")
        ProductNameTag.pack()
        ProductNameTag.place(x=50, y=100)
# ProductNameEntry
        ProductNameEntry=ttk.Entry(KSA,text="Product Name")
        ProductNameEntry.pack()
        ProductNameEntry.place(x=150,y=100)
# ProductQtyTag
        ProductQtyTag=tk.Label(KSA,text="Product Qty")
        ProductQtyTag.pack()
        ProductQtyTag.place(x=50, y=150)
# ProductQtyEntry
        ProductQtyEntry=ttk.Entry(KSA,text="Product Qty")
        ProductQtyEntry.pack()
        ProductQtyEntry.place(x=150,y=150)
# ProductPriceTag
        ProductPriceTag=tk.Label(KSA,text="Product Price(₹)")
        ProductPriceTag.pack()
        ProductPriceTag.place(x=50, y=200)
# ProductPriceEntry
        ProductPriceEntry=ttk.Entry(KSA,text="Product Price (₹)")
        ProductPriceEntry.pack()
        ProductPriceEntry.place(x=150,y=200)
# Defining Addnew Button
        def Addnewdef():
# Values
            Pno=ProductNumEntry.get()
            PName=ProductNameEntry.get()
            PQty=ProductQtyEntry.get()
            PPrice=ProductPriceEntry.get()
# Writing Stocks
            R=[Pno,PName,PQty,PPrice]
            x.writerow(R)
# Clearing Entry 
            ProductNumEntry.delete(0,'end')
            ProductNameEntry.delete(0,'end')
            ProductQtyEntry.delete(0,'end')
            ProductPriceEntry.delete(0,'end')
# Defining Submit Button
        def Submitdef():
            Pno=ProductNumEntry.get()
            PName=ProductNameEntry.get()
            PQty=ProductQtyEntry.get()
            PPrice=ProductPriceEntry.get()
            R=[Pno,PName,PQty,PPrice]
            x.writerow(R)
            o.close()
            k.destroy()

# SubmitButton
        Submit=ttk.Button(KSA,text="Submit and Close", command=Submitdef)
        Submit.pack()
        Submit.place(x=45,y=250)
# AddNewButton
        Addnew=ttk.Button(KSA,text="Submit and Add New", command=Addnewdef)
        Addnew.pack()
        Addnew.place(x=170,y=250)
        KSA.mainloop()

    def KSSwin():
        HMS.withdraw()   
        KSS=tk.Toplevel()
        KSS.geometry("400x400")
        KSS.title("Bill Generation")
        KSS.resizable(0,0)
        o=open("Bill.csv",'w',newline="")
        x=csv.writer(o)
        fields=['UPN','Name','Qty','MRP','Price']
        x.writerow(fields)

        SecVar=tk.StringVar()
        TerVar=tk.IntVar()
        QuadVar=tk.IntVar()

        def nex(event):
            UPN=UniqueProductNo.get() 
            o=open("stocks.csv")
            x=csv.reader(o)
            for row in x:
                if UPN==(row[0].split(',')[0]):
#Setting Variables
                    SecVar.set(row[1].split(',')[0])
                    TerVar.set(row[2].split(',')[0])
                    QuadVar.set(row[3].split(',')[0])
         
#Product Name
                    ProdName=ttk.Label(KSS,textvariable=SecVar)
                    ProdName.pack()
                    ProdName.place(x=100,y=100)
#Product Price 
                    SellPrice=tk.Label(KSS,textvariable=QuadVar)
                    SellPrice.pack()
                    SellPrice.place(x=100,y=150)         
            
#ComboBox for Unique Product Number
        Combobox=tk.StringVar() 
        UniqueProductNo=ttk.Combobox(KSS, width = 27, textvariable = Combobox) 
        EmptyList=[]
        o=open("stocks.csv")
        x=csv.reader(o)
        for row in x:
            intvar=(row[0])
            EmptyList.append(intvar)
            UniqueProductNo['values']=EmptyList
            UniqueProductNo.bind('<<ComboboxSelected>>',nex)
    
        UPN=UniqueProductNo.get()    
        UniqueProductNo.pack()
        UniqueProductNo.place(x=100,y=50) 
 
#ProductNumberLabel
        ProductNumberLabel=ttk.Label(KSS, text = "Prod No:")
        ProductNumberLabel.pack()
        ProductNumberLabel.place(x=25,y=50)

#ProductNameLabel
        ProductNameLabel=ttk.Label(KSS, text="Prod Name:")
        ProductNameLabel.pack()
        ProductNameLabel.place(x=25,y=100)

#ProductPriceLabel
        SellPriceLabel=ttk.Label(KSS,text='MRP:')
        SellPriceLabel.pack()
        SellPriceLabel.place(x=25,y=150)

#ProductQtyLabel
        ProductQtyLabel=ttk.Label(KSS,text='Prod Qty:')
        ProductQtyLabel.pack()
        ProductQtyLabel.place(x=25,y=200)

#ProductQtyEntry
        ProdQtyData=tk.IntVar()
        ProductQtyEntry=ttk.Entry(KSS,textvariable=ProdQtyData)
        ProductQtyEntry.place()
        ProductQtyEntry.place(x=100,y=200)

#TotalProductPriceLabel
        TotalPrice=tk.Label(KSS,text='Total Price:')
        TotalPrice.pack()
        TotalPrice.place(x=25,y=250)

        def next():
            UPN=UniqueProductNo.get() 
            o=open("stocks.csv",'r')
            x=csv.reader(o)
            for row in x:
                if UPN==(row[0].split(',')[0]):
#Setting Variables
                    SecVar.set(row[1].split(',')[0])
                    TerVar.set(row[2].split(',')[0])
                    QuadVar.set(row[3].split(',')[0])
                    PQE=ProductQtyEntry.get()
                    QuadData=QuadVar.get()
                    TerData=TerVar.get()
#Total Price
                    TP=tk.IntVar()
                    TP.set(QuadData*int(PQE))
#Total Price Label
                    TotalPrice=tk.Label(KSS,textvariable=TP)
                    TotalPrice.pack()
                    TotalPrice.place(x=100,y=250)
    
        def Addnew():
            o=open("Bill.csv",'a',newline="")
            x=csv.writer(o)
            SecData=SecVar.get()
            QuadData=QuadVar.get()
            UPN=UniqueProductNo.get()
            PQE=ProductQtyEntry.get()
            TP=tk.IntVar()
            TP.set(QuadData*int(PQE))
            tpn=TP.get()
            write=[UPN,SecData,PQE,QuadData,tpn]
            x.writerow(write) 
            o.close()
   
        def submit():  
            a=pd.read_csv('Bill.csv')
            total=(a['Price'].sum())
            inclGST=(total+((total/100)*12))
            Tprice=("Your total expense is ₹"+str(inclGST)+"\n"+"including GST 12%")
            print(str(Tprice))
            messagebox.showinfo('Bill',Tprice)
            k.destroy()

#Total Button
        NextButton=ttk.Button(KSS,text='Total',command=next)
        NextButton.pack()
        NextButton.place(x=25,y=300)
#Save Button
        Addnew=ttk.Button(KSS,text='Save',command=Addnew)
        Addnew.pack()
        Addnew.place(x=125,y=300)
#Sumit Button
        Submit=ttk.Button(KSS,text='Grand Total',command=submit) 
        Submit.pack()
        Submit.place(x=225,y=300)

        KSS.mainloop()


#KSA Button
    KSAb=ttk.Button(HMS,text="Add Stocks",command=KSAwin)
    KSAb.pack()
    KSAb.place(x=55,y=50)
#KSS Button
    KSSb=ttk.Button(HMS,text="Bill Gen",command=KSSwin) 
    KSSb.pack()
    KSSb.place(x=55,y=75) 
        
    HMS.mainloop()

# Access
def access():
    username=name.get()
    password=word.get()
    if username=="Admin" and password=="Password":
        msg1=tk.messagebox.showinfo("Info", "Access Granted")
        HomeScrn()
    elif username=="Developer#1" and password =="Shyaam":
        tk.messagebox.showinfo("Info","Access Granted")
        HomeScrn()
    elif username=="Developer#2" and password=="Sanjay":
        tk.messagebox.showinfo("Info", "Access Granted")
        HomeScrn()
    elif username=="Developer#3" and password=="Varadhan":
        tk.messagebox.showinfo("Info", "Access Granted")
        HomeScrn()
    else:
        tk.messagebox.askretrycancel("Access Denied", "Incorrect Password! Try Again")
       
def credits():
    credit=('Made By:','Shyaam Menon','Pranatharthi','G Sanjay')
    messagebox.showinfo('Credits','\n'.join(credit))
enter= ttk.Button(text='Credits',command=credits)
enter.pack()
enter.place(x=170,y=170)

def register():
   messagebox.showinfo('Register','To Register Contact the Server at Server@dev.com')
enter= ttk.Button(text='Register',command=register)
enter.pack()
enter.place(x=70,y=170)

# EnterButton
enter = ttk.Button(text="Connect",command=access)
enter.pack()
enter.place(x=260, y=170)    

k.mainloop()