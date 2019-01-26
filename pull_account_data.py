import requests
from account_traffic_report import AccountTrafficReport

class AccountData(AccountTrafficReport):

	def __init__(self, account_name, url='https://branden-account-api.herokuapp.com/traffic/api/v1/'):
		
		self.account_name = account_name
		self.request_data = self.get_account_data(url+'{}'.format(account_name))
		self.account_data = self.convert_data_to_list(self.request_data)
		AccountTrafficReport.__init__(self, self.account_data)

	def get_account_data(self, url):
		account_data = requests.get(url, headers={'Authorization': 'PXU04DAKncJXL85WpkNVXkT49PsbyL4i'})
		return account_data.json()

	def convert_data_to_list(self, request_data):
		return [int(score) for score in request_data['account_traffic'].split(',')]