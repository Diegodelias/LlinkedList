import unittest

from BinaryTree import *


class TestBinaryTree(unittest.TestCase):
    
    # def test_agregar_nodo_inicial(self):
    #     l = LinkedList(3)
    #     self.assertEqual(l.Listar(),[3])
     
    # def test_agregar_nodo_Inicio_lista(self):
    #     l = LinkedList(3)
    #     l.agregarInicio(17)
    #     self.assertEqual(l.Listar(),[17,3])

    
    # def test_agregar_nodo_Final_lista(self):
    #     l = LinkedList(3)
    #     l.agregarInicio(17)
    #     l.agregarFinal(7)
    #     l.agregarFinal(47)
    #     self.assertEqual(l.Listar(),[17,3,7,47])

     
    # def test_borrarNodo(self):
    #     l = LinkedList(3)
    #     l.agregarInicio(17)
    #     l.agregarFinal(7)
    #     l.agregarFinal(47)
    #     l.borrar(47)
    #     self.assertEqual(l.Listar(),[17,3,7])
    #     l.borrar(3)
    #     self.assertEqual(l.Listar(),[17,7])

     
    # def test_buscar_numero(self):
    #     l = LinkedList(3)
    #     l.agregarInicio(17)
    #     l.agregarFinal(7)
    #     l.agregarFinal(47)
    #     self.assertEqual(l.buscar(17),True)
    #     self.assertEqual(l.buscar(3),True)
    #     self.assertEqual(l.buscar(7),True)
    #     self.assertEqual(l.buscar(47),True)
    #     self.assertEqual(l.buscar(147),False)
    #     self.assertEqual(l.buscar(500),False)
    #     self.assertEqual(l.buscar(67),False)
    #     self.assertEqual(l.buscar(181),False)

    def test_buscar_numero(self):

        t = BinaryTree()
        t.insertar(12)
        t.insertar(15)
        t.insertar(18)
        t.insertar(4)
        t.insertar(9)
        t.insertar(34)
        t.insertar(52)
        self.assertEqual(t.buscar(12),True)
        self.assertEqual(t.buscar(18),True)
        self.assertEqual(t.buscar(34),True)
        self.assertEqual(t.buscar(52),True)
        self.assertEqual(t.buscar(4),True)
        self.assertEqual(t.buscar(181),False)
        self.assertEqual(t.buscar(2),False)
        self.assertEqual(t.buscar(105),False)
  



if __name__ == '__main__':
    unittest.main()