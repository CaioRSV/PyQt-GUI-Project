import os
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

from Func_SecondWindow import Ui_Func_SecondWindow
from Proj_SecWindow import Ui_Proj_SecWindow
from PyQt5 import QtTest, QtGui


conex=sqlite3.connect('database.db')
c = conex.cursor()

c.execute("CREATE TABLE IF NOT EXISTS '{}' {}".format('Funcionarios','("Nome", "Idade", "Endereco", "Salario", "Contratacao")'))
c.execute("CREATE TABLE IF NOT EXISTS '{}' {}".format('Projetos','("Id", "Nome", "Funcionarios_In", "Cliente", "Contato_Cliente")'))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 540)
        ######################################Limitar  dimensões
        MainWindow.setMaximumWidth(1000)
        MainWindow.setMinimumWidth(1000)
        MainWindow.setMaximumHeight(540)
        MainWindow.setMinimumHeight(540)
        #######################################
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(66, 63, 85);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(66, 63, 85, 80), stop:1 rgba(66, 63, 85, 255));\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Segoe UI\";")
        #
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.sideBar = QtWidgets.QFrame(self.centralwidget)
        self.sideBar.setGeometry(QtCore.QRect(0, 0, 71, 551))
        self.sideBar.setStyleSheet("background-color: rgb(45, 45, 58);")
        self.sideBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sideBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sideBar.setObjectName("sideBar")
        self.MainButton = QtWidgets.QPushButton(self.sideBar)
        self.MainButton.setGeometry(QtCore.QRect(0, 0, 71, 81))
        self.MainButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon_SideBar_Main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainButton.setIcon(icon)
        self.MainButton.setIconSize(QtCore.QSize(36, 36))
        self.MainButton.setObjectName("MainButton")
        self.SideBut1 = QtWidgets.QPushButton(self.sideBar)
        self.SideBut1.setGeometry(QtCore.QRect(0, 80, 71, 61))
        self.SideBut1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icon_SideBar_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SideBut1.setIcon(icon1)
        self.SideBut1.setIconSize(QtCore.QSize(32, 32))
        self.SideBut1.setObjectName("SideBut1")
        self.SideBut2 = QtWidgets.QPushButton(self.sideBar)
        self.SideBut2.setGeometry(QtCore.QRect(0, 140, 71, 61))
        self.SideBut2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icon_SideBar_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SideBut2.setIcon(icon2)
        self.SideBut2.setIconSize(QtCore.QSize(36, 36))
        self.SideBut2.setObjectName("SideBut2")
        self.SideBut3 = QtWidgets.QPushButton(self.sideBar)
        self.SideBut3.setGeometry(QtCore.QRect(0, 200, 71, 61))
        self.SideBut3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icon_SideBar_3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SideBut3.setIcon(icon3)
        self.SideBut3.setIconSize(QtCore.QSize(32, 32))
        self.SideBut3.setObjectName("SideBut3")
        self.topBar = QtWidgets.QFrame(self.centralwidget)
        self.topBar.setGeometry(QtCore.QRect(70, 0, 941, 21))
        self.topBar.setStyleSheet("background-color: rgb(45, 45, 58);")
        self.topBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topBar.setObjectName("topBar")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(70, 20, 931, 511))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_Main = QtWidgets.QWidget()
        self.page_Main.setObjectName("page_Main")
        self.Icon_Empresa = QtWidgets.QLabel(self.page_Main)
        self.Icon_Empresa.setGeometry(QtCore.QRect(310, 100, 271, 261))
        self.Icon_Empresa.setAutoFillBackground(False)
        self.Icon_Empresa.setText("")
        self.Icon_Empresa.setPixmap(QtGui.QPixmap("Empresa_Icon.png"))
        self.Icon_Empresa.setScaledContents(False)
        self.Icon_Empresa.setObjectName("Icon_Empresa")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page_Main)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 470, 921, 24))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loggedin_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.loggedin_lbl.setFont(font)
        self.loggedin_lbl.setStyleSheet("font: 700 11pt \"Segoe UI\";")
        self.loggedin_lbl.setObjectName("loggedin_lbl")
        self.horizontalLayout.addWidget(self.loggedin_lbl)
        self.UserName_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.UserName_lbl.setStyleSheet("font: italic 12pt \"Segoe UI\";")
        self.UserName_lbl.setObjectName("UserName_lbl")
        self.horizontalLayout.addWidget(self.UserName_lbl)
        self.stackedWidget.addWidget(self.page_Main)
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.label_Funcionarios = QtWidgets.QLabel(self.page_1)
        self.label_Funcionarios.setGeometry(QtCore.QRect(20, 20, 601, 71))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_Funcionarios.setFont(font)
        self.label_Funcionarios.setStyleSheet("font: 600 48pt \"Segoe UI\";")
        self.label_Funcionarios.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_Funcionarios.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_Funcionarios.setObjectName("label_Funcionarios")
        self.tabela_Funcionarios = QtWidgets.QTableWidget(self.page_1)
        self.tabela_Funcionarios.setGeometry(QtCore.QRect(20, 110, 591, 271))
        self.tabela_Funcionarios.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(223, 223, 223);\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(198, 198, 198);")
        self.tabela_Funcionarios.setObjectName("tabela_Funcionarios")
        self.tabela_Funcionarios.setColumnCount(5)
        self.tabela_Funcionarios.setRowCount(1)
        #
        #header = self.tabela_Funcionarios.horizontalHeader()
        #header.setSectionResizeMode(0,QtWidgets.QHeaderView.Stretch)
        self.tabela_Funcionarios.setColumnWidth(0, 172)
        #
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Funcionarios.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Funcionarios.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Funcionarios.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Funcionarios.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Funcionarios.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Funcionarios.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Funcionarios.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Funcionarios.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Funcionarios.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Funcionarios.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Funcionarios.setItem(0, 4, item)
        self.But_EditFunc = QtWidgets.QPushButton(self.page_1)
        self.But_EditFunc.setGeometry(QtCore.QRect(650, 110, 231, 71))
        self.But_EditFunc.setAutoFillBackground(False)
        self.But_EditFunc.setStyleSheet("font: 600 16pt \"Segoe UI\";\n"
"background-color: rgb(47, 45, 104);")
        self.But_EditFunc.setDefault(False)
        self.But_EditFunc.setObjectName("But_EditFunc")
        self.But_AddFunc = QtWidgets.QPushButton(self.page_1)
        self.But_AddFunc.setGeometry(QtCore.QRect(650, 310, 231, 71))
        self.But_AddFunc.setStyleSheet("font: 600 16pt \"Segoe UI\";\n"
"background-color: rgb(117, 117, 117);")
        self.But_AddFunc.setObjectName("But_AddFunc")
        #########addnow
        self.But_Refresh_Func = QtWidgets.QPushButton(self.page_1)
        self.But_Refresh_Func.setGeometry(QtCore.QRect(566, 70, 45, 41))
        self.But_Refresh_Func.setStyleSheet("background-color: rgb(42, 39, 66);")
        self.But_Refresh_Func.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icon_Refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.But_Refresh_Func.setIcon(icon4)
        self.But_Refresh_Func.setIconSize(QtCore.QSize(40, 40))
        self.But_Refresh_Func.setObjectName("But_Refresh_Func")
        #######addnow
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.tabela_Projetos = QtWidgets.QTableWidget(self.page_2)
        self.tabela_Projetos.setGeometry(QtCore.QRect(20, 100, 881, 261))
        self.tabela_Projetos.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(223, 223, 223);\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(198, 198, 198);")
        self.tabela_Projetos.setObjectName("tabela_Projetos")
        self.tabela_Projetos.setColumnCount(5)
        self.tabela_Projetos.setRowCount(1)
        #
        #header2 = self.tabela_Projetos.horizontalHeader()
        #header2.setSectionResizeMode(0,QtWidgets.QHeaderView.Stretch)
        self.tabela_Projetos.setColumnWidth(1, 199)
        self.tabela_Projetos.setColumnWidth(2, 250)
        self.tabela_Projetos.setColumnWidth(3, 170)
        self.tabela_Projetos.setColumnWidth(4, 143)
        #
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Projetos.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Projetos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Projetos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Projetos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Projetos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Projetos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Projetos.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Projetos.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Projetos.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Projetos.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_Projetos.setItem(0, 4, item)
        self.But_viewProjeto = QtWidgets.QPushButton(self.page_2)
        self.But_viewProjeto.setGeometry(QtCore.QRect(490, 420, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.But_viewProjeto.setFont(font)
        self.But_viewProjeto.setStyleSheet("font: 12pt \"Segoe UI\";\n"
"font: 600 9pt \"Segoe UI\";\n"
"font: 600 12pt \"Segoe UI\";")
        self.But_viewProjeto.setObjectName("But_viewProjeto")
        self.But_createProjeto = QtWidgets.QPushButton(self.page_2)
        self.But_createProjeto.setGeometry(QtCore.QRect(140, 420, 211, 71))
        self.But_createProjeto.setStyleSheet("background-color: rgb(159, 159, 159);\n"
"font: 600 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.But_createProjeto.setObjectName("But_createProjeto")
        self.label_Projetos = QtWidgets.QLabel(self.page_2)
        self.label_Projetos.setGeometry(QtCore.QRect(20, 10, 511, 91))
        self.label_Projetos.setStyleSheet("font: 600 48pt \"Segoe UI\";")
        self.label_Projetos.setObjectName("label_Projetos")
        ###addnow
        self.But_Refresh_Proj = QtWidgets.QPushButton(self.page_2)
        self.But_Refresh_Proj.setGeometry(QtCore.QRect(856, 60, 45, 41))
        self.But_Refresh_Proj.setStyleSheet("background-color: rgb(42, 39, 66);")
        self.But_Refresh_Proj.setText("")
        self.But_Refresh_Proj.setIcon(icon4)
        self.But_Refresh_Proj.setIconSize(QtCore.QSize(40, 40))
        self.But_Refresh_Proj.setObjectName("But_Refresh_Proj")
        ###addnow
        self.stackedWidget.addWidget(self.page_2)
        self.page_Last = QtWidgets.QWidget()
        self.page_Last.setObjectName("page_Last")
        self.label_Comunicado = QtWidgets.QLabel(self.page_Last)
        self.label_Comunicado.setGeometry(QtCore.QRect(20, 14, 541, 81))
        self.label_Comunicado.setStyleSheet("font: 600 48pt \"Segoe UI\";")
        self.label_Comunicado.setObjectName("label_Comunicado")
        self.text_Comunicado = QtWidgets.QTextEdit(self.page_Last)
        self.text_Comunicado.setGeometry(QtCore.QRect(30, 190, 541, 241))
        self.text_Comunicado.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"color: rgb(0, 0, 0);")
        self.text_Comunicado.setObjectName("text_Comunicado")
        self.text_ComunicadoAssunto = QtWidgets.QTextEdit(self.page_Last)
        self.text_ComunicadoAssunto.setGeometry(QtCore.QRect(30, 130, 541, 31))
        self.text_ComunicadoAssunto.setStyleSheet("background-color: rgb(244, 244, 244);\n"
"color: rgb(0, 0, 0);\n"
"font: 900 italic 12pt \"Segoe UI\";")
        self.text_ComunicadoAssunto.setObjectName("text_ComunicadoAssunto")
        self.label_comunicado2 = QtWidgets.QLabel(self.page_Last)
        self.label_comunicado2.setGeometry(QtCore.QRect(40, 110, 161, 16))
        self.label_comunicado2.setObjectName("label_comunicado2")
        self.label_Comunicado3 = QtWidgets.QLabel(self.page_Last)
        self.label_Comunicado3.setGeometry(QtCore.QRect(40, 170, 151, 16))
        self.label_Comunicado3.setObjectName("label_Comunicado3")
        self.But_EnviarComunicado = QtWidgets.QPushButton(self.page_Last)
        self.But_EnviarComunicado.setGeometry(QtCore.QRect(620, 270, 251, 81))
        self.But_EnviarComunicado.setStyleSheet("font: 36pt \"Segoe UI\";")
        self.But_EnviarComunicado.setObjectName("But_EnviarComunicado")
        self.stackedWidget.addWidget(self.page_Last)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ############Habilitar botões de mudar página
        #main
        self.MainButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Main))
        #1
        self.SideBut1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        #2
        self.SideBut2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        #3
        self.SideBut3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Last))
        #
        #####Adicionando Lista de Funcionários###########################################################
        c.execute("SELECT * from 'Funcionarios'")
        itens=[]
        for i in c.fetchall():
            itens.append(i)
        counterRows_Func=0
        for i in itens:
            counterRows_Func+=1
        self.tabela_Funcionarios.setRowCount(int(counterRows_Func))
        counterFunc=0
        for i in itens:
            counterFunc_Coluna=0
            for a in i:
                #
                item = QtWidgets.QTableWidgetItem()
                self.tabela_Funcionarios.setItem(counterFunc, counterFunc_Coluna, item)
                #
                self.tabela_Funcionarios.item(counterFunc, counterFunc_Coluna).setText(str(a))
                counterFunc_Coluna+=1
            counterFunc+=1
        
        #####Adicionando Lista de Projetos###########################################################
        c.execute("SELECT * from 'Projetos'")
        itens2=[]
        for i in c.fetchall():
            itens2.append(i)
        counterRows_Proj=0
        for i in itens2:
            counterRows_Proj+=1
        self.tabela_Projetos.setRowCount(int(counterRows_Proj))
        counterProj=0
        for i in itens2:
            counterProj_Coluna=0
            for a in i:
                #
                item = QtWidgets.QTableWidgetItem()
                self.tabela_Projetos.setItem(counterProj, counterProj_Coluna, item)
                #
                self.tabela_Projetos.item(counterProj, counterProj_Coluna).setText(str(a))
                counterProj_Coluna+=1
            counterProj+=1
        ###########################################################

        self.But_EditFunc.clicked.connect(self.check_ChangeFunc)
        
        #Definindo ItensFunc para as Funções de baixo
        
        self.itensFunc=str(itens)

        self.But_AddFunc.clicked.connect(self.SecondWindow_Func)
        self.But_AddFunc.clicked.connect(self.refresh_Func)

        ########################################################### VEZ DOS PROJETOS:

        self.But_viewProjeto.clicked.connect(self.check_ChangeProj)
        
        #Definindo ItensProj para as Funções de baixo
        
        self.itensProj=str(itens2)
        
        self.But_createProjeto.clicked.connect(self.SecondWindow_Proj)
        #



        self.But_EnviarComunicado.clicked.connect(self.sentMessage)

        ###
        self.But_Refresh_Func.clicked.connect(self.refresh_Func)
        self.But_Refresh_Proj.clicked.connect(self.refresh_Proj)
        #
        MainWindow.setWindowIcon(QtGui.QIcon('logo.png'))

    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Programa de Demonstração"))
        self.loggedin_lbl.setText(_translate("MainWindow", "Logged In as:"))
        self.UserName_lbl.setText(_translate("MainWindow", "UserName_lbl"))
        self.label_Funcionarios.setText(_translate("MainWindow", "Funcionários"))
        item = self.tabela_Funcionarios.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tabela_Funcionarios.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tabela_Funcionarios.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Idade"))
        item = self.tabela_Funcionarios.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Endereço"))
        item = self.tabela_Funcionarios.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Salário"))
        item = self.tabela_Funcionarios.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Contratação"))
        __sortingEnabled = self.tabela_Funcionarios.isSortingEnabled()
        self.tabela_Funcionarios.setSortingEnabled(False)
        item = self.tabela_Funcionarios.item(0, 0)
        item.setText(_translate("MainWindow", "Caio"))
        item = self.tabela_Funcionarios.item(0, 1)
        item.setText(_translate("MainWindow", "19"))
        item = self.tabela_Funcionarios.item(0, 2)
        item.setText(_translate("MainWindow", "N interessa"))
        item = self.tabela_Funcionarios.item(0, 3)
        item.setText(_translate("MainWindow", "R$ 5000,00"))
        item = self.tabela_Funcionarios.item(0, 4)
        item.setText(_translate("MainWindow", "21/11/2021"))
        self.tabela_Funcionarios.setSortingEnabled(__sortingEnabled)
        self.But_EditFunc.setText(_translate("MainWindow", "Confirmar alterações"))
        self.But_AddFunc.setText(_translate("MainWindow", "Adicionar/Remover"))
        item = self.tabela_Projetos.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tabela_Projetos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tabela_Projetos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tabela_Projetos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Funcionarios participantes"))
        item = self.tabela_Projetos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Cliente"))
        item = self.tabela_Projetos.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Contato"))
        __sortingEnabled = self.tabela_Projetos.isSortingEnabled()
        self.tabela_Projetos.setSortingEnabled(False)
        item = self.tabela_Projetos.item(0, 0)
        item.setText(_translate("MainWindow", "001"))
        item = self.tabela_Projetos.item(0, 1)
        item.setText(_translate("MainWindow", "Projeto demo"))
        item = self.tabela_Projetos.item(0, 2)
        item.setText(_translate("MainWindow", "Caio"))
        item = self.tabela_Projetos.item(0, 3)
        item.setText(_translate("MainWindow", "Quem sabe"))
        item = self.tabela_Projetos.item(0, 4)
        item.setText(_translate("MainWindow", "(00)9000-0000"))
        self.tabela_Projetos.setSortingEnabled(__sortingEnabled)
        self.But_viewProjeto.setText(_translate("MainWindow", "Confirmar alterações"))
        self.But_createProjeto.setText(_translate("MainWindow", "Criar/Deletar"))
        self.label_Projetos.setText(_translate("MainWindow", "Projetos"))
        self.label_Comunicado.setText(_translate("MainWindow", "Comunicado"))
        self.text_Comunicado.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_ComunicadoAssunto.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:12pt; font-weight:900; font-style:italic;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_comunicado2.setText(_translate("MainWindow", "Assunto:"))
        self.label_Comunicado3.setText(_translate("MainWindow", "Texto:"))
        self.But_EnviarComunicado.setText(_translate("MainWindow", "Enviar"))

############################################################################################################################

    def check_ChangeFunc(self):
        c.execute("SELECT * from 'Funcionarios'")
        itensFunc1=[]
        for i in c.fetchall():
            itensFunc1.append(i)
        #
        try:
            numRows = self.tabela_Funcionarios.rowCount()
            numColumn = self.tabela_Funcionarios.columnCount()
            listaItens=str(itensFunc1)
            novosItens=[]
            #
            novosItens_List=[]
            #
            for i in range(0,numRows):
                addAtual=''
                addAtual_Lista=[]
                for a in range(0,numColumn):
                    addAtual_Lista.append(str(self.tabela_Funcionarios.item(i,a).text()))
                    novosItens_List.append(str(self.tabela_Funcionarios.item(i,a).text()))
                addAtual+=str(addAtual_Lista)
                addAtual=addAtual.replace('[','(')
                addAtual=addAtual.replace(']',')')
                novosItens.append(addAtual)
            lista_novosItens=str(novosItens).replace('"','')
            if listaItens==lista_novosItens:
                pass
            if listaItens!=lista_novosItens:
                c.execute("SELECT * from 'Funcionarios'")
                NamesColunasAtual = list(map(lambda x: x[0], c.description))
                counterItens=0
                ##################################
                #
                c.execute("SELECT rowid, * from 'Funcionarios'")
                realID=[]
                #
                for i in c.fetchall():
                    realID.append(i[0])
                ##################################
                for linha in realID:
                    for col in NamesColunasAtual:
                        c.execute("UPDATE '{}' SET {} = '{}' WHERE rowid = {}".format('Funcionarios', col, novosItens_List[counterItens], linha))
                        counterItens+=1
                conex.commit()
                
        except:
            pass
            
###########CaioRSV###########
    def check_ChangeProj(self):
        c.execute("SELECT * from 'Funcionarios'")
        itensFunc1=[]
        try:
            numRows = self.tabela_Projetos.rowCount()
            numColumn = self.tabela_Projetos.columnCount()
            novosItens = []
            listaItens=str(itensFunc1)
            novosItens=[]
            #
            novosItens_List=[]
            #
            for i in range(0,numRows):
                addAtual=''
                addAtual_Lista=[]
                for a in range(0,numColumn):
                    addAtual_Lista.append(str(self.tabela_Projetos.item(i,a).text()))
                    novosItens_List.append(str(self.tabela_Projetos.item(i,a).text()))
                addAtual+=str(addAtual_Lista)
                addAtual=addAtual.replace('[','(')
                addAtual=addAtual.replace(']',')')
                novosItens.append(addAtual)
            lista_novosItens=str(novosItens).replace('"','')
            if str(listaItens)==lista_novosItens:
                pass
            if str(listaItens)!=lista_novosItens:
                c.execute("SELECT * from 'Projetos'")
                NamesColunasAtual = list(map(lambda x: x[0], c.description))
                counterItens=0
                ##################################
                #
                c.execute("SELECT rowid, * from 'Projetos'")
                realID=[]
                #
                for i in c.fetchall():
                    realID.append(i[0])
                ##################################
                for linha in realID:
                    for col in NamesColunasAtual:
                        c.execute("UPDATE '{}' SET {} = '{}' WHERE rowid = {}".format('Projetos', col, novosItens_List[counterItens], linha))
                        counterItens+=1
                conex.commit()
        except:
            pass
#####################
    def SecondWindow_Func(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Func_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()
#####
    def SecondWindow_Proj(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Proj_SecWindow()
        self.ui.setupUi(self.window)
        self.window.show()

#####################
    def sentMessage(self):
        self.But_EnviarComunicado.setText('Enviado!')
        self.text_ComunicadoAssunto.clear()
        self.text_Comunicado.clear()
        QtTest.QTest.qWait(2000)
        self.But_EnviarComunicado.setText('Enviar')
#####################
    def refresh_Func(self):
        c.execute("SELECT * from 'Funcionarios'")
        itens=[]
        for i in c.fetchall():
            itens.append(i)
        counterRows_Func=0
        for i in itens:
            counterRows_Func+=1
        self.tabela_Funcionarios.setRowCount(int(counterRows_Func))
        counterFunc=0
        for i in itens:
            counterFunc_Coluna=0
            for a in i:
                #
                item = QtWidgets.QTableWidgetItem()
                self.tabela_Funcionarios.setItem(counterFunc, counterFunc_Coluna, item)
                #
                self.tabela_Funcionarios.item(counterFunc, counterFunc_Coluna).setText(str(a))
                counterFunc_Coluna+=1
            counterFunc+=1
######
    def refresh_Proj(self):
        c.execute("SELECT * from 'Projetos'")
        itens2=[]
        for i in c.fetchall():
            itens2.append(i)
        counterRows_Proj=0
        for i in itens2:
            counterRows_Proj+=1
        self.tabela_Projetos.setRowCount(int(counterRows_Proj))
        counterProj=0
        for i in itens2:
            counterProj_Coluna=0
            for a in i:
                #
                item = QtWidgets.QTableWidgetItem()
                self.tabela_Projetos.setItem(counterProj, counterProj_Coluna, item)
                #
                self.tabela_Projetos.item(counterProj, counterProj_Coluna).setText(str(a))
                counterProj_Coluna+=1
            counterProj+=1
#####################
        

            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #
    MainWindow.show()
    sys.exit(app.exec_())
