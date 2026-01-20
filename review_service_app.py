from tkinter import*
import tkinter.messagebox as msg
root=Tk()

root.title('REVIEW SERVICE')
root.geometry('666x444')

f1=Frame(root,bg="#E8F4F8",width=666,height=444)
f1.pack()

def Sliderfunc():
    rt=Toplevel(root)
    rt.title('YOUR REVIEW')
    rt.geometry('444x333')
    f1= Frame(rt,height=333,width=444)
    f1.pack(side='top',pady=15)
    
    # Create Aqua to Pink gradient
    from PIL import Image, ImageDraw, ImageTk as ITK
    gradient_img = Image.new('RGB', (444, 333), color='white')
    gradient_draw = ImageDraw.Draw(gradient_img)
    
    # Draw gradient (Aqua to Pink)
    for y in range(333):
        ratio = y / 333
        r = int(0 + (255 - 0) * ratio)  # 0 to 255 (Red increases)
        g = int(255 + (105 - 255) * ratio)  # 255 to 105 (Green decreases)
        b = int(255 + (180 - 255) * ratio)  # 255 to 180 (Blue decreases)
        gradient_draw.line([(0, y), (444, y)], fill=(r, g, b))
    
    gradient_photo = ITK.PhotoImage(gradient_img)
    gradient_label = Label(f1, image=gradient_photo)
    gradient_label.image = gradient_photo
    gradient_label.pack(fill='both', expand=True)
    
    Label(gradient_label,text='Chose your Review Rate here you can decide',font=('Times New Roman',16 ,'bold '),bg='lightblue').pack(pady=5)
    sc=Scale(gradient_label,from_=0,to=10,orient='horizontal',bg='white')
    sc.pack(pady=5)
    
    def submit_review():
        if sc.get() == 0:
            msg.showerror('Error', 'Please enter your Review (Select 1-10)')
        else:
            msg.showinfo('Thank You!', 'Thank you for your valuable review!\n\nYour feedback helps us improve our services.\nWe appreciate your time and suggestions!')
            with open('Save Review.txt', 'a') as f:
                f.write(f"{sc.get()}: This is user's review\n")
            print(f"\nReview saved: {sc.get()}")
    
    Button(gradient_label, text='Enter your review', command=submit_review,pady=15,bg='green',fg='white',font='Helvatica 12 bold').pack(pady=15)
        


#Label(text='REVIEW SERVICE - APPLICATION OVERVIEW',font=('Times New Roman', 20 ,'bold')).pack()
Label(f1, bg='#E8F4F8',text="REVIEW SERVICE - APPLICATION OVERVIEW", font=("Helvetica", 20, "bold")).grid(row=0,column=1,sticky='n')


Label(f1, bg='#E8F4F8',text="Service Description:", font=("Times New Roman", 16, "bold")).grid(row=1,column=0)
                
Label(f1, bg='#E8F4F8',text='''The Review Service application is a user-friendly platform designed to collect, manage,
      \nand display customer feedback and ratings. This application enables businesses to gather valuable
      \ninsights from their clients regarding product quality, service satisfaction, and overall customer 
      \nexperience.''',
      pady=20, font=("Verdana",10, "bold")).grid(row=3,column=1)

Label(f1,bg='#E8F4F8',text='Key Services:',font='Arial 12 bold',pady=10).grid(row=5,column=0)

Label(f1,bg='#E8F4F8',text='''RATING SYSTEM : Users can rate services on a scale (0-10) using an intuitive \nslider interface
                     FEEDBACK COLLECTION : Comprehensive feedback mechanism for detailed customer reviews\n
            USER INTERFACE : Clean, responsive GUI built with Tkinter for easy accessibility \n
            DATA MANAGEMENT : Organize and store all customer reviews and ratings \n
              ANALYTICS: Track customer satisfaction trends and service performance metrics''',font='Trebuchet 9 bold',pady=10).grid(row=6,column=1)

Label(f1,bg='#E8F4F8',text='Purpose:',font='Georgia 12 bold').grid(row=7,column=0)

Label(f1,bg='#E8F4F8',text='This service helps businesses understand customer satisfaction levels,\n identify areas for improvement, and make data-driven decisions to enhance their offerings.',
      font=('Comic Sans', 9,' bold'),pady=10).grid(row=8,column=1)     
Button(f1, text="Submit Review", font=("Helvetica", 12, "bold"),command=Sliderfunc,bg="green", fg="white", padx=20, pady=10,).grid(row=10, column=1, pady=20)

root.mainloop()