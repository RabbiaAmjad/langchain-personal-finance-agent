import os
import math
from datetime import datetime

import streamlit as st
from langchain_core.tools import tool
from langchain_aws import ChatBedrockConverse
from langchain.agents import create_agent


# -----------------------------
# Streamlit page configuration
# -----------------------------

st.set_page_config(
    page_title="Personal Finance Assistant",
    page_icon="💰",
    layout="centered"
)


# -----------------------------
# AWS Bedrock configuration
# -----------------------------

AWS_REGION = "ap-southeast-2"
MODEL_ID = "global.amazon.nova-2-lite-v1:0"

BEDROCK_API_KEY = st.secrets["AWS_BEARER_TOKEN_BEDROCK"]

os.environ["AWS_BEARER_TOKEN_BEDROCK"] = BEDROCK_API_KEY
os.environ["AWS_DEFAULT_REGION"] = AWS_REGION


# -----------------------------
# Tool 1: Calculate Expense
# -----------------------------

@tool
def calculate_expense(
    amount: float,
    category: str,
    description: str
) -> str:
    """
    Log an expense with its amount, category, description, and current date.
    """
    date = datetime.now().strftime("%Y-%m-%d")

    return (
        f"Expense logged successfully!\n"
        f"Date: {date}\n"
        f"Amount: {amount:.2f} PKR\n"
        f"Category: {category.title()}\n"
        f"Description: {description}"
    )


# -----------------------------
# Tool 2: Get Budget Status
# -----------------------------

@tool
def get_budget_status(category: str) -> str:
    """
    Check the monthly budget, spending, and remaining amount for a category.
    """

    budgets = {
        "food": 15000,
        "transport": 10000,
        "entertainment": 8000,
        "shopping": 12000
    }

    spending = {
        "food": 6500,
        "transport": 3500,
        "entertainment": 5000,
        "shopping": 7000
    }

    category = category.lower()

    if category not in budgets:
        return (
            "Category not available. "
            "Choose food, transport, entertainment, or shopping."
        )

    budget = budgets[category]
    spent = spending[category]
    remaining = budget - spent

    return (
        f"{category.title()} Budget Status:\n"
        f"Monthly Budget: {budget:,} PKR\n"
        f"Spent: {spent:,} PKR\n"
        f"Remaining: {remaining:,} PKR"
    )


# -----------------------------
# Tool 3: Convert Currency
# -----------------------------

@tool
def convert_currency(
    amount: float,
    from_currency: str,
    to_currency: str
) -> str:
    """
    Convert an amount between supported currencies using fixed exchange rates.
    """

    rates = {
        "USD": 1.0,
        "PKR": 280.0,
        "EUR": 0.92,
        "GBP": 0.79
    }

    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in rates or to_currency not in rates:
        return "Supported currencies: USD, PKR, EUR, GBP."

    usd_amount = amount / rates[from_currency]
    converted_amount = usd_amount * rates[to_currency]

    return (
        f"{amount:.2f} {from_currency} = "
        f"{converted_amount:.2f} {to_currency}"
    )


# -----------------------------
# Tool 4: Calculate Savings Goal
# -----------------------------

@tool
def calculate_savings_goal(
    target_amount: float,
    monthly_savings: float
) -> str:
    """
    Calculate how many months are needed to reach a savings target.
    """

    if target_amount <= 0 or monthly_savings <= 0:
        return "Target amount and monthly savings must be greater than zero."

    months = math.ceil(target_amount / monthly_savings)

    return (
        f"You will reach your {target_amount:,.0f} PKR savings goal "
        f"in approximately {months} months."
    )


# -----------------------------
# Tool 5: Get Spending Tip
# -----------------------------

@tool
def get_spending_tip(category: str) -> str:
    """
    Provide a practical money-saving tip for a spending category.
    """

    tips = {
        "food": "Try planning your meals and limiting frequent food delivery orders.",
        "transport": "Compare transport options and combine trips when possible.",
        "entertainment": "Set a monthly entertainment limit and look for free activities.",
        "shopping": "Make a shopping list and avoid buying things on impulse."
    }

    category = category.lower()

    if category not in tips:
        return (
            "Available categories: "
            "food, transport, entertainment, shopping."
        )

    return f"Money-saving tip for {category.title()}: {tips[category]}"


# -----------------------------
# Create Finance Agent
# -----------------------------

tools = [
    calculate_expense,
    get_budget_status,
    convert_currency,
    calculate_savings_goal,
    get_spending_tip
]


llm = ChatBedrockConverse(
    model_id=MODEL_ID,
    region_name=AWS_REGION,
    temperature=0.7,
    max_tokens=512
)


finance_agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=(
        "You are a helpful Personal Finance Assistant. "
        "Help users with basic expense logging, budget checking, "
        "currency conversion, savings goals, and spending tips. "
        "Use the available tools whenever they are relevant. "
        "For requests involving multiple financial tasks, use all "
        "necessary tools. "
        "Present results clearly and concisely. "
        "Do not invent financial data that is not provided by the tools."
    )
)


# -----------------------------
# Agent function
# -----------------------------

def run_agent(query: str) -> str:
    """Send a user query to the finance agent and return its response."""

    result = finance_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        }
    )

    return result["messages"][-1].content


# -----------------------------
# Streamlit Interface
# -----------------------------

st.title("💰 Personal Finance Assistant")

st.write(
    "Ask me about your budget, expenses, currency conversion, "
    "savings goals, or spending habits."
)


# Sidebar
with st.sidebar:
    st.header("Quick Actions")

    if st.button("🍔 Check Food Budget"):
        st.session_state.quick_query = (
            "What is my remaining budget for food?"
        )

    if st.button("💱 Convert USD to PKR"):
        st.session_state.quick_query = (
            "Convert 50 USD to PKR."
        )

    if st.button("🎯 Savings Goal"):
        st.session_state.quick_query = (
            "I want to save 100,000 PKR. "
            "I can save 10,000 per month. "
            "When will I reach my goal?"
        )

    if st.button("💡 Food Saving Tip"):
        st.session_state.quick_query = (
            "I keep overspending on food. "
            "Give me a money-saving tip."
        )

    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Handle quick action
quick_query = st.session_state.pop("quick_query", None)

if quick_query:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": quick_query
        }
    )

    with st.chat_message("user"):
        st.markdown(quick_query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = run_agent(quick_query)

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )


# Normal chat input
user_query = st.chat_input(
    "Ask something about your finances..."
)


if user_query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_query
        }
    )

    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = run_agent(user_query)

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
