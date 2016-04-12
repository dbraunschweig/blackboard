import re
import tkinter
import tkinter.scrolledtext

text = ''

def key_released(variable):
    global text

    string = scrolledtext.get(1.0, tkinter.END)
    if text == string:
        return

    text = string
    regex = re.compile("^Thread:(.*)Post:(.*)Author:(.*)Posted Date:(.*)Status:Published", re.MULTILINE)
    name = ''
    count = 0
    result = ''

    while True:
        match = regex.search(string)
        if match == None:
            break

        author = match.group(3).strip()
        date = match.group(4).strip()

        if date.find("Edited Date:") > 0:
            date = date[0:date.find("Edited Date:")]

        if name != author:
            if name != '':
                result += str(count) + '\n'
                result += '\n'
            name = author
            count = 0

        result += author + ' - ' + date + '\n'
        count += 1
        string = string[match.end(0):]

    if result != "":
        result += str(count)
        scrolledtext.delete(1.0, tkinter.END)
        scrolledtext.insert(tkinter.END, result)
        text = result

root = tkinter.Tk()
root.wm_title("Blackboard Discussion Grader")

scrolledtext = tkinter.scrolledtext.ScrolledText(root)
scrolledtext.pack(fill="both", expand=True)

scrolledtext.bind("<KeyRelease>", key_released)

root.mainloop()
