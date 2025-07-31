# Income and Spending Survey Tool

This project is a comprehensive web application designed to collect, store, process, and visualize user data on income and spending habits. It was developed as a survey tool for a data analysis company in Washington, DC, to prepare for a new product launch in the healthcare industry.

The application features a user-friendly web form built with Flask and styled with Bootstrap, a MongoDB database for robust data storage, and a data analysis pipeline using Python's Pandas library and Jupyter Notebook for visualizations.

## Key Features

- **Modern Web Interface**: A clean, responsive, and user-friendly survey form built with **Flask** and styled professionally using **Bootstrap 5**.
- **Robust Data Storage**: Utilizes **MongoDB** to store user submissions, providing a flexible, NoSQL database solution.
- **Data Processing Pipeline**: A dedicated Python script (`data_processor.py`) fetches data from MongoDB and exports it into a clean CSV format, ready for analysis.
- **In-Depth Data Analysis**: A **Jupyter Notebook** (`data_analysis.ipynb`) uses Pandas for data manipulation and Matplotlib/Seaborn to generate insightful visualizations, such as:
  - Ages with the highest income.
  - Gender distribution across spending categories.
- **Cloud-Ready Deployment**: Fully configured for deployment on **Amazon Web Services (AWS)** using Elastic Beanstalk, with instructions for both the EB CLI and the AWS Management Console.

---

## Project Structure

```
final-project/
|-- app/
|   |-- static/
|   |   |-- js/
|   |   |   |-- main.js      # JavaScript for dynamic form elements
|   |-- templates/
|   |   |-- index.html     # The main survey form page
|   |   |-- success.html   # The "Thank You" page after submission
|   |-- main.py            # Core Flask application logic and routes
|-- data_processing/
|   |-- data_processor.py  # Script to fetch from MongoDB and create CSV
|-- analysis/
|   |-- data_analysis.ipynb# Jupyter Notebook for data visualization
|   |-- charts/            # Exported charts are saved here
|-- application.py         # Entry point for AWS Elastic Beanstalk
|-- requirements.txt       # List of all Python dependencies
|-- README.md              # This file
```

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python (3.8 or newer)
- `pip` (Python's package installer)
- Git for version control
- MongoDB Community Edition (and ensure the server is running)
- An AWS Account (for cloud deployment)

---

## Local Setup and Execution Guide

Follow these steps to run the application on your local machine.

### 1. Clone the Repository

Open your terminal and clone the project repository.

```bash
git clone <your-repository-link>
cd final-project
```

### 2. Create and Activate a Virtual Environment

This isolates the project's dependencies.

```bash
# Create the virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows (Command Prompt):
# .\venv\Scripts\activate
# On Windows (PowerShell):
# .\venv\Scripts\Activate.ps1
```

Your terminal prompt should now be prefixed with `(venv)`.

### 3. Install Dependencies

Install all the required Python packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Web Application

Ensure your local MongoDB server is running. Then, set the `FLASK_APP` environment variable and run the application.

**On PowerShell (Windows):**

```powershell
$env:FLASK_APP = "app.main"
flask run
```

**On Command Prompt (Windows):**

```cmd
set FLASK_APP=app.main
flask run
```

**On macOS/Linux:**

```bash
export FLASK_APP=app.main
flask run
```

Open your web browser and navigate to `http://127.0.0.1:5000`. Fill out and submit the form a few times to populate the database with sample data.

---

## Data Processing and Analysis

After collecting some data, you can process it and generate visualizations.

### 1. Generate the CSV File

Run the `data_processor.py` script. This will connect to your local MongoDB, fetch all the survey responses, and save them into a `user_data.csv` file inside the `analysis` folder.

```bash
python data_processing/data_processor.py
```

You should see a success message in your terminal.

### 2. Perform Data Analysis

Launch Jupyter Lab to run the analysis notebook.

```bash
jupyter lab
```

This will open a new tab in your browser.

- In the Jupyter interface, navigate into the `analysis` directory.
- Open the `data_analysis.ipynb` notebook.
- Run each cell in the notebook from top to bottom.
- The visualizations will be displayed directly in the notebook and also saved as `.png` files in the `analysis/charts/` directory, ready for use in presentations.

---

## Deployment to AWS Elastic Beanstalk

You can deploy this application to the cloud using one of two methods:

### Method 1: Using the AWS Management Console (Recommended for beginners)

1. **Create a `.zip` file:** Select all files and folders _inside_ your `final-project` directory and compress them into a single `survey-app.zip` file.
2. **Sign in to AWS:** Go to the Elastic Beanstalk service in the AWS Management Console.
3. **Create Application:** Click "Create application", give it a name (e.g., `survey-tool`), and create it.
4. **Create Environment:**
   - Choose "Web server environment".
   - Set the **Platform** to "Python".
   - For **Application code**, select "Upload your code" and upload your `survey-app.zip` file.
   - Choose the "Single instance (free tier eligible)" preset.
5. **Configure Environment Properties:**
   - On the "Configure service access" page, scroll down to **Environment properties**.
   - Add a new variable:
   - **Name:** `MONGO_URI`
   - **Value:** Paste your **MongoDB Atlas connection string** here. (You must use a cloud database like Atlas for a cloud deployment).
6. **Review and Submit:** Review your settings and click "Submit" to launch the environment. It will take 5-10 minutes. Once the health status is "Ok", your application is live at the provided URL.

### Method 2: Using the AWS EB CLI (Faster for developers)

1. **Install the EB CLI:** Follow the official AWS documentation to install the EB CLI.
2. **Initialize the Project:**
   ```bash
   eb init -p python-3.8 survey-tool --region us-east-1
   ```
3. **Create the Environment:** This command creates the environment and sets the required `MONGO_URI` environment variable in one step.
   ```bash
   eb create survey-tool-env --envvars MONGO_URI="<your_mongodb_atlas_uri>"
   ```
4. **Open the Application:** Once deployment is complete, open your live site.
   ```bash
   eb open
   ```
5. **Deploy Updates:** To deploy any future changes, simply run:
   ```bash
   eb deploy
   ```
