import random
import pickle
import tkinter
from tkinter import *
from tkinter import messagebox

def math_3_numbers_med_add():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    c = random.randint(1, 20)
    expression = f"{a}+{b}+{c}"
    return expression


def math_4_number_hard_add():
    a = random.randint(100, 1000)
    b = random.randint(100, 1000)
    c = random.randint(100, 1000)
    d = random.randint(100, 1000)
    expression = f"{a}+{b}+{c}+{d}"
    return expression

def math_3_number_med_mix():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = random.randint(1, 100)
    operator = ("+", "-")
    expression = f"{a}{random.choice(operator)}{b}{random.choice(operator)}{c}"
    return expression


def math_4_number_hard_mix():
    a = random.randint(10, 1000)
    b = random.randint(10, 1000)
    c = random.randint(10, 1000)
    d = random.randint(10, 1000)
    operator = ("+", "-")
    expression = f"{random.choice(operator)}{b}{random.choice(operator)}{c}{random.choice(operator)}{d}"
    return expression
#creating a binary file to store and read data later
def bin_file():
    f=open("highscore.bin","ab+")
    try:
        data=pickle.load(f)
        if len(data)==0:
            name_highscore={}
            pickle.dump(name_highscore,f)
            f.close()
        else:
            f.close()
    except:
        name_highscore = {}
        pickle.dump(name_highscore, f)
        f.close()
bin_file()
score=0
question_number=1
name=""
def update_score(name,score):
    f=open("highscore.bin","rb+")
    a=pickle.load(f)
    f.close()
    if len(a)==0:
        a[name]=score
        f = open("highscore.bin", "wb+")
        pickle.dump(a, f)
        f.close()

    else:
        key=a.keys()
        for i in key:
            high=a[i]
        if high<score:
            a.clear()
            a[name]=score
            f=open("highscore.bin","wb+")
            pickle.dump(a,f)
            f.close()
        else:
            pass

def first_page():
    fk = tkinter.Tk()
    fk.title("Maths Quiz Game!")
    fk.minsize(800, 500)
    fk.maxsize(800, 500)
    fk.configure(bg="pink")
    #Create a canvas object
    canvas= Canvas(fk, width= 800, height= 500, bg="bisque")
    #Add a text in Canvas
    canvas.create_text(380, 50, text="WELCOME TO MATHS QUIZ", fill="black", font=('Ariel 20 bold'))
    canvas.create_text(130, 250, text="ENTER YOUR NAME:", fill="black", font=('Helvetica 15 bold'))
    nameentry = Entry(fk)
    canvas.create_window(320, 250, window=nameentry)
    canvas.create_text(65, 400, text="HIGH SCORE:", fill="black", font=('Helvetica 15 bold'))
    #checking if there is a highscore or not:
    def high_score():
        f=open("highscore.bin","rb+")
        data=pickle.load(f)
        if len(data)==0:
            return 0
        else:
            key_value=data.items()
            for i in key_value:
                name=i[0]
                high_score=i[1]
                return f'{name}:{high_score}'
    canvas.create_text(70,430, text=high_score(), fill="dark green", font=('Helvetica 15 bold'))
    def submit():
        global name
        name=nameentry.get()
        if len(name)!=0:
            tk=tkinter.Tk()
            tk.title('QUIZ BEGINS!')
            tk.minsize(800, 500)
            tk.maxsize(800, 500)
            # Create a canvas object
            col=["lemon chiffon","light blue","light green","light pink","light yellow","light salmon","light sky blue","light steel blue","light coral","light goldenrod yellow","light sea green","light slate gray","light slate grey"]
            r_col=random.choice(col)
            canvas = Canvas(tk, width=800, height=500, bg=r_col)
            def random_ques():
                ques=[1,2,3,4]
                l=random.choice(ques)
                if l==1:
                    return math_3_number_med_mix()
                elif l==2:
                    return math_3_numbers_med_add()
                elif l==3:
                    return math_4_number_hard_add()
                else:
                    return math_4_number_hard_mix()
            def options():
                global question_number
                expression=(random_ques())
                canvas.create_text(100, 20, text=f">>Question:{question_number}>> {expression}", fill="Black",
                                   font=('Arial 13'))
                a=eval(expression)
                b=random.randint(a-10,a+10)
                c=random.randint(a-10,a+10)
                d=random.randint(a-10,a+10)
                option_list=[a,b,c,d]
                random.shuffle(option_list)
                return option_list,a

            tup=options()
            a=tup[0]
            ans=tup[1]
            for i in range(0, len(a)):
                if i == 0:
                    canvas.create_text(100, 100, text=f"{a[0]}", fill="Black",
                                       font=('Arial 13'))
                elif i == 1:
                    canvas.create_text(400, 100, text=f"{a[1]}", fill="Black",
                                       font=('Arial 13'))
                elif i == 2:
                    canvas.create_text(100, 300, text=f"{a[2]}", fill="Black",
                                       font=('Arial 13'))
                else:
                    canvas.create_text(400, 300, text=f"{a[3]}", fill="Black",
                                       font=('Arial 13'))
            def correct_option_a():
                global score,question_number,name
                if a[0]==ans:
                    score+=1
                    question_number+=1
                    tk.destroy()
                    submit()
                else:
                    tk.destroy()
                    update_score(name,score)
                    messagebox.showinfo("Wrong answer", f"{name} score is {score}")
                    name = ""
                    question_number=1

                    score=0
                    fk.destroy()
                    first_page()
            def correct_option_b():
                global score,question_number,name
                if a[1]==ans:
                    score+=1
                    question_number+=1
                    tk.destroy()
                    submit()
                else:
                    tk.destroy()
                    update_score(name, score)
                    messagebox.showinfo("Wrong answer", f"{name} score is {score}")
                    name = ""
                    question_number=1
                    score=0
                    fk.destroy()
                    first_page()
            def correct_option_c():
                global score,question_number,name
                if a[2]==ans:
                    score+=1
                    question_number+=1
                    tk.destroy()
                    submit()
                else:
                    tk.destroy()
                    update_score(name, score)
                    messagebox.showinfo("Wrong answer", f"{name} score is {score}")
                    name = ""
                    question_number=1

                    score=0
                    fk.destroy()
                    first_page()
            def correct_option_d():
                global score,question_number,name
                if a[3]==ans:
                    score+=1
                    question_number+=1
                    tk.destroy()
                    submit()
                else:
                    tk.destroy()
                    update_score(name, score)
                    messagebox.showinfo("Wrong answer", f"{name} score is {score}")
                    name=""
                    question_number=1

                    score=0
                    fk.destroy()
                    first_page()


            def select_option():
                submita = Button(tk, text="A", command=correct_option_a)
                submitb = Button(tk, text="B", command=correct_option_b)
                submitc = Button(tk, text="C", command=correct_option_c)
                submitd = Button(tk, text="D", command=correct_option_d)
                canvas.create_window(55, 100, window=submita)
                canvas.create_window(360, 100, window=submitb)
                canvas.create_window(55, 300, window=submitc)
                canvas.create_window(360, 300, window=submitd)
            select_option()
            canvas.pack()
            tk.mainloop()
        else:
            messagebox.showinfo("Name required", "Please enter your name")
            return name
    submit1 = Button(fk,text="Play" ,command=submit)
    canvas.create_window(400,250,window=submit1)
    canvas.pack()
    fk.mainloop()
first_page()
