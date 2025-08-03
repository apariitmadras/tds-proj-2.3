import requests
import json

def test_wikipedia_example():
    """Test the Wikipedia example"""
    question = """
    Scrape the list of highest grossing films from Wikipedia. It is at the URL:
    https://en.wikipedia.org/wiki/List_of_highest-grossing_films

    Answer the following questions and respond with a JSON array of strings containing the answer.

    1. How many $2 bn movies were released before 2020?
    2. Which is the earliest film that grossed over $1.5 bn?
    3. What's the correlation between the Rank and Peak?
    4. Draw a scatterplot of Rank and Peak along with a dotted red regression line through it.
       Return as a base-64 encoded data URI, `"data:image/png;base64,iVBORw0KG..."` under 100,000 bytes.
    """
    
    url = "http://localhost:5000/api/"
    response = requests.post(url, data=question)
    
    print("Wikipedia Example Response:")
    print(json.dumps(response.json(), indent=2))
    print("\n" + "="*50 + "\n")

def test_indian_courts_example():
    """Test the Indian courts example"""
    question = """
    The Indian high court judgement dataset contains judgements from the Indian High Courts, downloaded from ecourts website.
    
    Answer the following questions and respond with a JSON object containing the answer.

    {
      "Which high court disposed the most cases from 2019 - 2022?": "...",
      "What's the regression slope of the date_of_registration - decision_date by year in the court=33_10?": "...",
      "Plot the year and # of days of delay from the above question as a scatterplot with a regression line. Encode as a base64 data URI under 100,000 characters": "data:image/webp:base64,..."
    }
    """
    
    url = "http://localhost:5000/api/"
    response = requests.post(url, data=question)
    
    print("Indian Courts Example Response:")
    print(json.dumps(response.json(), indent=2))
    print("\n" + "="*50 + "\n")

def test_health_check():
    """Test health check endpoint"""
    url = "http://localhost:5000/health"
    response = requests.get(url)
    
    print("Health Check Response:")
    print(json.dumps(response.json(), indent=2))
    print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    try:
        test_health_check()
        test_wikipedia_example()
        test_indian_courts_example()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server. Make sure the app is running on localhost:5000")
    except Exception as e:
        print(f"Error: {e}")