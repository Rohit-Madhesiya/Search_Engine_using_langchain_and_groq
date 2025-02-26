# LangChain-Chat with Search

## Overview
This is a Streamlit-based chatbot that utilizes LangChain to perform web searches and retrieve information from sources like ArXiv, Wikipedia, and DuckDuckGo. The chatbot interacts with users and provides search-based responses using the Groq API for LLM processing.

## Features
- **Conversational Interface:** Chatbot-style interaction with users.
- **Web Search Capabilities:** Fetches information from ArXiv, Wikipedia, and DuckDuckGo.
- **Streamlit UI:** Provides an interactive user interface.
- **Groq API Integration:** Uses Llama3-8b-8192 model for response generation.
- **Real-time Response Streaming:** Displays responses interactively using `StreamlitCallbackHandler`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Rohit-Madhesiya/Search_Engine_using_langchain_and_groq.git
   cd Search_Engine_using_langchain_and_groq
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the project root.
   - Add the following line:
     ```env
     GROQ_API_KEY=<your_api_key>
     ```

## Usage

Run the Streamlit app with the following command:
```bash
streamlit run app.py
```

Once the app is running:
- Enter your Groq API key in the sidebar.
- Start chatting with the assistant.
- Ask questions related to Generative AI or other topics, and the bot will fetch relevant information.

## Dependencies
The project requires the following libraries (listed in `requirements.txt`):
- `streamlit`
- `langchain`
- `langchain-community`
- `langchain-text-splitters`
- `langchain_groq`
- `arxiv`
- `wikipedia`
- `duckduckgo-search`
- `python-dotenv`
- `ipykernel`

## Project Structure
```
├── app.py              # Main application file
├── requirements.txt    # List of dependencies
├── .env                # API key configuration (not included in repo)
└── tools_agents.ipynb  # Notebook for testing LangChain tools
```

## Contributing
Feel free to fork the repository and submit pull requests for improvements!

## Author
Developed by [Rohit Gupta]

