from tkinter import *
from tkinter import filedialog, Text
import os
import json

root = Tk()
apps = {
    "files": []
}


def addApp():
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("Executables", "*.exe"),
                                                                                          ("All Files", "*.")))

    if filename:
        apps["files"].append(filename)
        label = Label(frame, text=filename, bg="gray")
        label.pack()
    else:
        pass


def runApps():
    for app in apps["files"]:
        os.startfile(app)


canvas = Canvas(root, height=700, width=1080, bg="#263D42")
canvas.pack()

frame = Frame(root, bg="light grey")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = Button(root, text="Open File", padx=10, pady=5, fg="White", bg="#263D42", command=addApp)
openFile.pack()

runApps = Button(root, text="Run Apps", padx=10, pady=5, fg="White", bg="#263D42", command=runApps)
runApps.pack()


def saveApps():
    with open("save.json", "w") as json_file:
        json.dump(apps, json_file)

    successLabel = Label(frame, text="Save Complete!!", bg="gray")
    successLabel.pack()


def loadApps():
    global apps
    if os.path.isfile("save.json"):
        with open("save.json") as json_file:
            apps = json.load(json_file)
    else:
        errorLabel = Label(frame, text="NO SAVE FILE LOCATED ERROR!!", bg="gray")
        errorLabel.pack()

    for app in apps["files"]:
        label = Label(frame, text=app, bg="gray")
        label.pack()


save = Button(root, text="Save Apps", padx=10, pady=5, fg="White", bg="#263D42", command=saveApps)
save.pack()

load = Button(root, text="Load Apps", padx=10, pady=5, fg="White", bg="#263D42", command=loadApps)
load.pack()

root.mainloop()
