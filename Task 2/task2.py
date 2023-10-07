
# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.
# Perform the calculation and display the result.

import tkinter as tk

SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYLE = ("Arial", 40, "bold")
DIGIT_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 30)

OFFWHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_GRAY = "#f5f5f5"
LABEL_COLOR = "#25265E"
LIGHT_BLUE = "#CCEDFF"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""
        
        self.display_frame = self.create_display_frame()
        
        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            '.':(4,1), 0:(4,2)
        }
        
        self.operators = {"/":"\u00F7", "*":"\u00D7", "-":"-", "+":"+"}
        self.buttons_frame = self.create_buttons_frame()
        
        self.buttons_frame.rowconfigure(0, weight=1)

        for x in range(1,5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)


        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit: self.add_to_expression(digit)) 

        for key in self.operators:
            self.window.bind(str(key), lambda event, operator: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equal_button()
        self.create_square_button()
        self.create_sqrt_button()

    def create_display_labels(self):
        total_label =tk.Label(self.display_frame, text = self.total_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24,font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label =tk.Label(self.display_frame, text = self.current_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24,font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')
        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame
    
    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg= WHITE, fg= LABEL_COLOR, font=DIGIT_FONT_STYLE, borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
    
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operators.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFFWHITE, font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4,sticky=tk.NSEW)
            i+=1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=OFFWHITE, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.clear)
        button.grid(row=0, column=1,sticky=tk.NSEW)

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFFWHITE, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.square)
        button.grid(row=0, column=2,sticky=tk.NSEW)

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFFWHITE, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3,sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()

        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""
        
        except Exception as e:
            self.current_expression = "Error"

        finally:
            self.update_label()

    def create_equal_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3,columnspan=2,sticky=tk.NSEW)
        
    def update_total_label(self):
        expression = self.total_expression
        for opeator , symbol in self.operators.items():
            expression = expression.replace(opeator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])
    
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run() 