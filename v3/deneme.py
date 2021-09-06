import pyperclip

def copy_pasteDec():
    if not pyperclip.waitForNewPaste()=="":
        word=pyperclip.waitForNewPaste()

        with open("copy_paste.txt", "w", encoding="utf-8") as file:
            file.write(word)
        import turengv3
        turengv3.Ui_Form.lineEdit.setText(word)
        turengv3.Ui_Form.ttrr()




