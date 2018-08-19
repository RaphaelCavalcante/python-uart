from datainput import Datainput
from device import Device
import serial

def queryBuild(datainputs):
    dataframe = [b'1']
    if len(datainputs) > 0 and len(datainputs) < 2:
        for dataInput in datainputs:
            dataframe.append(str(dataInput.port).encode())
    dataframe.append(b'0')
    return dataframe

def main():
    device01 = Device("D01","device01", inputList=[Datainput(5)])
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    for res in queryBuild(device01.inputList):
        ser.write(res)
    ser.flush()
    ser.close()

def run():
    main()

if __name__ == "__main__":
    run()