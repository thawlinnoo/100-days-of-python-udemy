class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

def find_cheapest_flight(data, return_date):
    best_flights = data.get("best_flights", []) #get best_flight or otherwise just give empty list
    other_flights = data.get("other_flights", [])
    all_flights = best_flights + other_flights
    cheapest_flight = None
    cheapest_price = float("inf")
    for flight in all_flights:
        if "price" not in flight:
            continue
        if flight["price"] < cheapest_price:
            
            cheapest_price = flight["price"]
            cheapest_flight = flight
    if cheapest_flight is None:
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")
    else:
        origin = cheapest_flight["flights"][0]["departure_airport"]["id"]
        destination = cheapest_flight["flights"][-1]["arrival_airport"]["id"]
        date = cheapest_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
        price = cheapest_flight["price"]
        stops = len(cheapest_flight["flights"]) - 1
        return FlightData(price, origin, destination, date, return_date, stops)





        

        