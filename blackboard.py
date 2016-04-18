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
                result += str(count) + ' posts - ' + "{0:.2f}".format(total / count) + ' words\n'
                result += '\n'
            name = author
            count = 0
            total = 0

        index = string.find("Tags:", match.end(0))
        words = len(string[match.end(0):index].split(" "))
        total += words

        result += author + ' - ' + date + " - " + str(words) + ' words\n'
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
