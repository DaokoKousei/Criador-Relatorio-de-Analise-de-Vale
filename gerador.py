from tkinter import *
from tkinter.ttk import Combobox


class Programa(object):
    def __init__(self):


        #Tela do Programa

        tela = Tk()
        tela.geometry('800x500')
        tela.resizable(False,False)
        tela.title("Gerador de Analise de Vale")
        tela ['bg'] = 'white'
        tela.wm_iconbitmap('sis.ico')

        #Frame do conteudo

        self.frame = Frame(bg = 'grey')
        self.frame.pack()

        #Criação do CANVAS

        self.canvas = Canvas(self.frame, bg ="light grey", width="800", height="500", cursor = 'hand2')
        self.canvas.pack()

        #Carregamento
        carregamentoLabel = Label(tela, text = "N° Carregamento: ",bg = "light grey", fg = "black", font = ("arial",10))
        carregamentoLabel.place(x= 20, y = 50)
        
        nCarregamento = Entry(tela, text= "", bg = "white", fg = "black", bd = 2)
        nCarregamento.place(x=130, y = 50)


        #Tipo De Material

        carregamentoLabel = Label(tela, text = "Tipo de Material: ",bg = "light grey", fg = "black", font = ("arial",10))
        carregamentoLabel.place(x= 310, y = 50)
        
        nCarregamento = Entry(tela, text= "", bg = "white", fg = "black", bd = 2)
        nCarregamento.place(x=410, y = 50)
        

        #Combox's

        opcoes1 = ("SIM","NÃO")
        opcoes2 = ("MANTER", "CANCELAR")
        opcoes3 = ("LOGISTICA", "MOTORISTA", "NÃO DEFINIDO")


        falta = Combobox(tela, value = opcoes1)
        falta.place(x=60, y = 450)

        #Status

        statusLabel = Label (tela, text = "Status: ", bg = "light grey", fg = "black", font = ("arial",10))
        statusLabel.place(x = 580, y = 50)
        
        status = Combobox(tela, value = opcoes2, width = "13")
        status.place(x=630, y = 50)


        #Botoes

        btnGerar = Button(tela, width = "15", text = "Gerar")
        btnGerar.place(x = 520, y = 460)

        btnFechar = Button(tela, width = "15", text = "Fechar")
        btnFechar.place(x = 650, y = 460)

        #Funções Botoes
        
if __name__ == '__main__':
    Programa()
