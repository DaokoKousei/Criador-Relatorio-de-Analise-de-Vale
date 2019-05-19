from tkinter import *
from tkinter.ttk import Combobox
from datetime import datetime
from reportlab.pdfgen import canvas
from tkinter.messagebox import *
import webbrowser


carregamento = str
vale1 = str
nome = str
tipoMaterial = str
valorFalta = str
valorSobra = str
digi = str
status1 = str
falta1 = str
sobra1 = str
tFalha = str
avaria1 = str
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
        
        relatorioLabel = Label(tela, text = "Relatório de Analise de Vale ",bg = "light grey", fg = "black", font = ("arial",17))
        relatorioLabel.place(x= 250, y = 15)

        #Carregamento
        carregamentoLabel = Label(tela, text = "N° Carregamento: ",bg = "light grey", fg = "black", font = ("arial",13))
        carregamentoLabel.place(x= 20, y = 70)
        
        nCarregamento = Entry(tela, text= "", bg = "white", fg = "black", bd = 2, width="10")
        nCarregamento.place(x=160, y = 70)
        


        #Tipo De Material

        materialLabel = Label(tela, text = "Tipo de Material: ",bg = "light grey", fg = "black", font = ("arial",13))
        materialLabel.place(x= 240, y = 70)
        
        material = Entry(tela, text= "", bg = "white", fg = "black", bd = 2, width= "15")
        material.place(x=370, y = 70)
        

        #Options

        opcoes1 = ("SIM","NÃO")
        opcoes2 = ("MANTER", "CANCELAR")
        opcoes3 = ("LOGISTICA", "MOTORISTA", "NÃO DEFINIDO")

        #Falta
        faltaLabel = Label(tela, text = "Falta: ", bg = "light grey", fg = "black", font = ("arial",13))
        faltaLabel.place(x = 20, y = 105)
        falta = Combobox(tela, value = opcoes1, width="5")
        falta.place(x=70, y = 105)

        #Valor da Falta

        vFaltaLabel = Label(tela, text = "Valor: ", bg = "light grey", fg = "black", font = ("arial",13))
        vFaltaLabel.place(x = 130, y = 105)
        vFalta = Entry(tela, text= "", bg = "white", fg = "black", bd = 2, width = "9")
        vFalta.place(x=180, y = 105)

        #Sobra
        sobraLabel = Label(tela, text = "Sobra: ", bg = "light grey", fg = "black", font = ("arial",13))
        sobraLabel.place(x = 270, y = 105)
        sobra = Combobox(tela, value = opcoes1, width="5")
        sobra.place(x=330, y = 105)

         #Valor da Sobra

        vSobraLabel = Label(tela, text = "Valor: ", bg = "light grey", fg = "black", font = ("arial",13))
        vSobraLabel.place(x = 390, y = 105)
        vsobra = Entry(tela, text= "", bg = "white", fg = "black", bd = 2, width = "9")
        vsobra.place(x=440, y = 105)
        
        
        #Avaria
        
        avariaLabel = Label(tela, text = "Avaria: ", bg = "light grey", fg = "black", font = ("arial",13))
        avariaLabel.place(x = 510, y = 105)
        avaria = Combobox(tela, value = opcoes1, width="5")
        avaria.place(x=570, y = 105)

        #Status

        statusLabel = Label (tela, text = "Status: ", bg = "light grey", fg = "black", font = ("arial",13))
        statusLabel.place(x = 630, y = 105)
        status = Combobox(tela, value = opcoes2, width = "9")
        status.place(x=690, y = 105)


        #Nome Motorista
        
    
        nomeLabel = Label(tela, text = "Nome do Motorista: ",bg = "light grey", fg = "black", font = ("arial",13))
        nomeLabel.place(x = 485, y = 70)
        
        nMotorista = Entry(tela, text= "", bg = "white", fg = "black", bd = 2, width="21")
        nMotorista.place(x=635, y = 70)
        

       
        #Imagem do Carregamento

        imgCarregamentoLabel = Label (tela, text = "Imagem do Carregamento: ", bg = "light grey", fg = "black", font = ("arial",13))
        imgCarregamentoLabel.place(x = 20, y = 135)
        imgCarregamento = Combobox(tela, value = opcoes1, width = "5")
        imgCarregamento.place(x=230, y = 135)
        

        #Imagem do Checkout

        imgCheckoutLabel = Label (tela, text = "Imagem do Check-Out: ", bg = "light grey", fg = "black", font = ("arial",13))
        imgCheckoutLabel.place(x = 295, y = 135)
        imgCheckout = Combobox(tela, value = opcoes1, width = "5")
        imgCheckout.place(x=480, y = 135)

        #Tipo de falha

        tipoFalhaLabel = Label (tela, text = "Tipo de falha: ", bg = "light grey", fg = "black", font = ("arial",13))
        tipoFalhaLabel.place(x = 540, y = 135)
        tipoFalha = Combobox(tela, value = opcoes3, width = "14")
        tipoFalha.place(x=660, y = 135)
        
        #Numero vale
        
    
        valeLabel = Label(tela, text = "Número do Vale: ",bg = "light grey", fg = "black", font = ("arial",13))
        valeLabel.place(x = 20, y = 165)
        
        nVale = Entry(tela, text= "", bg = "white", fg = "black", bd = 2, width="20")
        nVale.place(x=150, y = 165)


        #Detalhe

        detalheLabel = Label(tela, text = "Detalhe: ", bg = "light grey", fg = "black", font = ("arial",13))
        detalheLabel.place(x= 20, y = 230)
        escre = Text(tela, width = "92", height = "10")
        escre.place(x=20, y = 260)

        def enviar():
            carregamento = str(nCarregamento.get())
            tipoMaterial = str(material.get())
            valorFalta = str(vFalta.get())
            valorSobra = str(vsobra.get())
            digi = str(escre.get(1.0,END))
            avaria1 = str(avaria.get())
            falta1 = str(falta.get())
            sobra1 = str(sobra.get())
            tFalha = str(tipoFalha.get())
            imgCarregamento1 = str(imgCarregamento.get())
            imgCheck1 = str(imgCheckout.get())
            nome = str(nMotorista.get())
            status1 = str(status.get())
            vale1 = str(nVale.get())
            
            #DESENHO PDF
            
            c = canvas.Canvas("Relatorio De Analise De Vale {}.pdf" .format(carregamento))
            c.setFont("Helvetica-Bold", 12)

            c.drawString(25,800,"                          PROCESSO ADMINISTRATIVO - LAUDO DE ANALISE TÉCNICA")
            c.setFont('Helvetica', 12)

            #Retangulo
            c.rect(25, 435, 550, 350, fill=0) #coluna, linha, largura, tamanho
            c.setFont("Helvetica-Bold", 12)
            c.drawString(27,770,"Logística Reversa: ") 
            c.setFont("Helvetica", 12)
            c.setFont("Helvetica-Bold", 12)
            
            c.drawString(27,720,"Avaria:")
            c.setFont('Helvetica', 12)
            c.drawString(75,720,"{}" .format(avaria1))
            
            c.setFont("Helvetica-Bold", 12)
            c.drawString(120,720,"Falta: ")
            c.setFont('Helvetica', 12)
            c.drawString(160,720,"{}" .format(falta1))
            
            c.setFont("Helvetica-Bold", 12)
            c.drawString(200,720,"Sobra:")
            c.setFont('Helvetica', 12)
            c.drawString(245,720,"{}" .format(sobra1))
            
            c.setFont("Helvetica-Bold", 12)
            c.drawString(280,720,"Val. falta:  ")
            c.setFont('Helvetica', 12)
            c.drawString(340,720,"R$ {}" .format(valorFalta))
            
            c.setFont("Helvetica-Bold", 12)
            c.drawString(420,720,"Val. sobra:  ")
            c.setFont('Helvetica', 12)
            c.drawString(490,720,"R$ {}" .format(valorSobra))
            
            c.setFont("Helvetica-Bold", 12)
            c.drawString(27,700,"Tipo de material: ")
            c.setFont('Helvetica', 12)
            c.drawString(130,700,"{}" .format(tipoMaterial))
            
            c.setFont("Helvetica-Bold", 12)
            c.drawString(220,700,"Tipo de falha: ")
            c.setFont('Helvetica', 12)
            c.drawString(310,700,"{}" .format(tFalha))
            
            c.setFont("Helvetica-Bold", 12)
            c.drawString(27,680,"Imagem do carregamento: ")
            c.setFont('Helvetica', 12)
            c.drawString(185,680,"{}" .format(imgCarregamento1))
            
            c.setFont("Helvetica-Bold", 12)
            c.drawString(230,680,"Imagem do Check-Out: ")
            c.setFont('Helvetica', 12)
            c.drawString(370,680,"{}" .format(imgCheck1))
            
            c.setFont("Helvetica-Bold", 12)
            c.drawString(430,680,"Status: ")
            c.setFont("Helvetica", 12)
            c.drawString(480,680,"{}" .format(status1))
            
            c.setFont("Helvetica-Bold", 12)
            c.drawString(27,600,"Laudo:")
            c.setFont('Helvetica', 12)
            
            
            c.drawString(27,580,"{}".format(digi[0:80]))
            c.drawString(27,570,"{}".format(digi[81:161]))
            c.drawString(27,560,"{}".format(digi[162:242]))
            c.drawString(27,550,"{}".format(digi[322:402]))
            c.setFont('Helvetica',12)
            
            c.line(27,450,200,450)
            
            c.drawString(27, 440, "               Analista")
            
            c.setFont("Helvetica-Bold", 12)
            c.drawString(450, 440, " Data: {}" .format(data))
            c.setFont('Helvetica', 10)
            
            #Parte do transporte
            
            c.rect(25, 180, 550, 250, fill=0) #coluna, linha, largura, tamanho
            c.setFont("Helvetica-Bold", 12)
            c.drawString(27,415,"Transporte: ")
            c.setFont("Helvetica-Bold", 12)
            
            c.drawString(27,380,"Laudo: ")
            c.setFont('Helvetica', 11)
            
            
            c.drawString(27,300,"Ass. Aprovação: ____________________ Data: ___/___/____ Status: _________")
            c.drawString(27,270,"Eu, {} declaro que fui comunicado, tive acesso a analise realizada e".format(nome))
            c.setFont('Helvetica', 11)
            c.drawString(27,260,"estou ciente do desconto do vale ({}) tratado nesse processo.".format(vale1))
            
            c.drawString(27,210,"_______________________              _______________________             _______________________ ")
            
            c.drawString(27,190,"{}" .format(nome))
            
            c.drawString(200,190,"               TESTEMUNHA                                    TESTEMUNHA" .format(nome))
            
            
            
            
            
            #Parte DRH
            
            c.rect(25, 50, 550, 120, fill=0) #coluna, linha, largura, tamanho
            
            c.setFont("Helvetica-Bold", 12)
            c.drawString(27,153,"DRH: ")
            
            c.setFont("Helvetica", 12)
            
            c.drawString(27,100, "Autorizado desconto no valor de R$:______________ Data: ___/___/____")
            c.drawString(27,80, "Abonado:______________ Data: ___/___/____")
            
            
            c.save()
            showinfo(title="Sucesso",message="O relatório foi criado com sucesso!")
            webbrowser.open("Relatorio De Analise De Vale {}.pdf" .format(carregamento))
           
            
        
            

        def fechar():
            tela.destroy()

        #Botoes

        btnGerar = Button(tela, width = "15", text = "Gerar",command = enviar)
        btnGerar.place(x = 520, y = 460)

        btnFechar = Button(tela, width = "15", text = "Fechar", command = fechar)
        btnFechar.place(x = 650, y = 460)

        

Programa()