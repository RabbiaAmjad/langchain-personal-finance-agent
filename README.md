# 💰 Personal Finance Assistant Agent

<p align="center">
  <strong>AI-powered personal finance assistant built with LangChain, AWS Bedrock, and Streamlit</strong>
</p>

<p align="center">
  An intelligent financial assistant that understands natural-language requests, selects the appropriate tools, and can combine multiple tools to complete compound queries.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Agent-green)
![AWS Bedrock](https://img.shields.io/badge/AWS-Bedrock-orange?logo=amazon-aws&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white)
![License](https://img.shields.io/badge/Project-Academic-lightgrey)

</p>

<p align="center">

🚀 **https://langchain-personal-finance-agent-dtdkjzezwqzupfwtoz8mus.streamlit.app/**

</p>

---

## 📌 Overview

The **Personal Finance Assistant Agent** is an AI-powered application designed to help users with common personal finance tasks through natural-language interaction.

The agent uses **LangChain Agents**, **AWS Bedrock**, and **function calling / tool use** to analyze a user's request and automatically select the appropriate financial tool or combination of tools.

The project includes both:

- 📓 A **Jupyter Notebook** containing the complete agent implementation
- 💻 An interactive **Streamlit web application** for user-friendly interaction

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 AI Agent | Understands natural-language financial requests |
| 💰 Expense Tracking | Logs expenses with relevant details |
| 📊 Budget Analysis | Checks budget, spending, and remaining amounts |
| 💱 Currency Conversion | Converts amounts between supported currencies |
| 🎯 Savings Goals | Calculates the time required to reach a savings target |
| 💡 Spending Tips | Provides practical spending-related tips |
| 🔗 Compound Queries | Can use multiple tools for a single request |
| 💻 Streamlit UI | Provides an interactive web interface |
| ☁️ AWS Bedrock | Uses Amazon Bedrock for the language model |

---

## 🚀 Live Demo

The Personal Finance Assistant is deployed as an interactive Streamlit application.

### 👉 [Open the Personal Finance Assistant]- https://langchain-personal-finance-agent-dtdkjzezwqzupfwtoz8mus.streamlit.app/

The application allows users to enter natural-language queries and receive responses from the AI-powered financial agent.

### Example

```text
I spent $50 on groceries. What is my remaining food budget?
```

The agent can recognize that this request requires more than one operation and use the appropriate tools to process it.

> **Note:** Budget and spending figures in the application are based on the project's sample/demo data. Expenses logged through the application are maintained only for the current session.

---

# 🧠 How the Agent Works

The agent follows a tool-selection workflow:

```text
                    ┌─────────────────┐
                    │    User Query   │
                    └────────┬────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │  LLM Analyzes Query  │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Selects Tool(s)      │
                  └──────────┬───────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
          Expense          Budget        Currency
           Tool             Tool           Tool
              │              │              │
              └──────────────┼──────────────┘
                             │
                    ┌────────┴────────┐
                    │                 │
                    ▼                 ▼
                 Savings           Spending
                  Goal               Tip
                  Tool               Tool
                    │                 │
                    └────────┬────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │   Final AI Response  │
                  └──────────────────────┘
```

For compound queries, the agent can determine that multiple tools are needed and process the request accordingly.

---

# 🏗️ Architecture

```text
                         USER
                           │
                           ▼
                ┌─────────────────────┐
                │  Streamlit /        │
                │  Jupyter Interface  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   LangChain Agent   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   AWS Bedrock LLM   │
                │  Amazon Nova 2 Lite │
                └──────────┬──────────┘
                           │
                           ▼
              ┌────────────────────────────┐
              │       Tool Selection       │
              └─────────────┬──────────────┘
                            │
       ┌────────────────────┼────────────────────┐
       │                    │                    │
       ▼                    ▼                    ▼
 Calculate Expense    Budget Status       Convert Currency
       │                    │                    │
       └────────────────────┼────────────────────┘
                            │
                   ┌────────┴────────┐
                   │                 │
                   ▼                 ▼
          Calculate Savings     Get Spending Tip
               Goal
                   │                 │
                   └────────┬────────┘
                            │
                            ▼
                    Final Response
```

---

# 🛠️ Technology Stack

- **Python**
- **LangChain**
- **LangChain Agents**
- **AWS Bedrock**
- **Amazon Nova 2 Lite**
- **Function Calling / Tool Use**
- **Boto3**
- **Streamlit**
- **Jupyter Notebook**

---

# 🔧 Available Tools

The agent includes five specialized financial tools.

| # | Tool | Purpose |
|---|---|---|
| 1 | `calculate_expense` | Logs an expense with amount, category, description, and date |
| 2 | `get_budget_status` | Checks budget, spending, and remaining amount |
| 3 | `convert_currency` | Converts an amount between supported currencies |
| 4 | `calculate_savings_goal` | Calculates months required to reach a savings target |
| 5 | `get_spending_tip` | Provides a practical spending-related tip |

---

## 1. 💳 Calculate Expense

Logs an expense with its:

- Amount
- Category
- Description
- Date

Example:

```text
I spent $50 on groceries.
```

---

## 2. 📊 Get Budget Status

Checks the current budget status for a selected category.

The tool provides information about:

- Budget amount
- Current spending
- Remaining amount

Example:

```text
What is my food budget status?
```

---

## 3. 💱 Convert Currency

Converts an amount between supported currencies using predefined exchange rates.

Example:

```text
Convert 100 USD to EUR.
```

---

## 4. 🎯 Calculate Savings Goal

Calculates how many months are required to reach a savings target based on a monthly savings amount.

Example:

```text
How many months will it take to save $5000
if I save $500 every month?
```

---

## 5. 💡 Get Spending Tip

Provides a practical money-saving tip based on a selected spending category.

Example:

```text
Give me a spending tip for groceries.
```

---

# 🔗 Compound Queries

One of the key capabilities of the agent is handling **compound queries** that require multiple tools.

For example:

```text
I spent $50 on groceries. What is my remaining food budget?
```

The agent can:

```text
User Query
    ↓
Calculate Expense
    ↓
Update / Process Spending
    ↓
Get Budget Status
    ↓
Generate Final Response
```

This demonstrates the agent's ability to reason about a request and use multiple tools when required.

---

# 💻 Streamlit Application

The project includes an interactive Streamlit interface designed to make the financial agent easier to use.

The interface includes:

- 💰 Personal Finance Assistant branding
- 💬 Natural-language query input
- 🛠️ Available tool information
- 📊 Financial task support
- 🔗 Compound query support
- ℹ️ Demo-mode information
- Session-based expense interaction

### Example Queries

```text
Convert 100 USD to EUR.
```

```text
What is my food budget status?
```

```text
How many months will it take to save $5000
if I save $500 every month?
```

```text
Give me a spending tip for groceries.
```

```text
I spent $50 on groceries. What is my remaining food budget?
```

---

# 📸 Streamlit Application

Screenshots of the deployed Streamlit application:

<img width="959" height="436" alt="image" src="https://github.com/user-attachments/assets/e93b9d42-c271-4133-9f9c-b28143bae0af" />

<img width="959" height="433" alt="image" src="https://github.com/user-attachments/assets/94a97701-10d6-486a-9c93-6d67da16b487" />



---

# 📓 Jupyter Notebook

The Jupyter Notebook contains the complete development and implementation of the Personal Finance Assistant Agent.

The notebook demonstrates:

- Installing and importing dependencies
- Configuring AWS Bedrock
- Initializing the LLM
- Defining the five financial tools
- Testing tools individually
- Creating the LangChain agent
- Running sample queries
- Testing compound queries

### Notebook

```text
Personal_Finance_Assistant_Agent.ipynb
```

The notebook can be opened using:

- Jupyter Notebook
- JupyterLab
- VS Code
- Another compatible Jupyter environment

---

# ⚙️ Installation & Setup

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

---

## 3. Configure AWS Bedrock

This project uses **AWS Bedrock** to access the language model.

For local execution, configure your AWS credentials according to your AWS environment and the configuration used by the application.

**Never commit AWS credentials, API keys, or secret configuration files to GitHub.**

---

## 4. Run the Jupyter Notebook

Open:

```text
Personal_Finance_Assistant_Agent.ipynb
```

Run the notebook cells sequentially to:

1. Install/import dependencies
2. Configure AWS Bedrock
3. Initialize the language model
4. Define the five tools
5. Test the tools
6. Create the agent
7. Run sample queries
8. Test compound queries

---

# 🌐 Run Streamlit Locally

To run the web application locally:

```bash
streamlit run app.py
```

Streamlit will start the application and provide a local URL in the terminal.

Open that URL in your browser to interact with the Personal Finance Assistant.

---

# 🔐 Security & Credentials

Sensitive credentials must not be stored in the GitHub repository.

The project does **not** include:

- ❌ AWS access keys
- ❌ AWS secret keys
- ❌ API keys
- ❌ `.env` files containing credentials
- ❌ `secrets.toml` files containing credentials

For the deployed Streamlit application, sensitive configuration should be stored using **Streamlit Secrets**.

The repository's `.gitignore` file also helps prevent sensitive and unnecessary files from being committed.

---

# 📸 Sample Outputs

The following screenshots demonstrate the agent handling the required queries.

## Query 1 — Currency Conversion + Expense

<img width="843" height="311" alt="Screenshot 2026-09-25 001622" src="https://github.com/user-attachments/assets/25b3bfdf-1a8c-4491-99c4-b61f8d228f41" />


---

## Query 2 — Budget Status

<img width="849" height="249" alt="Screenshot 2026-09-25 001637" src="https://github.com/user-attachments/assets/12cfb6b7-e280-44fa-b1f8-546b9dede2d2" />


---

## Query 3 — Savings Goal

<img width="848" height="164" alt="Screenshot 2026-09-25 001706" src="https://github.com/user-attachments/assets/c85c72a9-e80d-495a-80cd-3b56ba41a828" />


---

## Query 4 — Spending Tip

<img width="851" height="218" alt="Screenshot 2026-09-25 001717 - Copy" src="https://github.com/user-attachments/assets/dd396bc4-6c36-40d0-bc12-083315653acf" />


---

## Query 5 — Expense + Budget

<img width="845" height="325" alt="Screenshot 2026-09-25 001729" src="https://github.com/user-attachments/assets/44afbfa2-11b3-4b68-afb1-243b34817731" />


---

## Compound Query

<img width="846" height="293" alt="Screenshot 2026-09-25 001743" src="https://github.com/user-attachments/assets/a02af2b2-5b5b-4b7f-87f7-db5a1777ef05" />


---

# 🧪 Testing

The project was tested using individual queries for all five tools and a compound query involving multiple tools.

The testing demonstrates that the agent can:

- Understand natural-language financial requests
- Identify the intended financial task
- Select the appropriate tool
- Pass the required parameters
- Process tool results
- Generate a natural-language response
- Use multiple tools when required

---

# 🎯 Project Objectives

The main objectives of this project are to demonstrate:

1. Building an AI agent using LangChain
2. Integrating an LLM through AWS Bedrock
3. Creating and registering custom tools
4. Using function calling / tool use
5. Allowing an agent to select tools dynamically
6. Handling compound queries using multiple tools
7. Building an interactive Streamlit interface
8. Deploying an AI application for demonstration

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

```

---

## 📄 File Description

| File / Folder | Description |
|---|---|
| `app.py` | Streamlit application for interacting with the finance agent |
| `Personal_Finance_Assistant_Agent.ipynb` | Complete Jupyter Notebook implementation |
| `requirements.txt` | Python dependencies required by the project |
| `.gitignore` | Prevents unnecessary and sensitive files from being committed |
| `screenshots/` | Screenshots demonstrating agent outputs and the Streamlit application |
| `README.md` | Project documentation |

---

# 📚 Project Deliverables

This project includes:

- ✅ Jupyter Notebook with the complete agent implementation
- ✅ Five functional financial tools
- ✅ Individual tool demonstrations
- ✅ Compound query demonstration
- ✅ Streamlit interactive application
- ✅ GitHub repository
- ✅ Project documentation
- ✅ Screenshots of sample outputs

---

# 👩‍💻 Author

### Rabbia Amjad

**B.Sc. Business Data Analytics**  
**COMSATS University Islamabad**

---

<p align="center">
  Made with 🐍 Python, 🤖 LangChain, ☁️ AWS Bedrock, and 💻 Streamlit
</p>
