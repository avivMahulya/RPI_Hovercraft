import errorCodes


class Controller:

    def initializeConnection(self, target_ip):
        # Connect To target
        # return ErrorCodes.Success if the connection established
        # return ErrorCodes.Fail if the connection failed
        return ErrorCodes.Success

    def toggleHover(self):
        # toggle Hover status (Turn ON/OFF the hover motor)
        return  ErrorCodes.Success

    def turn(self , value):
        #send command to turn
        # The value is between -30 to 30
        return ErrorCodes.Success

    def moveForward(self,value):
        #send command to move forward
        # The value is between 0 to 100
        return ErrorCodes.Success

    def moveBackward(self,value):
        #send command to move backward
        # The value is between 0 to 100
        return ErrorCodes.Success

    def moveBackward(self,value):
        #send command to move backward
        # The value is between 0 to 100
        return ErrorCodes.Success