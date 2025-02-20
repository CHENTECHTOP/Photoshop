from PyQt5.QtWidgets import QApplication, QWidget,  QHBoxLayout, QVBoxLayout, QListView, QPushButton

from workwithfile import load_btn

app = QApplication([])
window = QWidget()
window.resize(1000, 700)

main_layout = QHBoxLayout()
left_layout = QVBoxLayout()
main_layout.addLayout(left_layout)
right_layout = QVBoxLayout()
main_layout.addWidget(right_layout)

# Ліва частина віджети
file_list = QListView()
left_layout.addWidget(file_list)
load_btn = QPustbutton("Завантажити фото")
left_yalout.addWidget(load_btn)

window.setLayout(main_layout)

window.show()
app.exec()