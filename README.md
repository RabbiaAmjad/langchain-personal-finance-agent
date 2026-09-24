# 💰 Personal Finance Assistant Agent

An AI-powered Personal Finance Assistant built using **LangChain Agents, AWS Bedrock, and function calling**. The agent can understand a user's financial request and automatically select the appropriate tool or combination of tools to complete the task.

## 🚀 Project Overview

The Personal Finance Assistant supports common financial tasks such as:

* Logging expenses
* Checking budget status
* Converting currencies
* Calculating savings goals
* Providing spending tips

The agent can also handle queries that require **multiple tools in a single interaction**.

### Agent Workflow

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

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **LangChain Agents**
* **AWS Bedrock**
* **Amazon Nova 2 Lite**
* **Function Calling / Tool Use**
* **Jupyter Notebook**

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

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/personal-finance-assistant-agent.git
cd personal-finance-assistant-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Open the notebook

Open:

```text
Personal_Finance_Assistant_Agent.ipynb
```

using Jupyter Notebook, JupyterLab, or another compatible environment.

### 4. Configure AWS Bedrock

Configure the AWS Bedrock credentials in the notebook's configuration section.

### 5. Run the notebook

Run the cells sequentially to:

* Install and import dependencies
* Configure AWS Bedrock
* Initialize the LLM
* Define the five tools
* Test the tools individually
* Create the Personal Finance Agent
* Run sample queries
* Test a compound query

## 📸 Sample Outputs

### Query 1 — Currency Conversion + Expense

![Query 1](screenshots/query-1-expense-currency.png)

### Query 2 — Budget Status

![Query 2](screenshots/query-2-budget-status.png)

### Query 3 — Savings Goal

![Query 3](screenshots/query-3-savings-goal.png)

### Query 4 — Spending Tip

![Query 4](screenshots/query-4-spending-tip.png)

### Query 5 — Expense + Budget

![Query 5](screenshots/query-5-expense-budget.png)

### Compound Query

![Compound Query](screenshots/compound-query.png)

## 📁 Project Structure

```text
personal-finance-assistant-agent/
│
├── Personal_Finance_Assistant_Agent.ipynb
├── README.md
├── requirements.txt
├── .gitignore
│
└── screenshots/
    ├── query-1-expense-currency.png
    ├── query-2-budget-status.png
    ├── query-3-savings-goal.png
    ├── query-4-spending-tip.png
    ├── query-5-expense-budget.png
    └── compound-query.png
```

## 👩‍💻 Author

**Rabbia Amjad**
B.Sc. Business Data Analytics
COMSATS University Islamabad
