import webbrowser
#Biblioteca "webbrowser" — fornece uma interface de alto nível para permitir a exibição de documentos Web aos Usuários.

from tkinter import *
# Biblioteca "tkinter" — fornece interface padrão do Python para o kit de ferramentas gráficas Tk

root = Tk( ) # root vai representar  a janela gráfica criada pelo tkinter
root.title('Abrir Browser') # função ".title" cria o título da janela
root.geometry('300x200') # função ".geometry" define dimensões da janela gráfica


def google():
    webbrowser.open('www.google.com')
# função "google" criada para utilizar biblioteca "webbrowser" com função ".open" para abrir site do Google

mygoogle = Button(root, text='Abrir o Google', command= google).pack(pady=20)
# Objeto "mygoogle" cria botão para janela gráfica "root" com texto "Abrir o Google"(text)
# "command" chama função "google"
# Função ".pack" define posição do botão com "pady=20"

root.mainloop()
# Método ".mainloop" usado para exibir tela do objeto "root"