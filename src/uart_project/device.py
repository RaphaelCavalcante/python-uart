class device:
    def __init__(self, serialNumber, deviceName, inputList):
        self.serialNumber = serialNumber
        self.deviceName = deviceName
        self.inputList = inputList
        
    def getDeviceName(self):
        return self.deviceName

    def getDeviceSerialNumber(self):
        return self.serialNumber
        
    def getInputList(self):
        return self.inputList