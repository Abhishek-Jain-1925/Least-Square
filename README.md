# Least-Square

🚗 *A Streamlit WebApp that predicts the price of a used car using various regression models. This project follows the complete life cycle of a data science project, including data scraping, cleaning, feature engineering, exploratory data analysis, model training, hyperparameter tuning, and deployment. The Tech Stack includes Machine Learning, Regression, Linear Regression, Polynomial Regression, Lasso Regression, Ridge Regression, and Streamlit. Data was scraped from Cars24.com using Octoparse, and the project was containerized using Docker and deployed on Render.* 📊🔧🔬

## Objective

The objective of this project is to develop a web application that can accurately predict the price of a used car based on its features and specifications. By utilizing regression models and machine learning techniques, the web application provides users with an estimate of the fair market value for a particular used car, aiding in the decision-making process for both buyers and sellers. 💰🚙🎯

## Features

- **Regression Models:** The web application utilizes various regression models such as Linear Regression, Lasso Regression, and Ridge Regression to predict the price of a used car. 📈🔍

- **Data Scraping:** The initial dataset was scraped from Cars24.com using Octoparse, extracting relevant information about used cars, including features, specifications, and prices. 🕷️📊

- **Data Cleaning and Feature Engineering:** The scraped data was cleaned and processed to handle missing values, outliers, and categorical variables. Feature engineering techniques were employed to extract useful information and create meaningful features. 🧹🔧💡

- **Exploratory Data Analysis:** Visualizations and statistical analysis were performed to gain insights into the relationships between features and the target variable, identify patterns, and understand the data distribution. 📊📉📈

- **Hyperparameter Tuning:** The regression models were fine-tuned by exploring different hyperparameter combinations using techniques like cross-validation to optimize their performance and enhance prediction accuracy. 🎛️🔬🔍

- **CICD Pipeline:** A Continuous Integration and Continuous Deployment (CICD) pipeline was established to automate the model training and deployment process, ensuring seamless updates and efficient workflow. ⚙️🚀

- **Dockerization:** The project was containerized using Docker, providing a consistent and reproducible environment for running the web application. 🐳🚀

- **Deployment:** The containerized web application was deployed on the Render platform, making it accessible to users via a web interface. 🌐🚀

## Tech Stack

The project leverages the following technologies and techniques:

- Machine Learning: Utilized regression models for predicting car prices based on features.

- Regression: Employed various regression techniques such as Linear Regression, Polynomial Regression, Lasso Regression, and Ridge Regression.

- Streamlit: Built the web application interface using the Streamlit framework to provide an interactive and user-friendly experience.

## Installation and Setup

To run the Used Car Price Prediction WebApp locally, follow these steps:

1. Clone the repository to your local machine.
   
>git clone https://github.com/Abhishek-Jain-1925/Least-Square.git


2. Navigate to the project directory.

>cd Least-Square


3. Create a virtual environment and activate it.

>python3 -m venv env
>source env/bin/activate


4. Install the required dependencies.

>pip install -r requirements.txt


5. Run the Streamlit app.

>streamlit run app.py

6. Access the web application by visiting `http://localhost:8501` in your web browser.



## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make the necessary changes and commit your code.

4. Push your changes to your forked repository.

5. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The project is inspired by the need for accurate used car price predictions and aims to provide users with valuable insights into the fair market value of used cars. 🚀🌟

---

👤 **Author**

- Mr.Abhishek Sachin Dhondalkar(Fergusson College, Pune.)
- Email: jainabhishek1925@gmail.com
- LinkedIn: [Abhishek Dhondalkar](https://www.linkedin.com/in/janedoe/](https://www.linkedin.com/in/abhishek-dhondalkar-7ab14220b))

---

Feel free to reach out to us if you have any questions or need further assistance. We hope you find the Used Car Price Prediction WebApp useful and insightful! 🚗💰📊



