import sys

from datetime import datetime

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, \
    QGridLayout, QLineEdit, QPushButton, QComboBox


class speed_calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average speed calculator")
        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel("Distance")
        self.distance_line_edit = QLineEdit()

        time_hours_label = QLabel("Time (hours)")
        self.time_hours_Line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_speed)

        self.combo = QComboBox()
        self.combo.addItems(['Metric (km)', 'Imperial (miles)'])

        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.combo, 0, 2)
        grid.addWidget(time_hours_label, 1, 0)
        grid.addWidget(self.time_hours_Line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        #Get distance and time from the input boxes
        distance = float(self.distance_line_edit.text())
        time = float(self.time_hours_Line_edit.text())

        # Calculate average speed
        speed = distance/time

        if self.combo.currentText() == "Metric (km)":
            speed = round(speed, 2)
        if self.combo.currentText() == "Imperial (miles)":
            speed = round(speed * 0.621372, 2)
            unit = 'mph'

        #Display the result
        self.output_label.setText(f"Average Speed: {speed} {unit}")

        app = QApplication(sys.argv)
        calculator = speed_calculator
        calculator.show()
        sys.exit(app,exec())
