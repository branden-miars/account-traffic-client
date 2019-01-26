
class AccountTrafficReport:
	"""Generates an object based on traffic report data. 

		Creates an object with:
			account_data: raw data from traffic report
			account_average: Average of the traffic data
			account_high: highest point in the traffic data and the number of occurences
			account_low: lowest point in the traffic data and the number of occurences
			account_recommendation: Utilizes average, high, and low to provide a dictionary 
			of recommendations"""

	def __init__(self, account_data):

		self.account_data = account_data
		self.account_average = self.get_average_of_data()
		self.account_high = self.get_highest_of_data()
		self.account_low = self.get_lowest_of_data()
		self.account_recommendation = self.get_server_recommendation()

	def get_average_of_data(self):
		total = 0
		for score in self.account_data:
			total += score
		return total / len(self.account_data)

	def get_highest_of_data(self):
		return [max(self.account_data), self.account_data.count(max(self.account_data))]

	def get_lowest_of_data(self):
		return [min(self.account_data), self.account_data.count(min(self.account_data))]

	def get_server_recommendation(self):
		score_key = {'P1 or P1.5': [0, 7], 'P2': [7.1, 10], 'P3': [10.1, 14], 'P4': [14.1, 25], 'P5': [25.1, 40], 'P6': [40.1, 80]}
		recommendations = {}
		for key, value in score_key.items():
			if self.account_average >= value[0] and self.account_average <= value[1]:
				recommendations['Average'] = [key, self.account_average]
			if self.account_high[0] >= value[0] and self.account_high[0] <= value[1]:
				recommendations['High'] = [key, self.account_high[0], self.account_high[1]]
			if self.account_low[0] >= value[0] and self.account_low[0] <= value[1]:
				recommendations['Low'] = [key, self.account_low[0], self.account_low[1]]
		return recommendations