from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("My App")
        self.resize(800, 600)

        # Create central widget
        central_widget = QtWidgets.QWidget()

        # Create file drop area
        file_drop_area = QtWidgets.QLabel("Drag and drop files here")
        file_drop_area.setAlignment(QtCore.Qt.AlignCenter)

        # Create settings tab
        settings_widget = QtWidgets.QWidget()
        settings_layout = QtWidgets.QVBoxLayout(settings_widget)
        settings_label = QtWidgets.QLabel("Settings")
        settings_layout.addWidget(settings_label)

        # Create readout tab
        readout_widget = QtWidgets.QWidget()
        readout_layout = QtWidgets.QVBoxLayout(readout_widget)
        readout_label = QtWidgets.QLabel("Readout")
        readout_layout.addWidget(readout_label)

        # Create dock widget for settings tab
        settings_dock = QtWidgets.QDockWidget("Settings")
        settings_dock.setWidget(settings_widget)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, settings_dock)

        # Create dock widget for readout tab
        readout_dock = QtWidgets.QDockWidget("Readout")
        readout_dock.setWidget(readout_widget)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, readout_dock)

        # Set central widget and file drop area
        layout = QtWidgets.QVBoxLayout(central_widget)
        layout.addWidget(file_drop_area)
        self.setCentralWidget(central_widget)

# Create application instance and run
app = QtWidgets.QApplication([])
app.setStyle("Breeze")  # Set the style to Breeze
window = MainWindow()
window.show()
app.exec_()
