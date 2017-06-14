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
import random, tkFileDialog


class ExampleApp(Frame):
    """ An example application for TkInter.  Instantiate
        and call the run method to run. """

    def __init__(self, master):
        Frame.__init__(self, master, width=300, height=200)
        self.master.title('Alg Project')
        self.pack_propagate(0)
        self.pack()
        self.points = list()

        # Sets min max windows
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        Label(self, text="Min X = ").grid(row=0, column=0)
        self.minX = StringVar()
        self.minXSet = Entry(self, textvariable=self.minX).grid(row=0, column=1)
        self.minX.set('0')

        Label(self, text="Max X = ").grid(row=0, column=2)
        self.maxX = StringVar()
        self.maxXSet = Entry(self, textvariable=self.maxX).grid(row=0, column=3)
        self.maxX.set('100000')

        # YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
        Label(self, text="Min Y = ").grid(row=1, column=0)
        self.minY = StringVar()
        self.minYSet = Entry(self, textvariable=self.minY).grid(row=1, column=1)
        self.minY.set('0')

        Label(self, text="Max Y = ").grid(row=1, column=2)
        self.maxY = StringVar()
        self.maxYSet = Entry(self, textvariable=self.maxY).grid(row=1, column=3)
        self.maxY.set('100000')

        # ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
        Label(self, text="Min Z = ").grid(row=2, column=0)
        self.minZ = StringVar()
        self.minZSet = Entry(self, textvariable=self.minZ).grid(row=2, column=1)
        self.minZ.set('0')

        Label(self, text="Max Z = ").grid(row=2, column=2)
        self.maxZ = StringVar()
        self.maxZSet = Entry(self, textvariable=self.maxZ).grid(row=2, column=3)
        self.maxZ.set('100000')

        # Number of points #####################################
        Label(self, text="Number of points = ").grid(row=3, column=0)
        self.numPoi = StringVar()
        self.numPoiSet = Entry(self, textvariable=self.numPoi).grid(row=3, column=1)
        self.numPoi.set('100')

        # Save field ###############################################
        Label(self, text="Save as ").grid(row=4, column=0)
        self.fileText = StringVar()
        self.fileTextSet = Entry(self, textvariable=self.fileText).grid(row=4, column=1)
        self.fileButton = Button(self,
                                 text='...',
                                 command=lambda: self.fileText.set(tkFileDialog.asksaveasfilename(
                                     initialdir="/",
                                     title="Select file",
                                     filetypes=(
                                         ("Object files", "*.Obj"), (
                                             "all files",
                                             "*.*"))))).grid(row=4, column=3)

        # Radio Group which function ###############################
        self.v = IntVar()
        self.bt1 = Radiobutton(self, text="Option1",
                               value=1, variable=self.v,
                               command=lambda: self.setButton()).grid(row=5)
        self.bt2 = Radiobutton(self, text="Option2",
                               value=2, variable=self.v,
                               command=lambda: self.setButton()).grid(row=6)

        # The go button and the Exit button
        self.launchButton = Button(self,
                                   padx=5, pady=5, bd=8,
                                   text='Launch',
                                   command=lambda: self.startApp()).grid(row=8, column=1)
        self.exitButton = Button(self,
                                 padx=5, pady=5, bd=8,
                                 text='Exit',
                                 command=lambda: self.quit()).grid(row=8, column=2)

    def startApp(self):
        """Starts selected algorithms"""
        print("sent tupples")
        self.makePoints()

    def makePoints(self):
        """Creates sets of tupples for App"""
        if self.v.get() == 1:
            x = eval(self.maxX.get()) - eval(self.minX.get())
            y = eval(self.maxY.get()) - eval(self.minY.get())
            z = eval(self.maxZ.get()) - eval(self.minZ.get())
            for x in range(eval(self.numPoi.get())):
                self.points.append((random.random() * x - (x/2),
                                    random.random() * y - (y/2),
                                    random.random() * z - (z/2)))
                print("tripple")
        if self.v.get() == 2:
            x = eval(self.maxX.get()) - eval(self.minX.get())
            y = eval(self.maxY.get()) - eval(self.minY.get())
            for x in range(eval(self.numPoi.get())):
                self.points.append((random.random() * x - (x/2),
                                    random.random() * y - (y/2)))
                print("double")

    def setButton(self):
        if self.v.get() == 1:
            self.minZSet.configure(state='enabled')
        if self.v.get() == 2:
            self.minZSet.configure(state='disabled')

    def run(self):
        """ Run the app """
        self.mainloop()


app = ExampleApp(Tk())
app.run()
