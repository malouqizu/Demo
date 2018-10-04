import serial.tools.list_ports
import serial
import time

plist = serial.tools.list_ports.comports()
if len(plist)>0:
    serial_name = plist[0][0]
    ser = serial.Serial(serial_name,921600,timeout=0.5)
    print("可用端口：",ser.name)
    #ser.flushInput()
    #ser.flushOutput()
    ser.reset_output_buffer()
    ser.reset_input_buffer()
    wn=ser.write("AT+H\n".encode('utf-8'))
    print("发送",wn,"字节")
    for i in range(0,10):
        size1=ser.in_waiting
        if size1 > 0:
            print(size1)
            rn = ser.read(size1).decode('utf-8')
            print(rn)
            ser.close()
            break
        time.sleep(1)
        print(i)
    else:
        print("没有接收到任何内容！")
else:
    print("没有发现任何端口！")


