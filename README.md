# Insta Random Bot

Telegram bot that shows the follower count of a public Instagram profile and randomly selects one follower.

## Features

- Works with **public Instagram profiles**
- Shows **follower count**
- Picks a **random follower**
- Multi-language: Uzbek, Russian, English
- No Instagram login required

## How to Use

1. Send an Instagram profile link to the bot
2. The bot shows number of followers
3. Then selects one random follower from the list

## Commands

- `/start` - Start the bot
- `/language` - Change language

## Deployment

1. Create `.env` file with the following content:

```
BOT_TOKEN=your_bot_token
API_ID=your_api_id
API_HASH=your_api_hash
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run the bot:
```
python main.py
```

## License

MIT
