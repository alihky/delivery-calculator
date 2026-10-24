# Delivery Income Calculator

A web-based delivery income calculator built with Python and FastAPI. The application estimates net earnings after taxes, INPS contributions, and vehicle-related expenses over a selected period.

## Features

- Calculate estimated net income from gross earnings.
- Select a calculation period of 1 to 12 months.
- Choose a tax rate of 5% or 15%.
- Select an ATECO code to determine the INPS calculation method.
- Calculate daily transportation expenses based on the number of days worked.
- Include optional annual vehicle insurance costs.
- Validate input data using Pydantic.
- Display a breakdown of expenses and estimated net income.
- Provide a responsive HTML interface with real-time form submission to the FastAPI backend.

## Technologies Used

- **Python** — application logic and calculations
- **FastAPI** — backend and API endpoints
- **Pydantic** — input validation
- **Jinja2** — HTML template rendering
- **HTML and CSS** — user interface and responsive layout
- **JavaScript** — form validation, API requests, and displaying results
- **Uvicorn** — ASGI server

## Project Structure

```text
delivery_calculator/
├── main.py
├── requirements.txt
├── templates/
│   └── index.html
└── README.md
```

The local `.venv` virtual environment is not included in the repository.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/alihky/delivery-calculator.git
cd delivery-calculator
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m uvicorn main:app --reload
```

### 6. Open the application

Open the following address in your browser:

http://127.0.0.1:8000

The API documentation is available at:

http://127.0.0.1:8000/docs

## How It Works

1. Enter the total gross income.
2. Select the applicable tax rate.
3. Select an ATECO code.
4. Enter the number of months covered by the income.
5. Optionally enter daily transportation expenses and total days worked.
6. Optionally include annual vehicle insurance costs.
7. Submit the form to calculate estimated expenses and net income.

The frontend sends the input data to the `/calculation` endpoint using a JSON POST request. FastAPI validates the data, performs the calculations, and returns the results as JSON.

## API Endpoint

### `GET /`

Returns the HTML calculator interface rendered with Jinja2.

### `POST /calculation`

Accepts JSON input and returns the calculation results, including:

- Gross income
- Estimated tax amount
- INPS contributions
- Transportation expenses
- Total expenses
- Estimated net income

The request data is validated using a Pydantic model, including numeric ranges and permitted tax rates and ATECO codes.

## Calculation Assumptions

The application uses predefined assumptions in the code:

- A 67% taxable income coefficient.
- A selected tax rate of 5% or 15%.
- An INPS rate of 26.07% for ATECO code `53.20.00`.
- A fixed INPS contribution of €266.66 per month for ATECO code `82.99.99`.
- Transportation expenses based on daily costs and total days worked.
- Annual vehicle insurance allocated proportionally to the selected number of months.

These values are configurable in the application code and should be verified against the user's actual tax and social security circumstances.

## Disclaimer

This project is intended for educational and estimation purposes only. The calculations are based on predefined assumptions and may not reflect current Italian tax regulations or an individual's actual tax and social security obligations. The results should not be considered official tax, accounting, or financial advice.

## Purpose

This project demonstrates practical experience with Python backend development, FastAPI endpoint design, Pydantic validation, server-rendered HTML templates, and frontend-to-backend communication.
