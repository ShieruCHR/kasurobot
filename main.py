import io
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from PIL import Image, ImageDraw, ImageFont

load_dotenv()

intents = discord.Intents.default()
bot = commands.Bot(intents=intents, command_prefix=lambda _, __: False)

# 画像のテキスト描画位置（中心）
x1, y1 = 577, 353


@bot.event
async def on_ready():
    await bot.tree.sync()


@bot.hybrid_command(description="どうせすぐ廃れるのに…")
async def generate(ctx, *, message: str):
    image = Image.open("image.png")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("font.ttf", 80)

    chunks = [message[i : i + 10] for i in range(0, len(message), 10)]
    text = "\n".join(chunks)

    draw.text((x1, y1), text, font=font, align="center", anchor="mm", fill=(0, 0, 0))

    image_bytes = io.BytesIO()
    image.save(image_bytes, format="PNG")
    image_bytes.seek(0)

    file = discord.File(image_bytes, filename="image.png")
    await ctx.send(file=file)


bot.run(os.getenv("TOKEN"))
