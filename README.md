# Textbook Q&A System

This project implements a Textbook Q&A System, which extracts content from textbooks, creates a hierarchical tree-based index, and uses a Retrieval Augmented Generation (RAG) system along with a language model to answer questions based on the content.

## Features

- Content extraction from textbooks
- Hierarchical tree-based indexing
- Retrieval Augmented Generation (RAG) system
- Question answering using a language model
- Streamlit-based user interface

## Project Structure

```
QA_project/
├── data/
│   ├── textbook1.txt
│   ├── index1.pkl
├── extraction/
│   ├── extract_text.py
│   ├── process_text.py
├── ui/
│   ├── app.py
│   ├── requirements.txt
|   ├── test.py
├── .venv/
├── README.md
```

## Installation

### Prerequisites

- Python 3.8 or higher
- Virtual environment tool (e.g., `venv` or `virtualenv`)

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Pavan14K/textbook-qa-system.git
    cd textbook-qa-system
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r ui/requirements.txt
    ```

## Running the Project

### Extracting Text

1. **Extract text from the textbooks:**

    ```bash
    python extraction/extract_text.py path/to/textbook.pdf data/textbook1.txt
    ```

### Processing Text

1. **Process the extracted text to create the hierarchical index:**

    ```bash
    python extraction/process_text.py data/textbook1.txt data/index1.pkl
    ```

### Running the Streamlit Application

1. **Run the Streamlit application:**

    ```bash
    streamlit run ui/app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to interact with the Q&A system.

## Usage

- Enter your question in the input field on the Streamlit app interface.
- The system will retrieve relevant content from the textbooks and generate an answer based on the content.

## Troubleshooting

- **Index not found**: Ensure that the `index1.pkl` file is generated and located in the `data` directory.
- **Module not found**: Verify that all dependencies are installed correctly by running `pip install -r ui/requirements.txt`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.