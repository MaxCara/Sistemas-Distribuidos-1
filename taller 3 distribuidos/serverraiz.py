import SocketServer
import math

def op(numero1, numero2):
	raiz=1/float(numero1)
		#print raiz
	return pow(numero2, raiz)

class mihandler(SocketServer.BaseRequestHandler):
	"""docstring for mihandler"""
	def handle(self):		
		self.operacion = self.request.recv(1024).split("@")
		print self.operacion	
		self.numero1 = int(self.operacion[0])
		self.numero2 = int(self.operacion[1])
		self.operan = str(op(self.numero1, self.numero2))
		print "los numeros recibidos son: ", self.numero1, " y ",self.numero2, " y el resultado de la operacion es: ", self.operan
		self.request.send(self.operan)

def main():
	host= "localhost"
	puerto = 9996 

	server1= SocketServer.TCPServer((host, puerto), mihandler)
	print "server6 corriendo"
	server1.serve_forever()

main() 