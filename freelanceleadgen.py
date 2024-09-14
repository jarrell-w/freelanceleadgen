import requests

def getResults(next_page_token=''):

    api_key = "AIzaSyD8qjSOAp3tv7Hj9lTVsq2fBW6RjVzhpaE"

    search_query = "hvac"
    location = "39.8592,-75.0144" 
    radius = 500 

    if next_page_token:
        url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={search_query}&pagetoken={next_page_token}&key={api_key}"
    else:
        url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={search_query}&location={location}&radius={radius}&key={api_key}"

    response = requests.get(url)
    data = response.json()

    # Get the list of places and the next page token
    places = data.get('results', [])
    next_page_token = data.get('next_page_token', None)

    # Parse the response to get business details
    for place in places:
        place_id = place.get('place_id')
        googleURL = f"https://maps.googleapis.com/maps/api/place/details/json?fields=name%2Crating%2Cformatted_phone_number%2Cwebsite&place_id={place_id}&key={api_key}"
        websiteResponse = requests.get(googleURL)
        placesweb = websiteResponse.json().get('result', {})
        if placesweb.get('website') is None:
            print(f"\nBusiness: {placesweb.get('name')}, Phone Number: {placesweb.get('formatted_phone_number')}, Rating: {placesweb.get('rating')}, Website: {placesweb.get('website')}\n")

    # If there is a next page token, make a recursive call to get the next page of results
    if next_page_token:
        getResults(next_page_token)

getResults()
