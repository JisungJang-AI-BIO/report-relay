"""
Slack Webhook Sender
Sends formatted messages to Slack via Incoming Webhook.
"""

import logging
import requests
from datetime import datetime
from typing import Optional

logger = logging.getLogger(__name__)


def send_to_slack(
    webhook_url: str,
    author: str,
    content: str,
    timestamp: datetime,
    channel_name: str = "Discord",
    attachments: Optional[list] = None
) -> bool:
    """
    Send a message to Slack via Incoming Webhook.
    
    Args:
        webhook_url: Slack Incoming Webhook URL
        author: Message author name
        content: Message content
        timestamp: Message timestamp
        channel_name: Source channel name for context
        attachments: List of attachment URLs (optional)
    
    Returns:
        True if message sent successfully, False otherwise
    """
    # Format timestamp in Korean timezone
    time_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    
    # Build message blocks
    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{author}* ({channel_name})\n{content}"
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"📅 {time_str}"
                }
            ]
        }
    ]
    
    # Add attachments if present
    if attachments:
        attachment_text = "\n".join([f"📎 <{url}|첨부파일>" for url in attachments])
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": attachment_text
            }
        })
    
    payload = {
        "blocks": blocks,
        "text": f"{author}: {content[:100]}..."  # Fallback text
    }
    
    try:
        response = requests.post(
            webhook_url,
            json=payload,
            timeout=10
        )
        response.raise_for_status()
        logger.info(f"Message sent to Slack successfully: {author}")
        return True
    except requests.RequestException as e:
        logger.error(f"Failed to send message to Slack: {e}")
        return False
