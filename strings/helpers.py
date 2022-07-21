#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✘ **<u>Admin Commands:</u>**

**C** stands for channel play.

◉ /pause or /cpause - Pause the playing music.
◉ /resume or /cresume- Resume the paused music.
◉ /mute or /cmute- Mute the playing music.
◉ /unmute or /cunmute- Unmute the muted music.
◉ /skip or /cskip- Skip the current playing music.
◉ /stop or /cstop- Stop the playing music.
◉ /shuffle or /cshuffle- Randomly shuffles the queued playlist.
◉ /seek or /cseek - Forward Seek the music to your duration
◉ /seekback or /cseekback - Backward Seek the music to your duration
◉ /restart - Restart bot for your chat .

✘ <u>**Loop Play:**</u>

◉ /loop or /cloop [1-10] 
    - When activated, the bot will repeat playback for 1-10 times in voice chat.

✘ <u>**Auth Users:**</u>

Auth users can use admin commands without admin rights in your chats.

◉ /auth [Username] - Add a user to AUTH LIST of the group.
◉ /unauth [Username] - Remove a user from AUTH LIST of the group.
◉ /authusers - Check AUTH LIST of the group."""


HELP_2 = """✘ <u>**Play Commands:**</u>

• Available Commands = play , vplay , cplay
• ForcePlay Commands = playforce , vplayforce , cplayforce

**C** stands for channel play.
**V** stands for video play.
**Force** stands for force play.

◉ /play or /vplay or /cplay  - Bot will start playing your given query on voice chat or Stream live links on voice chats.
◉ /playforce or /vplayforce or /cplayforce -  **Force Play** stops the current playing track on voice chat and starts playing the searched track instantly without disturbing/clearing queue.
◉ /channelplay [Chat username or id] or [Disable] - Connect channel to a group and stream music on channel's voice chat from your group.


✘ **<u>Bot's Server Playlists:</u>**
◉ /playlist  - Check Your Saved Playlist On Servers.
◉ /deleteplaylist - Delete any saved music in your playlist
◉ /play  - Start playing Your Saved Playlist from Servers."""


HELP_3 = """✘ <u>**Bot Commands:**</u>

◉ /stats - Get Top 10 Tracks Global Stats, Top 10 Users of bot, Top 10 Chats on bot, Top 10 Played in a chat etc etc.
◉ /sudolist - Check Sudo Users of Bot
◉ /lyrics [Music Name] - Searches Lyrics for the particular Music on web.
◉ /song [Track Name] or [YT Link] - Download any track from youtube in mp3 or mp4 formats.
◉ /player -  Get a interactive Playing Panel.

**C** stands for channel play.

◉ /queue or /cqueue- Check Queue List of Streaming."""

HELP_4 = """✘ <u>**Extra  Commands:**</u>

◉ /start - Start the Music Bot.
◉ /help  - Get Commands Helper Menu with detailed explanations of commands.
◉ /ping- Ping the Bot and check Ram, Cpu etc stats of Bot.

HELP_5 = """✘ **<u>ADD & REMOVE SUDO USERS :</u>**
◉ /addsudo [Username or Reply to a user]
◉ /delsudo [Username or Reply to a user]

✘ **<u>HEROKU:</u>**
◉ /usage - Dyno Usage.

✘ **<u>CONFIG VARS:</u>**
◉ /get_var - Get a config var from Heroku or .env.
◉ /del_var - Delete any var on Heroku or .env.
◉ /set_var [Var Name] [Value] - Set a Var or Update a Var on heroku or .env. Seperate Var and its Value with a space.

✘ **<u>BOT COMMANDS:</u>**
◉ /reboot - Reboot your Bot. 
◉ /update - Update Bot.
◉ /speedtest - Check server speeds
◉ /maintenance [enable / disable] 
◉ /logger [enable / disable] - Bot logs the searched queries in logger group.
◉ /get_log [Number of Lines] - Get log of your bot from heroku or vps. Works for both.
◉ /autoend [enable|disable] - Enable Auto stream end after 3 mins if no one is listening.

✘ **<u>STATS COMMANDS:</u>**
◉ /activevoice - Check active voice chats on bot.
◉ /activevideo - Check active video calls on bot.
◉ /stats - Check Bots Stats

✘ **<u>BLACKLIST CHAT FUNCTION:</u>**
◉ /blacklistchat [CHAT_ID] - Blacklist any chat from using Music Bot
◉ /whitelistchat [CHAT_ID] - Whitelist any blacklisted chat from using Music Bot
◉ /blacklistedchat - Check all blacklisted chats.

✘ **<u>BLOCKED FUNCTION:</u>**
◉ /block [Username or Reply to a user] - Prevents a user from using bot commands.
◉ /unblock [Username or Reply to a user] - Remove a user from Bot's Blocked List.
◉ /blockedusers - Check blocked Users Lists

✘ **<u>GBAN FUNCTION:</u>**
◉ /gban [Username or Reply to a user] - Gban a user from bot's served chat and stop him from using your bot.
◉ /ungban [Username or Reply to a user] - Remove a user from Bot's gbanned List and allow him for using your bot
◉ /gbannedusers - Check Gbanned Users Lists

✘ **<u>VIDEOCALLS FUNCTION:</u>**
/set_video_limit [Number of Chats] - Set a maximum Number of Chats allowed for Video Calls at a time. Default to 3 chats.
/videomode [download|m3u8] - If download mode is enabled, Bot will download videos instead of playing them in M3u8 form. ByDefault to M3u8. You can use download mode when any query doesnt plays in m3u8 mode.

✘ **<u>PRIVATE BOT FUNCTION:</u>**
/authorize [CHAT_ID] - Allow a chat for using your bot.
/unauthorize [CHAT_ID] - Disallow a chat from using your bot.
/authorized - Check all allowed chats of your bot.

✘ **<u>BROADCAST FUNCTION:</u>**
/broadcast [Message or Reply to a Message] - Broadcast any message to Bot's Served Chats.

<u>options for broadcast:</u>
**-pin** : This will pin your message 
**-pinloud** : This will pin your message with loud notification
**-user** : This will broadcast your message to the users who have started your bot.
**-assistant** : This will broadcast your message from assistant account of your bot.
**-nobot** : This will force your bot to not broadcast message

**Example:** `/broadcast -user -assistant -pin Hello Testing`

"""
