import serial.tools.list_ports
import serial
import time

plist = serial.tools.list_ports.comports()
serial_name = plist[0][0]
ser = serial.Serial("COM4",115200,timeout=1)
ser.reset_output_buffer()
ser.reset_input_buffer()
cmd='at+cmgs="15011552375"'
cmd1="AT"
wn=ser.write((cmd+"\r\n").encode('utf-8'))
time.sleep(1)
rn=ser.read(ser.in_waiting).decode('utf-8').strip().split("\r\n")

#str=""
#fl=str.join(rn).upper().startswith("AT")
#print(fl)
print(rn)
print("端口",ser.name,"总共发送",wn,"字节")
print("端口",ser.name,"总共接收",len(rn),"字节")
ser.close()





