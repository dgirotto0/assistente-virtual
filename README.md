# Virtual Assistant

Virtual Assistant is a chatbot application that leverages Natural Language Processing (NLP) with NLTK and integrates with Twilio’s WhatsApp API. The project is designed to handle customer inquiries about services (such as those provided by ItaOleo) by detecting keywords in user messages and responding with appropriate, pre-defined answers.

## Features

- **Natural Language Processing with NLTK:**
  - **Tokenization:** Splits user messages into individual words.
  - **Stop Words Removal:** Filters out common words (using Portuguese stopwords) to focus on meaningful tokens.
  - **Lemmatization:** Reduces words to their base or dictionary form using the WordNet lemmatizer.
  
- **Twilio Integration:**
  - Sends and receives WhatsApp messages using Twilio’s API.
  - Uses FastAPI to create a REST endpoint that handles incoming messages from Twilio’s webhook.
  
- **Modular Design:**
  - Separation between the NLP response logic and Twilio messaging functionality.
  - Simple and extensible codebase that can be enhanced for additional functionality.

- **Error Handling and Logging:**
  - Logs detailed information about message processing and any errors encountered during runtime.

## Project Structure

```
virtual-assistant/
├── app.py             # Contains the 'response' function for processing incoming messages with NLTK.
├── twilio_app.py      # FastAPI app that integrates with Twilio to send/receive WhatsApp messages.
├── .env               # Environment file containing Twilio credentials (not included in the repository).
├── requirements.txt   # List of required Python packages.
└── README.md          # This file.
```

## Prerequisites

- **Python 3.8+**
- The following Python packages:
  - `nltk`
  - `fastapi`
  - `twilio`
  - `python-dotenv`
  - `uvicorn` (for running the FastAPI server)
- **Twilio Account:** Set up a Twilio account with access to the WhatsApp sandbox or a production WhatsApp number.
- **NLTK Data:** Ensure the necessary NLTK data packages are installed:
  ```bash
  python -m nltk.downloader punkt stopwords wordnet
  ```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/virtual-assistant.git
   cd virtual-assistant
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   - Create a `.env` file in the project root with the following content:
     ```dotenv
     TWILIO_ACCOUNT_SID=your_twilio_account_sid
     TWILIO_AUTH_TOKEN=your_twilio_auth_token
     TWILIO_NUMBER=your_twilio_whatsapp_number
     ```

## Usage

1. **Run the FastAPI server:**
   ```bash
   uvicorn twilio_app:app --reload
   ```

2. **Expose your local server to the Internet (optional):**
   - Use a tool like [ngrok](https://ngrok.com/) to expose your local development server. For example:
     ```bash
     ngrok http 8000
     ```
   - Configure your Twilio account to use the provided ngrok URL as the webhook for incoming messages.

3. **Test the Virtual Assistant:**
   - Send a WhatsApp message (using your configured Twilio number) with queries like:
     - "Olá" (greeting)
     - "Qual o horário de funcionamento?" (inquiry about hours)
     - "Qual o endereço?" (inquiry about location)
   - The assistant will process your message and respond accordingly based on detected keywords.

## Code Overview

### NLP Response Function (`app.py`)

- **Function:** `response(question)`
  - **Input:** A string containing the user’s question.
  - **Process:**
    - Converts the text to lowercase and tokenizes it.
    - Removes Portuguese stopwords.
    - Applies lemmatization to each token.
    - Checks for greetings and specific keyword categories (services, location, hours, phone, payment).
  - **Output:** A context-specific response string.

### Twilio Integration with FastAPI (`twilio_app.py`)

- **FastAPI Endpoint:** Listens for POST requests at `/`.
- **Functionality:**
  - Parses the incoming form data from Twilio.
  - Extracts the sender’s WhatsApp number and the message body.
  - Processes the message using the `response` function.
  - Sends the generated reply back to the user via WhatsApp.

## Logging and Error Handling

- The application uses Python’s built-in `logging` module to record information about sent messages and any errors that occur during processing.
- In the event of an error, the assistant sends a fallback error message to the user and logs the error details for further troubleshooting.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please feel free to:
- Open an issue on GitHub.
- Submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Twilio:** For providing the API and comprehensive documentation.
- **NLTK:** For the powerful natural language processing tools.
- **FastAPI:** For the fast and easy-to-use web framework.
