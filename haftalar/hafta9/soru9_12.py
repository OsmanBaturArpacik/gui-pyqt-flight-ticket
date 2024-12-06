from PyQt5.QtWidgets import *
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

		self.label = QLabel("Bir metin yazin: ", self)
		self.lineEdit = QLineEdit(self)
		self.button = QPushButton("Butona Tikla", self)
		self.button.clicked.connect(self.btnOnClicked)
		self.checkBox = QCheckBox("Onay Kutusu", self)
		self.comboBox = QComboBox(self)
		self.comboBox.addItems(["Python", "C++", "Java"])
		self.slider = QSlider(self)
		self.slider.setOrientation(1)
		self.slider.setRange(0, 100)
		self.radioButton1 = QRadioButton("Secenek 1", self)
		self.radioButton2 = QRadioButton("Secenek 2", self)
		self.spinBox = QSpinBox(self)
		self.spinBox.setRange(-100, 100)
		self.textEdit = QTextEdit(self)

		layout.addWidget(self.label)
		layout.addWidget(self.lineEdit)
		layout.addWidget(self.button)
		layout.addWidget(self.checkBox)
		layout.addWidget(self.comboBox)
		layout.addWidget(self.slider)
		layout.addWidget(self.radioButton1)
		layout.addWidget(self.radioButton2)
		layout.addWidget(self.spinBox)
		layout.addWidget(self.textEdit)

		centralWidget.setLayout(layout)


	def btnOnClicked(self):
		inputText = self.lineEdit.text()
		checkboxState = "isaretlendi" if self.checkBox.isChecked() else "isaretlenmedi"
		selectedLanguage = self.comboBox.currentText()
		sliderValue = self.slider.value()
		radioSelection = "Secenek 1" if self.radioButton1.isChecked() else "Secenek 2"
		spinValue = self.spinBox.value()
		textEdited = self.textEdit.toPlainText()
		self.label.setText(f"{inputText}\n{checkboxState}\n{selectedLanguage}\n{sliderValue}\n{radioSelection}\n{spinValue}\n{textEdited}")



if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())