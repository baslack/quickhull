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

from Tkinter import *
import Tkinter as tk
import Tkconstants, tkFileDialog


class ExampleApp(tk.Frame):
    """ An example application for TkInter.  Instantiate
        and call the run method to run. """

    def __init__(self, master):
        tk.Frame.__init__(self, master, width=300, height=200)
        self.master.title('Alg Project')
        self.grid()

        # Sets min max windows
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        tk.Label(self, text="Min X = ").grid(row=0, column=0)
        self.minX = tk.StringVar()
        self.minXSet = tk.Entry(self, textvariable=self.minX).grid(row=0, column=1)
        self.minX.set('0')

        tk.Label(self, text="Max X = ").grid(row=0, column=2)
        self.maxX = tk.StringVar()
        self.maxXSet = tk.Entry(self, textvariable=self.maxX).grid(row=0, column=3)
        self.maxX.set('100000')

        # YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
        tk.Label(self, text="Min Y = ").grid(row=1, column=0)
        self.minY = tk.StringVar()
        self.minYSet = tk.Entry(self, textvariable=self.minY).grid(row=1, column=1)
        self.minY.set('0')

        tk.Label(self, text="Max Y = ").grid(row=1, column=2)
        self.maxY = tk.StringVar()
        self.maxYSet = tk.Entry(self, textvariable=self.maxY).grid(row=1, column=3)
        self.maxY.set('100000')

        # ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
        tk.Label(self, text="Min Z = ").grid(row=2, column=0)
        self.minZ = tk.StringVar()
        self.minZSet = tk.Entry(self, textvariable=self.minZ).grid(row=2, column=1)
        self.minZ.set('0')

        tk.Label(self, text="Max Z = ").grid(row=2, column=2)
        self.maxZ = tk.StringVar()
        self.maxZSet = tk.Entry(self, textvariable=self.maxZ).grid(row=2, column=3)
        self.maxZ.set('100000')

        # Number of points #####################################
        tk.Label(self, text="Number of points = ").grid(row=4, column=0)
        self.numPoi = tk.StringVar()
        self.numPoiSet = tk.Entry(self, textvariable=self.numPoi).grid(row=4, column=1)
        self.numPoi.set('100')

        # Save field ###############################################
        tk.Label(self, text="Save as ").grid(row=5, column=0)
        self.fileText = tk.StringVar()
        self.fileTextSet = tk.Entry(self, textvariable=self.numPoi).grid(row=5, column=1)
        self.filButton = tk.Button(self,
                                     text='...',
                                     command=self.fileText.set(tkFileDialog.asksaveasfilename(
                                         initialdir="/",
                                         title="Select file",
                                         filetypes=(
                                             ("Object files", "*.Obj"), (
                                                 "all files",
                                                 "*.*"))))).grid(row=5, column=3)

        # Radio Group which function ###############################
        self.v = int
        tk.Radiobutton(self, text="Python", padx=20, variable=self.v, value=1).grid(row=6)
        tk.Radiobutton(self, text="Perl", padx=20, variable=self.v, value=2).grid(row=7)

        # The go button and the Exit button
        self.goButton = tk.Button(self, text='Launch',
                                  command=self.startApp()).grid(row=8, column=1)
        self.exitButton = tk.Button(self, text='Exit',
                                    command=tk.quit(self)).grid(row=8, column=2)

    def startApp(self):
        """Starts selected algorithms"""
        print('%s, %s!' % (self.minX.get(),
                           self.maxX.get()))

    def run(self):
        """ Run the app """
        self.mainloop()


app = ExampleApp(tk.Tk())
app.run()
