from bluepy import btle 

MAX_VIBE = 20
DEVICE = "<your device address>" # can use your bluetooth manager to look this up 
UUID = "<device's UUID>" # can use `for characteristic in peripheral.getCharacteristics: print(characteristic)` to look this up

# can't always initially connect, especially if the device is off
peripheral = None
while True:
    try:
        peripheral = btle.Peripheral(DEVICE, "random")
        break
    except:
        pass
    
characteristic = peripheral.getCharacteristics(uuid = btle.UUID(UUID))[0]

def vibe(level):
    characteristic.write(f'Vibrate:{level}'.encode('ascii'))
        
def stop():
    vibe(0)

