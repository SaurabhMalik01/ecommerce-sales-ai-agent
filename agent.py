import os
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Please set GEMINI_API_KEY in .env file")

genai.configure(api_key=GEMINI_API_KEY, transport="rest")

CSV_FILE = "Amazon Sale Report.csv"
df = pd.read_csv(CSV_FILE, low_memory=False)
print(f"✅ Loaded {len(df)} rows from {CSV_FILE}")

df_sales = df[df['Status'].str.lower() != 'cancelled']

model = genai.GenerativeModel(model_name="gemini-2.5-pro")

while True:
    question = input("\nAsk about sales data (or type 'exit'): ").strip()
    if question.lower() == "exit":
        print("👋 Goodbye!")
        break

    answer_text = "⚠️ Could not calculate answer"

    if "average price" in question.lower():
        total_amount = df_sales['Amount'].sum()
        total_qty = df_sales['Qty'].sum()
        avg_price = total_amount / total_qty
        answer_text = f"₹{avg_price:.2f}"

    elif "most expensive" in question.lower():
        max_row = df_sales.loc[df_sales['Amount'].idxmax()]
        answer_text = f"{max_row['Style']} (₹{max_row['Amount']})"

    elif "most reviews" in question.lower():
        if 'Number of Reviews' in df_sales.columns:
            max_row = df_sales.loc[df_sales['Number of Reviews'].idxmax()]
            answer_text = f"{max_row['Style']} ({max_row['Number of Reviews']} reviews)"
        else:
            answer_text = "No 'Number of Reviews' column in dataset"

    else:
        sample_data = df_sales.head(5).to_string(index=False)
        prompt_text = f"""
        You are a helpful data analyst AI.
        Provide a concise answer.

        Sample data:
        {sample_data}

        Question: {question}
        """
        response = model.generate_content(prompt_text)
        answer_text = response.text.strip() if response.text else "⚠️ No response"

    print("\n🤖 Answer:", answer_text)
