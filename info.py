def welcome(name):
    return f"*Selamat Bergabung Di {name}🙊*\n\n_Semoga Dapat teman atau jodoh_\n\n*NOTE:*\nWAJIB JOIN\n[👥 ɢʀᴏᴜᴘ](t.me/onsbase_grub) | [ᴄʜᴀɴɴᴇʟ 1📣](t.me/onsbase) | [ᴄʜᴀɴɴᴇʟ 2📣](t.me/ratemyonspartner) | [ᴄʜᴀɴɴᴇʟ 3📣](t.me/menfesonsbase) | [📱ᴏᴡɴᴇʀ](t.me/nazhak)"


def user_help():
    return """With this bot you can chat with Guys and Girls anonymously based on your preferences of age, gender.

Commands
/start - start the bot
/next — find a new partner
/stop — stop this dialog
/settings - settings menu
/sharelink - share profile to partner
/report - Report a message
/help - show the guide

"""

def age_user():
    return "settings di @testeronsbot"


def partner_match(gender):
    if gender == "Boy":
        partner = "🤴🏻 Boy"
    else:
        partner = "👸🏻 Girl"

    return f"""Partner: {partner}
/next — find a new partner
/stop — stop this dialog"""


def partner_not_found():
    return """🔎 Searching for a partner"""


def destroy(who=None):
    if who == "You":
        return """You stopped the dialog 🙄
Type /next to find a new partner
"""
    elif who == "Your":
        return """Your partner has stopped the dialog 😞
Type /next to find a new partner
"""


def invalid_destroy():
    return """You have no partner 🤔
Type /next to find a new partner"""
