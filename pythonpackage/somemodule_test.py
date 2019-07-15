import unittest
import importlib
import pythonpackage.somemodule as somemodule

class SomeModuleTests(unittest.TestCase): 

    def test_invoke_returns_qpis(self):
        result = somemodule.invoke()
        self.assertTrue(True)

    
if __name__ == '__main__':
    unittest.main()