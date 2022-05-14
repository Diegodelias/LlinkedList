


class LinkedList :
    def __init__(self,numero):
        self.head = { 'numero' : numero, 'link' : None}
        self.tail = self.head
        self.largoLinkedList = 1

    def agregarFinal(self,num):
       # recorrer linkedList  mientras link != None:
       #cuando sea igual None
       nodoNuevo = {'numero' : num , 'link' : None}
       self.tail['link'] = nodoNuevo
       self.tail = nodoNuevo
       self.largoLinkedList = self.largoLinkedList + 1
       return self

    def agregarInicio(self,num):    
         nodoNuevo = {'numero' : num , 'link' : None}
         nodoNuevo['link'] = self.head
         self.head = nodoNuevo
         self.largoLinkedList = self.largoLinkedList + 1
         return self






linkedList = LinkedList(3)
linkedList.agregarFinal(20)
linkedList.agregarInicio(55)

print(linkedList.head)
print(linkedList.tail)