from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Show_Ticket(QDialog):
    def __init__(self):
        super().__init__()

        # Create a QLabel to display the ticket image
        label = QLabel(self)

        # Load the ticket image using QPixmap
        pixmap = QPixmap('Ticket.png')

        # Set the pixmap to the label
        label.setPixmap(pixmap)

        # Set the size and position of the label based on the image size
        label.setGeometry(0, 0, pixmap.width(), pixmap.height())

        # Create a layout to manage the positioning of the label
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        self.setLayout(layout)

# Example usage:
# app = QApplication([])
# window = Show_Ticket()
# window.exec_()
