import bluetooth

name="bt_server"
target_name="siggen"
uuid="00001101-0000-1000-8000-00805F9B34FB"

def runServer():
serverSocket=bluetooth.BluetoothSocket(bluetooth.RFCOMM )
    port=bluetooth.PORT_ANY
    serverSocket.bind(("",port))
    print "Listening for connections on port: ", port   
    serverSocket.listen(1)
    port=serverSocket.getsockname()[1]
    inputSocket, address=serverSocket.accept()
    print "Got connection with" , address
    data=inputSocket.recv("1024")
    print "received [%s] \n " % data    
    inputSocket.close()
    serverSocket.close()  

runServer()  