def washhands():
    print("Washing hands")
def servefood():
    print("serving food")
def eatfood():
    washhands()
    servefood()
    print("Eating food")
    washhands()
eatfood()