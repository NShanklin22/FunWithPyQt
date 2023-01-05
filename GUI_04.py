
# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from screeninfo import get_monitors
import time


# This application features the following:
# 1. A loading bar that can be activated via a button and function
# 2. Two frames, one with an example of how text can be added
# 3. A button which opens a file selections window

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
        layout01 = QVBoxLayout()
        layout02 = QHBoxLayout()

        # Frame for app updates)
        my_frame01 = QFrame()
        my_frame01.setFrameShape(QFrame.StyledPanel)

        # FontSize stores the default font size for the window
        FontSize = 18
        LabelSeparation = int(FontSize * 1.5)

        self.Label01 = QLabel("Click Load Database and select an AS-P xml export", my_frame01)
        self.Label01.move(0,0)
        self.Label01.resize(sizeX,int(FontSize *1.5))
        self.Label01.setFont(QFont('Helveitca', 18))
        # Label 02
        self.Label02 = QLabel("", my_frame01)
        self.Label02.move(0,LabelSeparation)
        self.Label02.setFont(QFont('Helveitca', 18))
        self.Label02.resize(sizeX,int(FontSize *1.5))
        self.Label03 = QLabel("", my_frame01)
        self.Label03.move(0,LabelSeparation * 2)
        self.Label03.setFont(QFont('Helveitca', 18))

        ##### Frame 02 ######

        # Create a text box to add to frame01
        my_frame02 = QFrame()
        my_frame02.setFrameShape(QFrame.StyledPanel)

        ## Add text to the frame








        ########################




        # Add the progress bar
        self.progress_bar = QProgressBar(self)

        mainLayout.addWidget(self.progress_bar)


        # Add the labels to the first layout
        layout01.addWidget(my_frame01)
        layout01.addWidget(my_frame02)

        # Add the two buttons to the second layout
        my_button01 = QPushButton("Load Database", clicked = self.getfile)
        my_button02 = QPushButton("Analyze Database")

        layout02.addWidget(my_button01)
        layout02.addWidget(my_button02)


        # Add layout01 and layout02 to mainLayout
        mainLayout.addLayout(layout01)
        mainLayout.addLayout(layout02)

        self.setLayout(mainLayout)

        self.show()

    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "xml files (*.xml)")

        self.Label02.setText("File {} selected".format(fname))

    def progressAnimation(self):
        print("Nate!")
        # setting for loop to set value of progress bar
        for i in range(101):
            # slowing down the loop
            time.sleep(0.05)
            # setting value to progress bar
            self.progress_bar.setValue(i)

app = QApplication([])
mw = MainWindow()

# Run the app
app.exec_()