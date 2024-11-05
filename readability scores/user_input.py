from tkinter import filedialog

def user_input():
    """User input : raw text"""
    filepath = filedialog.askopenfilename(title= "Chosissez un fichier en texte brut...",
    filetypes=[("Texte brut", "*.txt")])
    file=open(filepath, encoding="utf8", errors='ignore')
    texte=file.read()
    file.close()
    return texte