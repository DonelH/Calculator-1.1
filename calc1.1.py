# Basic Calculator with Increase/Decrease font size functionality using tkinter
# Version 1.1 features increasing entry/results box font size and
# being able to do calculations based off results.

from tkinter import *
import tkinter.font as tkFont
import math

expression = ""

#Function for pressing button functionality
def press(num):
    global expression
    if (type(expression) == float):
        str(expression)
    expression = expression + str(num)
    equation.set(expression)
    
#Function for equal functionality
def equalpress():
    try:
        global expression
        global result
        total = str(eval(expression))
        equation.set(total)
        expression = total
        print(expression)
    except:
        equation.set(" error ")
        expression = ""
        
# Function for squaring numbers
def square():
    global expression
    squared = math.pow(int(expression), 2)
    equation.set(squared)
    expression = squared
    print(expression)
    print(type(expression))
    
# Function for square rooting numbers
def squareRoot():
    global expression
    squareRooted = math.sqrt(int(expression))
    equation.set(squareRooted)
    expression = squareRooted
    print(expression)

#Functions for Increasing/Decreasing font size    
def fontSizePlus():
    textSize = fontSize.cget('size') + 3
    fontSize.configure(size = textSize)
    
def fontSizeMinus():
    textSize = fontSize.cget('size') - 3
    fontSize.configure(size = textSize)

#Function for clearing calculator    
def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="#f7f7f7")
    gui.title("Basic Calculator")
    gui.geometry("330x200")
    fontSize = tkFont.Font(size=10)
    
    equation = StringVar()
    expression_field = Entry(gui, border=5, textvariable=equation,
                             font = fontSize)

    expression_field.grid(columnspan=5, ipadx=70, ipady=5)

    equation.set('')
    
    # Individual Button Setup
    button1 = Button(gui, text=' 1 ', font=fontSize, fg='#d9d9d9', bg='#252525', 
                     command=lambda: press(1), height=2, width=7) 
    button1.grid(row=2, column=0, sticky=(N, S, E, W))
    
    button2 = Button(gui, text=' 2 ', font=fontSize, fg='#d9d9d9', bg='#252525', 
                     command=lambda: press(2), height=2, width=7) 
    button2.grid(row=2, column=1, sticky=(N, S, E, W)) 
  
    button3 = Button(gui, text=' 3 ', font=fontSize, fg='#d9d9d9', bg='#252525', 
                     command=lambda: press(3), height=2, width=7) 
    button3.grid(row=2, column=2, sticky=(N, S, E, W)) 
  
    button4 = Button(gui, text=' 4 ', font=fontSize, fg='#d9d9d9', bg='#252525', 
                     command=lambda: press(4), height=2, width=7) 
    button4.grid(row=3, column=0, sticky=(N, S, E, W)) 
  
    button5 = Button(gui, text=' 5 ', font=fontSize, fg='#d9d9d9', bg='#252525', 
                     command=lambda: press(5), height=2, width=7) 
    button5.grid(row=3, column=1, sticky=(N, S, E, W)) 
  
    button6 = Button(gui, text=' 6 ', font=fontSize, fg='#d9d9d9', bg='#252525', 
                     command=lambda: press(6), height=2, width=7) 
    button6.grid(row=3, column=2, sticky=(N, S, E, W)) 
  
    button7 = Button(gui, text=' 7 ', font=fontSize, fg='#d9d9d9', bg='#252525', 
                     command=lambda: press(7), height=2, width=7) 
    button7.grid(row=4, column=0, sticky=(N, S, E, W)) 
  
    button8 = Button(gui, text=' 8 ', font=fontSize, fg='#d9d9d9', bg='#252525', 
                     command=lambda: press(8), height=2, width=7) 
    button8.grid(row=4, column=1, sticky=(N, S, E, W)) 
  
    button9 = Button(gui, text=' 9 ', font=fontSize, fg='#d9d9d9', bg='#252525', 
                     command=lambda: press(9), height=2, width=7) 
    button9.grid(row=4, column=2, sticky=(N, S, E, W)) 
  
    button0 = Button(gui, text=' 0 ', font=fontSize, fg='#d9d9d9', bg='#252525', 
                     command=lambda: press(0), height=2, width=7) 
    button0.grid(row=5, column=0, sticky=(N, S, E, W)) 
  
    plus = Button(gui, text=' + ', font=fontSize, fg='#d9d9d9', bg='#252525', 
                  command=lambda: press("+"), height=2, width=7) 
    plus.grid(row=2, column=3, sticky=(N, S, E, W)) 
  
    minus = Button(gui, text=' - ', font=fontSize, fg='#d9d9d9', bg='#252525', 
                   command=lambda: press("-"), height=2, width=7) 
    minus.grid(row=3, column=3, sticky=(N, S, E, W)) 
  
    multiply = Button(gui, text=' * ', font=fontSize, fg='#d9d9d9', bg='#252525', 
                      command=lambda: press("*"), height=2, width=7) 
    multiply.grid(row=4, column=3, sticky=(N, S, E, W)) 
  
    divide = Button(gui, text=' / ', font=fontSize, fg='#d9d9d9', bg='#252525', 
                    command=lambda: press("/"), height=2, width=7) 
    divide.grid(row=5, column=3, sticky=(N, S, E, W))
    
    square = Button(gui, text=' x^2 ', font=fontSize, fg='#d9d9d9',
                    bg='#252525', command=square, height=2, width=7)
    square.grid(row=2, column=4, sticky=(N, S, E, W))
    
    squareRoot = Button(gui, text=' sqrt ', font=fontSize, fg='#d9d9d9',
                        bg='#252525', command=squareRoot, height=2, width=7)
    squareRoot.grid(row=3, column=4, sticky=(N, S, E, W))

    fontSizePlus = Button(gui, text=' Font Size++ ',
                          fg='#d9d9d9', bg='#252525', command=fontSizePlus,
                          height=2, width=7)
    fontSizePlus.grid(row=4, column=4, sticky=(N, S, E, W))

    fontSizeMinus = Button(gui, text=' Font Size-- ',
                          fg='#d9d9d9', bg='#252525', command=fontSizeMinus,
                          height=2, width=7)
    fontSizeMinus.grid(row=5, column=4, sticky=(N, S, E, W))
    
    equal = Button(gui, text=' = ', font=fontSize, fg='#d9d9d9', bg='#252525', 
                   command=equalpress, height=2, width=7) 
    equal.grid(row=5, column=2, sticky=(N, S, E, W)) 
  
    clear = Button(gui, text='Clear', font=fontSize, fg='#d9d9d9', bg='#252525', 
                   command=clear, height=2, width=7) 
    clear.grid(row=5, column='1', sticky=(N, S, E, W))

    # Weights for configurations to expand with window
    gui.columnconfigure(0, weight=1)
    gui.columnconfigure(1, weight=1)
    gui.columnconfigure(2, weight=1)
    gui.columnconfigure(3, weight=1)
    gui.columnconfigure(4, weight=1)

    gui.rowconfigure(1, weight=1)
    gui.rowconfigure(2, weight=1)
    gui.rowconfigure(3, weight=1)
    gui.rowconfigure(4, weight=1)
    gui.rowconfigure(5, weight=1)
    
    gui.mainloop()
