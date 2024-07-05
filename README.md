# Financial Chatbot

## Overview

Financial Chatbot is a Python-based application that allows users to query financial data using natural language. It integrates data analysis with Flask for web interaction and supports terminal-based queries for easy access.

## Features

- **Query Types**: Supports queries for total revenue, net income changes, average revenue growth, average net income growth, company comparisons, and historical trends.
- **Interfaces**: Provides both a web interface and a terminal interface for interacting with the chatbot.
- **Data Analysis**: Utilizes Pandas for data manipulation and aggregation to provide real-time financial insights.
- **Natural Language Processing**: Uses SpaCy for entity recognition to extract company names from user queries.
- **Responsive Design**: Web interface designed with HTML and CSS for a user-friendly experience.

## Getting Started

### Prerequisites

- Python 3.x
- Install required libraries: `pip install -r requirements.txt`

### Installation

1. Clone the repository:
git clone https://github.com/your-username/financial-chatbot.git
cd financial-chatbot

2. Install dependencies:
pip install -r requirements.txt

### Usage

#### Web Interface

1. Run the Flask app:
python main.py

3. Access the chatbot at `http://localhost:5000` in your web browser.

#### Terminal Interface

1. Run the terminal chatbot:
python main.py terminal

2. Follow the prompts to enter financial queries.

## Examples

- **Query Format**: Use queries in the format `'Company: Query Type'`, e.g., `Microsoft: Total Revenue`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built as part of the BCDX-GenAI project for financial data analysis.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.




