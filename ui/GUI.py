# Basic Interface:
#
# Numeric Fields:
# Min X, Min Y, Min Z
# Max X, Max Y, Max Z
# Number of Points:
# Radio Button:
# Options:
# QuickHull3D
# Chan Minimalist
# String or Browser Field:
# Filename
# Start Button:
# Exit Button:
#
# Start should take the
# range values from the Min Max
# generate a point cloud, in other words
# a list of tuples of 3 elements,
# of random points.
#
# That point cloud should be submitted
# to the appropriate algo, along with
# the filename. The algo should hull
# the point cloud and generate the obj
# using the Mesh class in the geo
# package.
#
# Exit should close the app.

# Gui by Bishop
# Started 6/9/17
# The GUI for Algorithms Project

import Tkinter as tk

class ExampleApp(tk.Frame):
    ''' An example application for TkInter.  Instantiate
        and call the run method to run. '''
    def __init__(self, master):
        # Initialize window using the parent's constructor
        tk.Frame.__init__(self, master, width=300, height=200)
        # Set the title
        self.master.title('Alg Project')

        # This allows the size specification to take effect
        self.pack_propagate(0)

        # We'll use the flexible pack layout manager
        self.pack()

        # The greeting selector
        # Use a StringVar to access the selector's value
        self.greeting_var = tk.StringVar()
        self.greeting = tk.OptionMenu(self, self.greeting_var, 'hello', 'goodbye', 'heyo')
        self.greeting_var.set('hello')

        # The recipient text entry control and its StringVar
        self.recipient_var = tk.StringVar()
        self.recipient = tk.Entry(self, textvariable=self.recipient_var)
        self.recipient_var.set('world')

        # The go button
        self.go_button = tk.Button(self, text='Go', command=self.print_out)

        # Put the controls on the form
        self.go_button.pack(fill=tk.X, side=tk.BOTTOM)
        self.greeting.pack(fill=tk.X, side=tk.TOP)
        self.recipient.pack(fill=tk.X, side=tk.TOP)

    def print_out(self):
        ''' Print a greeting constructed
            from the selections made by
            the user. '''
        print('%s, %s!' % (self.greeting_var.get().title(),
                           self.recipient_var.get()))
    def run(self):
        ''' Run the app '''
        self.mainloop()

app = ExampleApp(tk.Tk())
app.run()
