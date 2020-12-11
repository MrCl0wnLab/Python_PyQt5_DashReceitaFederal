__author__ = "Cleiton Pinheiro"
__nick__ = "Mr. Cl0wn"
__email__ = "mrcl0wnLab@gmail.com"
__blog__ = "https://blog.mrcl0wn.com/"

import sys
import json
import datetime

from ui_ReceitaFederal import  Ui_MainWindow
from assets import files

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)
        
        self.ui_main.pushButton_BtnDeclarar.clicked.connect(lambda x:self.click_button('DECLARAR'))
        self.ui_main.pushButton_BtnServico.clicked.connect(lambda x:self.click_button('SERVIÇO'))
        self.ui_main.pushButton_BtnAssuntos.clicked.connect(lambda x:self.click_button('ASSUNTOS'))
        self.ui_main.pushButton_BtnAcessoInfo.clicked.connect(lambda x:self.click_button('ACESSO INFO'))
        self.ui_main.pushButton_BtnComposicao.clicked.connect(lambda x:self.click_button('COMPOSIÇÃO'))
        self.ui_main.pushButton_BtnConsultaProcessos.clicked.connect(lambda x:self.click_button('CONSULTA PROCESSOS'))
        self.ui_main.pushButton_BtnCentraisConteudo.clicked.connect(lambda x:self.click_button('CENTRAIS DE CONTEÚDO'))
        self.ui_main.pushButton_BtnCanaisAtendimento.clicked.connect(lambda x:self.click_button('CANAIS DE ATENDIMENTO'))
        self.ui_main.pushButton_BtnOndeEncontro.clicked.connect(lambda x:self.click_button('ONDE ENCONTRO'))
        self.ui_main.pushButton_BtnGovbr.clicked.connect(lambda x:self.click_button('GOV.BR'))

        self.ui_main.pushButton_BtnConfiguracao.clicked.connect(lambda x:self.click_button('CONFIGURAÇÃO'))
        self.ui_main.pushButton_BtnFeedback.clicked.connect(lambda x:self.click_button('FEEDBACK'))
        self.ui_main.pushButton_BtnSugestao.clicked.connect(lambda x:self.click_button('SUGESTÃO'))

        self.ui_main.pushButton_BtnCPF.clicked.connect(lambda x:self.click_button('CPF'))
        self.ui_main.pushButton_BtnAlfandega.clicked.connect(lambda x:self.click_button('ALFANDEGA'))
        self.ui_main.pushButton_BtnAjusteAnual.clicked.connect(lambda x:self.click_button('AJUSTE ANUAL'))
        self.ui_main.pushButton_BtnImpostoRenda.clicked.connect(lambda x:self.click_button('DECLARAR IMPOSTO'))
        self.ui_main.pushButton_BtnDeclaracaoImport.clicked.connect(lambda x:self.click_button('DECLAÇÃO DE IMPORTAÇÃO'))

        self.ui_main.pushButton_BtnHistorico.clicked.connect(lambda x:self.click_button('HISTORICO'))

        self.ui_main.pushButton_BtnAjuda01.clicked.connect(lambda x:self.click_button('AJUDA 01'))
        self.ui_main.pushButton_BtnAjuda02.clicked.connect(lambda x:self.click_button('AJUDA 02'))
        self.ui_main.pushButton_BtnAjuda03.clicked.connect(lambda x:self.click_button('AJUDA 03'))
        self.ui_main.pushButton_BtnAjuda04.clicked.connect(lambda x:self.click_button('AJUDA 04'))
        
        self.ui_main.pushButton_BtnRestituicaoIR.clicked.connect(lambda x:self.click_button('RESTITUIÇÃO'))
        self.ui_main.pushButton_BtnAjuda.clicked.connect(lambda x:self.click_button('AJUDA'))
        
        data_file_dict = self.open_file_json('data.json','r')
        self.set_dash_value(data_file_dict)

        self.show()

    # Set values in Dash
    def set_dash_value(self,data_dict):
        if data_dict:
            self.ui_main.label_TxtTopDataUser.setText(data_dict.get('user'))
            self.ui_main.label_TxtTopDataUserType.setText(data_dict.get('profile_type'))
            self.ui_main.label_TxtValorRestituicao.setText("R$"+data_dict.get('receita_value'))
            self.ui_main.pushButton_TopAlert.setText(data_dict.get('notification'))
            self.ui_main.lineEdit_TxtDataAtual.setText(self.date_now())

    # Clicked buttons
    def click_button(self,value):
        print('CLICKED',value)

    # Open File data.json
    def open_file_json(self, file_name_str, mode):
        try:
            data_file = open(
                file_name_str,
                mode=mode,
                encoding='utf-8',
                errors='ignore')
            data_file = json.load(data_file)
        except IOError as e:
            return str(e)
        else:
            return data_file

    # Get date formatted
    def date_now(self):
        now = datetime.datetime.now()
        return str(now.strftime("%A %d/%m/%Y")).capitalize()

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        pass
