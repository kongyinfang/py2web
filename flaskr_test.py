# -*- coding: utf-8 -*-

import os
import unittest
import tempfile
import flaskr

class FlaskrTestCase(unittest.TestCase):

	def setUp(self):
		self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
		flaskr.app.config['TESTING'] = True
		self.app = flaskr.app.test_client()
		flaskr.init_db()

	def tearDown(self):
		os.close(self.db_fd)
		os.unlink(flaskr.DATABASE)
		# os.unlink(flaskr.app.config['DATABASE'])

	def test_empty_db(self):
		rv = self.app.get('/')
		assert 'No entries here so far' in rv.data


if __name__ == '__main__':
	unittest.main()




# import os
# import unittest
# import tempfile
# import flaskr

# class FlaskrTestCase(unittest.TestCase):

# 	def setUp(self):
# 		self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
# 		# flaskr.app.config['TESTING'] = True
# 		self.app = flaskr.app.test_client()
# 		flaskr.init_db()

# 	def tearDown(self):
# 		os.close(self.db_fd)
# 		os.unlink(flaskr.DATABASE)

# 	def test_empty_db(self):
# 		rv = self.app.get('/')
# 		assert 'No entries here so far ' in rv.data

# if __name__ == '__main__':
# 	unittest.main()