# -*- coding: utf-8 -*-
import re


class HTMLFormatter:
    def __init__(self):
        self.url = ''

    def tsformat(self, mathobject):
        return ''

    def urlformat(self, matchobject):
        self.url = '[url=' + matchobject.group(0) + ']INSERT TEXT HERE[/url]'
        return str(self.url)


# Testing name
text = """[8:45 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: Welcome everyone to the first interview of the year. Joining us today is the mastermind behind Extra Mario World, ya boi, Von Fahrenheit. How are you doin today?
[8:45 AM] Von Fahrenheit: Hello there! I’m good! I was starving but I just got my hands on some fried chicken so now I’m great :)
[8:46 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: Oo fried chicken sounds pretty good right about now
[8:46 AM] Von Fahrenheit: Better believe it
[8:47 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: Great to hear. Now that you've got some energy with you let's start off with the basic questions: When and how did you find out about romhacking?
[8:48 AM] Von Fahrenheit: I don’t know exactly, but probably around 2007-2009ish
[8:48 AM] Von Fahrenheit: I saw a video playthrough a Zelda hack called parallell worlds and was kind of blown away by the fact that you can change games
[8:49 AM] Von Fahrenheit: I thought they were more or less static before then I suppose
[8:50 AM] Von Fahrenheit: Link to the Past hackers use a program called Hyrule Magic, which is really terrible and easily breaks your ROM. That’s the reason I stuck with SMW, actually; Lunar Magic is that much better than Hyrule Magic.
[8:52 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: Oh I feel you man, we're pretty spoiled with Lunar Magic here haha definitely one of the better hacking tools out there
[8:52 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: same reason why I've stuck with smw as well :derpyoshi:
[8:53 AM] Von Fahrenheit: I still wanna make a Castlevania 3 hack some day lmao
[8:53 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: why not start now?
[8:53 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: :zoomEyes:
[8:55 AM] Von Fahrenheit: Honestly because I’m terrible with knowing when to quit. I have a handful of hacking ideas I want to try at some point but that will have to wait until after Extra Mario World is done ;)
[8:56 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: tru dat
[8:58 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: Before we get into Extra Mario World, now that there's a working demo of the most recent iteration of the game more people have seen your ASM skillz and all the cool things you can do. You were even an ASM mod at one point, if I recall correctly. 
So what inspired you to learn ASM?
[8:59 AM] Von Fahrenheit: Haha, now we’re talking!
[9:02 AM] Von Fahrenheit: I think first I saw some guy make an ASM showcase on youtube. He showed 32x32 blocks, some new powerup, stuff like that. I didn’t know what ASM meant but I thought it was incredible. Then I played this small 5-level ASM hack that mostly relied on gimmicks. It was basic stuff like a limited number of jumps in a level, one level where you played as Yoshi, one level where you had to swim with a bomb and make sure it didn’t explode, that kind of stuff. It ended with a very simple custom boss too. Overall it’s stuff we sneeze at now but it blew my mind at the time.
[9:05 AM] Von Fahrenheit: There’s another part to this story though. Someone made a hack of Super Mario 64 that simply added another player character (named ”Blario”, for some ungodly reason) that was controlled by player 2. I played this with a friend and found it brilliantly enjoyable. I thought ”this just has to exist for Super Mario World” and tried to find something similar. There wasn’t anything similar, but I did find a sprite programming tutorial by Nesquik Bunny.
[9:06 AM] Von Fahrenheit: Now, as soon as my little kid eyes landed on those words, ”sprite programming tutorial”, I thought that surely I had discovered some sort of holy ancient artifact. There’s no way normal people can just make things and put them in video games, right? That’s way too amazing to be true!
[9:08 AM] Von Fahrenheit: But I gave it a shot, and... it turned out to actually work. This realization probably made me nut a few times but I was too excited to notice. And so my first undertaking ever was making a sprite that could function as a second player. I did accomplish this after an obscene amount of trial and error, but that served as motivation to learn ASM.
[9:10 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: I remember those 32x32 blocks... When someone finally made a public version of that I went nuts tbh. Having those things is definitely cool, but being able to make those things is a lot of people's dreams I feel.
[9:10 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: wait
[9:10 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: but you're telling me
[9:10 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: your first ASM project ever
[9:11 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: was the second player sprite??
[9:12 AM] Von Fahrenheit: Yeah, that’s why I wanted to learn ASM in the first place. I actually asked one of my teachers if it could be my graduation project in high school and he said yes, so I got to have a presentation where I showed my ROM hack at school. I pulled up some volonteers and had them play for the crowd. Unfortunately they were really bad and couldn’t even beat the first level lol
[9:13 AM] Von Fahrenheit: The second player used the koopa graphics. I think that was before I learned about dynamic sprites so I just used something that was always loaded.
[9:13 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: :monkaOMEGA~1:
[9:14 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: thats pretty nuts for your first ASM thing
[9:14 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: even I didnt know that
[9:14 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: :HAhaa:
[9:14 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: ASM tutorial when?
[9:14 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: :derpyoshi:
[9:14 AM] Von Fahrenheit: lmao
[9:15 AM] Von Fahrenheit: I think all the necessary tutorials are already made to be honest. But yeah, that’s where Koops came from lol
[9:18 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: True
[9:18 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: But what advice do you have for people who want to learn ASM or are just starting out?
[9:18 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: Cuz I know even for me as a CS Major, ASM can look daunting to people who aren't familiar with it
[9:18 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: :HAhaa:
[9:19 AM] Von Fahrenheit: My best advice eh?
[9:20 AM] Von Fahrenheit: I would say set up a concrete goal. ”Learn ASM” is much too vague because you won’t actually know when you have done that. ”Be able to make a custom boss” is a much better goal because it’s operational. You will know with certainty when you have reached it, and you can approach it in incremental steps by making sprites of increasing complexity.
[9:27 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: I can agree with that. It's always important to set goals for oneself anyways
[9:27 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: Okay, now the part that other people have probably been waiting for: Extra Mario World!
[9:27 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: Where did you get the idea from?
[9:28 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: actually first, why don't you tell us what Extra Mario World is
[9:28 AM] Von Fahrenheit: It’s the :b:️EST hack of all time :sunglasses:
[9:30 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: :b: erry nice :EZ:
[9:31 AM] Von Fahrenheit: But somewhat more seriously it’s Super Mario World with a bit of extra everything. The idea came from the multiplayer hack I made, when I thought that I might as well make new levels too. Then I wanted to make custom bosses, because I love boss fights and Mario games usually have pretty lackluster ones. Then, you know, the second player was already different from Mario so why not have a bunch of characters to choose from?
[9:32 AM] Von Fahrenheit: It’s easy to see how this train of thought can spiral out of control, which it did, and the result is the concept for Extra Mario World. The name was totally stolen from the SMB hack ”Extra Mario Bros.”, which is a hack I admire a lot. Supposedly someone already made a Metroid-style SMW hack called ”Extra Mario World” a few years back, but don’t tell nobody ok?
[9:35 AM] Von Fahrenheit: ”All ideas are good ideas” was kind of the modus operandum early in development. EMW eventually got stripped of a lot of fat but this early stage of mad exploration was certainly important.
[9:40 AM] Von Fahrenheit: But what it is now? Well, you should totally check out our thread if you’re curious (hint hint). It’s the logical extreme of a chocolate hack I suppose, without sacrificing the Mario spirit. It has co-op, a bunch of different player characters, new levels, custom enemies and bosses, all the graphics and music are new, and so on. In my opinion it shares more conceptual space with a fan game than a hack, but it is technically still a ROM hack, so there you go.
[9:43 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: and where can these people find this thread? :expand:
[9:44 AM] Von Fahrenheit: Didn’t know if I was actually allowed to link it lol
[9:44 AM] Von Fahrenheit: https://www.smwcentral.net/?p=viewthread&t=78766
[9:44 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: why not? :derpyoshi:
[9:46 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: Care to elaborate on the custom characters for the game? Besides Mario, we got Kadaal and Leeway
[9:46 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: what can you tell us about those characters and are there more to come?
[9:54 AM] Von Fahrenheit: Yes! Kadaal is actually the continuation of the player 2 sprite actually. He shares very little other than being a purple turtle though. Kadaal and Leeway are both able to fight in melee and take a few cues from games like Castlevania and Megaman Zero. Their physics are very different from Mario's, but I think that's actually a benefit.
[9:55 AM] Von Fahrenheit: Luigi is under development right now, and he'll be something more familiar for most players.
[9:55 AM] Von Fahrenheit: We're also working on at least 2 more characters but their identities are secret for now ;)
[9:57 AM] Von Fahrenheit: Something true for all the characters is that they can be upgraded (sort of like a Metroidvania) to increase their mobility and combat capabilities.
[9:59 AM] Von Fahrenheit: Balancing a roster of different characters makes me really appreciate skilled game designers like Sakurai haha
[10:04 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: Gotta keep wanting more :derpyoshi:
[10:05 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: What else about the game should people know about? Will it have an overworld, etc
[10:05 AM] Von Fahrenheit: Oh what should they know? Hmm
[10:06 AM] Von Fahrenheit: We do not have an overworld. We replaced that with a level select menu that makes navigation much quicker, especially when hunting down yoshi coins you might have missed.
[10:07 AM] Von Fahrenheit: I guess people should know that we have a difficulty selection! You choose easy, normal or insane, and can choose to enable extra challenges like instant death, no check points, or time limits on top of that.
[10:09 AM] Von Fahrenheit: It's pretty unique and should help players find a reasonable challenge for their skill level :)
[10:12 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: Well it seems that's about all the questions I could think of. Anything else you wanna add before we wrap this thing up?
[10:13 AM] Von Fahrenheit: You wanna join extra mario world btw? Hit us up! We're currently looking for level designers. Programmers and composers are also wanted :)
[10:13 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: Yea, don't be afraid to reach out. Von Fahrenheit is the main guy but if you can't reach him for some reason Eminus and I are also available to pm.
[10:13 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: :HAhaa:
[10:14 AM] Von Fahrenheit: Kids, set up goals for yourself and try to accomplish them. Your life will be better if you do :)
[10:15 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: :Pog:
[10:17 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: And that's gunna be it for this interview. Thanks for joining me today. It was great getting to know more about you and your hacking background. Hopefully SMWC will be around by the time we finish EMW :HAhaa:
[10:18 AM] Von Fahrenheit: lmao of course it will!
[10:18 AM] Von Fahrenheit: Well, this is Von Fahrenheit signing out!
[10:18 AM] Qats ( ͡° ͜ʖ├┬┴┬┴: :jeanneFlag:"""

# HTTP regex
urlRegex = r'(?P<url>https?://[^\s]+)'
# Discord timestamp regex
tsRegex = r'(\[\d+:\d+\s(AM|PM)\]\s)'
# HTML Discord Interview Formatter
formatter = HTMLFormatter()
urlPattern = re.compile(urlRegex)
timestampPattern = re.compile(tsRegex)
# Remove all timestamps
text = timestampPattern.sub(formatter.tsformat, text)
# Format all URLs to be SMWC post ready
out = urlPattern.sub(formatter.urlformat, text)
print(out)
