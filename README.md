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

<img width="843" height="311" alt="Screenshot 2026-09-25 001622" src="https://github.com/user-attachments/assets/a79729b7-d341-414f-a49b-3a24f24b4254" />


### Query 2 — Budget Status

<img width="849" height="249" alt="Screenshot 2026-09-25 001637" src="https://github.com/user-attachments/assets/5d907751-04ab-47ba-b648-10865b558ec4" />


### Query 3 — Savings Goal

<img width="848" height="164" alt="Screenshot 2026-09-25 001706" src="https://github.com/user-attachments/assets/c974dfda-ba1b-4feb-8087-1ce723bbfcd9" />


### Query 4 — Spending Tip

<img width="851" height="218" alt="Screenshot 2026-09-25 001717" src="https://github.com/user-attachments/assets/9d376478-1345-4724-9db1-5d29bccf7c4a" />


### Query 5 — Expense + Budget

<img width="851" height="218" alt="Screenshot 2026-09-25 001717 - Copy" src="https://github.com/user-attachments/assets/6b666fb0-6862-4e07-93ac-ccf4578f4efe" />


### Compound Query

<img width="846" height="293" alt="Screenshot 2026-09-25 001743" src="https://github.com/user-attachments/assets/c0d86dec-fff2-4d68-b453-edbf6df94355" />


## 📁 Project Structure

```text
personal-finance-assistant-agent/
│
├── Personal_Finance_Assistant_Agent.ipynb
├── README.md
├── requirements.txt
├── .gitignore

```

## 👩‍💻 Author

**Rabbia Amjad**
B.Sc. Business Data Analytics
COMSATS University Islamabad
