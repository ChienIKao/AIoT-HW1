# Simple Linear Regression Web Application

This project demonstrates a simple linear regression model with a web interface built using Streamlit. Users can modify parameters such as the slope (`a`), intercept (`b`), noise level, and the number of data points. The application also highlights the top 5 outliers on the plot.

## Features
- Interactive web interface for parameter adjustment.
- Visualization of the regression line and data points.
- Highlighting and annotation of the top 5 outliers.

---

## Prerequisites
Ensure you have the following installed:
- Python 3.7 or higher
- `uv` (if using the `uv` tool for environment management)

---

## Installation Steps

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Initialize the Environment**
   If you are using `uv`:
   ```bash
   uv init
   ```

3. **Install Dependencies**
   Install the required Python packages:
   ```bash
   uv add -r requirements.txt
   ```

   Alternatively, if not using `uv`, install dependencies directly:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Application

1. **Start the Streamlit App**
   If using `uv`:
   ```bash
   uv run streamlit run streamlit_app.py
   ```

   Without `uv`:
   ```bash
   streamlit run streamlit_app.py
   ```

2. **Access the Application**
   Open your browser and navigate to the URL displayed in the terminal (usually `http://localhost:8501`).

---

## Bash History Reference
Here is a summary of the key commands used during development, grouped by purpose:

### Environment Setup
- `uv init`: Initialize the environment.
- `uv add streamlit`: Add the Streamlit package to the environment.
- `uv add -r requirements.txt`: Install all dependencies from the `requirements.txt` file.

### Running the Application
- `streamlit run streamlit_app.py`: Run the Streamlit application directly.
- `uv run streamlit run streamlit_app.py`: Run the Streamlit application using the `uv` tool.

### Miscellaneous
- `clear`: Clear the terminal screen.
- `history`: Display the command history.

This organized summary replaces the raw history log for better readability.

---

## Notes
- Ensure the `requirements.txt` file is up-to-date with all necessary dependencies.
- If you encounter issues with `streamlit` not being recognized, ensure the correct Python environment is activated.

Enjoy exploring the application!
