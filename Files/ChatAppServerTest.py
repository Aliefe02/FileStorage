import logging
from numpysocket import NumpySocket
import sounddevice as sd
import threading

logger = logging.getLogger('simple server')
logger.setLevel(logging.INFO)

HEADER = 64
PORT = 4321
SERVER = 'localhost' #socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

fs=44100
duration = 5 # seconds

s = NumpySocket()
s.bind(ADDR)
s.listen()
print("Listening on localhost...")
conn, addr = s.accept()
print("Connected")
def recv():
    while True:
        data = conn.recv()
        print("Recieved")
        sd.play(data, fs)
        sd.wait()

def send(data):
    conn.sendall(data)

def RecordSound():
    try:
        while True:
            myrecording = sd.rec(duration * fs, samplerate=fs, channels=2, dtype='float64')  
            sd.wait()
            #conn.sendall(myrecording)
            sendVoice = threading.Thread(target=send,args=[myrecording])
            sendVoice.start()
    except KeyboardInterrupt:
        print("Record Stopped!")

recorder = threading.Thread(target=RecordSound,args=())
recorder.start()

receiver = threading.Thread(target=recv,args=())
receiver.start()
