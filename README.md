# Lead Generator App
## Description
The Lead Generator App is a personal project designed to help you find potential freelance clients by identifying businesses in a specified area that do not have a website. The app utilizes the Google Places API to search for businesses based on a given query and location. It then filters and lists businesses without a website, including their phone numbers and ratings.

## Features
Business Search: Searches for businesses based on a specified query (e.g., "HVAC") and location.
Website Check: Identifies businesses that do not have a website.
Business Details: Provides information such as business name, phone number, and rating for businesses without a website.
Pagination Handling: Automatically handles pagination to fetch results from multiple pages.
## How It Works
API Request: Sends a request to the Google Places API to search for businesses based on the provided query, location, and radius.
Pagination: Handles pagination using the next_page_token to retrieve results from additional pages if available.
Business Details Fetching: For each business found, makes a subsequent request to retrieve detailed information, including the presence of a website.
Filter Results: Filters businesses to only include those without a website and prints their details.
