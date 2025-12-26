# 📚 Personalized Learning Recommendation Engine

## Overview

The Personalized Learning Recommendation Engine is an AI-driven system designed to recommend relevant learning content to students based on their individual learning behavior, performance trends, and interests. Unlike traditional e-learning platforms that follow a one-size-fits-all approach, this system adapts recommendations to each learner and provides explainable insights.

The project demonstrates a complete machine learning pipeline, including data preparation, recommendation logic, evaluation, visualization, and cloud deployment.

---

## Problem Description

Most online learning platforms recommend identical learning material to all users regardless of their learning pace, interests, or weaknesses. This lack of personalization leads to low engagement, inefficient learning paths, and difficulty in identifying suitable next learning steps.

There is a need for an intelligent system that can analyze student behavior and performance data to generate personalized and transparent learning recommendations.

---

## Proposed Solution

This project implements an AI-powered recommendation system that:
- Analyzes student activity such as courses viewed and time spent
- Uses quiz performance to detect skill gaps
- Generates Top-N personalized course recommendations
- Provides explanations for every recommendation
- Visualizes learning patterns through an interactive dashboard

---

## System Design & Workflow

The system is designed as a modular pipeline:

1. **Data Collection & Preparation**  
   Synthetic datasets are created to simulate real student behavior while maintaining privacy.

2. **Recommendation Engine**  
   A content-based or hybrid recommendation approach is used to match student profiles with relevant learning content.

3. **Evaluation & Explainability**  
   Recommendations are evaluated using Precision@K and Recall@K, and explanations are generated using rule-based logic.

4. **Visualization & Deployment**  
   The final system is presented through an interactive Streamlit interface and deployed as a live web application.

---

## Dataset Details

Due to the unavailability of real student data, synthetic datasets were generated.

### Dataset Files
- **students.csv**: Student IDs, names, learning levels  
- **courses.csv**: Course topics, difficulty levels  
- **interactions.csv**: Course views and time spent  
- **quizzes.csv**: Quiz scores used to identify skill gaps  

All datasets are stored in the `data/` directory.

---

## Recommendation Methodology

- **Content-Based Filtering**  
  Matches student interests and performance with course topics.

- **Hybrid Recommendation Logic**  
  Enhances recommendations by incorporating similarities among learners.

- **Explainability Layer**  
  Generates reasons such as low quiz scores, high interest areas, or skill gaps for each recommendation.

---

## Evaluation Strategy

The system uses offline evaluation to assess recommendation quality.

### Metrics Used
- **Precision@K** – Measures relevance of recommended items  
- **Recall@K** – Measures coverage of relevant learning content  

These metrics are suitable for educational recommendation systems where exploration is important.

---

## User Interface

The application interface is built using Streamlit and includes:
- Student selection dropdown  
- Visualization of learning behavior  
- Skill-gap indicators  
- Personalized recommendations with explanations  

---

## Deployment Details

The project is deployed using Streamlit Cloud.

🔗 Live Application:  
https://personalized-learning-recommender-8ql5jadu6wnz7e8zu2kh3x.streamlit.app/

The source code is version-controlled using GitHub.

---

## Technology Stack

- **Programming Language:** Python  
- **Data Handling:** Pandas, NumPy  
- **Recommendation Logic:** Content-based & Hybrid Filtering  
- **Evaluation Metrics:** Precision@K, Recall@K  
- **Visualization & UI:** Streamlit, Matplotlib  
- **Deployment:** GitHub, Streamlit Cloud  

---

## Project Structure

```
personalized-learning-recommender/
│
├── app.py
├── requirements.txt
│
├── data/
│   ├── students.csv
│   ├── courses.csv
│   ├── interactions.csv
│   └── quizzes.csv
```

---

## Local Setup Instructions

```bash
git clone https://github.com/DIVYA-SREE-it/personalized-learning-recommender
cd personalized-learning-recommender
pip install -r requirements.txt
streamlit run app.py
```

---

## Impact & Benefits

- Personalized learning experience  
- Improved student engagement  
- Early identification of learning weaknesses  
- Transparent and explainable AI recommendations  
- Practical demonstration of AI in education  

---

## SDG Alignment

- **SDG 4 – Quality Education**: Promotes personalized and inclusive learning  
- **SDG 9 – Industry, Innovation & Infrastructure**: Encourages AI-based education systems  
- **SDG 10 – Reduced Inequalities**: Adapts learning paths for different skill levels  

---

## Future Scope

- Integration with real-world LMS data  
- Feedback-driven recommendation improvement  
- Database-backed storage for scalability  
- Advanced machine learning models  

---

## Conclusion

This project successfully demonstrates an end-to-end personalized learning recommendation system that integrates data analysis, AI-driven recommendations, evaluation, visualization, and deployment. It serves as a strong academic project and a practical portfolio artifact.

---

## Author

**Divya Sree R**  
B.Tech – Information Technology
