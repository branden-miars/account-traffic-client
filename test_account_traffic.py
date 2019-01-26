import unittest
from parameterized import parameterized 
from account_traffic_report import AccountTrafficReport


class TestAccountTraffic(unittest.TestCase):

	test_object_1 = AccountTrafficReport([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
	test_object_2 = AccountTrafficReport([5, 12, 20, 2])
	test_object_3 = AccountTrafficReport([1, 100])
	
	@parameterized.expand([
	('All the same', test_object_1.account_average, 5),
	('Small data set', test_object_2.account_average, 9.75),
	('Large gap', test_object_3.account_average, 50.5),
	])
	def test_account_average(self, _, account_average, expected_average):
		self.assertEqual(account_average, expected_average)

	@parameterized.expand([
	('All the same', test_object_1.account_high, 5, 10),
	('Small data set', test_object_2.account_high, 20, 1),
	('Large gap', test_object_3.account_high, 100, 1),
	])
	def test_get_highest_of_data(self, _, account_high, expected_high, expected_count):
		self.assertEqual(account_high[0], expected_high)
		self.assertEqual(account_high[1], expected_count)

	@parameterized.expand([
	('All the same', test_object_1.account_low, 5, 10),
	('Small data set', test_object_2.account_low, 2, 1),
	('Large gap', test_object_3.account_low, 1, 1),
	])
	def test_get_lowest_of_data(self, _, account_low, expected_low, expected_count):
		self.assertEqual(account_low[0], expected_low)
		self.assertEqual(account_low[1], expected_count)
	