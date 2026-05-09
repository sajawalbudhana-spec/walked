import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WALLET = "TTWYTUp1VEbTkQJcwnmujwsfKJ6Ud3Y3au"
CONTACT = "@sajawalbudhana3"


def main_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📣  Channel Subscribers", callback_data="ch_subs")],
        [InlineKeyboardButton("👥  Group Members",       callback_data="grp_members")],
        [InlineKeyboardButton("💎  Premium Services",    callback_data="premium")],
        [InlineKeyboardButton("💳  Payment & Pricing",   callback_data="pricing")],
        [InlineKeyboardButton("📞  Place an Order",      callback_data="contact")],
        [InlineKeyboardButton("🏆  Why Choose Us?",      callback_data="about")],
    ])


def back_btn():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🛒  Order Now", callback_data="contact")],
        [InlineKeyboardButton("🔙  Main Menu", callback_data="main_menu")],
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "┌─────────────────────────┐\n"
        "│   🚀  TG PROMOTION HUB   │\n"
        "└─────────────────────────┘\n\n"
        "Welcome to the *#1 Telegram Growth Service* 🌍\n\n"
        "We help creators, brands & businesses grow\n"
        "their Telegram presence with *real, active* members.\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "✅  Real & Verified Members\n"
        "✅  Fast Delivery — 24 to 72 hrs\n"
        "✅  100% Safe — No Password Needed\n"
        "✅  24/7 Customer Support\n"
        "✅  Trusted by 500+ Clients\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "👇 Select a service to get started:"
    )
    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=main_keyboard())


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # ── MAIN MENU ──────────────────────────────────────
    if data == "main_menu":
        text = (
            "┌─────────────────────────┐\n"
            "│   🚀  TG PROMOTION HUB   │\n"
            "└─────────────────────────┘\n\n"
            "Welcome to the *#1 Telegram Growth Service* 🌍\n\n"
            "We help creators, brands & businesses grow\n"
            "their Telegram presence with *real, active* members.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "✅  Real & Verified Members\n"
            "✅  Fast Delivery — 24 to 72 hrs\n"
            "✅  100% Safe — No Password Needed\n"
            "✅  24/7 Customer Support\n"
            "✅  Trusted by 500+ Clients\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👇 Select a service to get started:"
        )
        await query.edit_message_text(text, parse_mode="Markdown", reply_markup=main_keyboard())

    # ── CHANNEL SUBSCRIBERS ────────────────────────────
    elif data == "ch_subs":
        text = (
            "📣 *CHANNEL SUBSCRIBERS*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🟢 *REAL SUBSCRIBERS*\n"
            "│  Genuine accounts, active users\n"
            "│\n"
            "├  1,000   subs  ─  *$20*\n"
            "├  3,000   subs  ─  *$55*\n"
            "├  5,000   subs  ─  *$90*\n"
            "├  10,000  subs  ─  *$170*\n"
            "└  25,000  subs  ─  *$400*\n\n"
            "🔵 *PROXY / MIXED SUBSCRIBERS*\n"
            "│  High-speed bulk delivery\n"
            "│\n"
            "├  1,000   subs  ─  *$8*\n"
            "├  5,000   subs  ─  *$35*\n"
            "├  10,000  subs  ─  *$60*\n"
            "└  25,000  subs  ─  *$130*\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "⚡  Delivery: 24 – 72 hours\n"
            "🔒  Safe & Secure — No password required\n"
            "♻️  Partial refill guarantee included"
        )
        await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_btn())

    # ── GROUP MEMBERS ──────────────────────────────────
    elif data == "grp_members":
        text = (
            "👥 *GROUP MEMBERS*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🟢 *REAL GROUP MEMBERS*\n"
            "│  Active users, niche-targeted\n"
            "│\n"
            "├  1,000   members  ─  *$22*\n"
            "├  3,000   members  ─  *$60*\n"
            "├  5,000   members  ─  *$95*\n"
            "├  10,000  members  ─  *$180*\n"
            "└  25,000  members  ─  *$420*\n\n"
            "🔵 *PROXY / MIXED MEMBERS*\n"
            "│  Fast delivery, bulk packages\n"
            "│\n"
            "├  1,000   members  ─  *$9*\n"
            "├  5,000   members  ─  *$38*\n"
            "├  10,000  members  ─  *$65*\n"
            "└  25,000  members  ─  *$140*\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "⚡  Delivery: 24 – 72 hours\n"
            "🔒  Safe & Secure — No admin rights needed\n"
            "♻️  Partial refill guarantee included"
        )
        await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_btn())

    # ── PREMIUM SERVICES ───────────────────────────────
    elif data == "premium":
        text = (
            "💎 *PREMIUM SERVICES*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🔴 *AD-BASED SUBSCRIBERS* (Targeted)\n"
            "│  Real users via Telegram Ads\n"
            "│  Niche-specific targeting\n"
            "│\n"
            "├  1,000   subs  ─  *$40*\n"
            "├  3,000   subs  ─  *$110*\n"
            "├  5,000   subs  ─  *$180*\n"
            "└  10,000  subs  ─  *$340*\n\n"
            "🔴 *AD-BASED GROUP MEMBERS* (Targeted)\n"
            "│  Real users, topic-matched\n"
            "│\n"
            "├  1,000   members  ─  *$45*\n"
            "├  3,000   members  ─  *$120*\n"
            "├  5,000   members  ─  *$190*\n"
            "└  10,000  members  ─  *$360*\n\n"
            "⭐ *CUSTOM PACKAGE*\n"
            "Need a specific quantity or mix?\n"
            "Contact us for a tailored quote!\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🎯  Geo & niche targeting available\n"
            "📊  Analytics report on request\n"
            "♻️  Refill guarantee included"
        )
        await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_btn())

    # ── PRICING & PAYMENT ──────────────────────────────
    elif data == "pricing":
        text = (
            "💳 *PAYMENT & PRICING*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "We accept *USDT via TRC20 network* only.\n"
            "Fast, secure & borderless payments.\n\n"
            "📥 *Deposit Wallet Address:*\n"
            f"`{WALLET}`\n\n"
            "_(Tap to copy the address)_\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📋 *HOW TO ORDER — 4 Easy Steps:*\n\n"
            "1️⃣  Choose your service & quantity\n"
            "2️⃣  Send USDT to the wallet above\n"
            "3️⃣  Screenshot your payment receipt\n"
            "4️⃣  DM us your receipt + channel/group link\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "⏱  Orders processed within *1–6 hours*\n"
            "🚀  Delivery starts in *24–72 hours*\n"
            "🔐  Payment verified before work begins\n"
            "💬  Support: @sajawalbudhana3"
        )
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("📣  Channel Subs",    callback_data="ch_subs"),
             InlineKeyboardButton("👥  Group Members",   callback_data="grp_members")],
            [InlineKeyboardButton("💎  Premium Ads",     callback_data="premium")],
            [InlineKeyboardButton("🔙  Main Menu",       callback_data="main_menu")],
        ])
        await query.edit_message_text(text, parse_mode="Markdown", reply_markup=markup)

    # ── CONTACT ────────────────────────────────────────
    elif data == "contact":
        text = (
            "📞 *PLACE AN ORDER*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"💬  Contact us directly: *{CONTACT}*\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📝 *Please send us the following:*\n\n"
            "▸  Service type _(Subs / Members / Ads)_\n"
            "▸  Package quantity\n"
            "▸  Your channel or group link\n"
            "▸  Payment screenshot _(USDT TRC20)_\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "⏱  Response time: *1 – 6 hours*\n"
            "🕐  Working hours: *9 AM – 11 PM (PKT)*\n"
            "🌍  Serving clients worldwide\n\n"
            "We will confirm your order and\n"
            "begin delivery within 24 – 72 hours ✅"
        )
        await query.edit_message_text(text, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙  Main Menu", callback_data="main_menu")]
            ]))

    # ── ABOUT ──────────────────────────────────────────
    elif data == "about":
        text = (
            "🏆 *WHY CHOOSE TG PROMOTION HUB?*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "We are Pakistan's most trusted Telegram\n"
            "growth agency — run by a verified creator.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "👤  *Owner:*      @sajawalbudhana3\n"
            "🎥  *YouTube:*    30,000+ Subscribers\n"
            "📍  *Based in:*   Pakistan 🇵🇰\n"
            "👜  *Clients:*    500+ Served\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "⭐  *Our Guarantees:*\n\n"
            "✅  Real & verified members only\n"
            "✅  Partial refill on drop\n"
            "✅  No bots or fake accounts\n"
            "✅  Secure payment via USDT\n"
            "✅  24/7 after-order support\n"
            "✅  Confidential & professional\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 Start growing your channel today!"
        )
        await query.edit_message_text(text, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🛒  Order Now",  callback_data="contact")],
                [InlineKeyboardButton("🔙  Main Menu",  callback_data="main_menu")],
            ]))


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    logger.info("TG Promotion Hub Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
