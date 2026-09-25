import os
import math
from datetime import datetime

import streamlit as st

from langchain_core.tools import tool
from langchain_aws import ChatBedrockConverse
from langchain.agents import create_agent


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Personal Finance Assistant",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM STYLING
# ============================================================

st.markdown(
    """
    <style>

    /* Main page */
    .main {
        padding-top: 1rem;
    }

    /* Hero section */
    .hero {
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 1.5rem;
        background: linear-gradient(
            135deg,
            rgba(49, 51, 63, 0.08),
            rgba(255, 255, 255, 0.03)
        );
        border: 1px solid rgba(128, 128, 128, 0.15);
    }

    .hero-title {
        font-size: 2.4rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }

    .hero-subtitle {
        font-size: 1.05rem;
        opacity: 0.75;
    }

    /* Feature cards */
    .feature-card {
        padding: 1.2rem;
        border-radius: 16px;
        border: 1px solid rgba(128, 128, 128, 0.18);
        min-height: 125px;
        margin-bottom: 1rem;
    }

    .feature-icon {
        font-size: 1.7rem;
    }

    .feature-title {
        font-weight: 650;
        font-size: 1.05rem;
        margin-top: 0.3rem;
    }

    .feature-description {
        font-size: 0.88rem;
        opacity: 0.7;
        margin-top: 0.25rem;
    }

    /* Section titles */
    .section-title {
        font-size: 1.3rem;
        font-weight: 650;
        margin-top: 1rem;
        margin-bottom: 0.8rem;
    }

    /* Demo notice */
    .demo-notice {
        padding: 0.9rem 1rem;
        border-radius: 12px;
        background: rgba(255, 193, 7, 0.10);
        border: 1px solid rgba(255, 193, 7, 0.25);
        font-size: 0.9rem;
        margin-bottom: 1.2rem;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        border-right: 1px solid rgba(128, 128, 128, 0.15);
    }

    /* Chat input */
    div[data-testid="stChatInput"] {
        padding-bottom: 1rem;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
    }

    /* Hide Streamlit footer */
    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "expenses" not in st.session_state:
    st.session_state.expenses = []

if "pending_query" not in st.session_state:
    st.session_state.pending_query = None


# ============================================================
# AWS BEDROCK CONFIGURATION
# ============================================================

AWS_REGION = "ap-southeast-2"
MODEL_ID = "global.amazon.nova-2-lite-v1:0"


# Streamlit Cloud Secret
# The actual API key must NOT be placed in this file.

try:
    BEDROCK_API_KEY = st.secrets["AWS_BEARER_TOKEN_BEDROCK"]
except Exception:
    BEDROCK_API_KEY = os.getenv("AWS_BEARER_TOKEN_BEDROCK")


if not BEDROCK_API_KEY:
    st.error(
        "AWS Bedrock credentials are not configured. "
        "Please add AWS_BEARER_TOKEN_BEDROCK to Streamlit Secrets."
    )
    st.stop()


os.environ["AWS_BEARER_TOKEN_BEDROCK"] = BEDROCK_API_KEY
os.environ["AWS_DEFAULT_REGION"] = AWS_REGION


# ============================================================
# TOOL 1 — CALCULATE EXPENSE
# ============================================================

@tool
def calculate_expense(
    amount: float,
    category: str,
    description: str
) -> str:
    """Log an expense with amount, category and description."""

    date = datetime.now().strftime("%Y-%m-%d")

    # Save expense for the current Streamlit session
    st.session_state.expenses.append(
        {
            "date": date,
            "amount": float(amount),
            "category": category.title(),
            "description": description,
        }
    )

    return (
        f"Expense logged successfully:\n"
        f"- Date: {date}\n"
        f"- Amount: PKR {amount:,.2f}\n"
        f"- Category: {category.title()}\n"
        f"- Description: {description}"
    )


# ============================================================
# TOOL 2 — GET BUDGET STATUS
# ============================================================

@tool
def get_budget_status(category: str) -> str:
    """Check remaining monthly budget for a spending category."""

    budgets = {
        "food": 15000,
        "transport": 10000,
        "entertainment": 8000,
        "shopping": 12000,
    }

    spending = {
        "food": 6500,
        "transport": 3500,
        "entertainment": 5000,
        "shopping": 7000,
    }

    category = category.lower().strip()

    if category not in budgets:
        return (
            f"Category '{category}' is not available. "
            "Choose from: food, transport, entertainment, shopping."
        )

    budget = budgets[category]
    spent = spending[category]
    remaining = budget - spent

    return (
        f"Budget Status — {category.title()}:\n"
        f"- Monthly Budget: PKR {budget:,.0f}\n"
        f"- Amount Spent: PKR {spent:,.0f}\n"
        f"- Remaining Budget: PKR {remaining:,.0f}"
    )


# ============================================================
# TOOL 3 — CONVERT CURRENCY
# ============================================================

@tool
def convert_currency(
    amount: float,
    from_currency: str,
    to_currency: str
) -> str:
    """Convert between supported currencies using fixed rates."""

    rates = {
        "USD": 1.0,
        "PKR": 280.0,
        "EUR": 0.92,
        "GBP": 0.79,
    }

    from_currency = from_currency.upper().strip()
    to_currency = to_currency.upper().strip()

    if from_currency not in rates or to_currency not in rates:
        return (
            "Unsupported currency. "
            "Available currencies: USD, PKR, EUR, GBP."
        )

    amount_in_usd = amount / rates[from_currency]
    converted_amount = amount_in_usd * rates[to_currency]

    return (
        f"{amount:,.2f} {from_currency} = "
        f"{converted_amount:,.2f} {to_currency}"
    )


# ============================================================
# TOOL 4 — CALCULATE SAVINGS GOAL
# ============================================================

@tool
def calculate_savings_goal(
    target_amount: float,
    monthly_savings: float
) -> str:
    """Calculate how long it will take to reach a savings target."""

    if target_amount <= 0:
        return "Target amount must be greater than zero."

    if monthly_savings <= 0:
        return "Monthly savings must be greater than zero."

    months = math.ceil(target_amount / monthly_savings)

    return (
        f"Savings Goal:\n"
        f"- Target Amount: PKR {target_amount:,.0f}\n"
        f"- Monthly Savings: PKR {monthly_savings:,.0f}\n"
        f"- Time Required: {months} month(s)"
    )


# ============================================================
# TOOL 5 — GET SPENDING TIP
# ============================================================

@tool
def get_spending_tip(category: str) -> str:
    """Return a practical money-saving tip for a spending category."""

    tips = {
        "food": (
            "Try meal planning and set a weekly food budget. "
            "Reducing food delivery orders can also lower spending."
        ),

        "transport": (
            "Compare public transport, carpooling, and ride-hailing "
            "costs. Planning trips together can reduce transport expenses."
        ),

        "entertainment": (
            "Set a monthly entertainment limit and look for free or "
            "low-cost activities before spending on paid entertainment."
        ),

        "shopping": (
            "Use a 24-hour waiting rule before non-essential purchases "
            "and compare prices before buying."
        ),
    }

    category = category.lower().strip()

    if category not in tips:
        return (
            f"No specific tip available for '{category}'. "
            "Available categories: food, transport, entertainment, shopping."
        )

    return (
        f"Money-saving tip for {category.title()}:\n"
        f"{tips[category]}"
    )


# ============================================================
# AGENT
# ============================================================

tools = [
    calculate_expense,
    get_budget_status,
    convert_currency,
    calculate_savings_goal,
    get_spending_tip,
]


@st.cache_resource
def create_finance_agent():

    return create_agent(
        model=ChatBedrockConverse(
            model_id=MODEL_ID,
            region_name=AWS_REGION,
            temperature=0.7,
            max_tokens=512,
        ),
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
        ),
    )


finance_agent = create_finance_agent()


# ============================================================
# AGENT RUNNER
# ============================================================

def run_agent(query: str) -> str:

    result = finance_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query,
                }
            ]
        }
    )

    return result["messages"][-1].content


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 💰 Finance Assistant")

    st.caption(
        "Your AI assistant for everyday money management."
    )

    st.divider()

    st.markdown("### 🧰 What I can do")

    st.markdown(
        """
        💸 **Expenses**  
        Log your spending

        📊 **Budgets**  
        Check category budgets

        💱 **Currency**  
        Convert supported currencies

        🎯 **Savings**  
        Plan savings goals

        💡 **Tips**  
        Get spending advice
        """
    )

    st.divider()

    # --------------------------------------------------------
    # SESSION SUMMARY
    # --------------------------------------------------------

    st.markdown("### 📋 This Session")

    expense_count = len(st.session_state.expenses)
    total_expenses = sum(
        expense["amount"]
        for expense in st.session_state.expenses
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Expenses",
            expense_count
        )

    with col2:
        st.metric(
            "Total",
            f"PKR {total_expenses:,.0f}"
        )

    if st.session_state.expenses:

        st.caption("Recent expenses")

        for expense in st.session_state.expenses[-5:]:
            st.write(
                f"**PKR {expense['amount']:,.0f}** · "
                f"{expense['category']}"
            )

    else:
        st.caption("No expenses logged yet.")

    st.divider()

    # --------------------------------------------------------
    # QUICK ACTIONS
    # --------------------------------------------------------

    st.markdown("### ⚡ Quick Actions")

    if st.button(
        "💸 Log an Expense",
        use_container_width=True
    ):
        st.session_state.pending_query = (
            "Log an expense of 2000 PKR for food "
            "with the description 'Lunch'."
        )
        st.rerun()

    if st.button(
        "📊 Check Food Budget",
        use_container_width=True
    ):
        st.session_state.pending_query = (
            "What is my remaining budget for food?"
        )
        st.rerun()

    if st.button(
        "💱 Convert USD → PKR",
        use_container_width=True
    ):
        st.session_state.pending_query = (
            "Convert 50 USD to PKR."
        )
        st.rerun()

    if st.button(
        "🎯 Savings Goal",
        use_container_width=True
    ):
        st.session_state.pending_query = (
            "I want to save 100,000 PKR and can save "
            "10,000 PKR per month. How long will it take?"
        )
        st.rerun()

    if st.button(
        "💡 Food Saving Tip",
        use_container_width=True
    ):
        st.session_state.pending_query = (
            "Give me a money-saving tip for food."
        )
        st.rerun()

    st.divider()

    # --------------------------------------------------------
    # CLEAR
    # --------------------------------------------------------

    if st.button(
        "🗑️ Clear Session",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.session_state.expenses = []
        st.session_state.pending_query = None
        st.rerun()


# ============================================================
# MAIN HERO SECTION
# ============================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-title">
            💰 Personal Finance Assistant
        </div>

        <div class="hero-subtitle">
            Your AI assistant for expenses, budgets,
            currency conversion, savings goals, and spending tips.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# DEMO MODE NOTICE
# ============================================================

st.markdown(
    """
    <div class="demo-notice">
        ℹ️ <b>Demo Mode:</b>
        Budget and spending figures are sample data.
        Expenses logged in the sidebar are kept only for this session.
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# FEATURE CARDS
# ============================================================

st.markdown(
    '<div class="section-title">✨ What can I help you with?</div>',
    unsafe_allow_html=True,
)

col1, col2, col3, col4, col5 = st.columns(5)

features = [
    (
        col1,
        "💸",
        "Expenses",
        "Log and organize your spending",
    ),
    (
        col2,
        "📊",
        "Budgets",
        "Check your category budgets",
    ),
    (
        col3,
        "💱",
        "Currency",
        "Convert supported currencies",
    ),
    (
        col4,
        "🎯",
        "Savings",
        "Plan your savings goals",
    ),
    (
        col5,
        "💡",
        "Tips",
        "Get practical spending tips",
    ),
]

for column, icon, title, description in features:

    with column:

        st.markdown(
            f"""
            <div class="feature-card">
                <div class="feature-icon">{icon}</div>
                <div class="feature-title">{title}</div>
                <div class="feature-description">
                    {description}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# SUGGESTED QUESTIONS
# ============================================================

if not st.session_state.messages:

    st.markdown(
        '<div class="section-title">💬 Try asking...</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "📊 How much food budget do I have left?",
            use_container_width=True,
        ):
            st.session_state.pending_query = (
                "How much food budget do I have left?"
            )
            st.rerun()

        if st.button(
            "💱 Convert 100 USD to PKR",
            use_container_width=True,
        ):
            st.session_state.pending_query = (
                "Convert 100 USD to PKR."
            )
            st.rerun()

    with col2:

        if st.button(
            "🎯 I want to save 50,000 PKR",
            use_container_width=True,
        ):
            st.session_state.pending_query = (
                "I want to save 50,000 PKR and can save "
                "10,000 PKR per month. How long will it take?"
            )
            st.rerun()

        if st.button(
            "💡 Give me a shopping saving tip",
            use_container_width=True,
        ):
            st.session_state.pending_query = (
                "Give me a money-saving tip for shopping."
            )
            st.rerun()


# ============================================================
# CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ============================================================
# USER INPUT
# ============================================================

user_input = st.chat_input(
    "Ask something about your finances..."
)


# ============================================================
# HANDLE QUICK ACTION
# ============================================================

if st.session_state.pending_query:

    user_input = st.session_state.pending_query
    st.session_state.pending_query = None


# ============================================================
# PROCESS QUERY
# ============================================================

if user_input:

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        with st.spinner("🤔 Thinking..."):

            try:

                answer = run_agent(user_input)

                st.markdown(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                    }
                )

            except Exception as e:

                error_message = (
                    "Sorry, I couldn't process that request. "
                    "Please try again."
                )

                st.error(error_message)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message,
                    }
                )
