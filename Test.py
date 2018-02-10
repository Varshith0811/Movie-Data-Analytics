import unittest

from Movie import getRating

class Test(unittest.TestCase):

  def testGetRating(self):
    title = 'Bladerunner'
    self.assertEqual(getRating(title), 8.0, 'Blade Runner's rating should be equal to 8.0')
    
    
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
