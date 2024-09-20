import sys
import socket
import ipaddress
from PyQt5 import QtWidgets, QtCore, QtGui
from concurrent.futures import ThreadPoolExecutor

class PortScannerApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Port Scanner")
        self.setGeometry(100, 100, 400, 450)
        self.setStyleSheet("background-color: #1e1e1e; color: #ffffff; font-family: Arial;")

        self.initUI()
        
        # Timer to change color
        self.color_timer = QtCore.QTimer(self)
        self.color_timer.timeout.connect(self.update_title_color)
        self.color_timer.start(100)  # Change the color every 100 ms
        self.hue = 0

    def initUI(self):
        layout = QtWidgets.QVBoxLayout()

        # Title
        self.title_label = QtWidgets.QLabel("PortSeeker", self)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setFont(QtGui.QFont("Arial", 24))
        layout.addWidget(self.title_label)

        # IP address input field
        self.ip_input = QtWidgets.QLineEdit(self)
        self.ip_input.setPlaceholderText("IP Address (e.g., 192.168.1.1)")
        self.ip_input.setStyleSheet("background-color: #2e2e2e; color: #ffffff; padding: 10px; border-radius: 5px;")
        
        # Start port input field
        self.start_port_input = QtWidgets.QLineEdit(self)
        self.start_port_input.setPlaceholderText("Start Port (1-65535)")
        self.start_port_input.setStyleSheet("background-color: #2e2e2e; color: #ffffff; padding: 10px; border-radius: 5px;")
        
        # End port input field
        self.end_port_input = QtWidgets.QLineEdit(self)
        self.end_port_input.setPlaceholderText("End Port (1-65535)")
        self.end_port_input.setStyleSheet("background-color: #2e2e2e; color: #ffffff; padding: 10px; border-radius: 5px;")
        
        # Scan button
        self.scan_button = QtWidgets.QPushButton("Scan", self)
        self.scan_button.setStyleSheet("background-color: #ff4081; color: #ffffff; padding: 10px; font-size: 16px; border-radius: 5px;")
        self.scan_button.clicked.connect(self.start_scan)

        # Error label
        self.error_label = QtWidgets.QLabel(self)
        self.error_label.setStyleSheet("color: red;")
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)

        # Info note
        self.info_label = QtWidgets.QLabel("Note: The higher the port range, the longer it will take.\n"
                                           "If the program becomes unresponsive, it is normal, please be patient.", self)
        self.info_label.setStyleSheet("color: #ffffff; margin-top: 10px;")
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)

        # Add widgets to the layout
        layout.addWidget(self.ip_input)
        layout.addWidget(self.start_port_input)
        layout.addWidget(self.end_port_input)
        layout.addWidget(self.scan_button)
        layout.addWidget(self.error_label)
        layout.addWidget(self.info_label)

        self.setLayout(layout)

    def update_title_color(self):
        # Change the color based on the hue value
        rgb = QtGui.QColor.fromHsv(self.hue % 360, 255, 255)
        self.title_label.setStyleSheet(f"color: rgb({rgb.red()}, {rgb.green()}, {rgb.blue()});")
        self.hue += 1  # Increment hue value

    def scan_port(self, ip, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            return port if sock.connect_ex((ip, port)) == 0 else None

    def scan_ports(self, ip, start_port, end_port):
        open_ports = []
        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = {executor.submit(self.scan_port, ip, port): port for port in range(start_port, end_port + 1)}
            for future in futures:
                try:
                    port = future.result()
                    if port is not None:
                        open_ports.append(port)
                except Exception as e:
                    print(f"Error scanning port: {e}")
        return open_ports

    def start_scan(self):
        self.error_label.setText("")  # Reset the error message
        ip = self.ip_input.text()
        start_port_text = self.start_port_input.text()
        end_port_text = self.end_port_input.text()

        if not ip or not start_port_text or not end_port_text:
            self.error_label.setText("Please fill in all fields.")
            return

        # Check if the IP address is valid
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            self.error_label.setText("Invalid IP address.")
            return

        try:
            start_port = int(start_port_text)
            end_port = int(end_port_text)
            if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
                raise ValueError
        except ValueError:
            self.error_label.setText("Ports must be valid numbers (1-65535).")
            return

        # Change button text and disable
        self.scan_button.setText("Please wait...")
        self.scan_button.setEnabled(False)

        # Start scanning in a thread
        QtCore.QThread(self.scan_ports_thread(ip, start_port, end_port))

    def scan_ports_thread(self, ip, start_port, end_port):
        open_ports = self.scan_ports(ip, start_port, end_port)

        # Return to the main thread to update the UI
        QtCore.QMetaObject.invokeMethod(self, "finish_scan", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(list, open_ports))

    @QtCore.pyqtSlot(list)
    def finish_scan(self, open_ports):
        result_text = f"Open ports: {open_ports}" if open_ports else "No open ports found."
        QtWidgets.QMessageBox.information(self, "Scan Result", result_text)

        # Reactivate the button
        self.scan_button.setText("Scan")
        self.scan_button.setEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PortScannerApp()
    window.show()
    sys.exit(app.exec_())
