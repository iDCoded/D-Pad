from tkinter import messagebox


def alert(alert_text):
    """ Displays an Alert box.  """
    messagebox.showerror(title="Error opening File", message=alert_text)


if __name__ == '__main__':
    alert('Test')
