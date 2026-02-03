"""
Report Relay - Discord to Slack Notification Bridge
Main entry point for the bot.
"""

import os
import sys
import logging
from datetime import datetime
from dotenv import load_dotenv

from discord_listener import DiscordListener
from slack_sender import send_to_slack

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


def main():
    """Main entry point."""
    # Load environment variables
    load_dotenv()
    
    # Get configuration
    discord_token = os.getenv("DISCORD_BOT_TOKEN")
    channel_id_str = os.getenv("DISCORD_CHANNEL_ID")
    slack_webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    
    # Validate configuration
    if not discord_token:
        logger.error("DISCORD_BOT_TOKEN is not set")
        sys.exit(1)
    
    if not channel_id_str:
        logger.error("DISCORD_CHANNEL_ID is not set")
        sys.exit(1)
    
    if not slack_webhook_url:
        logger.error("SLACK_WEBHOOK_URL is not set")
        sys.exit(1)
    
    try:
        channel_id = int(channel_id_str)
    except ValueError:
        logger.error(f"Invalid DISCORD_CHANNEL_ID: {channel_id_str}")
        sys.exit(1)
    
    # Create message handler
    def handle_message(
        author: str,
        content: str,
        timestamp: datetime,
        channel_name: str,
        attachments: list
    ):
        """Handle incoming Discord messages by forwarding to Slack."""
        send_to_slack(
            webhook_url=slack_webhook_url,
            author=author,
            content=content,
            timestamp=timestamp,
            channel_name=channel_name,
            attachments=attachments
        )
    
    # Create and run Discord client
    logger.info("Starting Report Relay bot...")
    logger.info(f"Target channel ID: {channel_id}")
    
    client = DiscordListener(
        channel_id=channel_id,
        message_handler=handle_message
    )
    
    try:
        client.run(discord_token)
    except Exception as e:
        logger.error(f"Bot error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
