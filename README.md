how to run 
1. Clone the repository:
   
  git clone https://github.com/YOUR_USERNAME/weatherforecast.git

  cd weatherforecast

3. Create and activate a virtual environment:
   
  python -m venv .venv

Windows (Git Bash):

  source .venv/Scripts/activate

5. Install dependencies:
   
  pip install -r requirements.txt

7. Create a .env file in the weatherforecast directory:
   
  API_KEY=your_openweather_api_key

9. running the app
    
   python weatherforecast/main.py

requirements:

  Python 3.9+
  
  OpenWeather API key

NOTES:

The application retrieves forecast data in 3-hour intervals from the OpenWeather API. It iterates through the response and keeps only the first forecast entry encountered for each date.

As a result, the displayed temperature represents the first available forecast for that day, not the daily average, minimum, or maximum temperature.

  
