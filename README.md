# 💰 Personal Finance Assistant Agent

An AI-powered personal finance assistant built with **LangChain Agents, AWS Bedrock, and function calling**.

The project demonstrates how an AI agent can understand a user's natural-language financial request, decide which tool or combination of tools is needed, execute those tools, and return a useful response.

> **Built as part of the Gen AI Bootcamp — Session 5: LangChain Agents & Function Calling | AWS Bedrock.**

---

## 🎯 Project Overview

Traditional programs usually follow a predefined flow: the developer decides which function should run for a particular input.

This project demonstrates a different approach.

The **LLM acts as the decision-maker**. Based on the user's request, the agent determines which financial tool should be called and can use multiple tools when a request involves more than one task.

### Agent Workflow

```text
User Query
     ↓
AWS Bedrock LLM
     ↓
Agent determines required tool(s)
     ↓
Tool execution
     ↓
Tool result
     ↓
Final response
```

For example:

> "I spent 50 USD on food today, convert it to PKR and log it."

The agent can determine that the request requires:

```text
convert_currency
       ↓
calculate_expense
```

---

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **LangChain Agents**
* **AWS Bedrock**
* **Amazon Nova 2 Lite**
* **Function Calling / Tool Use**
* **Jupyter Notebook**

---

## 🔧 Tools Implemented

The agent is equipped with five financial tools.

### 1. `calculate_expense`

Logs an expense using the amount, category, description, and current date.

**Parameters:**

* `amount`
* `category`
* `description`

---

### 2. `get_budget_status`

Checks the remaining monthly budget for a selected spending category.

**Supported categories:**

* Food
* Transport
* Entertainment
* Shopping

---

### 3. `convert_currency`

Converts an amount between supported currencies using predefined exchange rates.

**Supported currencies:**

* USD
* PKR
* EUR
* GBP

No external currency API is required for this tool.

---

### 4. `calculate_savings_goal`

Calculates the number of months required to reach a savings target based on the amount the user can save each month.

**Parameters:**

* `target_amount`
* `monthly_savings`

---

### 5. `get_spending_tip`

Provides a practical money-saving tip based on the spending category where the user is overspending.

---

## 🤖 Agent Capabilities

The Personal Finance Assistant can:

* 💸 Log expenses
* 📊 Check category budgets
* 💱 Convert currencies
* 🎯 Calculate savings timelines
* 💡 Provide spending tips
* 🔗 Combine multiple tools for a single request

The key feature of the project is **tool selection**: users do not need to specify which function should be used. They can simply describe what they want in natural language.

---

## 🧪 Example Queries

### Expense + Currency Conversion

```text
I spent 50 USD on food today, convert it to PKR and log it.
```

### Budget Status

```text
What is my remaining budget for entertainment?
```

### Savings Goal

```text
I want to save 100,000 PKR. I can save 10,000 per month.
When will I reach my goal?
```

### Spending Tip

```text
I keep overspending on food, give me a money-saving tip.
```

### Expense + Budget

```text
Log 2000 PKR for transport and show my transport budget status.
```

### Compound Query

```text
I want to save 60,000 PKR by reducing my food spending.
Give me a food-saving tip and tell me how many months it
will take if I save 10,000 PKR every month.
```

The compound queries demonstrate that the agent can select and use **multiple tools within a single interaction**.

---

## 📂 Project Structure

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

---

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

The notebook requires access to **AWS Bedrock**.

Add your own AWS Bedrock credentials/token in the configuration section of the notebook before running the agent.

**Never commit real API keys, access tokens, passwords, or other credentials to GitHub.**

### 5. Run the notebook

Run the cells sequentially to:

1. Install/import dependencies
2. Configure AWS Bedrock
3. Initialize the LLM
4. Define the five tools
5. Test each tool individually
6. Create the Personal Finance Agent
7. Run the required sample queries
8. Test the compound query

---

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

---

## 🔐 Security Note

This repository does **not** contain AWS credentials.

If you run this project locally, use your own AWS Bedrock credentials and keep them outside version control.

---

## 📌 Project Scope

This is an **educational prototype** demonstrating LangChain agents and function calling.

The currency conversion uses fixed exchange rates and the budget values are predefined for demonstration purposes. The assistant is not intended to provide professional financial advice.

---

## 👩‍💻 Author

**Rabbia Amjad**

Business Data Analytics Student
COMSATS University Islamabad

Interested in **data analytics, AI, and building technology-driven solutions with practical impact.**
