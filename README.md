# insurance-challenge



This project is a Django-based web application.

## Prerequisites

- Python 3.x
- Django framework
- Django rest framework

## Installation

1. Clone the repository:

   ```bash
   git clonehttps://github.com/amjadahmadi/insurance-challenge.git
   cd insurance-challenge
   python3 -m venv venv
   ```
2. Navigate to the project directory: 
   ```bash
   cd insurance-challenge
   ```
3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
4. Activate the virtual environment:

    for Windows:
   ```bash
   venv\Scripts\activate
   ```
    for macOS/Linux:
   ```bash
   source venv/bin/activate
   ```
5. Install the project dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Perform database migrations:  
   ```bash
   pip install -r requirements.txt
   ```
#Usage

1. Start the development server:
   ```bash
   python manage.py runserver
   ```
   

2. Open your web browser and navigate to http://localhost:8000/engine/calculate/ to access the application.

#csc
First, I created a separate class for each insurance and used the basic insurance class to access the property of insurances that are the same. With this, the parameters that have the same effect can be applied.
After that, we first check whether the insurance is eligible or not, then the amount of points is calculated by functions that we defined in the basic class.