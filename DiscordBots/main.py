import os, logging, discord
from dotenv import load_dotenv
from discord.ext import commands
from groq import Groq
from google import genai   # ✅ new SDK

load_dotenv()

GROQ_KEY = os.getenv("GROQ_API_KEY")
API_KEY = os.getenv("GEMINI_API_KEY")
TOKEN = os.getenv("DISCORD_TOKEN")

groq_client = Groq(api_key=GROQ_KEY)
client = genai.Client(api_key=API_KEY)  # ✅ new client


handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

SWEAR_WORDS = ["fuck", "shit", "dick", "pussy", "slot", "damn", "goddamn", "ass"]
FRUSTRATION_KEYWORDS = ["just give", "i don't get", "answer me", "confused", "help"]

MAX_CHARS = 5000
CONTEXT = ""

context_path = os.path.abspath("details.txt")
with open(context_path, "r", encoding="utf-8") as f:
    CONTEXT = f.read()


# =====================
# AI CALL
# =====================
def ask_groq(prompt):
    completion = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion
def answer(prompt):
    try:
        ask_groq(prompt)
    except Exception as e:            
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return getattr(response, "text", "⚠️ No response")
        except Exception as e:
            try:
                response = client.models.generate_content(
                    model="gemini-2.0-flash-lite",
                    contents=prompt
                )
                return getattr(response, "text", "⚠️ No response")
            except Exception as e:
                print(f"⚠️ Error: {str(e)}")
                return "Sorry, there was a problem processing your request. :("
    

# =====================
# PROMPT BUILDING
# =====================
def is_frustrated(text):
    return sum(word in text.lower() for word in FRUSTRATION_KEYWORDS) >= 2


def build_prompt(user_prompt, context, mode):
    frustrated = is_frustrated(user_prompt)

    if mode == "!biz":
        return f"""
You are a formal assistant for CodeCraft.
Your responses should be BRIEF, under 500 words.

Use this official context:
{context}

Now answer the user query carefully and efficiently
User question:
{user_prompt}
"""

    elif mode == "!code":
        extra = ""
        if frustrated:
            extra = "The student is frustrated. Be clearer, but still guide instead of giving full answers."

        return f"""
You are a coding tutor for CodeCraft inspired by CS50.
Your responses must ALWAYS be less than 1500 words.
Additional context: { context }
RULES:
- Do NOT immediately give full answers
- Start with guiding questions
- Provide hints and small examples
- Be structured and educational

{extra}

User question:
{user_prompt}
"""

    elif mode == "!start":
        return f"""
You are introducing CodeCraft to a new student.
Your response must be in no more than 7 sentences.
Context:
{context}
"""

    return user_prompt


# =====================
# COMMAND: CONTEXT
# =====================
@bot.command()
async def context(ctx):
    global CONTEXT  # ✅ fix scope

    messages = []

    async for msg in ctx.channel.history(limit=50):
        if not msg.author.bot:
            messages.append(msg.content)

    messages.reverse()
    combined = "\n".join(messages)

    last_chunk = combined[-200:]

    # ✅ prevent infinite growth
    CONTEXT = (CONTEXT + "\n" + last_chunk)[-MAX_CHARS:]
    print("CONTEXT: \n", CONTEXT)
    await ctx.send("✅ Context updated.")


# =====================
# EVENTS
# =====================
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")


@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to CodeCraft, {member.name} 👋")

    intro = answer(build_prompt("", CONTEXT, "!start"))
    await member.send(intro)


async def get_recent_history(channel, limit=50, max_chars=5000):
    messages = []

    async for msg in channel.history(limit=limit):
        if not msg.author.bot:
            messages.append(f"{msg.author.name}: {msg.content}")

    messages.reverse()  # oldest → newest
    combined = "\n".join(messages)

    return combined[-max_chars:]


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    # ✅ fixed swear filter
    if any(word in content for word in SWEAR_WORDS):
        await message.delete()
        await message.channel.send(f"{message.author.mention}, watch your language ⚠️")
        return

    if not "@bot" in message.content.lower() or "!no_reply" in message.content.lower():
        return
        
        # ✅ single response (no spam)
    mode = "!code" if "code" in content else "!biz"

    history = await get_recent_history(message.channel)

    prompt = build_prompt(
        user_prompt=message.content,
        context=CONTEXT + "\n\nRecent conversation:\n" + history,
        mode=mode
)
    response = answer(prompt)

    # ✅ avoid Discord 2000 char limit crash
    await message.channel.send(response[:2000])

    await bot.process_commands(message)


# =====================
# RUN
# =====================
if __name__ == "__main__":
    bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)