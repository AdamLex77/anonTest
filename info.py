def welcome(name):
    return f"*Selamat Bergabung {name}🙊*\n\n_Semoga Dapat teman atau jodoh_\n\nType /next - untuk mencari jodoh\nType /help - show the guide\n\n*WAJIB JOIN*\n[👥 ɢʀᴏᴜᴘ](t.me/onsbase_grub) | [ᴄʜᴀɴɴᴇʟ 1📣](t.me/onsbase) | [ᴄʜᴀɴɴᴇʟ 2📣](t.me/ratemyonspartner) | [ᴄʜᴀɴɴᴇʟ 3📣](t.me/menfesonsbase)"


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
Type /setsex to set gender
Type /setinfo to set age and domisili

jangan lupa sebar sebar link @cintasatumalambot agar lebih ramai pengunannya"""


def invalid_destroy():
    return """You have no partner 🤔
Type /next to find a new partner
Type /setsex to set gender
Type /setinfo to set age and domisili

jangan lupa sebar sebar link @cintasatumalambot agar lebih ramai pengunannya"""
