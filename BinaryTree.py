


class Nodo:
    def __init__(self,num):
        self.derecha = None
        self.izquierda= None
        self.numero = num


class BinaryTree:
    def __init__(self):
        self.raiz = None


    def insertar(self,num):
       
        Nodo_actual = self.raiz
        nodoPadre = None
        while  Nodo_actual is not None:
            nodoPadre =  Nodo_actual
            if num <  Nodo_actual.numero :
                 Nodo_actual =  Nodo_actual.izquierda
            elif num >  Nodo_actual.numero:
                 Nodo_actual =  Nodo_actual.derecha
            else:
                print(num , "ya existe en el arbol")
                return
        temp = Nodo(num)

        if nodoPadre == None:
            self.raiz = temp
        elif num < nodoPadre.numero: 
            nodoPadre.izquierda = temp
        else:
            nodoPadre.derecha = temp
        



    def buscar(self,num):
        actual = self.raiz
        while actual is not None:
            if  num < actual.numero:
                actual = actual.izquierda
            elif num > actual.numero:
                actual = actual.derecha
            else:
                return True
        return False

    def borrar(self,num):
        nodo = self.raiz
        nodoPadre= None
        #buscar nodo que contenga numero a borrar
        # al terminar ciclo nodo hara referecia al nodo que contenga el numero a borrar
        #al terminar ciclo nodoPadre hará referecia al nodo padre del nodo que tenga el numero a borrar
        while nodo is not None:
            if num == nodo.numero:
                break
            nodoPadre = nodo

            if num < nodo.numero:
                nodo = nodo.izquierda
            else:
                nodo = nodo.derecha
        #si el numero no se encuentra 
        if nodo == None:
            print(num , " no fue encontrado")

     #nodo padre con  2 hijos buscar sucesor que le siga en orden al numero a borrar para ponerlo en lugar del numero que se borra
        if nodo.izquierda is not None and nodo.derecha is not None:
            nodoPadre_reemplazo = nodo

            #rama derecha del nodo
            nodo_reemplazo = nodo.derecha
            
            #iterar sobre lado izquierdo (con origen rama derecha del nodo) hasta encontrar nodo que no tenga nada a la izquierda
            while nodo_reemplazo.izquierda is not None:
                nodoPadre_reemplazo = nodo_reemplazo
                nodo_reemplazo = nodo_reemplazo.izquierda
            #copiar info del sucesor enconctrado   
            nodo.numero = nodo_reemplazo.numero
            #borrar sucesor
            nodo = nodo_reemplazo
            nodoPadre =  nodoPadre_reemplazo
    # 1 o ninfun hijo
        if nodo.izquierda is not None: #nodo a borrar tiene nhijo rama izquierda
            nodo_hijo = nodo.izquierda
        else:
            nodo_hijo = nodo.derecha

        if nodoPadre == None: #nodo a borrar es nodo raiz
            self.raiz = nodo_hijo
        elif nodo == nodoPadre.izquierda:
            nodoPadre.izquierda = nodo_hijo
        else:
            nodoPadre.derecha = nodo_hijo


 


    def listar(self):
        self._listar(self.raiz,0,10)


    def _listar(self,raiz,espacio,altura):
   
        if raiz is None:
            return
        #incremetnear distancia entere los nieveles
        espacio += altura

        #listar rama derecha primero
        self._listar(raiz.derecha,espacio, altura)
        print()

        #imprimir el nodo actual 
        for i in range(altura,espacio):
            print(' ', end='')

        print(raiz.numero, end='')

        #listar  izquierda
        print()
        self._listar(raiz.izquierda,espacio,altura)





        
   





                    


                     



        


   



tree = BinaryTree()
tree.insertar(13)
tree.insertar(3)
tree.insertar(14)
tree.insertar(18)
tree.insertar(1)
tree.insertar(4)

tree.listar()

print("------------------------------------------")


tree.borrar(4)
# tree.borrar(3)
tree.listar()
print(tree.buscar(34))



print("------------------------------------------")

tree.borrar(14)
# tree.borrar(3)
tree.listar()


