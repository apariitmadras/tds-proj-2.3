# Data Analyst Agent

A Flask-based API that uses machine learning and data analysis to source, prepare, analyze, and visualize data. This agent can handle various types of data analysis tasks including web scraping, statistical analysis, and data visualization.

## Features

- **Web Scraping**: Scrapes data from websites like Wikipedia
- **Data Analysis**: Performs statistical analysis and calculations
- **Data Visualization**: Creates charts and plots encoded as base64 data URIs
- **Multiple Data Sources**: Handles various data formats and sources
- **RESTful API**: Simple POST endpoint for easy integration

## Project Structure

```
data-analyst-agent/
├── app.py                 # Main Flask application
├── data_analyzer.py       # Core data analysis logic
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── run.sh               # Startup script
├── test_client.py       # Test client for API
├── sample_questions/    # Sample question files
│   ├── question1.txt    # Wikipedia example
│   └── question2.txt    # Indian courts example
└── README.md           # This file
```

## Installation

### Method 1: Local Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd data-analyst-agent
   ```

2. **Make the run script executable**
   ```bash
   chmod +x run.sh
   ```

3. **Run the startup script**
   ```bash
   ./run.sh
   ```

4. **Configure environment variables**
   - Edit the `.env` file with your API keys (optional for basic functionality)
   - Set `OPENAI_API_KEY` if you want to use OpenAI for generic analysis

### Method 2: Manual Installation

1. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

### Method 3: Docker

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

2. **Or build and run manually**
   ```bash
   docker build -t data-analyst-agent .
   docker run -p 5000:5000 data-analyst-agent
   ```

## Usage

### API Endpoint

The application exposes a single API endpoint:

```
POST http://localhost:5000/api/
```

### Example Requests

1. **Using curl with a file**
   ```bash
   curl -X POST "http://localhost:5000/api/" -F "file=@sample_questions/question1.txt"
   ```

2. **Using curl with direct data**
   ```bash
   curl -X POST "http://localhost:5000/api/" -d "Analyze the correlation in this dataset..."
   ```

3. **Using Python requests**
   ```python
   import requests
   
   with open('sample_questions/question1.txt', 'r') as f:
       question = f.read()
   
   response = requests.post('http://localhost:5000/api/', data=question)
   result = response.json()
   ```

### Testing

Run the test client to verify the installation:

```bash
python test_client.py
```

This will test both example scenarios:
- Wikipedia highest-grossing films analysis
- Indian high court dataset analysis

## Supported Analysis Types

### 1. Wikipedia Data Scraping
- Scrapes tabular data from Wikipedia pages
- Performs statistical analysis on the data
- Creates visualizations with regression lines

### 2. Database Queries
- Supports DuckDB queries for large datasets
- Handles structured data analysis
- Generates statistical reports

### 3. Generic Data Analysis
- Uses OpenAI API for general data questions (requires API key)
- Flexible analysis based on question content

## Response Formats

The API returns different formats based on the question type:

### Array Response (Wikipedia example)
```json
[1, "Titanic", 0.485782, "data:image/png;base64,iVBORw0KG..."]
```

### Object Response (Indian courts example)
```json
{
  "Which high court disposed the most cases from 2019 - 2022?": "Madras High Court",
  "What's the regression slope...": "0.0234",
  "Plot the year and # of days...": "data:image/png;base64,..."
}
```

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: OpenAI API key for generic analysis (optional)
- `PORT`: Port number for the Flask app (default: 5000)

### Dependencies

Key Python packages:
- `flask`: Web framework
- `pandas`: Data manipulation
- `matplotlib`: Data visualization
- `beautifulsoup4`: Web scraping
- `requests`: HTTP requests
- `scipy`: Statistical analysis
- `duckdb`: Database queries
- `openai`: AI-powered analysis

## Limitations

1. **Image Size**: Plots are limited to 100KB as base64 data URIs
2. **Response Time**: Complex analyses must complete within 3 minutes
3. **Data Sources**: Some datasets may require authentication or special access
4. **OpenAI API**: Generic analysis requires a valid OpenAI API key

## Troubleshooting

### Common Issues

1. **Connection Error**: Make sure the app is running on the correct port
2. **Import Errors**: Ensure all dependencies are installed in the virtual environment
3. **Memory Issues**: Large datasets may require more system resources
4. **API Rate Limits**: OpenAI API has usage limits

### Debug Mode

To run in debug mode:
```bash
export FLASK_DEBUG=1
python app.py
```

## Development

### Adding New Analysis Types

1. Add a new method in `DataAnalyzer` class
2. Update the `process_question` method to route to your new handler
3. Test with sample questions

### Extending Data Sources

The system can be extended to support:
- Database connections (PostgreSQL, MySQL, etc.)
- Cloud storage (AWS S3, Google Cloud Storage)
- APIs and web services
- File uploads (CSV, Excel, JSON)

## License

This project is provided as-is for educational and development purposes.