import socket
import threading
import time


def connect(port):
    """Cria a conexao TCP"""

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', port))
        print('conexao TCP estabelecida')
        return s
    except:
        print('falhou em fazer o a conexao TCP como cliente')
        return 0
        # self.terminate()
    else:
        print('continuando')


def get_state_reward(s, act):
    """Da o estado e a recompensa que o agente recebeu"""

    s.send(str(act).encode())
    data = ''
    data_recv = False
    while not data_recv:
        data = s.recv(1024).decode()
        try:
            data = eval(data)
            data_recv = True
        except:
            data_recv = False

    # convert the data to decimal int
    estado = data['estado']
    recompensa = data['recompensa']

    return estado, recompensa
