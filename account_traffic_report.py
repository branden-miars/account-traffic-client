
class AccountTrafficReport:

	def __init__(self, account_data):
		self.account_data = account_data
		self.account_average = self.get_average_of_data(self.account_data)
		self.account_high = self.get_highest_of_data(self.account_data)
		self.account_low = self.get_lowest_of_data(self.account_data)
		self.account_recommendation = self.get_server_recommendation(self.account_data)

	def get_average_of_data(self, account_data):
		total = 0
		for score in account_data:
			total += score
		return total / len(account_data)

	def get_highest_of_data(self, account_data):
		return [max(account_data), account_data.count(max(account_data))]

	def get_lowest_of_data(self, account_data):
		return [min(account_data), account_data.count(min(account_data))]

	def get_server_recommendation(self, account_average, account_high, account_low):
		score_key = {'P1 or P1.5': [0, 7], 'P2': [7.1, 10], 'P3': [10.1, 14], 'P4': [14.1, 25], 'P5': [25.1, 40], 'P6': [40.1, 80]}
		recommendations = {}
		for key, value in score_key.items():
			if account_average >= value[0] and account_average <= value[1]:
				recommendations['Average'] = [key, account_average]
			if account_high[0] >= value[0] and account_average <= value[1]:
				recommendations['High'] = [key, account_high[0], account_high[1]]
			if account_low[0] >= value[0] and account_average <= value[1]:
				recommendations['Low'] = [key, account_low[0], account_low[1]]
		return recommendations