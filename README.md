# 🚢 Titanic Survival Prediction

This repository contains a deployed machine learning model for predicting Titanic survival. The deployment includes:  

- **FastAPI** backend API serving predictions from a pre-trained logistic regression model.
- **Streamlit** frontend web application for interacting with the API.

The project is fully containerized using **Docker** and orchestrated with **docker-compose**.



---

## Setup and Run Locally


```bash
git clone <your_repo_url>
cd titanic-survival-prediction/code/deployment
docker-compose up --build
```
This will start two services:

FastAPI: http://localhost:8000

Streamlit: http://localhost:8501

## Use the application

Open your browser and go to http://localhost:8501 to interact with the Streamlit app.

The Streamlit app sends input data to the FastAPI backend and displays the prediction.
