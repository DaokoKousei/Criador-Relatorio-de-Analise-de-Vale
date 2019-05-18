from tkinter import *
from tkinter.ttk import Combobox
from datetime import datetime

carregamento = str
tipoMaterial = str
valorFalta = str
valorSobra = str
digi = str
status1 = str
falta1 = str
sobra1 = str
tFalha = str
imgCarregamento1 = str
imgCheck1 = str
now = datetime.now()
data = now.strftime("%d/%m/%Y")



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
        carregamentoLabel = Label(tela, text = "N° Carregamento: ",bg = "light grey", fg = "black", font = ("arial",13))
        carregamentoLabel.place(x= 20, y = 50)
        
        nCarregamento = Entry(tela, text= "", bg = "white", fg = "black", bd = 2)
        nCarregamento.place(x=160, y = 50)
        


        #Tipo De Material

        materialLabel = Label(tela, text = "Tipo de Material: ",bg = "light grey", fg = "black", font = ("arial",13))
        materialLabel.place(x= 310, y = 50)
        
        material = Entry(tela, text= "", bg = "white", fg = "black", bd = 2)
        material.place(x=440, y = 50)
        

        #Options

        opcoes1 = ("SIM","NÃO")
        opcoes2 = ("MANTER", "CANCELAR")
        opcoes3 = ("LOGISTICA", "MOTORISTA", "NÃO DEFINIDO")

        #Falta
        faltaLabel = Label(tela, text = "Falta: ", bg = "light grey", fg = "black", font = ("arial",13))
        faltaLabel.place(x = 20, y = 90)
        falta = Combobox(tela, value = opcoes1, width="11")
        falta.place(x=70, y = 90)

        #Valor da Falta

        vFaltaLabel = Label(tela, text = "Valor da falta: ", bg = "light grey", fg = "black", font = ("arial",13))
        vFaltaLabel.place(x = 170, y = 90)
        vFalta = Entry(tela, text= "", bg = "white", fg = "black", bd = 2, width = "11")
        vFalta.place(x=280, y = 90)

        #Sobra
        sobraLabel = Label(tela, text = "Sobra: ", bg = "light grey", fg = "black", font = ("arial",13))
        sobraLabel.place(x = 380, y = 90)
        sobra = Combobox(tela, value = opcoes1, width="11")
        sobra.place(x=440, y = 90)

         #Valor da Sobra

        vSobraLabel = Label(tela, text = "Valor da sobra: ", bg = "light grey", fg = "black", font = ("arial",13))
        vSobraLabel.place(x = 555, y = 90)
        vsobra = Entry(tela, text= "", bg = "white", fg = "black", bd = 2, width = "11")
        vsobra.place(x=675, y = 90)



        #Status

        statusLabel = Label (tela, text = "Status: ", bg = "light grey", fg = "black", font = ("arial",13))
        statusLabel.place(x = 580, y = 50)
        status = Combobox(tela, value = opcoes2, width = "14")
        status.place(x=640, y = 50)

        #Imagem do Carregamento

        imgCarregamentoLabel = Label (tela, text = "Imagem do Carregamento: ", bg = "light grey", fg = "black", font = ("arial",13))
        imgCarregamentoLabel.place(x = 20, y = 125)
        imgCarregamento = Combobox(tela, value = opcoes1, width = "14")
        imgCarregamento.place(x=230, y = 125)
        

        #Imagem do Checkout

        imgCheckoutLabel = Label (tela, text = "Imagem do Check-Out: ", bg = "light grey", fg = "black", font = ("arial",13))
        imgCheckoutLabel.place(x = 415, y = 125)
        imgCheckout = Combobox(tela, value = opcoes1, width = "14")
        imgCheckout.place(x=600, y = 125)

        #Tipo de falha

        tipoFalhaLabel = Label (tela, text = "Tipo de falha: ", bg = "light grey", fg = "black", font = ("arial",13))
        tipoFalhaLabel.place(x = 20, y = 160)
        tipoFalha = Combobox(tela, value = opcoes3, width = "15")
        tipoFalha.place(x=135, y = 160)


        #Detalhe

        detalheLabel = Label(tela, text = "Detalhe: ", bg = "light grey", fg = "black", font = ("arial",13))
        detalheLabel.place(x= 20, y = 250)
        escre = Text(tela, width = "90", height = "10")
        escre.place(x=20, y = 280)

        def enviar():
            carregamento = str(nCarregamento.get())
            tipoMaterial = str(material.get())
            valorFalta = str(vFalta.get())
            valorSobra = str(vsobra.get())
            digi = str(escre.get(1.0, END))
            status1 = str(status.get())
            falta1 = str(falta.get())
            sobra1 = str(sobra.get())
            tFalha = str(tipoFalha.get())
            imgCarregamento1 = str(imgCarregamento.get())
            imgCheck1 = str(imgCheckout.get())
            
            
            
            
            arquivo = open("Relatorio De Analise De Vale {}.txt" .format(carregamento),"w")

            arquivo.write("{} \n" .format(tipoMaterial))
            arquivo.write("{} \n" .format(valorFalta))
            arquivo.write("{} \n" .format(valorSobra))
            arquivo.write("{} \n" .format(data))
            arquivo.write("{} \n" .format(digi))
            arquivo.write("{} \n" .format(status1))
            arquivo.write("{} \n" .format(falta1))
            arquivo.write("{} \n" .format(sobra1))
            arquivo.write("{} \n" .format(tFalha))
            arquivo.write("{} \n" .format(imgCarregamento1))
            arquivo.write("{} \n" .format(imgCheck1))
            

        def fechar():
            tela.destroy()

        #Botoes

        btnGerar = Button(tela, width = "15", text = "Gerar",command = enviar)
        btnGerar.place(x = 520, y = 460)

        btnFechar = Button(tela, width = "15", text = "Fechar", command = fechar)
        btnFechar.place(x = 650, y = 460)

        

Programa()
