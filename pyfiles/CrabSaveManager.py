
import shutil
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, filedialog
import os


def CreateWidgets():
    saveLabel = Label(root, text="Save Directory : ")
    saveLabel.grid(row=0, column=0,
                          pady=5, padx=5)

    root.destinationText = Entry(root, width=50,
                                 textvariable=destinationLocation)
    root.destinationText.insert('1',
                                defaultLocation)
    root.destinationText.grid(row=0, column=1,
                              pady=0, padx=0,
                              columnspan=2)

    dest_browseButton = Button(root, text="Browse",
                               command=DestinationBrowse, width=15)
    dest_browseButton.grid(row=0, column=4,
                           pady=5, padx=5)
    



    Save1_Button = Button(root, text="Save1",
                             command=SetSave1, width=15)
    Save1_Button.grid(row=1, column=0,
                         pady=5, padx=5)
    Save2_Button = Button(root, text="Save2",
                             command=SetSave2, width=15)
    Save2_Button.grid(row=1, column=1,
                         pady=5, padx=5)
    Save3_Button = Button(root, text="Save3",
                             command=SetSave3, width=15)
    Save3_Button.grid(row=1, column=2,
                         pady=5, padx=5)
    
    
    SaveSlot = Label(root, text="Save Slot : ")
    SaveSlot.grid(row=1, column=3,
                          pady=5, padx=5)
    
    root.CurrentLabel = Label(root, text="1", textvariable=saveNum)
    root.CurrentLabel.grid(row=1, column=4,
                          pady=5, padx=5)


    
    CM = Label(root, text="Action : ")
    CM.grid(row=2, column=0, 
                          pady=5, padx=5)
    
    root.CurrentMode = Label(root, text="Load", textvariable = StateMode)
    root.CurrentMode.grid(row=2, column=1,columnspan=2,
                          pady=5, padx=5)



    Load_Button = Button(root, text="Load my files",
                           command=Load, width=30)
    Load_Button.grid(row=3, column=1,
                       pady=5, padx=5)

    Save_Button = Button(root, text="Save my files",
                           command=Save, width=30)
    Save_Button.grid(row=3, column=2,
                       pady=5, padx=5)





    Fishing_Button = Button(root, text="Fishing Line",
                             command=CopyFishing, width=20)
    Fishing_Button.grid(row=4, column=1,
                         pady=5, padx=5)

    Parry_Button = Button(root, text="Parry",
                               command=CopyParry, width=20)
    Parry_Button.grid(row=4, column=2,
                           pady=5, padx=5)

    Trash_Button = Button(root, text="Trash Day",
                              command=CopyTrash, width=20)
    Trash_Button.grid(row=5, column=1,
                          pady=5, padx=5)

    Grove_Button = Button(root, text="Enter Grove (pagurus)",
                         command=CopyGrove, width=20)
    Grove_Button.grid(row=5, column=2,
                     pady=5, padx=5)

    Heikea_Button = Button(root, text="Heikea",
                          command=CopyHeikea, width=20)
    Heikea_Button.grid(row=6, column=1,
                      pady=5, padx=5)

    Voltai_Button = Button(root, text="Voltai",
                               command=CopyVoltai, width=20)
    Voltai_Button.grid(row=6, column=2,
                           pady=5, padx=5)

    Mailbox_Button = Button(root, text="Mailbox Piece",
                                 command=CopyMailbox, width=20)
    Mailbox_Button.grid(row=7, column=1,
                             pady=5, padx=5)

    Boat_Button = Button(root, text="Boat Powered",
                          command=CopyBoat, width=20)
    Boat_Button.grid(row=7, column=2,
                      pady=5, padx=5)

    Roland_Button = Button(root, text="Roland",
                            command=CopyRoland, width=20)
    Roland_Button.grid(row=8, column=1,
                        pady=5, padx=5)

    Depression_Button = Button(root, text="Depression Sequence",
                             command=CopyDepression, width=20)
    Depression_Button.grid(row=8, column=2,
                         pady=5, padx=5)

    Inkerton_Button = Button(root, text="Inkerton",
                          command=CopyInkerton, width=20)
    Inkerton_Button.grid(row=8, column=1,
                      pady=5, padx=5)

    Camstcha_Button = Button(root, text="Camstcha",
                            command=CopyCamstcha, width=20)
    Camstcha_Button.grid(row=8, column=2,
                        pady=5, padx=5)

    Praya_Button = Button(root, text="Praya Dubia",
                               command=CopyPraya, width=20)
    Praya_Button.grid(row=9, column=1,
                           pady=5, padx=5)

    Firth_Button = Button(root, text="Firth",
                         command=CopyFirth, width=20)
    Firth_Button.grid(row=9, column=2,
                     pady=5, padx=5)

    GG_Button = Button(root, text="GG",
                          command=CopyGG, width=20)
    GG_Button.grid(row=10, column=1,
                      pady=5, padx=5)
    

    Extra1_Button = Button(root, text="Additional Save One",
                           command=CopyExtra1, width=20)
    Extra1_Button.grid(row=11, column=1,
                       pady=5, padx=5)

    Extra2_Button = Button(root, text="Additional Save Two",
                           command=CopyExtra2, width=20)
    Extra2_Button.grid(row=11, column=2,
                       pady=5, padx=5)

    Extra3_Button = Button(root, text="Additional Save Three",
                           command=CopyExtra3, width=20)
    Extra3_Button.grid(row=12, column=1,
                       pady=5, padx=5)

    Extra4_Button = Button(root, text="Additional Save Four",
                           command=CopyExtra4, width=20)
    Extra4_Button.grid(row=12, column=2,
                       pady=5, padx=5)
    
    

def DestinationBrowse():
    destinationdirectory = filedialog.askdirectory(initialdir="")
    WriteSavePath(destinationdirectory)
    root.destinationText.replace('1', destinationdirectory)
    
# Write the path in the savePath file
def WriteSavePath(message):
    writeFile = os.path.join(os.path.dirname(__file__), "savePath.txt")
    writeFileWrite = open(writeFile, "w")
    writeFileWrite.write('%s' % str(message))
    writeFileWrite.close()
    return


def SetSave1():
    #destinationdirectory = os.path.join(os.environ['USERPROFILE'], "AppData\LocalLow\Aggro Crab\AnotherCrabsTreasure\Save1")
    #WriteSavePath(destinationdirectory)
    NewLoc = defaultLocation+"\Save1"
    destinationLocation.set(NewLoc)
    saveNum.set("1")
    root.CurrentLabel.config(text = "1")

def SetSave2():
    #destinationdirectory = os.path.join(os.environ['USERPROFILE'], "AppData\LocalLow\Aggro Crab\AnotherCrabsTreasure\Save2")
    #WriteSavePath(destinationdirectory)
    NewLoc = defaultLocation+"\Save2"
    destinationLocation.set(NewLoc)
    saveNum.set("2")
    root.CurrentLabel.config(text = "2")

def SetSave3():
    #destinationdirectory = os.path.join(os.environ['USERPROFILE'], "AppData\LocalLow\Aggro Crab\AnotherCrabsTreasure\Save3")
    #WriteSavePath(destinationdirectory)
    NewLoc = defaultLocation+"\Save3"
    destinationLocation.set(NewLoc)
    saveNum.set("3")
    root.CurrentLabel.config(text = "3")


def Save():
    StateMode.set("save")
    root.CurrentMode.config(text = "Save")

def Load():
    StateMode.set("load")
    root.CurrentMode.config(text = "Load")


def SaveLoad(Loc_Folder):
    isExist = os.path.exists(Loc_Folder)
    if not isExist:
        os.makedirs(Loc_Folder)

    SaveNumber = str(int(saveNum.get()) - 1)
    DestSaveName = "/SaveFile_" + SaveNumber + ".CRAB"

    destination_location = destinationLocation.get()

    DestinationSave = destination_location + DestSaveName
    Loc_Save = Loc_Folder + "/SaveFile_0.CRAB"

    if StateMode.get() == "load":
        NewLoad = shutil.copy(Loc_Save, "./!TempSave")
        os.replace(NewLoad, "./!TempSave" + DestSaveName)
        shutil.copy("./!TempSave" + DestSaveName, destinationLocation.get())
        messagebox.showinfo(title="Crab load", message="You loaded on the slot " + saveNum.get())
    else:
        saveReply = messagebox.askokcancel(title="Crab save", message="Do you want to save the slot " + saveNum.get() + "?")
        if saveReply:
            NewSave = shutil.copy(DestinationSave, Loc_Folder)
            os.replace(NewSave, Loc_Folder+'/SaveFile_0.CRAB')
            messagebox.showinfo(title="Crab save", message="You saved the slot " + saveNum.get())

# Read path
def ReadSavePath():
    readFile = os.path.join(os.path.dirname(__file__), "savePath.txt")
    readFileRead = open(readFile, "r")
    read = readFileRead.readline()
    readFileRead.close()
    return read

def CopyFishing():
    Loc_Folder = "./Fishing Line/"
    SaveLoad(Loc_Folder)


def CopyParry():
    Loc_Folder = "./Parry/" 
    SaveLoad(Loc_Folder)

def CopyTrash():
    Loc_Folder = "./Trash Day/"
    SaveLoad(Loc_Folder)

def CopyGrove():
    Loc_Folder = "./Enter Grove/"
    SaveLoad(Loc_Folder)

def CopyHeikea():
    Loc_Folder = "./Heikea/"
    SaveLoad(Loc_Folder)

def CopyVoltai():
    Loc_Folder = "./Voltai/"
    SaveLoad(Loc_Folder)

def CopyMailbox():
    Loc_Folder = "./Mailbox Piece/"
    SaveLoad(Loc_Folder)

def CopyBoat():
    Loc_Folder = "./Boat Powered/"
    SaveLoad(Loc_Folder)

def CopyRoland():
    Loc_Folder = "./Roland/"
    SaveLoad(Loc_Folder)

def CopyDepression():
    Loc_Folder = "./Depression Sequence/"
    SaveLoad(Loc_Folder)

def CopyInkerton():
    Loc_Folder = "./Inkerton/"
    SaveLoad(Loc_Folder)

def CopyCamstcha():
    Loc_Folder = "./Camstcha/"
    SaveLoad(Loc_Folder)

def CopyPraya():
    Loc_Folder = "./Praya Dubia/"
    SaveLoad(Loc_Folder)

def CopyFirth():
    Loc_Folder = "./Firth/"
    SaveLoad(Loc_Folder)

def CopyGG():
    Loc_Folder = "./GG/"
    SaveLoad(Loc_Folder)

def CopyExtra1():
    Loc_Folder = "./Extra 1/"
    SaveLoad(Loc_Folder)

def CopyExtra2():
    Loc_Folder = "./Extra 2/"
    SaveLoad(Loc_Folder)

def CopyExtra3():
    Loc_Folder = "./Extra 3/"
    SaveLoad(Loc_Folder)

def CopyExtra4():
    Loc_Folder = "./Extra 4/"
    SaveLoad(Loc_Folder)


root = tk.Tk()
root.title('Another Crab\'s Creasure Save Manager')
root.geometry('')
root.iconbitmap('./Crab.ico')
root.resizable(False, False)

destinationLocation = StringVar()
defaultLocation = ReadSavePath()

saveNum = StringVar()
saveNum.set("1")
SaveName = "SaveFile_0.CRAB"

StateMode = StringVar()
StateMode.set("load")
CreateWidgets()

root.mainloop()
