from datainput import datainput
from device import device
def main():
    inputPorts = [datainput("A0", 0), datainput("A1", 1), datainput("A2", 2)]
    device01 = device(203412, "dev01", inputPorts)
    print(device01.getDeviceName())
def run():
    main()

if __name__ == "__main__":
    run()