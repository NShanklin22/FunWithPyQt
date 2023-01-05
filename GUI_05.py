
# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from screeninfo import get_monitors
import pandas as pd
import time

# This application has the goal of featuring the following
# [X] Open a CSV file and read the data into a pandas dataframe
# [] Display the pandas dataframe in a table
# [X] Features a button which will take the user to a new window

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        ##############################
        ### Seting up the window #####
        ##############################
        # Determine the size of the PC window
        screen = get_monitors()[0]

        # Define the x and y size of the screen
        sizeX = int(screen.width/2)
        sizeY = int(screen.height/2)

        # Deine the location of the window so that it is at the center of the screen
        locX = int(sizeX/2)
        locY = int(sizeY/2)

        # Define the geometry of the window
        self.setGeometry(locX,locY,sizeX,sizeY)

        # Add a title
        self.setWindowTitle("SEBA+ Database Analyzer")

        ##############################
        ## Setting up the layout #####
        ##############################
        # Create a vertical layout
        mainLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()

        # Create the stack widget
        self.Stack = QStackedWidget(self)
        mainLayout.addWidget(self.Stack)

        self.stack1 = QWidget()
        self.stack2 = QWidget()

        self.PageOne()
        self.PageTwo()

        #########################
        # Using the Q stacked widget

        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)

        ########################








        ##### This section of code adds the buttons to the main layout

        # Add the two buttons to the second layout
        my_button01 = QPushButton("Load Data", clicked = self.getfile)
        my_button02 = QPushButton("Data Table", clicked = self.PageUp)
        my_button03 = QPushButton("Data Chart", clicked = self.PageDown)

        buttonLayout.addWidget(my_button01)
        buttonLayout.addWidget(my_button02)
        buttonLayout.addWidget(my_button03)

        # Add layout01 and layout02 to mainLayout
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)
        self.show()

    def PageUp(self):
        self.Stack.setCurrentIndex(1)

    def PageDown(self):
        self.Stack.setCurrentIndex(0)

    # Function defined for the first page
    def PageOne(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        Label01 = QLabel("Click Load Database and select an AS-P xml export", frame)
        layout = QVBoxLayout()
        layout.addWidget(frame)
        self.stack1.setLayout(layout)

    # Function defined for the second page
    def PageTwo(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        Label01 = QLabel("This is the second fucking page!", frame)
        layout = QVBoxLayout()
        layout.addWidget(frame)
        self.stack2.setLayout(layout)

    def getfile(self):
        file,_ = QFileDialog.getOpenFileName(self)
        print("here")
        df = pd.read_csv(file)
        print("here")
        print(df.head())

app = QApplication([])
mw = MainWindow()



# Run the app
app.exec_()