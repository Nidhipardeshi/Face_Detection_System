import winsound

def alarm():
    for _ in range(5):
        winsound.Beep(1000, 500)