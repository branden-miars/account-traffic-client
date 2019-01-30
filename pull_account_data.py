import requests
import os
from account_traffic_report import AccountTrafficReport

class AccountData(AccountTrafficReport):
	"""Obtains account json data from API and inherits the traffic report data that 
	account_traffic_report generates. 

		Args: 
			account_name: name of the account to perform the API request for
			url: the url of the API to make the request to(optional for local testing)

	"""

	def __init__(self, account_name, url='https://branden-account-api.herokuapp.com/traffic/api/v1/'): 

		self.account_name = account_name
		self.url = url
		self.request_data = self.get_account_data()
		self.account_data = self.convert_data_to_list()
		AccountTrafficReport.__init__(self, self.account_data)

	def get_account_data(self):
		"""Make request to API for json account data

			Args:
				url: the url of the API to make the request to(optional for local testing)
		"""
		key = os.environ.get('ACCOUNT_API_SECRET')
		if key == None or key == '':
			raise Exception('Secret key not set')
		
		account_data = requests.get(self.url+self.account_name, headers={'Authorization': key})
		if account_data == None or account_data == '':
			raise Exception('API call failed. No data returned')
		return account_data.json()
		

	def convert_data_to_list(self):
		"""Converts portion of json data to list for processing

			Args:
				request_data: json data from API
		"""
		return [int(score) for score in self.request_data['account_traffic'].split(',')]