# Real Estate Project Summary

This project aims to build a real estate price prediction. The project follows these major steps:

## Project Steps

1. **Data Collection:** Fetching real estate datasets from various sources to build a comprehensive dataset for analysis.

2. **Exploratory Data Analysis (EDA):** Analyzing and exploring the collected data to gain insights into real estate trends, pricing, location-based analysis, etc.

3. **Machine Learning Model Creation:** Developing predictive models using machine learning algorithms to forecast real estate prices or any other relevant predictions.

4. **Model Serialization:** Saving the trained machine learning model into a pickle file for easy reusability and deployment.

5. **Flask Web Application:** Creating a user-friendly web interface using Flask to interact with the machine learning model and visualize predictions.

6. **Load Balancing with Nginx:** Implementing Nginx as a load balancer to efficiently distribute incoming web traffic among multiple servers for better performance and scalability.

7. **Deployment on AWS Server:** Deploying the Flask web application, along with Nginx for load balancing, on an AWS server to make it publicly accessible.


- `/artifacts`: Contains loaction name and Saved machine learning models.
- `/static`: Contain CSS and JS file.
- `/templates`: Contain HTML file.
- `/server.py` : server.py file contain flask application
- `/util.py` : util.py file contain backend logic of the application

## Usage

To run the project locally:

1. Clone the repository.
2. Set up the Python environment with dependencies (requirements.txt).
3. Follow the instructions in the `/webapp` directory to start the Flask application.

## Contributors

- [Kashif Malik](https://www.linkedin.com/in/kashif-malik-2924a9258/)
