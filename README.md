# ChatWithSQL

## Description
ChatWithSQL is a Python project that enables users to interact with an SQL database using natural language queries. By leveraging OpenAI's language model, the project translates user questions into SQL queries and retrieves the corresponding data from the database.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Examples](#examples)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation
To set up the project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ChatWithSQL.git
    cd ChatWithSQL
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    - Create a `.env` file in the project root directory.
    - Add your OpenAI API key to the `.env` file:
        ```plaintext
        OPENAI_API_KEY=your_openai_api_key
        ```

## Usage
To use ChatWithSQL, create an instance of the `ChatWithSql` class with your database credentials and call the `message` method with your query.

```python
from yourmodule import ChatWithSql

# Replace with your actual database credentials
chat_sql = ChatWithSql(db_user='root', db_password='yourpassword', db_host='localhost', db_name='yourdatabase')
response = chat_sql.message('How many columns are there in the table?')
print(response)