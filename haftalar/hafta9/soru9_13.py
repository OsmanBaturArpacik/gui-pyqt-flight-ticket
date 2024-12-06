from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QFormLayout, QLabel, QLineEdit, \
	QGridLayout, QVBoxLayout, QHBoxLayout, QCheckBox, QComboBox
import sys

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('layout')
		self.setGeometry(700, 400, 350, 250) # xy width height

		centralWidget = QWidget()
		self.setCentralWidget(centralWidget)

		layout = QVBoxLayout()

		self.nameLineEdit = QLineEdit(self)
		self.nameLineEdit.setPlaceholderText("Adinizi Giriniz")
		self.checkBox = QCheckBox("Abonelik onayi okudum onayliyorum",self)
		self.comboBox = QComboBox(self)
		self.comboBox.addItems(["Istanbul", "Ankara", "Kutahya"])
		self.label = QLabel("Sonuc burada gozukecek", self)
		self.btn = QPushButton("Goster", self)
		self.btn.clicked.connect(self.onClicked)

		layout.addWidget(self.nameLineEdit)
		layout.addWidget(self.checkBox)
		layout.addWidget(self.comboBox)
		layout.addWidget(self.label)
		layout.addWidget(self.btn)

		centralWidget.setLayout(layout)


	def onClicked(self):
		inputText = self.nameLineEdit.text()
		checkboxState = "Abonelik onaylandi" if self.checkBox.isChecked() else "Abonelik onaylanmadi"
		selectedCity = self.comboBox.currentText()
		self.label.setText(f"{inputText}\n{checkboxState}\n{selectedCity}")


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())