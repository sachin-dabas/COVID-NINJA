from cmu_112_graphics import *

# splashScreenMode
def splashScreenMode_redrawAll(app,canvas):
    canvas.create_text(app.width//2,app.height//2, text = "Battle of Pathogens",
                             font = 'Arial 24 bold', fill='brown')
    canvas.create_text(app.width//2,app.height//2+100, text = "Press any key",
                             font = 'Arial 18 bold', fill='brown')

def splashScreenMode_keyPressed(app,event):
    app.mode = 'gameMode'
