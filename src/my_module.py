# Class hotel with the  following objects:
# Hotel name
# Value of regular customer stay on working days
# Value of reward customer stay on working days
# Value of regular customer stay on weekend
# Value of reward customer stay on weekend
# Hotel classification
class hotel:
    def __init__(self, hotel_name, hotel_regular_workdays, hotel_rewards_workdays, hotel_regular_weekend,
                 hotel_rewards_weekend, hotel_classification):
        self.name = hotel_name
        self.regular_workdays = hotel_regular_workdays
        self.rewards_workdays = hotel_rewards_workdays
        self.regular_weekend = hotel_regular_weekend
        self.rewards_weekend = hotel_rewards_weekend
        self.classification = hotel_classification

    # The function total price discount the classification divided by 10, in a way to sort the values in function of
    # classification if the prices in different hotels are the same
    def total_price(self, client_type, amount_workdays, amount_weekend):
        if client_type == 'Regular':
            value = self.regular_workdays * amount_workdays + self.regular_weekend * amount_weekend - self.classification / 10
        else:
            value = self.rewards_workdays * amount_workdays + self.rewards_weekend * amount_weekend - self.classification / 10
        return value


# Creating the objects as described
lakewood = hotel('Lakewood', 110, 80, 90, 80, 3)
bridgewood = hotel('Bridgewood', 160, 110, 60, 50, 4)
ridgewood = hotel('Ridgewood', 220, 100, 150, 40, 5)


# Function that returns the smallest hotel value
def get_cheapest_hotel(input):
    # Returning a error if the input is irregular:
    if 'Regular' not in input and 'Reward' not in input:
        return 'error'
    client_type = 'Regular' if 'Regular' in input else 'Reward'

    # Breaking the input for data processing:
    input_split = input.split()
    workdays = ['mon', 'tues', 'wed', 'thur', 'fri']
    weekend = ['sat', 'sun']
    amount_workdays = 0
    amount_weekend = 0

    for part in input_split:
        for day in workdays:
            if day in part:
                amount_workdays += 1
        for day in weekend:
            if day in part:
                amount_weekend += 1

    lakewood_value = lakewood.total_price(client_type, amount_workdays, amount_weekend)
    bridgewood_value = bridgewood.total_price(client_type, amount_workdays, amount_weekend)
    ridgewood_value = ridgewood.total_price(client_type, amount_workdays, amount_weekend)

    # Creating a tuple with the stay value and the name of the hotel:
    values_tuple = [(lakewood_value, lakewood.name),
                    (bridgewood_value, bridgewood.name),
                    (ridgewood_value, ridgewood.name)]
    values_tuple.sort()

    # With the values_tuple sorted, the first position represents the cheapest hotel
    return values_tuple[0][1]
