from tkinter import messagebox


def alert(alert_text):
    """ Displays an Alert box.  """
    messagebox.showerror(title="Oops", message=alert_text)


def info(info_text):
    """ Displays an Information box """
    messagebox.showinfo(title="Information", message=info_text)


if __name__ == '__main__':
    alert('Test')
