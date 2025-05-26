# CareerMate
# CareerMateBot

CareerMateBot is a Discord bot designed to assist users with career advice, respond to greetings, and welcome new members to the **CareerMate Server**. It operates in the `#college-community` channel and uses the `llama3.2-vision:latest` model from Ollama to provide helpful responses. This project is perfect for anyone looking to create a friendly Discord bot for career guidance!

---

## Overview

CareerMateBot helps users in a Discord server by:
- Answering career-related questions (e.g., "How do I prepare for an interview?").
- Responding to greetings like “Hi” or “Hello.”
- Welcoming new members to the server in the `#college-community` channel.

The bot is built using Python, `discord.py`, and `ollama`, and can be automated to run continuously on your system.

---

## Features

- **Career Advice**: Ask questions like “How do I get a job?” and get helpful tips powered by the `llama3.2-vision:latest` model.
- **Greetings**: Say “Hi,” “Hello,” or “Hy buddy,” and the bot will respond with “Hey buddy! How can I assist you today?”
- **Welcome Messages**: Automatically welcomes new members in the `#college-community` channel.

---

## Project Structure

Here’s how the project is organized:

- `src/`
  - `index.js`: server main code.
- `spidey_bot.py`: Main bot logic.
- `.env `- environment variables files.
- `requirements.txt`: Lists required Python packages.
- `venv`: virtual environment file.
- `README.md`: Project documentation.

---

## Installation

Follow these steps to set up CareerMateBot on your system.

### Prerequisites
- A Discord account and server.
- Python 3.10 or higher installed.
- Ollama installed on your system.

### Step 1: Create a Discord Server
1. Open Discord and create a server named “CareerMate Server.”
2. Add a channel called `#college-community`.
3. Add your email in discord and verified First.

### Step 2: Create the Bot in Discord Developer Portal
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click “New Application,” name it “CareerMateBot,” and click “Create.”  
3. Go to the “Bot” tab, click “Add Bot,” and copy the bot token .
   - **Note**: Keep this token private!

### Step 3: Configure the Redirect URL
The redirect URL is important for OAuth2 authentication, allowing the bot to handle callbacks after joining the server.

1. In the Developer Portal, go to “OAuth2” → “General.”
2. Under “Redirects,” click “Add Redirect.”
3. Enter the following URL:
   ```
   http://localhost:4000/api/auth/discord/redirect
   ```
4. Save the changes.

### Step 4: Add the Bot to Your Server
This step authorizes the bot to join your server.

1. In the Developer Portal, go to “OAuth2” → “URL Generator.”
2. Under “Scopes,” check:
   - `bot`
3. Under “Bot Permissions,” check:
   - Send Messages
   - Read Messages/View Channels
4. Copy the generated URL at the bottom (e.g., `https://discord.com/api/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=3072&scope=bot`).
5. Paste the URL into your browser’s address bar and press Enter.
6. Select “CareerMate Server” from the dropdown, review the permissions, and click “Authorize.”
7. Verify that “CareerMateBot” appears in your server’s member list (it will be offline until you run the code).

### Step 5: Create a Webhook for Welcome Messages
A webhook allows the bot to send messages to a specific channel, such as welcome messages for new members.

1. In Discord, go to “CareerMate Server” and click on `#college-community`.
2. Click the gear icon next to the channel name to open settings.
3. Go to “Integrations” and click “Create Webhook.”
4. Name the webhook “CareerMateBot Welcome” and ensure the channel is `#college-community`.
5. Copy the “Webhook URL” (e.g., `https://discord.com/api/webhooks/123456789012345678/abcXYZ...`).
   - **Note**: Save this URL securely, as it’s needed for sending messages to the channel.

### Step 6: Enable Intents
Intents allow the bot to access specific events, like reading messages and detecting new members.

1. In the Developer Portal, go to “Bot.”
2. Under “Privileged Gateway Intents,” enable:
   - Server Members Intent
   - Message Content Intent
3. Save the changes.

### Step 7: Bot Permissions and Scopes
The bot needs specific permissions and scopes to function:

- **OAuth2 Scopes** (for joining the server):
  - `bot`: Allows the bot to join the server.
- **Bot Permissions** (for actions in the server):
  - Send Messages
  - Read Messages/View Channels

### Step 8: Clone the Repository
Clone this repository to your local machine:

```bash
git clone https://github.com/YOUR_USERNAME/CareerMateBot.git
cd CareerMateBot
```

### Step 9: Install Dependencies
Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Step 10: Set Up Ollama
Ollama powers the bot’s career advice feature.

1. Download and install Ollama from [ollama.com](https://ollama.com).
2. Start the Ollama server:
   ```bash
   ollama serve
   ```
3. Pull the `llama3.2-vision:latest` model:
   ```bash
   ollama pull llama3.2-vision:latest
   ```
   - **Note**: Ensure your system has at least 6.2 GB of free memory. If you encounter memory issues (e.g., "model requires more system memory (6.2 GiB) than is available (4.8 GiB)"), close other programs or use a smaller model like `llava:7b`.

### Step 11: Configure the Bot Token
Add your bot token to the configuration file:

1. Open `config/bot_config.py`.
2. Replace `YOUR_BOT_TOKEN_HERE` with the token you copied:
   ```python
   BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
   ```

### Step 12: Run the Bot
Start the bot manually to test it:

```bash
cd CareerMateBot
python src/spidey_bot.py
```

You should see a message like:
```
2025-05-26 15:24:XX,XXX - INFO - Logged in as CareerMateBot
```

---

## Automation

To run the bot automatically on your system:

1. **Use the Batch Script**:
   - The repository includes `run_spidey_bot.bat`, a batch script for Windows.
   - Double-click `run_spidey_bot.bat` to start the bot and Ollama server automatically.

2. **Run on System Startup** (Windows):
   - Press `Windows Key + R`, type `shell:startup`, and press Enter.
   - Copy `run_spidey_bot.bat` into the Startup folder.
   - The bot will start automatically whenever your computer boots.

---

## Usage

Interact with CareerMateBot in the `#college-community` channel of your **CareerMate Server**:

1. **Say Hello**:
   - Type “Hi,” “Hello,” or “Hy buddy.”
   - The bot responds: “Hey buddy! How can I assist you today? I can help with career questions—just ask!”

2. **Ask a Career Question**:
   - Type a question like “How do I get a job?”
   - The bot responds with advice, e.g., “Practice for interviews and be confident!”

3. **Welcome New Members**:
   - When someone joins the server, the bot sends a message in `#college-community`:
     - “Welcome @User to the CareerMate Server! We’re excited to have you in the #college-community channel.”

---

## Troubleshooting

If the bot isn’t working, try these steps:

- **Bot Doesn’t Start**:
  - Ensure Ollama is running (`ollama serve`).
  - Check if your system has enough memory (close other programs).
- **Bot Doesn’t Join the Server**:
  - Verify you copied and pasted the OAuth2 URL correctly in your browser.
  - Ensure you selected “CareerMate Server” during authorization.
- **Bot Doesn’t Send Welcome Messages**:
  - Check if the bot has permission to send messages in `#college-community`.
  - Verify the webhook URL is correct and set to the right channel.
  - Ensure “Server Members Intent” is enabled in the Developer Portal.
- **Bot Doesn’t Respond to Messages**:
  - Ensure “Message Content Intent” is enabled in the Developer Portal.
- **Check Logs**:
  - Open `logs/bot.log` to see error messages.

---

## Resources

For advanced customization, learn about OAuth2 for Discord bots:  
- [Discord OAuth2 Documentation](https://discord.com/developers/docs/topics/oauth2)

---

## Contributing

Contributions are welcome! If you’d like to improve CareerMateBot:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -m "Add your feature"`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Author**: Aidev  
**Project**: CareerMateBot  
**Date**: May 26, 2025
