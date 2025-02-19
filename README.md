project-sprint-7-tripleten

Description:
This project aims to deploy a web application using Streamlit, 
which displays two graphs: a histogram that shows the distribution 
of kilometers driven by cars and a scatter plot that illustrates the 
relationship between price and kilometers driven.


Prerequisites:
- Python 3.12.2 or higher
- Required libraries:
  - streamlit
  - pandas
  - plotly express


Installation in local:
1. Clone the repository:
   git clone https://github.com/gerzon13medin/project-sprint-7-tripleten.git
2. Navigate to the project folder:
   cd my-repo
3. Create a virtual environment (optional but recommended):
   python -m venv env
4. Activate the virtual environment:
   - On Windows: env\Scripts\activate
   - On macOS/Linux: source env/bin/activate
5. Install dependencies:
   pip install -r requirements.txt

How to run the application:
To run the application, use the following command in the terminal:
   streamlit run app.py


Project Structure:
📂 PROJECT-SPRINT-7-TRIPLETEN
 📂 notebooks             # Auxiliary file to test code                
 📂 src/utils             # Auxiliary functions 
 📂 streamlit             # Main file to configurate the web service
├── app.py                # Main appliation file
├── README.txt            # This file
├── requirements.txt      # List of dependencies
└── vehicles_us.csv       # Dataset
 


App already deployed on Render link below to access the website:
https://project-sprint-7-tripleten.onrender.com/


Author:
Gerzon Medina Ortiz