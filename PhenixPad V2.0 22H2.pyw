import tkinter
import os
import webbrowser
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
#code Name : Designe Sun 
#Build:207
#Name:Phenixpad X V2.0 22H2

class Notepad:

    #variables
    __root = Tk()

    #default window width and height
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFichierMenu = Menu(__thisMenuBar,tearoff=0)
    __thisEditionMenu = Menu(__thisMenuBar,tearoff=0)
    __thisAideMenu = Menu(__thisMenuBar,tearoff=0)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self,**kwargs):
        #initialization
                

        #set window size (the default is 300x300)

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            print("Error please to restart")
           

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            print("Error please to restart")
            
  
        #set the window text
        self.__root.title("Nouveaux Fichier - PhenixPad X V2.0 22H2")
            
        #center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight /2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        #to make the textarea auto resizable
        self.__root.grid_rowconfigure(0,weight=1)
        self.__root.grid_columnconfigure(0,weight=1)

        #add controls (widget)

        self.__thisTextArea.grid(sticky=N+E+S+W)

        self.__thisFichierMenu.add_command(label="Nouveaux",command=self.__newFile)
        self.__thisFichierMenu.add_command(label="Ouvrir",command=self.__openFile)
        self.__thisFichierMenu.add_command(label="Sauvegarder",command=self.__saveFile)
        self.__thisMenuBar.add_cascade(label="Fichier",menu=self.__thisFichierMenu)
        

        self.__thisEditionMenu.add_command(label="Couper",command=self.__cut)
        self.__thisEditionMenu.add_command(label="Copier",accelerator = "Ctrl + C" ,command=self.__copy)
        self.__thisEditionMenu.add_command(label="Coller", accelerator = "Ctrl + V" ,command=self.__paste)
        self.__thisEditionMenu.add_separator()
        self.__thisEditionMenu.add_command(label="Exit",command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="Edition",menu=self.__thisEditionMenu)
        
        
        
        
            
        self.__thisAideMenu.add_command(label="A propos de PhenixPad X",command=self.__showAbout)
        self.__thisAideMenu.add_command(label="contrat d'utilisation de PhenixPad X",command=self.__showAbout4)
        self.__thisAideMenu.add_command(label="voir sa version installer ",command=self.__showAbout5)
        self.__thisMenuBar.add_cascade(label="Aide",menu=self.__thisAideMenu)
        
       


        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT,fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

      
      
    def __quitApplication(self):
        self.__root.destroy()
        
    def __showAbout(self):
        showinfo("A propos de Phenixpad X V2.0 22H2","Created by: Phenix :Phenixpad X V 2.0 : Facile à utiliser, nous avons conçu Phenixpad X avec des fonctionnalités utiles. Il sera mis à jour chaque mois pour améliorer l'utilisation du phenixpad X. N'oubliez pas de toujours le mettre à jour pour bénéficier des dernières améliorations. Tous droits réservés.")
    def __showAbout4(self):
          showinfo("contrat d'utilisation de PhenixPad X","TERME DU CONTRAT LOGICIEL SLOPPY FOURNIT AUX PHENIX PAD X:Le logiciel est protégez par  Phenix , nous nous  chargons du devellopment et de l amelioration de l aplication.\n Phenix ce chargera de faire dans l aplication:\n . Les mise a jour,J'usqua sa fin du support.\nAssurez l amelioration du produit.\nAssurez les correction de bug trouvée dans le produit.\nAssurez le service technique  d aide si un utlisateur recontre des probleme d utilisation de l aplication.\ncondition d instalation du logiciel :nous fournisson le logiciel gratuitement , il n ya pas de restricion d installation  par nombre d'ordinateur , vous pouvez deployez le logiciel sur tout votre parc informatique.")
    def __showAbout5(self):
        showinfo("Version Installer", "Version Installer :\nV2.0 22H2")
    
    


    def __openFile(self):
        
        self.__file =  askopenfilename(defaultextension=".txt",filetypes=[("Text Documents",".txt")])
        
        if self.__file == "":
            #no file to open
            self.__file = None
        else:
            

            #try to open the file 

            #set the window title
            self.__root.title(os.path.basename(self.__file) + " - PhenixPad X 22H2")
            self.__thisTextArea.delete(1.0,END)

            file = open(self.__file,"r")

            self.__thisTextArea.insert(1.0,file.read())

            file.close() 
           
        
    def __newFile(self):
        self.__root.title("New File - PhenixPad X V2.0 22H2")
        self.__file = None
        self.__thisTextArea.delete(1.0,END)

    def __saveFile(self):
       
        if self.__file == None:
            #save as new file
            self.__file = asksaveasfilename(initialfile='New Name.txt',defaultextension=".txt",filetypes=[("Text Documents",".txt"),("Text Documents",".txt")])
            
            if self.__file == "":
                self.__file = None
                

                
            else:
                #try to save the file
                file = open(self.__file,"w")
                file.write(self.__thisTextArea.get(1.0,END))
                file.close()
                #change the window title
                self.__root.title(os.path.basename(self.__file) + " - Phenixpad X V2.0 22H2")
                
            
        else:
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")
   

    def run(self):

        #run main application
        self.__root.mainloop()




#run main application
notepad = Notepad(width=600,height=400)
notepad.run()