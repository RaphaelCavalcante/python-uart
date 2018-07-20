import serial

def main():
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    ser.write(b'ping')
    ser.close()

def run():
    main()

if __name__ == "__main__":
    run()