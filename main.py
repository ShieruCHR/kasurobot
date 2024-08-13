import io
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from PIL import Image, ImageDraw, ImageFont

load_dotenv()

intents = discord.Intents.default()
bot = commands.Bot(intents=intents, command_prefix="")

# 画像のテキスト描画位置（中心）
robot = (577, 353)
dragon = (260, 203)


@bot.event
async def on_ready():
    await bot.tree.sync()


def generate_image(
    original: str,
    message: str,
    center: tuple[int, int],
    fontsize: int = 80,
    chunk: int = 10,
):
    image = Image.open(original)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("font.ttf", fontsize)

    chunks = [message[i : i + chunk] for i in range(0, len(message), chunk)]
    text = "\n".join(chunks)

    draw.text(center, text, font=font, align="center", anchor="mm", fill=(0, 0, 0))
    return image


@bot.hybrid_command(name="robot", description="どうせすぐ廃れるのに…")
async def _robot(ctx, *, message: str):
    image = generate_image(
        "image.png",
        message,
        robot,
    )

    image_bytes = io.BytesIO()
    image.save(image_bytes, format="PNG")
    image_bytes.seek(0)

    file = discord.File(image_bytes, filename="image.png")
    await ctx.send(file=file)


@bot.hybrid_command(name="dragon", description="好きなBot発表ドラゴン")
async def _dragon(ctx, *, message: str):
    image = generate_image(
        "dragon.png",
        message,
        dragon,
        60,
    )

    image_bytes = io.BytesIO()
    image.save(image_bytes, format="PNG")
    image_bytes.seek(0)

    file = discord.File(image_bytes, filename="image.png")
    await ctx.send(file=file)


bot.run(os.getenv("TOKEN"))
