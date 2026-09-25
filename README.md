# 💰 Personal Finance Assistant Agent

An AI-powered Personal Finance Assistant built using **LangChain Agents, AWS Bedrock, and function calling**.

The agent understands a user's financial request and automatically selects the appropriate tool or combination of tools to complete the task. The project is implemented in a Jupyter Notebook and is also available through an interactive **Streamlit web application**.

---

## 🚀 Live Demo

Try the deployed Streamlit application:

👉 **[Open the Personal Finance Assistant](YOUR_STREAMLIT_URL)**

The web application provides an interactive interface where users can enter natural-language financial queries and receive responses from the AI agent.

> **Note:** The application uses AWS Bedrock credentials configured through Streamlit secrets. No AWS credentials or API keys are stored in the GitHub repository.

---

## 📌 Project Overview

The Personal Finance Assistant supports common financial tasks such as:

- Logging expenses
- Checking budget status
- Converting currencies
- Calculating savings goals
- Providing spending tips

The agent can also handle **compound queries** that require multiple tools in a single interaction.

For example, a user can ask a question that requires an expense to be processed and then have the budget status calculated.

---

## ✨ Features

### 🤖 AI-Powered Agent

The application uses a LangChain agent with **AWS Bedrock** to understand natural-language financial requests and determine which tool or tools are required.

### 🛠️ Five Financial Tools

The agent includes five specialized tools:

1. Calculate Expense
2. Get Budget Status
3. Convert Currency
4. Calculate Savings Goal
5. Get Spending Tip

### 🔗 Multi-Tool / Compound Queries

The agent can use more than one tool when a user's request requires multiple operations.

### 💻 Interactive Streamlit Interface

The project includes a Streamlit web application with:

- Interactive chat-style input
- Financial assistant interface
- Tool descriptions
- Sample queries
- Session-based expense tracking
- User-friendly responses

### 📓 Jupyter Notebook Implementation

The complete agent implementation and tool development are documented in the Jupyter Notebook.

---

## 🧠 Agent Workflow

The overall workflow is:

```text
User Query
    ↓
LLM analyzes the request
    ↓
Selects the appropriate tool(s)
    ↓
Tool executes the required operation
    ↓
LLM processes the result
    ↓
Final Response
```

For a compound query, the agent can determine that multiple tools are required and execute the appropriate sequence of operations.

---

## 🏗️ Architecture

The project has two main interfaces built around the same financial-agent concept:

```text
                    ┌──────────────────────┐
                    │      User Query      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Streamlit /        │
                    │   Jupyter Interface  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   LangChain Agent    │
                    │   + AWS Bedrock LLM  │
                    └──────────┬───────────┘
                               │
                  ┌────────────┼────────────┐
                  │            │            │
                  ▼            ▼            ▼
              Expense       Budget       Currency
               Tool          Tool          Tool
                  │            │            │
                  └────────────┼────────────┘
                               │
                  ┌────────────┴────────────┐
                  │                         │
                  ▼                         ▼
             Savings Goal              Spending Tip
                 Tool                      Tool
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Final Response    │
                    └──────────────────────┘
```

---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **LangChain Agents**
- **AWS Bedrock**
- **Amazon Nova 2 Lite**
- **Function Calling / Tool Use**
- **Jupyter Notebook**
- **Streamlit**
- **Boto3**

---

## 🔧 Available Tools

### 1. Calculate Expense

Logs an expense with its amount, category, description, and date.

### 2. Get Budget Status

Checks the budget, spending, and remaining amount for a selected category.

### 3. Convert Currency

Converts an amount between supported currencies using predefined exchange rates.

### 4. Calculate Savings Goal

Calculates how many months are required to reach a savings target based on a monthly savings amount.

### 5. Get Spending Tip

Provides a practical money-saving tip based on the selected spending category.

---

## 📋 Tool Summary

| Tool | Purpose |
|---|---|
| `calculate_expense` | Logs an expense |
| `get_budget_status` | Checks budget and remaining amount |
| `convert_currency` | Converts between supported currencies |
| `calculate_savings_goal` | Calculates time required to reach a savings target |
| `get_spending_tip` | Provides a spending-related financial tip |

---

# 💻 Streamlit Application

The Streamlit application provides a user-friendly interface for interacting with the Personal Finance Assistant.

Users can enter natural-language queries instead of directly calling individual Python functions.

### Example Queries

```text
Convert 100 USD to EUR.

What is my food budget status?

How many months will it take to save $5000
if I save $500 every month?

Give me a spending tip for groceries.

I spent $50 on groceries. What is my remaining
food budget?
```

The final example is a **compound query** because it requires more than one operation.

---

## 📸 Streamlit Application

The deployed application provides an interactive interface for submitting financial queries.

![Streamlit Application](screenshots/streamlit_app.png)

---

# 📓 Jupyter Notebook

The Jupyter Notebook contains the development and implementation of the Personal Finance Assistant agent.

The notebook demonstrates:

- Installing and importing dependencies
- Configuring AWS Bedrock
- Initializing the LLM
- Defining the five financial tools
- Testing tools individually
- Creating the LangChain agent
- Running sample queries
- Testing compound queries

Open:

```text
Personal_Finance_Assistant_Agent.ipynb
```

using Jupyter Notebook, JupyterLab, or another compatible environment.

---

# ⚙️ Setup & Installation

## 1. Clone the Repository

```bash
git clone https://github.com/RabbiaAmjad/langchain-personal-finance-agent.git
cd langchain-personal-finance-agent
```

---

## 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains the dependencies required by the project, including the libraries used for LangChain, AWS Bedrock, and Streamlit.

---

## 3. Configure AWS Bedrock

The project uses **AWS Bedrock** to access the language model.

For local notebook execution, configure your AWS credentials according to your AWS environment and the configuration used in the notebook.

**Do not commit AWS credentials, API keys, or secret configuration files to GitHub.**

---

## 4. Run the Jupyter Notebook

Open:

```text
Personal_Finance_Assistant_Agent.ipynb
```

Run the cells sequentially.

The notebook demonstrates the complete agent development process and tool functionality.

---

# 🌐 Run the Streamlit Application Locally

After installing the dependencies, run:

```bash
streamlit run app.py
```

Streamlit will start a local web server and provide a local URL in the terminal.

Open that URL in your browser to interact with the Personal Finance Assistant.

---

# 🔐 Security & Credentials

AWS credentials and API keys should **never be committed to the repository**.

The project uses environment-specific configuration for sensitive credentials.

For the deployed Streamlit application, sensitive values should be configured through **Streamlit Secrets** rather than being written directly into `app.py`.

The repository intentionally does not contain:

- AWS access keys
- AWS secret keys
- API keys
- `.env` files containing credentials
- `secrets.toml` files containing credentials

The `.gitignore` file is configured to help prevent sensitive files from being committed.

---

# 📸 Sample Outputs

The following screenshots demonstrate the agent handling the required sample queries.

## Query 1 — Currency Conversion + Expense

![Currency Conversion and Expense](screenshots/currency.png)

---

## Query 2 — Budget Status

![Budget Status](screenshots/budget.png)

---

## Query 3 — Savings Goal

![Savings Goal](screenshots/savings.png)

---

## Query 4 — Spending Tip

![Spending Tip](screenshots/spending_tip.png)

---

## Query 5 — Expense + Budget

![Expense and Budget](screenshots/expense.png)

---

## Compound Query

The agent can also handle a query that requires multiple tools.

![Compound Query](screenshots/compound_query.png)

This demonstrates the agent's ability to analyze a request and use multiple tools when necessary.

---

# 📁 Project Structure

```text
personal-finance-assistant-agent/
│
├── app.py
├── Personal_Finance_Assistant_Agent.ipynb
├── README.md
├── requirements.txt
├── .gitignore
│
└── screenshots/
    ├── streamlit_app.png
    ├── currency.png
    ├── budget.png
    ├── savings.png
    ├── spending_tip.png
    ├── expense.png
    └── compound_query.png
```

### File Description

| File / Folder | Description |
|---|---|
| `app.py` | Streamlit application for interacting with the finance agent |
| `Personal_Finance_Assistant_Agent.ipynb` | Complete Jupyter Notebook implementation |
| `requirements.txt` | Python dependencies required by the project |
| `.gitignore` | Prevents unnecessary and sensitive files from being committed |
| `screenshots/` | Screenshots demonstrating agent outputs and the Streamlit application |
| `README.md` | Project documentation |

---

# 🧪 Testing

The project was tested using individual queries for all five tools as well as a compound query involving multiple tools.

The tests demonstrate that the agent can:

- Identify the user's intended financial task
- Select the appropriate tool
- Pass the required parameters to the tool
- Process the tool result
- Return a natural-language response
- Use multiple tools for compound requests

---

# 🎯 Project Objectives

The main objectives of this project are to demonstrate:

1. Building an AI agent using LangChain
2. Integrating an LLM through AWS Bedrock
3. Creating and registering custom tools
4. Using function calling / tool use
5. Allowing an agent to select tools dynamically
6. Handling compound queries using multiple tools
7. Building an interactive interface with Streamlit
8. Deploying an AI application for public demonstration

---

# 👩‍💻 Author

**Rabbia Amjad**  
B.Sc. Business Data Analytics  
COMSATS University Islamabad
