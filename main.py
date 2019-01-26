import argparse
from pull_account_data import AccountData
from account_traffic_report import AccountTrafficReport

bold_red = '\x1b[1;31;40m'
bold_green = '\x1b[1;32;40m'
bold_blue = '\x1b[1;34;40m'
reset_text = '\x1b[0m'

def print_to_screen(account, url='https://branden-account-api.herokuapp.com/traffic/api/v1/'):

	traffic_report = AccountData(account, url)
	
	print(bold_red + 'Account: {}'.format(traffic_report.account_name) + reset_text)
	print('----------------')
	print(bold_green + 'Average Score: {}'.format(traffic_report.account_average) + reset_text)
	print(bold_green + 'Highest Score: {} - Number of days with this score: {}'.format(traffic_report.account_high[0], traffic_report.account_high[1]) + reset_text)
	print(bold_green + 'Lowest Score: {} - Number of days with this score: {}'.format(traffic_report.account_low[0], traffic_report.account_low[1]) + reset_text)
	print('----------------')
	print(bold_blue + 'Recommendation:' + reset_text)
	for key, value in traffic_report.account_recommendation.items():
		print(bold_blue + 'Based on {}: {}'.format(key, value[0]) + reset_text)

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Pull account traffic report')
	parser.add_argument('--account', '-a',
						help='Account name to pull traffic for')
	args = parser.parse_args()

	print_to_screen(args.account, 'http://0.0.0.0:8080/traffic/api/v1/')
