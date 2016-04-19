import re
import tkinter
import tkinter.scrolledtext

text = ''
done = False

def key_released(variable):
    global text
    global done

    if done:
        return

    string = scrolledtext.get(1.0, tkinter.END)
    if text == string:
        return

    text = string
    regex = re.compile("^Thread:(.*)Post:(.*)Author:(.*)Posted Date:(.*)Status:Published", re.MULTILINE)
    name = ''
    total = 0
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
        content = text[match.end(0):text.find("Tags: ", match.end(0))]
        content = content.strip()
        words = len(content.split())

        if name != author:
            if name != '':
                result += str(count) + ' post(s)'
                if count > 0:
                    result += ' - {:.1f} words per post average'.format(total / count)
                result += '\n\n'
            result += author + '\n'
            name = author
            total = 0
            count = 0

        result += date + ' - ' + str(words) + ' words\n'
        total = total + words
        count += 1
        string = string[match.end(0):]

    result += str(count) + ' post(s)'
    if count > 0:
                    result += ' - {:.1f} words per post average'.format(total / count)
    done = True
    scrolledtext.delete(1.0, tkinter.END)
    scrolledtext.insert(tkinter.END, result)

root = tkinter.Tk()
root.wm_title("Blackboard Discussion Grader")

scrolledtext = tkinter.scrolledtext.ScrolledText(root)
scrolledtext.pack(fill="both", expand=True)

scrolledtext.bind("<KeyRelease>", key_released)

root.mainloop()
