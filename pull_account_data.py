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

	def __init__(self, account_name, 
		url='https://branden-account-api.herokuapp.com/traffic/api/v1/'):
		"""Constructor for AccountData, sets name, obtains scores, and inherits 
		traffic report data"""

		self.account_name = account_name
		self.request_data = self.get_account_data(url+'{}'.format(account_name))
		self.account_data = self.convert_data_to_list(self.request_data)
		AccountTrafficReport.__init__(self, self.account_data)

	def get_account_data(self, url):
		"""Make request to API for json account data

			Args:
				url: the url of the API to make the request to(optional for local testing)
		"""
		key = os.environ.get('ACCOUNT_API_SECRET')
		account_data = requests.get(url, headers={'Authorization': key})
		return account_data.json()

	def convert_data_to_list(self, request_data):
		"""Converts portion of json data to list for processing

			Args:
				request_data: json data from API
		"""
		return [int(score) for score in request_data['account_traffic'].split(',')]