import africastalking
import logging
from core.config import AT_API_KEY, AT_USERNAME, AT_SHORTCODE

logger = logging.getLogger(__name__)

# Initialize Africa's Talking
africastalking.initialize(AT_USERNAME, AT_API_KEY)
sms = africastalking.SMS


async def send_sms(to: str, message: str) -> bool:
    """Send SMS via Africa's Talking API.
    
    Args:
        to: Phone number to send to (e.g., +254712345678)
        message: Message content
        
    Returns:
        True if sent successfully, False otherwise
    """
    try:
        # Ensure phone number has country code
        if not to.startswith("+"):
            to = f"+{to}"
        
        logger.info(f"Sending SMS to {to}: {message[:50]}...")
        
        response = sms.send(message, [to])
        
        logger.info(f"SMS response: {response}")
        
        # Check if any message was sent successfully
        recipients = response.get("SMSMessageData", {}).get("Recipients", [])
        if recipients:
            status = recipients[0].get("status", "")
            if status == "Success":
                return True
            logger.warning(f"SMS status: {status}")
        
        return False
        
    except Exception as e:
        logger.error(f"Failed to send SMS: {e}", exc_info=True)
        return False
