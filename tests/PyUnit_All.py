#load all tests and run them all.
#for the time being, need to invoke the set_environment script
#to set up data base informations.
import unittest
loader = unittest.TestLoader()
mods = loader.discover('.',pattern='*test*.py',top_level_dir=None)
suite = unittest.TestSuite(mods)
print suite 
runner = unittest.TextTestRunner()
runner.run(suite)
