import PyQt5
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from screeninfo import get_monitors

class MainWindow(qtw.QWidget):
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
        self.setWindowTitle("Nate!")

        ##############################
        ## Setting up the layout #####
        ##############################

        # Create a vertical layout
        mainLayout = qtw.QVBoxLayout()
        layout01 = qtw.QHBoxLayout()
        layout02 = qtw.QVBoxLayout()

        # Create a label
        my_label01 = qtw.QLabel("Hello Nate!")
        my_label02 = qtw.QLabel("This is a second label")
        my_label03 = qtw.QLabel("Fuck you Nate")

        # Change the font size of the label
        my_label01.setFont(qtg.QFont('Helveitca', 18))
        my_label02.setFont(qtg.QFont('Helveitca', 28))
        my_label03.setFont(qtg.QFont('Helveitca', 38))

        # Add the labels to the first layout
        layout01.addWidget(my_label01)
        layout01.addWidget(my_label02)
        layout01.addWidget(my_label03)

        # Add the two buttons to the second layout
        my_button01 = qtw.QPushButton("Nate!")
        my_button02 = qtw.QPushButton("Nate!")

        layout02.addWidget(my_button01)
        layout02.addWidget(my_button02)

        # Add layout01 and layout02 to mainLayout
        mainLayout.addLayout(layout01)
        mainLayout.addLayout(layout02)

        self.setLayout(mainLayout)

        self.show()

app = qtw.QApplication([])
mw = MainWindow()

# Run the app
app.exec_()