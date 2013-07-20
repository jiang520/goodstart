


import unittest

def add(a, b):
    return a+b
class func_add_testcase(unittest.TestCase):
    def testadd(self):
        self.assertEqual(3, add(1, 2), add(1, 2))
        self.assertEqual(-10, add(-4, -6))
        self.assertEqual(0, add(-4, 4), "msg")
                         
                         
                         
if __name__ == "__main__":
    suite=unittest.TestSuite()
    suite.addTest(func_add_testcase("testadd"))
    
    runner = unittest.TextTestRunner()
    runner.run(suite); 