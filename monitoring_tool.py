import requests
import yaml
import telegram
from telegram.error import Unauthorized

# Load configuration
with open("config.yaml", 'r') as file:
    config = yaml.safe_load(file)

# Set configuration variables
validator_address = config['validator_address']
bor_rpc = config['rpc_endpoints']['bor']
heimdall_rpc = config['rpc_endpoints']['heimdall']
telegram_token = config['telegram']['bot_token']
chat_id = config['telegram']['chat_id']

# Initialize Telegram bot
bot = telegram.Bot(token=telegram_token)

# Functions to get Bor and Heimdall heights
def get_bor_height():
    try:
        response = requests.get(f"{bor_rpc}/blockNumber")
        return response.json()['result']
    except Exception as e:
        send_alert(f"Failed to fetch Bor height: {e}")
        return None

def get_heimdall_height():
    try:
        response = requests.get(f"{heimdall_rpc}/latest-header")
        return response.json()['result']['number']
    except Exception as e:
        send_alert(f"Failed to fetch Heimdall height: {e}")
        return None

# Function to check checkpoints
def check_checkpoints():
    try:
        response = requests.get(f"{heimdall_rpc}/checkpoints")
        data = response.json()
        signed = any(checkpoint['signer'] == validator_address for checkpoint in data['result'])
        proposed = any(checkpoint['proposer'] == validator_address for checkpoint in data['result'])
        return signed, proposed
    except Exception as e:
        send_alert(f"Failed to check checkpoints: {e}")
        return False, False

# Function to send alerts via Telegram
def send_alert(message):
    try:
        bot.send_message(chat_id=chat_id, text=message)
    except Unauthorized:
        print("Bot token is unauthorized. Please check the Telegram bot token and chat ID.")
    except Exception as e:
        print(f"Failed to send alert: {e}")

# Monitor function
def monitor():
    try:
        signed, proposed = check_checkpoints()
        bor_height = get_bor_height()
        heimdall_height = get_heimdall_height()

        if bor_height is None or heimdall_height is None:
            return

        # Alert if checkpoints not signed or proposed
        if not signed:
            send_alert(f"Validator {validator_address} missed signing a checkpoint.")
        if not proposed:
            send_alert(f"Validator {validator_address} missed proposing a checkpoint.")

        # Alert if heights are not increasing
        if int(bor_height) <= 0:
            send_alert("Bor height is not increasing!")
        if int(heimdall_height) <= 0:
            send_alert("Heimdall height is not increasing!")
        
        print(f"Bor Height: {bor_height}, Heimdall Height: {heimdall_height}")
    except Exception as e:
        send_alert(f"Error occurred: {e}")

# Main script loop
if __name__ == "__main__":
    monitor()

