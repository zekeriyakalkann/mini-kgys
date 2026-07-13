from datetime import datetime


LOG_FILE = "logs/system.log"


def write_log(level, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_message = f"[{timestamp}] [{level}] {message}\n"

    with open(LOG_FILE, "a") as file:
        file.write(log_message)


def info(message):
    write_log("INFO", message)


def warning(message):
    write_log("WARNING", message)


def error(message):
    write_log("ERROR", message)