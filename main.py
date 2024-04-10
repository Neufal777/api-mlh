
import requests
import json

class FlightEngine:
    def __init__(self) -> None:
        self.base_url = "https://test.api.amadeus.com"
        self.api_key = ""
        self.api_secret = ""


    @property
    def get_token(self):
        data = {'grant_type': 'client_credentials','client_id': self.api_key, 'client_secret': self.api_secret}
        
        response_json = requests.post(f'{self.base_url}/v1/security/oauth2/token', data=data).json()
        
        return response_json.get('access_token')
    
    def get_flights(self, origin, destination, departure_date, adults, non_stop, max_results):
        token = self.get_token
        
        url = f"{self.base_url}/v2/shopping/flight-offers?originLocationCode={origin}&destinationLocationCode={destination}&departureDate={departure_date}&adults={adults}&nonStop={non_stop}&max={max_results}"

        headers = {'Authorization': f'Bearer {token}'}

        flight_json = requests.request("GET", url, headers=headers).json()
        
        for flight in flight_json['data']:
            print(f"Price: {flight['price']['total']} {flight['price']['currency']}")
            for itinerary in flight['itineraries']:
                for segment in itinerary['segments']:
                    print(f"{segment['departure']['iataCode']} -> {segment['arrival']['iataCode']} ({segment['carrierCode']}{segment['number']} - {segment['duration']} )")

flights = FlightEngine()
flights.get_flights("BCN", "SFO", "2024-06-20", 1, "false", 5)