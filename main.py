import argparse
from pull_account_data import AccountData

bold_red = '\x1b[1;31;40m'
bold_green = '\x1b[1;32;40m'
bold_blue = '\x1b[1;34;40m'
reset_text = '\x1b[0m'

def print_to_screen(account_object):
	"""Handles the formatting and printing output to terminal

		Args:
			account_object: Object containing the traffic report data for printing"""
	
	
	print(bold_red + 'Account: {}'.format(account_object.account_name) + reset_text)
	print('----------------')
	print(bold_green + 'Average Score: {}'.format(account_object.account_average) + reset_text)
	print(bold_green + 'Highest Score: {} - Number of days with this score: {}'.format(account_object.account_high[0], account_object.account_high[1]) + reset_text)
	print(bold_green + 'Lowest Score: {} - Number of days with this score: {}'.format(account_object.account_low[0], account_object.account_low[1]) + reset_text)
	print('----------------')
	print(bold_blue + 'Recommendation:' + reset_text)
	for key, value in account_object.account_recommendation.items():
		print(bold_blue + 'Based on {}: {}'.format(key, value[0]) + reset_text)

if __name__ == '__main__':
	"""Parses arugments to create the AccountData object, containing traffic data
	and the plan level recommendations"""

	parser = argparse.ArgumentParser(description='Pull account traffic report')
	parser.add_argument('--account', '-a',
						help='Account name to pull traffic for')
	parser.add_argument('--url', '-u',
						default='https://branden-account-api.herokuapp.com/traffic/api/v1/',
						help='Enter API URL to make request to')
	args = parser.parse_args()
	AccountData = AccountData(args.account, args.url)
	print_to_screen(AccountData)
