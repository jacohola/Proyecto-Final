import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='-', intents=intents)

consejos = [
    "Usa menos plástico.",
    "Apaga las luces que no uses.",
    "Camina o usa bicicleta.",
    "Separa la basura correctamente.",
    "Usa una botella reutilizable.",
    "Lleva tu bolsa al supermercado.",
    "Come más vegetales y menos carne.",
    "Lava tu ropa con agua fría.",
    "Reutiliza envases y frascos.",
    "Compra productos locales y de temporada.",
    "Evita el uso de papel innecesario.",
    "Cierra la llave mientras te cepillas.",
]

datos = [
    "Un árbol puede absorber 20 kg de CO₂ al año.",
    "El 70% de los residuos marinos son plásticos.",
    "Cada minuto se venden 1 millón de botellas plásticas.",
    "Una ducha de 5 minutos consume unos 60 litros de agua.",
    "El transporte genera el 25% de las emisiones de gases de efecto invernadero.",
    "Una bombilla LED gasta 80% menos energía que una normal.",
    "Los océanos absorben el 30% del CO₂ que emitimos.",
    "La carne genera más emisiones que los vegetales.",
    "El 30% de la comida producida se desperdicia.",
    "Cada tonelada de papel reciclado ahorra 17 árboles.",
]

retos = [
    "Hoy no uses plástico de un solo uso.",
    "Ve al trabajo o escuela sin usar gasolina.",
    "Planta algo o cuida una planta.",
    "No comas carne hoy.",
    "Reutiliza algo en lugar de tirarlo.",
    "Recoge 5 pedazos de basura en la calle o parque.",
    "No uses aire acondicionado hoy.",
    "Dúchate en menos de 5 minutos.",
    "Comparte un consejo ecológico con un amigo.",
    "Apaga todos los aparatos que no uses hoy.",
]

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user.name}')

@bot.command(name='consejo', help='Te da un consejo para cuidar el medio ambiente.')
async def dar_consejo(ctx):
    consejo = random.choice(consejos)
    await ctx.send(f"🌿 Consejo ecológico: {consejo}")

@bot.command(name='dato', help='Te da un dato curioso sobre el medio ambiente.')
async def dar_dato(ctx):
    dato = random.choice(datos)
    await ctx.send(f"🌍 Dato curioso: {dato}")

@bot.command(name='reto', help='Te da un reto ecológico para hoy.')
async def dar_reto(ctx):
    reto = random.choice(retos)
    await ctx.send(f"💪 Reto ecológico: {reto}")

TOKEN = 'TU TOKEN AQUI'#Token de discord
bot.run(TOKEN)







