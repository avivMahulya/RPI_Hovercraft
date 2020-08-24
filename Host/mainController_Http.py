import keyboard  # using module keyboard
import httpClient

commands = {'forward' : 0,
           'back' : 0,
           'right' : 0,
           'left': 0
           }
           
def initDict(myDict):
    for x in myDict:
        myDict[x] =0
 

init_status = httpClient.initConnection()
if init_status == True:
    
    while True:  # making a loop
        initDict(commands)
        printBolean = False
        if keyboard.is_pressed('w'):  # if key 'w' is pressed 
            commands['forward'] = 100
        if keyboard.is_pressed('s'):  # if key 's' is pressed 
            commands['back'] = 100
        if keyboard.is_pressed('a'):  # if key 'a' is pressed     
            commands['left'] = 100
        if keyboard.is_pressed('d'):  # if key 'd' is pressed 
            commands['right'] = 100
        if keyboard.is_pressed('v'):  # if key 'q' is pressed
            commands['stop'] = True
        else:
            commands['stop'] = False
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            print("quiting")
            
            break
        if keyboard.is_pressed('p'):  # if key 'p' is pressed 
            printBolean = True
        if(printBolean):    
            print('*******')
            print(commands)
            print('*******')
        
        httpClient.sendCommands(commands)
    
    

        