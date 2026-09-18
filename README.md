# 💼 CareerGenie — AI Career Advisor

CareerGenie is a **multi-turn AI-powered career advisor chatbot** built using **LangChain, Google Gemini, Python, and Streamlit**.

The chatbot helps users with career planning, Data Analytics, Business Analytics, Software Development, AI/ML, resume preparation, interview preparation, skill-gap analysis, and learning roadmaps.

---

## 🚀 Project Overview

CareerGenie is designed as a domain-specific conversational AI application.

Instead of treating every user message as an independent question, CareerGenie maintains the **conversation history**, allowing users to ask follow-up questions naturally.

### Example

**User:**

> I am a BTech CSE graduate.

**CareerGenie:**

> You can explore several technology career paths...

**User:**

> I want to become a Data Analyst.

**CareerGenie:**

> You should focus on SQL, Excel, Power BI, Python, and statistics...

**User:**

> I already know Python and Power BI.

**CareerGenie:**

> In that case, your next focus should be SQL, statistics, and portfolio projects...

The chatbot uses the previous conversation to provide more relevant responses.

---

## 🎯 Objectives

The main objectives of this project are:

* Build a domain-specific AI chatbot
* Integrate Google Gemini with LangChain
* Implement multi-turn conversations
* Apply prompt engineering techniques
* Build a user-friendly Streamlit interface
* Secure API credentials using environment variables
* Implement error handling and fallback responses
* Add application logging
* Separate UI, business logic, prompts, and API integration
* Demonstrate a scalable project structure

---

## 🧠 Key Features

### 1. Multi-Turn Conversation

CareerGenie maintains the conversation history so users can ask follow-up questions without repeating their background.

### 2. Google Gemini Integration

The application uses Google's Gemini model to generate natural-language responses.

### 3. LangChain

LangChain is used as the orchestration layer between the application and Gemini.

It handles:

* Message formatting
* System prompts
* Human messages
* AI messages
* LLM invocation

### 4. Advanced Prompt Engineering

A structured system prompt defines:

* AI role
* Domain
* Behavior
* Response style
* Domain constraints
* Career-related responsibilities

### 5. Streamlit I
