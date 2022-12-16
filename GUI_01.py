import PyQt5
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add a title
        self.setWindowTitle("Nate!")

        # Set Vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # Create a label
        my_label = qtw.QLabel("Hello Nate!")

        # Change the font size of the label
        my_label.setFont(qtg.QFont('Helveitca', 18))
        self.layout().addWidget(my_label)

        # Create an entry box
        my_entry = qtw.QLineEdit()
        self.layout().addWidget(my_entry)

        # Add a button
        my_button = qtw.QPushButton("Nate!", clicked = lambda: Nate())
        self.layout().addWidget(my_button)

        self.show()

        # Define a function which calls the set text method on the label defined earlier
        def Nate():
            my_label.setText(f"Hello {my_entry.text()}")

app = qtw.QApplication([])
mw = MainWindow()

# Run the app
app.exec_()