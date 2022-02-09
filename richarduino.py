# Richarduino Connection Script
import serial

class Richarduino:

    # Initialize function
    def __init__(self, port, baudrate, timeout):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout

    # Function to get version
    def getVersion(self):
        print("Attempting to retrieve version...")
        data = bytes([ord('V')])
        
        try:
            conn = serial.Serial(self.port, baudrate=self.baudrate, timeout=self.timeout)
            conn.write(data)
            resp = conn.read(4).decode('utf-8')
            print("Recieved version: 0x" + resp)
            conn.close()
            return resp
        except:
            print("ERROR: Could not write data to RichArduino")
    
    # Function to set data at an address
    def poke(self, address, data):
        sendAddress = bytes.fromhex(address[2:])
        sendData = bytes.fromhex(data[2:])
        print("Sending data " + data + " to address " + address)
        try:
            conn = serial.Serial(self.port, baudrate=self.baudrate, timeout=self.timeout)
            conn.write(bytes([ord('W')]))
            conn.write(sendAddress)
            conn.write(sendData)
            print("Success: sent " + sendData)
            conn.close()
        except:
            print("ERROR: Could not write to address " + str(sendAddress))
        
    # Function to get data from an address
    def peek(self, address):
        print("Attempting to retrieve from address " + address)
        sendAddress = bytes.fromhex(address[2:])
        try:
            conn = serial.Serial(self.port, baudrate=self.baudrate, timeout=self.timeout)
            conn.write(bytes([ord('R')]))
            conn.write(sendAddress)
 
            resp = bytes.hex(conn.read(8))
            print("Recieved data from address " + address + ": 0x" + resp)
            conn.close()
            return resp
        except:
            print("ERROR: Could not write to address " + str(sendAddress))

    # Function to load program in a bin file into SRAM
    def program(self, bin):

        lines = []
        counter = 0

        print("Attempting to load program...")
        for line in bin:
                address = line[:8].decode('utf-8')
                data = line[9:].decode('utf-8')
                if data != '':
                    lines.append({'address': address, 'data': data})
                    counter+= 1

        counter *= 4

        try:
            conn = serial.Serial(self.port, baudrate=self.baudrate, timeout=self.timeout)
            conn.write(bytes([ord('P')]))
            conn.write(counter.to_bytes(4, byteorder='big'))

            for line in lines:
                print(line)
                conn.write(bytes.fromhex(line['data']))

            print("Success: Program loaded!")
            
            conn.close()
        except:
            print("ERROR: Could not load program into SRAM")