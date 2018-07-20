import serial

def main():
    ser = serial.Serial('/dev/ttyUSB0')
    print(ser.name)
    ser.write(b'hello')
    ser.close()

def run():
    main()

if __name__ == "__main__":
    run()