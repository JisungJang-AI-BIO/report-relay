"""
Discord Message Listener
Listens for messages in specified Discord channels and forwards to Slack.
"""

import discord
import logging
from datetime import datetime, timezone
from typing import Callable, Optional

logger = logging.getLogger(__name__)


class DiscordListener(discord.Client):
    """Discord client that listens for messages and forwards them."""
    
    def __init__(
        self,
        channel_id: int,
        message_handler: Callable[[str, str, datetime, str, list], None],
        *args,
        **kwargs
    ):
        """
        Initialize the Discord listener.
        
        Args:
            channel_id: ID of the channel to monitor
            message_handler: Callback function to handle messages
                            (author, content, timestamp, channel_name, attachments)
        """
        # Set up intents
        intents = discord.Intents.default()
        intents.message_content = True  # Required for reading message content
        
        super().__init__(intents=intents, *args, **kwargs)
        
        self.target_channel_id = channel_id
        self.message_handler = message_handler
    
    async def on_ready(self):
        """Called when the bot is ready and connected."""
        logger.info(f"Discord bot logged in as {self.user}")
        logger.info(f"Monitoring channel ID: {self.target_channel_id}")
        
        # Verify channel access
        channel = self.get_channel(self.target_channel_id)
        if channel:
            logger.info(f"Successfully connected to channel: #{channel.name}")
        else:
            logger.warning(f"Could not find channel with ID: {self.target_channel_id}")
    
    async def on_message(self, message: discord.Message):
        """Called when a message is received."""
        # Ignore messages from self
        if message.author == self.user:
            return
        
        # Only process messages from the target channel
        if message.channel.id != self.target_channel_id:
            return
        
        # Extract message details
        author = message.author.display_name
        content = message.content or "(첨부파일)"
        timestamp = message.created_at.replace(tzinfo=timezone.utc)
        channel_name = message.channel.name
        
        # Get attachment URLs
        attachments = [attachment.url for attachment in message.attachments]
        
        # Log the message
        logger.info(f"New message from {author} in #{channel_name}: {content[:50]}...")
        
        # Call the message handler
        try:
            self.message_handler(
                author=author,
                content=content,
                timestamp=timestamp,
                channel_name=channel_name,
                attachments=attachments
            )
        except Exception as e:
            logger.error(f"Error handling message: {e}")
    
    async def on_error(self, event: str, *args, **kwargs):
        """Handle errors gracefully."""
        logger.exception(f"Error in event {event}")
