import pandas as pd
import spacy

from flask import Flask, request, jsonify, render_template


file_path = '/Users/kushpai/Documents/Masters/BCG/BCDX-GenAI/Task-1/BCGX-GenAI.csv'
df = pd.read_csv(file_path)

df['Revenue Growth (%)'] = df.groupby('Company')['Total Revenue (in billions)'].pct_change() * 100
df['Net Income Growth (%)'] = df.groupby('Company')['Net Income (in billions)'].pct_change() * 100
df.fillna(0, inplace=True)

summary = df.groupby('Company').agg({
    'Revenue Growth (%)': 'mean',
    'Net Income Growth (%)': 'mean'
}).reset_index()

nlp = spacy.load('en_core_web_sm')


def get_financial_data(company_name, query_type):
    company_data = df[df['Company'] == company_name]
    if company_data.empty:
        return "Company not found."

    if query_type == "total_revenue":
        total_revenue = company_data['Total Revenue (in billions)'].iloc[-1]
        return f"The total revenue for {company_name} is ${total_revenue:,.2f} billion."
    elif query_type == "net_income_change":
        net_income_change = company_data['Net Income Growth (%)'].iloc[-1]
        return f"The net income for {company_name} has changed by {net_income_change:.2f}% over the last year."
    elif query_type == "revenue_growth":
        revenue_growth = summary.loc[summary['Company'] == company_name, 'Revenue Growth (%)'].values[0]
        return f"The average revenue growth for {company_name} is {revenue_growth:.2f}%."
    elif query_type == "net_income_growth":
        net_income_growth = summary.loc[summary['Company'] == company_name, 'Net Income Growth (%)'].values[0]
        return f"The average net income growth for {company_name} is {net_income_growth:.2f}%."
    elif query_type == "historical_trends":
        historical_data = company_data[['Year', 'Total Revenue (in billions)', 'Net Income (in billions)']]
        return historical_data.to_string(index=False)

    else:
        return "Query type not recognized."

    

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html', response=None)

@app.route('/chatbot', methods=['GET'])
def chatbot():
    user_query = request.args.get('query')
    response = chatbot_response(user_query)
    return render_template('index.html', response=response)


def terminal_chatbot():
    while True:
        user_query = input("Ask a financial question (format: 'Company Name: Query Type', 'quit' to exit): ")
        if user_query.lower() == 'quit':
            break
        response = chatbot_response(user_query)
        print(response)


def chatbot_response(user_query):
    parts = user_query.lower().split(':')
    if len(parts) != 2:
        return "Please provide queries in the format 'Company: Query Type'."

    company_name = parts[0].strip().title()
    query_type = parts[1].strip().replace(' ', '_')

    return get_financial_data(company_name, query_type)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

