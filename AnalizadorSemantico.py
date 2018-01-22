txt = " "
 cont = 0
 def incremetarContador():
 	global cont
 	cont +=1
 	return "%d" %cont
 
 class Nodo():
 	pass
 
 class Null(Nodo):
 	def __init__(self):
 		self.type = 'void'
 
 	def imprimir(self,ident):
 		print ident + "nodo nulo"
 
 	def traducir(self):
 		global txt
 		id = incremetarContador()
 		txt += id+"[label= "+"nodo_nulo"+"]"+"\n\t"
 
 		return id

class program(Nodo):
 	def __init__(self,son1,name):
 		self.name = name
 		self.son1 = son1
 
 	def imprimir(self,ident):
 		self.son1.imprimir(" "+ident)
 
 		print ident + "Nodo: "+self.name
 
 	def traducir(self):
 		global txt
 		id = incremetarContador()
 
 		son1 = self.son1.traducir()
 
 		txt += id +"[label= "+self.name+"]"+"\n\t"
 
 		txt += id +"->"+son1+"\n\t"
 
 		return "digraph G {\n\t"+txt+"}" 

 class block(Nodo):
 	def __init__(self,son1,son2,son3,son4,name):
 		self.name = name
 		self.son1 = son1
 		self.son2 = son2
 		self.son3 = son3
 	#	self.son4 = son4
 
 	def imprimir(self,ident):
 
 		#if str(type(self.son1)) == "<type 'tuple'>":
 		if type(self.son1) == type(tuple()):
 			#print "entro tupla"
 			self.son1[0].imprimir(" "+ident)
 		#elif str(type(self.son1)) == "<type 'instance'>":
 		else:
 			#print "entro instance"
 			self.son1.imprimir(" "+ident)
 
 		#if str(type(self.son2)) == "<type 'tuple'>":
 		if type(self.son2) == type(tuple()):
 			#print "entro tupla"
 			self.son2[0].imprimir(" "+ident)
 		#elif str(type(self.son2)) == "<type 'instance'>":
 		else:
 			#print "entro instance"
 			self.son2.imprimir(" "+ident)
 
 		#if str(type(self.son3)) == "<type 'tuple'>":
 		if type(self.son3) == type(tuple()):
 			#print "entro tupla"
 			self.son3[0].imprimir(" "+ident)
 		#elif str(type(self.son3)) == "<type 'instance'>":
 		else:
 			#print "entro instance"
 			self.son3.imprimir(" "+ident)

    #############################################################
 		#if str(type(self.son4)) == "<type 'tuple'>":
 	#	if type(self.son4) == type(tuple()):
 			#print "entro tupla"
 	#		self.son4[0].imprimir(" "+ident)
 		#elif str(type(self.son4)) == "<type 'instance'>":
 	#	else:
 			#print "entro instance"
 	#		self.son4.imprimir(" "+ident)
 
 
 		print ident + "Nodo: "+self.name
 			
 	def traducir(self):
 		global txt
 		id = incremetarContador()
 
 		if type(self.son1) == type(tuple()):
 			son1 = self.son1[0].traducir()
 		else:
 			son1 = self.son1.traducir()
 
 		if type(self.son2) == type(tuple()):
 			son2 = self.son2[0].traducir()
 		else:
 			son2 = self.son2.traducir()
 
 		if type(self.son3) == type(tuple()):
 			son3 = self.son3[0].traducir()
 		else:
 			son3 = self.son3.traducir()
 
 #		if type(self.son3) == type(tuple()):
 #			son4 = self.son4[0].traducir()
 #		else:
 #			son4 = self.son4.traducir()
 
 		txt += id + "[label= "+self.name+"]"+"\n\t"
 		txt += id + " -> " + son1 + "\n\t"
 		txt += id + " -> " + son2 + "\n\t"
 		txt += id + " -> " + son3 + "\n\t"
 #		txt += id + " -> " + son4 + "\n\t"
 
 		return id

class varDecl1(Nodo):
 	def __init__(self,son1,son2,son3,name):
 		self.name = name
 		self.son1 = son1
 		self.son2 = son2
 		self.son3 = son3
 	#	self.son4 = son4
 
 	def imprimir(self,ident):
 		self.son1.imprimir(" "+ident)
 		self.son2.imprimir(" "+ident)
 		self.son3.imprimir(" "+ident)
 	#	self.son4.imprimir(" "+ident)
 
 		print ident + "Nodo: "+self.name
 			
 	def traducir(self):
 		global txt
 		id = incremetarContador()
 
 		son1 = self.son1.traducir()
 		son2 = self.son2.traducir()
 		son3 = self.son3.traducir()
 	#	son4 = self.son4.traducir()
 
 		txt += id + "[label= "+self.name+"]"+"\n\t"
 		txt += id + " -> " + son1 + "\n\t"
 		txt += id + " -> " + son2 + "\n\t"
 		txt += id + " -> " + son3 + "\n\t"
 	#	txt += id + " -> " + son4 + "\n\t"
 
 		return id

         
class varDecl2(Nodo):
 	def __init__(self,son1,son2,name):
 		self.name = name
 		self.son1 = son1
 		self.son2 = son2
 	#	self.son3 = son3
 	#	self.son4 = son4
 
 	def imprimir(self,ident):
 		self.son1.imprimir(" "+ident)
 		self.son2.imprimir(" "+ident)
 	#	self.son3.imprimir(" "+ident)
 	#	self.son4.imprimir(" "+ident)
 
 		print ident + "Nodo: "+self.name
 			
 	def traducir(self):
 		global txt
 		id = incremetarContador()
 
 		son1 = self.son1.traducir()
 		son2 = self.son2.traducir()
 	#	son3 = self.son3.traducir()
 	#	son4 = self.son4.traducir()
 
 		txt += id + "[label= "+self.name+"]"+"\n\t"
 		txt += id + " -> " + son1 + "\n\t"
 		txt += id + " -> " + son2 + "\n\t"
 	#	txt += id + " -> " + son3 + "\n\t"
 	#	txt += id + " -> " + son4 + "\n\t"
 
 		return id

   class p_varDeclSen1(Nodo):
 	def __init__(self,son1,son2,son3,son4,son5,name):
 		self.name = name
 		self.son1 = son1
 		self.son2 = son2
 	#	self.son3 = son3
 	#	self.son4 = son4
 
 	def imprimir(self,ident):
 		self.son1.imprimir(" "+ident)
 		self.son2.imprimir(" "+ident)
 	#	self.son3.imprimir(" "+ident)
 	#	self.son4.imprimir(" "+ident)
 
 		print ident + "Nodo: "+self.name
 			
 	def traducir(self):
 		global txt
 		id = incremetarContador()
 
 		son1 = self.son1.traducir()
 		son2 = self.son2.traducir()
 		son3 = self.son3.traducir()
 		son4 = self.son4.traducir()
 		son5 = self.son4.traducir()
 
 		txt += id + "[label= "+self.name+"]"+"\n\t"
 		txt += id + " -> " + son1 + "\n\t"
 		txt += id + " -> " + son2 + "\n\t"
 		txt += id + " -> " + son3 + "\n\t"
 		txt += id + " -> " + son4 + "\n\t"
 		txt += id + " -> " + son5 + "\n\t"

 		return id
 
      
class varDeclSen2(Nodo):
 	def __init__(self,son1, name):
 		self.name = name
 		self.son1 = son1
 
 	def imprimir(self,ident):
 		self.son1.imprimir(" "+ident)
 
 		print ident + "Nodo: "+self.name
 			
 	def traducir(self):
 		global txt
 		id = incremetarContador()
 
 		son1 = self.son1.traducir()
 
 		txt += id + "[label= "+self.name+"]"+"\n\t"
 		txt += id + " -> " + son1 + "\n\t"
 
 		return id


 class p_J1(Nodo):
 	def __init__(self,son1,son2,name):
 		self.name = name
 		self.son1 = son1
 		self.son2 = son2
 #		self.son3 = son3
 #		self.son4 = son4
 
 	def imprimir(self,ident):
 		self.son1.imprimir(" "+ident)
 		self.son2.imprimir(" "+ident)
 #		self.son3.imprimir(" "+ident)
 #		self.son4.imprimir(" "+ident)
 
 		print ident + "Nodo: "+self.name
 			
 	def traducir(self):
 		global txt
 		id = incremetarContador()
 
 		son1 = self.son1.traducir()
 		son2 = self.son2.traducir()
 #		son3 = self.son3.traducir()
 #		son4 = self.son4.traducir()
 
 		txt += id + "[label= "+self.name+"]"+"\n\t"
 		txt += id + " -> " + son1 + "\n\t"
 		txt += id + " -> " + son2 + "\n\t"
 #		txt += id + " -> " + son3 + "\n\t"
 #		txt += id + " -> " + son4 + "\n\t"
 
 		return id

 class decfun1(Nodo):
 	def __init__(self,son1,son2,son3,son4,son5,son6,son7,son8,son9,name):
 		self.name = name
 		self.son1 = son1
 		self.son2 = son2
 		self.son3 = son3
 		self.son4 = son4
        self.son5 = son5
 		self.son6 = son6
 		self.son7 = son7
 		self.son8 = son8 
 		self.son9 = son9 
 
 	def imprimir(self,ident):
 		self.son1.imprimir(" "+ident)
 		self.son2.imprimir(" "+ident)
 		self.son3.imprimir(" "+ident)
 		self.son4.imprimir(" "+ident)
        self.son5.imprimir(" "+ident)
 		self.son6.imprimir(" "+ident)
 		self.son7.imprimir(" "+ident)
 		self.son8.imprimir(" "+ident) 
 		self.son9.imprimir(" "+ident) 
 
 		print ident + "Nodo: "+self.name
 			
 	def traducir(self):
 		global txt
 		id = incremetarContador()
 
 		son1 = self.son1.traducir()
 		son2 = self.son2.traducir()
 		son3 = self.son3.traducir()
 		son4 = self.son4.traducir()
        son5 = self.son5.traducir()
 		son6 = self.son6.traducir()
 		son7 = self.son7.traducir()
 		son8 = self.son8.traducir()  
 
 		txt += id + "[label= "+self.name+"]"+"\n\t"
 		txt += id + " -> " + son1 + "\n\t"
 		txt += id + " -> " + son2 + "\n\t"
 		txt += id + " -> " + son3 + "\n\t"
 		txt += id + " -> " + son4 + "\n\t"
     #   txt += id + "[label= "+self.name+"]"+"\n\t"
 		txt += id + " -> " + son5 + "\n\t"
 		txt += id + " -> " + son6 + "\n\t"
 		txt += id + " -> " + son7 + "\n\t"
 		txt += id + " -> " + son8 + "\n\t" 
 		txt += id + " -> " + son9 + "\n\t" 
 
 		return id        


class decTipos1(Nodo):
 	def __init__(self,son1,name):
 		self.name = name
 		self.son1 = son1
 
 	def imprimir(self,ident):
 		#self.son1.imprimir(" "+ident)
 
 		self.son1.imprimir(" "+ident)
 
 		# if type(self.son1) == type(tuple()):
 		# 	self.son1[0].imprimir(" "+ident)
 		# else:
 		# 	self.son1.imprimir(" "+ident)
 
 		print ident + "Nodo: "+self.name
 
 	def traducir(self):
 		global txt
 		id = incremetarContador()
 
 		if type(self.son1) == type(tuple()):
 			son1 = self.son1[0].traducir()
 		else:
 			son1 = self.son1.traducir()
 
 		#son1 = self.son1.traducir()
 
 		txt += id +"[label= "+self.name+"]"+"\n\t"
 		txt += id +"->"+son1+"\n\t"
 
 		return id


class decT1(Nodo):
 	def __init__(self,son1,name):
 		self.name = name
 		self.son1 = son1
 
 	def imprimir(self,ident):
 		#self.son1.imprimir(" "+ident)
 
 		self.son1.imprimir(" "+ident)
 
 		# if type(self.son1) == type(tuple()):
 		# 	self.son1[0].imprimir(" "+ident)
 		# else:
 		# 	self.son1.imprimir(" "+ident)
 
 		print ident + "Nodo: "+self.name
 
 	def traducir(self):
 		global txt
 		id = incremetarContador()
 
 		if type(self.son1) == type(tuple()):
 			son1 = self.son1[0].traducir()
 		else:
 			son1 = self.son1.traducir()
 
 		#son1 = self.son1.traducir()
 
 		txt += id +"[label= "+self.name+"]"+"\n\t"
 		txt += id +"->"+son1+"\n\t"
 
 		return id


class decT2(Nodo):
 	def __init__(self,son1,name):
 		self.name = name
 		self.son1 = son1
 
 	def imprimir(self,ident):
 		#self.son1.imprimir(" "+ident)
 
 		self.son1.imprimir(" "+ident)
 
 		# if type(self.son1) == type(tuple()):
 		# 	self.son1[0].imprimir(" "+ident)
 		# else:
 		# 	self.son1.imprimir(" "+ident)
 
 		print ident + "Nodo: "+self.name
 
 	def traducir(self):
 		global txt
 		id = incremetarContador()
 
 		if type(self.son1) == type(tuple()):
 			son1 = self.son1[0].traducir()
 		else:
 			son1 = self.son1.traducir()
 
 		#son1 = self.son1.traducir()
 
 		txt += id +"[label= "+self.name+"]"+"\n\t"
 		txt += id +"->"+son1+"\n\t"
 
 		return id



class decT3(Nodo):
 	def __init__(self,son1,name):
 		self.name = name
 		self.son1 = son1
 
 	def imprimir(self,ident):
 		#self.son1.imprimir(" "+ident)
 
 		self.son1.imprimir(" "+ident)
 
 		# if type(self.son1) == type(tuple()):
 		# 	self.son1[0].imprimir(" "+ident)
 		# else:
 		# 	self.son1.imprimir(" "+ident)
 
 		print ident + "Nodo: "+self.name
 
 	def traducir(self):
 		global txt
 		id = incremetarContador()
 
 		if type(self.son1) == type(tuple()):
 			son1 = self.son1[0].traducir()
 		else:
 			son1 = self.son1.traducir()
 
 		#son1 = self.son1.traducir()
 
 		txt += id +"[label= "+self.name+"]"+"\n\t"
 		txt += id +"->"+son1+"\n\t"
 
 		return id


class Sprima1(Nodo):
 	def __init__(self,son1,son2,son3,son4,name):
 		self.name = name
 		self.son1 = son1
 		self.son2 = son2
 		self.son3 = son3
 		self.son4 = son4
 
 	def imprimir(self,ident):
 
 		#if str(type(self.son1)) == "<type 'tuple'>":
 		if type(self.son1) == type(tuple()):
 			#print "entro tupla"
 			self.son1[0].imprimir(" "+ident)
 		#elif str(type(self.son1)) == "<type 'instance'>":
 		else:
 			#print "entro instance"
 			self.son1.imprimir(" "+ident)
 
 		#if str(type(self.son2)) == "<type 'tuple'>":
 		if type(self.son2) == type(tuple()):
 			#print "entro tupla"
 			self.son2[0].imprimir(" "+ident)
 		#elif str(type(self.son2)) == "<type 'instance'>":
 		else:
 			#print "entro instance"
 			self.son2.imprimir(" "+ident)
 
 		#if str(type(self.son3)) == "<type 'tuple'>":
 		if type(self.son3) == type(tuple()):
 			#print "entro tupla"
 			self.son3[0].imprimir(" "+ident)
 		#elif str(type(self.son3)) == "<type 'instance'>":
 		else:
 			#print "entro instance"
 			self.son3.imprimir(" "+ident)
 
 		#if str(type(self.son4)) == "<type 'tuple'>":
 		if type(self.son4) == type(tuple()):
 			#print "entro tupla"
 			self.son4[0].imprimir(" "+ident)
 		#elif str(type(self.son4)) == "<type 'instance'>":
 		else:
 			#print "entro instance"
 			self.son4.imprimir(" "+ident)
 
 
 		print ident + "Nodo: "+self.name
 			
 	def traducir(self):
 		global txt
 		id = incremetarContador()
 
 		if type(self.son1) == type(tuple()):
 			son1 = self.son1[0].traducir()
 		else:
 			son1 = self.son1.traducir()
 
 		if type(self.son2) == type(tuple()):
 			son2 = self.son2[0].traducir()
 		else:
 			son2 = self.son2.traducir()
 
 		if type(self.son3) == type(tuple()):
 			son3 = self.son3[0].traducir()
 		else:
 			son3 = self.son3.traducir()
 
 		if type(self.son3) == type(tuple()):
 			son4 = self.son4[0].traducir()
 		else:
 			son4 = self.son4.traducir()
 
 		txt += id + "[label= "+self.name+"]"+"\n\t"
 		txt += id + " -> " + son1 + "\n\t"
 		txt += id + " -> " + son2 + "\n\t"
 		txt += id + " -> " + son3 + "\n\t"
 		txt += id + " -> " + son4 + "\n\t"
 
 		return id
 