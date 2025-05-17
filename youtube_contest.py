#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication , QMessageBox ,QHBoxLayout, QRadioButton , QWidget , QLabel , QVBoxLayout
#создание приложения и главного окна
def show_result():
    setText('')
    

app = QApplication([])
main_win = QWidget()
main_win.resize(400,200)
main_win.setWindowTitle('Конкурс от Crazy People')



def win ():
    victory_win = QMessageBox()
    victory_win.setText('Верно! Вы выиграли гироскутер')
    victory_win.exec_()
    main_win.close()

def lose ():
    lose_l = QMessageBox()
    lose_l.setText('Неправильно')
    lose_l.exec_()
    main_win.close()



question = QLabel('В каком году канал получил "золотую кнопку" от YouTube?')

r_btn = QRadioButton('2005 ')
r_btn1 = QRadioButton('2010 ')
r_btn2 = QRadioButton('2015 ')
r_btn3 = QRadioButton('2020 ')

v_line = QVBoxLayout()
h_line = QHBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()

h_line.addWidget(question , alignment= Qt.AlignCenter )
h_line1.addWidget(r_btn , alignment= Qt.AlignCenter )
h_line1.addWidget(r_btn1 , alignment= Qt.AlignCenter )
h_line2.addWidget(r_btn2 , alignment= Qt.AlignCenter )
h_line2.addWidget(r_btn3 , alignment= Qt.AlignCenter )

v_line.addLayout(h_line)
v_line.addLayout(h_line1)
v_line.addLayout(h_line2)



r_btn2.clicked.connect(win)
r_btn.clicked.connect(lose)
r_btn1.clicked.connect(lose)
r_btn3.clicked.connect(lose)


main_win.setLayout(v_line)
main_win.show()
app.exec_()
#создание виджетов главного окна
 
#расположение виджетов по лэйаутам

#обработка нажатий на переключатели

#отображение окна приложения 