# Ecommerce Sales AI Agent

A Python AI agent that analyzes Amazon sales data using the Gemini 2.5 Pro API.  
Users can interactively ask questions about sales data, such as:

- Average price of products
- Most expensive products 
- Products with the most reviews
- Other insights based on your dataset

## Project Structure

```
Ecommerce_Product_Insights_Agent/
│
├── agent.py                 # Main Python AI agent script
├── Amazon Sale Report.csv   # Sample Amazon sales data
├── .env                    # Stores Gemini API key (ignored by Git)
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ecommerce-sales-ai-agent.git
   cd ecommerce-sales-ai-agent
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a .env file:**
   - Create a `.env` file in the project root
   - Add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

4. **Run the AI agent:**
   ```bash
   python agent.py
   ```

## Usage

- Type questions about your Amazon sales data, for example:
  - "What is the average price?"
  - "Show me the most expensive product"
  - "Which product has the most reviews?"
- The agent will respond with concise answers using:
  - Direct Python calculations for numerical queries
  - Gemini API for complex analysis and explanations
- Type `exit` to quit the agent

## Notes

- Keep your `.env` file private - it contains your API key
- The agent works with `Amazon Sale Report.csv`
- You can use your own data with similar column structure

## Dependencies

- pandas
- python-dotenv
- google-generativeai

Install all dependencies using:
```bash
pip install -r requirements.txt
```
