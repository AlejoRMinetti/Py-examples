import unittest

def es_mayor_de_edad(edad):
    if edad >=18:
        return False
    else:
        return False


class CajaCristalTest(unittest.TestCase):
    def test_es_mayor(self):
        edad = 20

        result = es_mayor_de_edad(edad)
        
        self.assertEqual(result,True)
    
    def test_es_menor(self):
        edad = 15

        result = es_mayor_de_edad(edad)
        
        self.assertEqual(result,False)
    
        
    
if __name__ == '__main__':
    unittest.main()