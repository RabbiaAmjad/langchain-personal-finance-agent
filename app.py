import os
import math
from datetime import datetime

import streamlit as st

from langchain_core.tools import tool
from langchain_aws import ChatBedrockConverse
from langchain.agents import create_agent


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Personal Finance Assistant",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main {
        padding-top: 1rem;
    }

    .hero {
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(128, 128, 128, 0.18);
        background: linear-gradient(
            135deg,
            rgba(49, 51, 63, 0.08),
            rgba(255, 255, 255, 0.03)
        );
    }

    .hero-title {
        font-size: 2.3rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }

    .hero-subtitle {
        font-size: 1rem;
        opacity: 0.72;
    }

    .demo-notice {
        padding: 0.9rem 1rem;
        border-radius: 12px;
        margin-bottom: 1.3rem;
        border: 1px solid rgba(255, 193, 7, 0.3);
        background: rgba(255, 193, 7, 0.08);
    }

    .section-title {
        font-size: 1.25rem;
        font-weight: 650;
        margin-top: 1rem;
        margin-bottom: 0.8rem;
    }

    .feature-card {
        padding: 1.1rem;
        border-radius: 15px;
        border: 1px solid rgba(128, 128, 128, 0.18);
        min-height: 120px;
        margin-bottom: 1rem;
    }

    .feature-icon {
        font-size: 1.7rem;
    }

    .feature-title {
        font-weight: 650;
        margin-top: 0.3rem;
    }

    .feature-description {
        font-size: 0.85rem;
        opacity: 0.7;
        margin-top: 0.25rem;
    }

    section[data-testid="stSidebar"] {
        border-right: 1px solid rgba(128, 128, 128, 0.15);
    }

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


# IMPORTANT:
# The real key stays inside Streamlit Cloud Secrets.
# Do NOT put the real key inside this file.

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
# TOOL 1 — EXPENSE
# ============================================================

@tool
def calculate_expense(
    amount: float,
    category: str,
    description: str
) -> str:
    """
    Log an expense with an amount, category and description.
    """

    date = datetime.now().strftime("%Y-%m-%d")

    return (
        f"Expense logged successfully.\n"
        f"Date: {date}\n"
        f"Amount: PKR {amount:,.2f}\n"
        f"Category: {category.title()}\n"
        f"Description: {description}"
    )


# ============================================================
# TOOL 2 — BUDGET
# ============================================================

@tool
def get_budget_status(category: str) -> str:
    """
    Check the remaining monthly budget for a category.
    """

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
            "Available categories are: "
            "food, transport, entertainment, shopping."
        )

    budget = budgets[category]
    spent = spending[category]
    remaining = budget - spent

    return (
        f"Budget Status for {category.title()}:\n"
        f"Monthly Budget: PKR {budget:,.0f}\n"
        f"Amount Spent: PKR {spent:,.0f}\n"
        f"Remaining Budget: PKR {remaining:,.0f}"
    )


# ============================================================
# TOOL 3 — CURRENCY
# ============================================================

@tool
def convert_currency(
    amount: float,
    from_currency: str,
    to_currency: str
) -> str:
    """
    Convert an amount between supported currencies.
    """

    rates = {
        "USD": 1.0,
        "PKR": 280.0,
        "EUR": 0.92,
        "GBP": 0.79,
    }

    from_currency = from_currency.upper().strip()
    to_currency = to_currency.upper().strip()

    if from_currency not in rates:
        return (
            f"Unsupported source currency: {from_currency}. "
            "Supported currencies: USD, PKR, EUR, GBP."
        )

    if to_currency not in rates:
        return (
            f"Unsupported destination currency: {to_currency}. "
            "Supported currencies: USD, PKR, EUR, GBP."
        )

    amount_in_usd = amount / rates[from_currency]

    converted_amount = amount_in_usd * rates[to_currency]

    return (
        f"{amount:,.2f} {from_currency} = "
        f"{converted_amount:,.2f} {to_currency}"
    )


# ============================================================
# TOOL 4 — SAVINGS GOAL
# ============================================================

@tool
def calculate_savings_goal(
    target_amount: float,
    monthly_savings: float
) -> str:
    """
    Calculate how many months are required to reach a savings goal.
    """

    if target_amount <= 0:
        return "The target amount must be greater than zero."

    if monthly_savings <= 0:
        return "Monthly savings must be greater than zero."

    months = math.ceil(
        target_amount / monthly_savings
    )

    return (
        f"Savings Goal:\n"
        f"Target Amount: PKR {target_amount:,.0f}\n"
        f"Monthly Savings: PKR {monthly_savings:,.0f}\n"
        f"Estimated Time: {months} month(s)"
    )


# ============================================================
# TOOL 5 — SPENDING TIP
# ============================================================

@tool
def get_spending_tip(category: str) -> str:
    """
    Provide a practical spending tip for a category.
    """

    tips = {
        "food": (
            "Plan meals in advance, set a weekly food budget, "
            "and reduce unnecessary food-delivery orders."
        ),

        "transport": (
            "Compare public transport, carpooling and ride-hailing "
            "options and combine trips whenever possible."
        ),

        "entertainment": (
            "Set a monthly entertainment limit and consider "
            "free or low-cost activities."
        ),

        "shopping": (
            "Wait 24 hours before making non-essential purchases "
            "and compare prices before buying."
        ),
    }

    category = category.lower().strip()

    if category not in tips:
        return (
            f"No specific tip is available for '{category}'. "
            "Available categories are: "
            "food, transport, entertainment, shopping."
        )

    return (
        f"Spending Tip for {category.title()}:\n"
        f"{tips[category]}"
    )


# ============================================================
# AGENT TOOLS
# ============================================================

tools = [
    calculate_expense,
    get_budget_status,
    convert_currency,
    calculate_savings_goal,
    get_spending_tip,
]


# ============================================================
# CREATE AGENT
# ============================================================

@st.cache_resource
def create_finance_agent():

    model = ChatBedrockConverse(
        model_id=MODEL_ID,
        region_name=AWS_REGION,
        temperature=0.7,
        max_tokens=512,
    )

    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=(
            "You are a helpful Personal Finance Assistant. "
            "You can help users with expenses, budgets, currency "
            "conversion, savings goals and spending tips. "
            "Use the appropriate tool whenever one is relevant. "
            "For compound requests, use all necessary tools. "
            "Never invent numerical results when a tool can provide "
            "the information. "
            "Keep answers clear, friendly and concise."
        ),
    )

    return agent


# ============================================================
# CREATE AGENT SAFELY
# ============================================================

try:
    finance_agent = create_finance_agent()

except Exception as e:

    st.error(
        "The Personal Finance Assistant could not initialize."
    )

    with st.expander("Technical details"):
        st.code(str(e))

    st.stop()


# ============================================================
# HELPER — CONVERT MESSAGE CONTENT TO TEXT
# ============================================================

def content_to_text(content):
    """
    Convert different LangChain/Bedrock content formats into
    readable text.
    """

    if content is None:
        return ""

    if isinstance(content, str):
        return content

    if isinstance(content, list):

        parts = []

        for item in content:

            if isinstance(item, str):
                parts.append(item)

            elif isinstance(item, dict):

                text_value = item.get("text")

                if text_value:
                    parts.append(str(text_value))

        return "\n".join(parts)

    return str(content)


# ============================================================
# HELPER — RECORD EXPENSES FROM TOOL CALLS
# ============================================================

def record_expenses_from_result(result):
    """
    Read successful expense tool calls after the agent finishes.

    This keeps Streamlit session state OUT of the LangChain tool
    itself, which makes the agent more reliable.
    """

    try:

        messages = result.get("messages", [])

        for message in messages:

            tool_calls = getattr(
                message,
                "tool_calls",
                None
            )

            if not tool_calls:
                continue

            for tool_call in tool_calls:

                tool_name = tool_call.get("name")

                if tool_name != "calculate_expense":
                    continue

                args = tool_call.get("args", {})

                amount = args.get("amount")
                category = args.get("category")
                description = args.get("description")

                if amount is None:
                    continue

                try:
                    amount = float(amount)
                except (TypeError, ValueError):
                    continue

                st.session_state.expenses.append(
                    {
                        "date": datetime.now().strftime(
                            "%Y-%m-%d"
                        ),
                        "amount": amount,
                        "category": str(
                            category or "Other"
                        ).title(),
                        "description": str(
                            description or ""
                        ),
                    }
                )

    except Exception:
        # Session tracking should NEVER break the agent.
        pass


# ============================================================
# RUN AGENT
# ============================================================

def run_agent(query: str) -> str:

    try:

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

        # Update temporary session expense list.
        record_expenses_from_result(result)

        messages = result.get("messages", [])

        # Find the final AI response.
        for message in reversed(messages):

            message_type = getattr(
                message,
                "type",
                ""
            )

            if message_type == "ai":

                answer = content_to_text(
                    getattr(message, "content", "")
                )

                if answer.strip():
                    return answer

        # Fallback
        if messages:

            answer = content_to_text(
                getattr(
                    messages[-1],
                    "content",
                    ""
                )
            )

            if answer.strip():
                return answer

        return (
            "I completed the request, but I couldn't "
            "generate a response."
        )

    except Exception as e:

        raise RuntimeError(
            f"Agent execution failed: {str(e)}"
        )


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
        Convert currencies

        🎯 **Savings**  
        Plan savings goals

        💡 **Tips**  
        Get spending advice
        """
    )

    st.divider()

    # ========================================================
    # SESSION SUMMARY
    # ========================================================

    st.markdown("### 📋 This Session")

    expense_count = len(
        st.session_state.expenses
    )

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

        for expense in reversed(
            st.session_state.expenses[-5:]
        ):

            st.write(
                f"**PKR {expense['amount']:,.0f}** · "
                f"{expense['category']}"
            )

    else:

        st.caption(
            "No expenses logged this session."
        )

    st.divider()

    # ========================================================
    # QUICK ACTIONS
    # ========================================================

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
            "I want to save 100000 PKR and "
            "can save 10000 PKR per month. "
            "How long will it take?"
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

    # ========================================================
    # CLEAR SESSION
    # ========================================================

    if st.button(
        "🗑️ Clear Session",
        use_container_width=True
    ):

        st.session_state.messages = []
        st.session_state.expenses = []
        st.session_state.pending_query = None

        st.rerun()


# ============================================================
# MAIN HERO
# ============================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-title">
            💰 Personal Finance Assistant
        </div>

        <div class="hero-subtitle">
            Your AI assistant for expenses, budgets,
            currency conversion, savings goals,
            and spending tips.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# DEMO NOTICE
# ============================================================

st.markdown(
    """
    <div class="demo-notice">
        ℹ️ <b>Demo Mode:</b>
        Budget and spending figures are sample data.
        Expenses logged here are kept only for the
        current session.
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

columns = st.columns(5)

features = [
    (
        "💸",
        "Expenses",
        "Log and organize spending"
    ),
    (
        "📊",
        "Budgets",
        "Check category budgets"
    ),
    (
        "💱",
        "Currency",
        "Convert supported currencies"
    ),
    (
        "🎯",
        "Savings",
        "Plan savings goals"
    ),
    (
        "💡",
        "Tips",
        "Get practical money tips"
    ),
]

for column, feature in zip(columns, features):

    icon, title, description = feature

    with column:

        st.markdown(
            f"""<div class="feature-card">
<div class="feature-icon">{icon}</div>
<div class="feature-title">{title}</div>
<div class="feature-description">{description}</div>
</div>""",
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
                "I want to save 50000 PKR and "
                "can save 10000 PKR per month. "
                "How long will it take?"
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
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# ============================================================
# CHAT INPUT
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
# PROCESS USER QUERY
# ============================================================

if user_input:

    # --------------------------------------------------------
    # USER MESSAGE
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )

    with st.chat_message("user"):

        st.markdown(user_input)

    # --------------------------------------------------------
    # ASSISTANT RESPONSE
    # --------------------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner("🤔 Thinking..."):

            try:

                answer = run_agent(
                    user_input
                )

                st.markdown(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                    }
                )

            except Exception as e:

                friendly_error = (
                    "I couldn't process that request. "
                    "Please try again."
                )

                st.error(
                    friendly_error
                )

                with st.expander(
                    "Show technical details"
                ):

                    st.code(
                        str(e)
                    )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": friendly_error,
                    }
                )
