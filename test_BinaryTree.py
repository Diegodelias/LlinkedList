import unittest

from BinaryTree import *


class TestBinaryTree(unittest.TestCase):

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