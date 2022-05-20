


class LinkedList :
    def __init__(self,numero):
        self.head = { 'numero' : numero, 'link' : None}
        self.tail = self.head
        self.largoLinkedList = 1

    def agregarFinal(self,num):
 
        nodoNuevo = {'numero' : num , 'link' : None}
        if self.head is None:
            self.head = nodoNuevo
            return
        nodo = self.head
        while nodo['link'] is not None:
            nodo = nodo['link']
        nodo['link'] = nodoNuevo



    def agregarInicio(self,num):    
       
        nodoNuevo = {'numero' : num , 'link' : None}
        nodoNuevo['link'] = self.head
        self.head = nodoNuevo




 

    def buscar(self,num):
        contador = 0
        res = False
        nodoActual = self.head
        while (nodoActual is not None ): 
            if  num == nodoActual['numero']:
                res =  True
            nodoActual = nodoActual['link']
            contador = contador + 1

        return res
           
        
             

        

    def Listar(self):
        contador = 0
        lista = []
        nodoActual = self.head
   
        while (nodoActual is not None ):
           
            lista.append(nodoActual['numero'])
            nodoActual = nodoActual['link']
            contador = contador + 1

        return lista


    def borrar(self,num):
      
        if self.head is None:
            print("lista vacia")
            return
        #borrar primer nodo
        if self.head['numero'] == num:
            self.head = self.head['link']
            return
        #borrar nodo intermedio o al final
        nodo = self.head
        while nodo['link'] is not None:

            if nodo['link']['numero'] == num:
               
                 break
               
            nodo = nodo['link']     
           
           
     
        if nodo['link'] is None:
            print("El numero ", num ,"no está en la lista")
        else:
           
            nodo['link'] = nodo['link']['link']



    


