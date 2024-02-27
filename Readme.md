```markdown
# Light-Weight OLLAMA Chatbot Interface

This project provides a lightweight chat interface for interacting with OLLAMA chatbot models using Streamlit. It allows users to select a model, configure parameters, and engage in a conversation with the chatbot.

## Features

- Model selection: Choose from a list of available OLLAMA models.
- Parameter configuration: Adjust the temperature and seed for the conversation.
- Conversation history: View the history of the conversation with the chatbot.
- Clear chat history: Reset the conversation history.

## Installation [Assuming that Ollama is installed in the machine]

REF: https://github.com/ollama/ollama

To set up the chatbot interface, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repository/ollama-chatbot-interface.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ollama-chatbot-interface
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage

Once the app is running, you can interact with it through the web interface:

1. Select a model from the sidebar.
2. Adjust the temperature and seed parameters as desired.
3. Type your message in the input field and press Enter to send it.
4. The chatbot's response will appear in the chat window.

## Contributing

Contributions are welcome! Here are some features that could be added:

- Append the conversational history in the GUI.
- Support for streaming responses.

Feel free to fork the repository and submit a pull request with your changes.


```

