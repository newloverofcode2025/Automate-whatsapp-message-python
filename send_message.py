import pywhatkit as kit

def send_whatsapp_message(phone_number, message, hour, minute):
    try:
        kit.sendwhatmsg(phone_number, message, hour, minute)
        print("Message scheduled successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    phone_number = "+918017199034"  # Replace with recipient's phone number (include country code)
    message = "Hello! This is Abhishek Banerjee sending an automated message using Python."
    hour = 18  # Specify the hour in 24-hour format
    minute = 36  # Specify the minute

    send_whatsapp_message(phone_number, message, hour, minute)