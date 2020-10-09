"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

    input_str = event.pattern_match.group(1)

    if input_str == "calll":

        await event.edit(input_str)

        animation_chars = [
        
            "`MODI KO PHONE LAGA RAHA HU RUK...`",
            "`Call Connected.`",
            "`MODI KA ASSISTANT: HELLO I AM MODI KA ASSISTANT . Who is this?`",
            "`Me: AARE MERE KO NAHK PEHCHANA MODI JI SE PUCHO GANGSTER NAAM`",
            "`User Authorised.`",
            "`Calling MODI G`  `At +916969696969`",
            "`Private  Call Connected...`",
            "`Me: MODI SUN AAPKINBAAR KA ELECTION NAHI JEETEGA.`",    
            "`MODI: TUM PUBG WALE HO KYA ?`",
            "`Me: LOG PYAR SE GANGSTER URF APOORV KA BAAP BOLTE HAI  ",
            "`MODI: AAARE AAP KI PHONE KARNE KI ZARURAT HI NAHI THI MAI KHUD AAPSE BAAT KARNA CHAHTA THA \n AXHA KOI NA MERI SARKAR BANNE DO EK BAAR PHIR AAPKA KAAM KARUNGA .`",
            "`Me: LAVDE KI SARKAR BANEGI.`",
            "`MODI: Aare sar chinta mat karie mai kara raha hu solve.`",
            "`Me: kaam to sunn le kya karna hai `",
            "`MODI : Haa bolie kya kaam hai aapka abhi solve karata hu .`",
            "`Me: mera ek beta hai uxhapoorv naam karke telegram pe bechare ko pubg nahu khelne ko mila to nasbandi karlia vo ab tum pubg ko unban kari or mai apoorv ki mummy ki khujli theek karke aata hu .`",
            "`Pavel: Bilkul sar aap chinta mat karna  \nBye Bye :)`",
            "`Private Call Disconnected.`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 18])
