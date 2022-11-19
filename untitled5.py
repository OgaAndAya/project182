from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Language Translator")
root.geometry("500x500")
root.configure(background_color= "orange")

languages_list= ["Japanese","English","Spanish","Italian","Chinese","Korean"]
dropdown= ttk.combobox(root,state= readonly,values= languages_list,width=50)
dropdown.place(relx=0.3,rely=0.5,anchor=CENTER)
dropdown_name.set("English")
label_output=Label(root,text="Output",bg= "orannge")
label_output.place(relx=0.5,rely=0.35,anchor= E)    
dropdown2= ttk.combobox(root,state= readonly,values= languages_list,width=50)
dropdown2.place(relx=0.15,rely=0.35,anchor=CENTER)
dropdown_name2.set("Japanese")
text_area2= Text(root,bg= "orange",fg="cursive",height=50,wrap= WORD,width=75,padx=15,pady=20,bd=0)
text_area2.place(relx=0.5,rely=0.25,anchor=CENTER)          

label= Label(root,text= "LANGUAGE TRANSLATOR",bg= "orange",font= "cursive")
label.place(relx=0.5,rely= 0.1,anchor= CENTER)
enter= Label(root,text="Enter Text",bg= "orange",font= "cursive")
enter.place(relx=0.2,rely=0.5,anchor=CENTER)
text_area= Text(root,bg= "orange",fg="cursive",height=50,wrap= WORD,width=75,padx=15,pady=20,bd=0)
text_area.place(relx=0.4,rely=0.5,anchor=CENTER)

btn = Button(root, text = "Translate", font = ("Comic Sans MS", 10, "italic"),bg = "orange", activebackground = "red", relief = "flat", pady = 2)
btn.place(relx = 0.5, rely = 0.8, anchor = CENTER)
root.mainloop()