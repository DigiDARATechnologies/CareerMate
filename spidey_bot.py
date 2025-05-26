import discord
from discord.ext import commands
import logging
from langchain_ollama import OllamaLLM

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Set up Discord intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True  # Needed for mention detection

# Initialize the Discord bot with intents (no command prefix needed)
bot = commands.Bot(command_prefix="", intents=intents)

# Initialize LLaMA 3.2 Vision model via Ollama using LangChain
try:
    logger.info("Initializing LLaMA 3.2 Vision model via Ollama...")
    llm = OllamaLLM(model="llama3.2-vision:latest")
    logger.info("LLaMA 3.2 Vision model initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize LLaMA 3.2 Vision model: {e}")
    raise

# Event: Bot is ready
@bot.event
async def on_ready():
    logger.info(f"Logged in as {bot.user.name} ({bot.user.id})")
    await bot.change_presence(activity=discord.Game(name="Helping with career advice!"))

# Handle all user messages
@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Log every message received for debugging
    logger.info(f"Received message from {message.author} in channel {message.channel.name}: {message.content}")

    # Process messages when the bot or a specific role is mentioned
    role_id = "1373980720535568472"  # Role ID from your logs
    role_mention = f"<@&{role_id}>"
    if bot.user.mentioned_in(message) or role_mention in message.content:
        logger.info(f"Bot or role mentioned in message: {message.content}")
        content = message.content.lower()
    
        # Remove the bot's mention and role mention from the content for cleaner processing
        content = content.replace(f"<@{bot.user.id}>", "").replace(role_mention, "").strip()
        logger.info(f"Processed content after removing mentions: {content}")

        # Handle greetings
        if "hy buddy" in content or "hello" in content or "hi" in content:
            logger.info("Detected greeting, responding...")
            await message.channel.send("Hey buddy! How can I assist you today? I can help with career questions or analyze your resume—just provide the text!")
            return

        # Handle image uploads (e.g., resumes)
        if message.attachments:
            logger.info("Detected image attachment")
            attachment = message.attachments[0]
            if not attachment.filename.endswith(('.jpg', '.png')):
                await message.channel.send("Unsupported file format. Please upload a JPG or PNG, or provide the text directly.")
                return

            # Prompt user to provide text
            await message.channel.send("I can’t extract text from images right now. Please paste the text of your resume, and I’ll analyze it for you!")
            return

        # Handle text-based questions
        if content:
            try:
                logger.info(f"Processing query with LangChain: {content}")
                # Special handling for career-related keywords
                if "resume" in content:
                    await message.channel.send("I can help with your resume! Please paste the text of your resume, and I’ll analyze it.")
                    return
                elif "interview" in content or "job" in content or "career" in content:
                    prompt = f"Career advice: {content}"
                else:
                    prompt = content

                # Get response from LLaMA 3.2 Vision via LangChain
                response = llm.invoke(prompt)
                logger.info(f"LangChain response: {response}")
                if len(response) > 1500:
                    response = response[:1500] + "... [Truncated]"
                await message.channel.send(response)
            except Exception as e:
                logger.error(f"Error in text query with LangChain: {e}")
                await message.channel.send("Sorry, I couldn’t process that. Try asking another way!")
    else:
        logger.info("No bot or role mention detected, skipping message.")

# Run the bot
if __name__ == "__main__":
    BOT_TOKEN = "MTM3MjQ3MzU4NTM4MTE1MDg2MQ.GDAgNh.RROiJNUcdjhCDsaaYIon3slcir3-Ofu32w1YLs"
    try:
        bot.run(BOT_TOKEN)
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")