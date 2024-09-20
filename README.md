# Chatbot for Management System

This repository contains a **Faculty Management System Chatbot** that helps students, faculty, and administrative staff manage various academic and administrative processes through an AI-powered conversational interface. The chatbot is designed to respond to queries about courses, GPA, summer programs, exams, sports activities, and more, streamlining the interaction between users and the university's management system.

## Features

- **Student Assistance**: 
  - Provides information on course registration, credit hours, and GPA calculations.
  - Helps students with details on summer courses, including registration deadlines and fees.
  - Answers common questions about exams, grades, and results.

- **Administrative Support**:
  - Offers guidance on the appeals process, military education, and result retrieval.
  - Helps users find the right academic advisor based on their year of study.
  
- **Extracurricular Activities**:
  - Provides information on sports activities and how to join university teams.

- **Technical Support**:
  - Offers basic guidance on solving administrative and technical problems related to the faculty.

## Dataset

The chatbot is trained on data provided in the `intents.json` file, which contains different categories of queries (intents) such as:

- **greeting**: Responds to greetings.
- **Thanks**: Handles expressions of gratitude.
- **Summer Course**: Provides information about summer course registration, fees, and duration.
- **GPA**: Answers questions related to GPA calculation and improvement.
- **Exams & Grades**: Answers queries about exam schedules and grading.
- **Technical Support**: Guides users on how to seek technical assistance.

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/M-craspo/Chatbot-for-Management-System-.git
   ```

2. **Install Dependencies**:
   The chatbot uses Python, TensorFlow, and TFLearn. Install the necessary libraries using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Chatbot**:
   After installing the dependencies, run the chatbot script:
   ```bash
   python main.py
   ```

4. **Interact with the Chatbot**:
   You can start asking questions related to the faculty management system, such as:
   - "How do I register for summer courses?"
   - "What is my GPA estimate?"
   - "When are the final exams for discrete mathematics?"

## File Structure

- `intents.json`: The dataset containing various patterns (user inputs) and responses for the chatbot.
- `main.py`: The main Python script that runs the chatbot, builds the machine learning model, and handles interactions.
- `data.pickle`: Stores preprocessed data to avoid regenerating the model every time the chatbot runs.
- `model.tflearn`: The trained model file saved by TensorFlow.

## Technologies Used

- **Python**: The programming language used to build the chatbot.
- **TensorFlow**: Used to create the deep learning model for the chatbot.
- **TFLearn**: High-level abstraction for building and training the neural network.
- **NLTK**: Natural Language Toolkit for text preprocessing and tokenization.
