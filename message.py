from tkinter import *


def alert(alert_text):
    """ Displays an Alert box.  """
    def exit():
        ROOT.destroy()

    ROOT = Tk()

    ROOT.title('Alert')

    # Alert popup geometry
    ROOT.geometry('300x150')
    ROOT.minsize(300, 150)
    ROOT.maxsize(300, 150)

    alert_frame = LabelFrame(ROOT, text='Alert')
    alert_frame.pack(fill='both', expand='yes')

    alert_display = Label(alert_frame, text=alert_text)
    alert_display.pack()

    okay_button = Button(ROOT, text='Okay', command=exit)
    okay_button.pack(side='right', anchor='se')

    ROOT.mainloop()


if __name__ == '__main__':
    alert('Test')
