def welcome(name):
    return f"*Wellcome to One Night Stand\n\n{name}🙊*\n\n_Hopefully you will find a soul mate or new friend_\n\nType /next - for find new crush\nType /help - show the guide\n\n*MUST JOIN!!*\n[👥 ɢʀᴏᴜᴘ](https://t.me/+eCrEtyovRWpmYzFl) | [ᴄʜᴀɴɴᴇʟ 📣](t.me/onsbase)"


def user_help():
    return """With this bot you can chat with Guys and Girls anonymously based on your preferences of age, gender.

Commands
/start - start the bot
/next — find a new partner
/stop — stop this dialog
/setsex - set your gender and partner sex
/setinfo - set your age and domisili
/sharelink - share profile to partner
/report - Report a message
/help - show the guide

"""

def age_user():
    return "settings di @testeronsbot"

def partner_not_found():
    return """🔎 Searching for a partner"""


def destroy(who=None):
    if who == "You":
        return """You stopped the dialog 🙄
Type /next to find a new partner
Type /setsex to set gender
Type /setinfo to set age and domisili

jangan lupa sebar sebar link @cintasatumalambot agar lebih ramai pengunannya"""
    elif who == "Your":
        return """Your partner has stopped the dialog 😞
Type /next to find a new partner

Don't forget share link @cintasatumalambot to make more friends"""


def invalid_destroy():
    return """You have no partner 🤔
Type /next to find a new partner

Don't forget share link @cintasatumalambot to make more friends"""
