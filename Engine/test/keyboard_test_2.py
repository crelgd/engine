import Engine as engine 

while True:
    key = engine.keyboard.ifClicked()

    if (key == False):
        print("Q could not pressed!")
    else:
        print("Q PRESSED!")