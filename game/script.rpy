# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image bg ocean = Image("ocean_01.png")
image bg ocean trails = Image("ocean_trails.png")
image bg ocean gloria = Image("ocean_gloria.png")
image bg ocean peggy = Image("ocean_bar.png")
image bg ocean ellie = Image("ocean_ellie.png")
image barry neutral = Image("barry_neutral.png", xalign = 0.0, yalign = 0.6)
image barry smirk = Image("barry_smirk.png", xalign = 0.0, yalign = 0.6)
image barry sad = Image("barry_sad.png", xalign = 0.0, yalign = 0.6)
image barry panic = Image("barry_panic.png", xalign = 0.0, yalign = 0.6)
image barry drunk1 = Image("barry_drunk1.png", xalign = 0.0, yalign = 0.6)
image barry drunk2 = Image("barry_drunk2.png", xalign = 0.0, yalign = 0.6)
image barry dead = Image("barry_dead.png", xalign = 0.0, yalign = 0.6)
image ellie reveal = Image("Ellie_yellow_W.png", xalign = 1.3, yalign = 0.0)
image ellie white = Image("Ellie_silhouette_W.png", xalign = 1.3, yalign = 0.0)
image ellie blue = Image("Ellie_silhouette_B.png", xalign = 1.3, yalign = 0.0)
image ellie yellow = Image("Ellie_silhouette_Y.png", xalign = 1.3, yalign = 0.0)
image ellie red = Image("Ellie_silhouette_R.png", xalign = 1.3, yalign = 0.0)
image ellie win = Image("Ellie_WIN.png", xalign = 0.5, yalign = 0.5)
image gloria neutral = Image("Gloria_neutral.png", xalign = 1.0, yalign = 0.4)
image gloria happy = Image("Gloria_happy.png", xalign = 1.0, yalign = 0.4)
image gloria mad = Image("Gloria_mad.png", xalign = 1.0, yalign = 0.4) 
image gloria book = Image("Gloria_book.png", xalign = 1.0, yalign = 0.4)
image gloria win = Image("Gloria_WIN.png", xalign = 0.5, yalign = 0.8)
image peggy neutral = Image("Peggy_neutral.png", xalign = 1.0, yalign = 0.3)
image peggy happy = Image("Peggy_happy.png", xalign = 1.0, yalign = 0.3)
image peggy negative = Image("Peggy_negative.png", xalign = 1.0, yalign = 0.3)
image peggy win = Image("Peggy_WIN.png", xalign = 0.5, yalign = 0.5)
image heart = Image("Heart.png", xalign = 0.5, yalign = 0.7)
image bartender = Image("bartender.png", xalign = 1.0, yalign = 0.3)

# Declare characters used by this game.
define b = Character('Barry', color="#0000FF")
define e = Character('Ellie', color="#FFFF00")
define g = Character('Gloria', color="#8000FF")
define p = Character('Peggy', color="#FF0000")

# The game starts here.
label start:
    $   ellie_gone = False
    $   ellie_level = 0
    $   gloria_gone = False
    $   gloria_mood = 0
    $   gloria_level = 0
    $   peggy_gone = False
    $   peggy_mood = 0
    $   peggy_level = 0    
    play music "underwater.ogg"
    scene bg ocean
    show barry neutral with dissolve
    
    "You wake up on the ocean floor..."

    b   "What is going on?"
    b   "Is any of this real?"
    b   "More importantly... where are the ladies?"
    
    label trails:
    play music "underwater.ogg" fadeout 1.0
    scene bg ocean trails with fade
    
    "You see 3 pheromone trails - yellow, red, and purple."
    
    menu:
        "Yellow - Leads to a nearby shipwreck.":
            if ellie_gone:
                jump elliegone
            if ellie_level is 0:
                jump ellieintro
            if ellie_level is 1:
                jump ellie1
                
        "Red - Leads to the local bar.":
            play music "jazzmusic.ogg" fadeout 1.0
            if peggy_gone:
                jump peggygone
            if peggy_level is 0:    
                jump peggyintro
            if peggy_level is 1:
                jump peggy1
            if peggy_level is 2:
                jump peggy2
            if peggy_level is 3:
                jump peggy3
                
        "Purple - Leads to a nearby park.":
            if gloria_gone:
                jump gloriagone
            if gloria_level is 0:
                jump gloriaintro
            if gloria_level is 1:
                jump gloria1
            if gloria_level is 2:
                jump gloria2
            if gloria_level is 3:
                jump gloria3
                

    

                
                
                
label ellieintro:
    $   ellie_level = 1
    scene bg ocean ellie with fade
    show barry neutral with dissolve
    show ellie white with dissolve
    
    e       "..."
    b       "(Wow! She’s huge!)"
    b       "(Maybe she’s out of my league…)"
    b       "(But I have to try!)"

    menu:
        "Be suave.":
                b   "Hey good looking!"
            
        "Be courteous":
                b   "What a lovely shipwreck you live in!"
            
        "Be funny.":
                b   "Did you hear the one about the priest, the rabbi, and the angler fish?"
            
e       "..."
b       "(She's quiet...)"
menu:
    "Ask her name.":
        b       "What's your name?"

    "Leave.":
        jump trails
        
e       "..."
b       "..."
e       "LE-105."
b       "Do you mind if I shorten that to Ellie?  It’s a pretty name."
b       "I’m Barry."
b       "So, you know…"
b       "I’m kind of in the market…"

menu:
    "Come on to her.":
        b       "So I was thinking we could rub fins later..."
        show ellie blue
        e       "..."
        show barry panic with dissolve
        b       "Sorry I didnt mean it like that."
        e       "..."
        b       "(I think I upset her, I should find some way to make her like me.)"
        jump trails
        
    "Back off.":
        b       "Um uh, if you know anyone then let me know!"
        jump trails
        
    "Leave.":
        jump trails
   
label ellie1:
    $   ellie_gone = True
    scene bg ocean ellie with fade
    show barry neutral with dissolve
    show ellie white with dissolve
    
    "As you approach the shipwreck, you find Ellie not too far from where she was originally."
    menu:
        "Enthusiastic greeting.":
            "Hey Ellie! How's it going!?!?"
        "Cautious greeting.":
            "Hello, remember me?"
            "I'm Barry?"
        "Romantic greeting.":
            "Hello my sweet sugar pea!"
    show ellie yellow with dissolve
    e   "..."
    menu:
        "Oh god I pissed her off! (Run!)":
            show barry panic with dissolve
            b   "Aaah!!!"
            jump trails
        "What a gorgeous glow you have!":
            e   "..."
            b   "Truly the most beautiful I have ever seen!"
            e   "..."
            show ellie red with dissolve
            menu:
                "Red means danger! (Run!)":
                    show barry panic with dissolve
                    b   "Oh sweet fish jesus, save me!"
                    jump trails
                "Ah red, the colour of love...":
                    b   "You really know how to set the mood."
                    e   "..."
                    b   "You are so sexy and mysterious."
                    e   "..."
                    b   "Ellie I have something to confess..."
                    e   "..."
                    menu:
                        "I am madly in love with you.":
                            e   "..."
                            b   "I will take your silence to mean that you feel the same way about me!"
                            b   "Thank Poseidon!  I have found love at last!"
                            menu:
                                "Go for the kiss!":
                                    jump ellievictory
                                "Wuss out at the last second!":
                                    show ellie blue with dissolve
                                    e   "..."
                                    b   "I'm going to go..."
                                    menu:
                                        "Leave (She was totally into you!)":
                                            jump trails
                        "You creep the hell out of me!":
                            show ellie blue with dissolve
                            e   "..."
                            b   "..."
                            e   "..."
                            menu:
                                "I should probably go...":
                                    jump trails

label elliegone:
    
    scene bg ocean ellie with fade
    show barry neutral with dissolve

    "The shipwreck appears to be abandoned..."
    b   "(I wonder where Ellie went...)"
    
    jump trails
                                    
label ellievictory:
    "Looks like things are about to get hot and heavy!"
    show barry smirk:
        ease 3.0 truecenter
    show ellie reveal:
        ease 3.0 truecenter
    pause 1.0
    show heart with dissolve:
        zoom 1.3
    pause 5.0
    hide barry
    hide gloria
    hide heart
    show ellie win with dissolve
    pause 3.0
    "Well that wasn't how you expected things to go..."
    "At least you went for it right?"
    menu:
        "End Game.":
            return
                                    
label gloriaintro:
    $   gloria_level = 1
    scene bg ocean gloria with fade
    show barry neutral with dissolve
    
    "The thermal vent park is usually deserted, but a scent led you here..."
    "And then you see her, with her nose buried in a book."
    
    show gloria book with dissolve
    b   "(She's beautiful!)"
    b   "(And she's all alone here...)"
    b   "(What a perfect opportunity!)"
    
    menu:
        "Be smooth.":
            b   "What's a fish like you doing in a place like this?"
            b   "You're hot enough without being by these steam vents."
            show gloria mad with dissolve
            g   "Do you think I'm that kind of fish?"
            g   "If you're going to be like that then you should just swim away."
            menu:
                "Apologize":
                    b   "I'm sorry. I was so taken in by your beauty that I had to say something."
                    show gloria neutral with dissolve
                    g   "Oh really? That's so sweet.  I guess it's okay."
                    jump neutralgloria0
                "Hit on her again.":
                    show barry smirk with dissolve
                    b   "Come on babe, you know I'm your type."
                    show gloria mad with dissolve
                    g   "!"
                    g   "How rude!"
                    g   "I'm leaving!"
                    $   gloria_gone = True
                    jump trails
        "Be polite.":
            b   "You look lonely."
            b   "Mind if I join you?"
            g   "Not at all!"
            jump neutralgloria0
        "Be romantic.":
            b   "She swims in beauty, like the sea"
            b   "of shadowy depths and shining waves."
            show gloria happy with dissolve
            g   "You know Lord Salmon!"
            g   "That's amazing!"
            jump happygloria0
            
label neutralgloria0:
    show gloria neutral with dissolve
    g   "I'm Gloria. Nice to meet you."
    g   "I like to come here and read. I think it's beautiful, and sometimes I find pearls!"
    g   "I don't often see other fish here. It's nice to have some company."
    g   "I usually sit by myself and read."
    
    menu:
        "Ask about her book.":
            b   "So what are you reading?"
            g   "Oh, this?"
            show gloria book with dissolve
            g   "This is a collection of Classical poetry!"
            g   "Sharkespeare is my favourite."
            g   "I'm actually just in the middle of a sonnet. Why don't you come back later?"
            menu:
                "Leave. (She seems to like you a bit!)":
                     $       gloria_mood = 1
                     jump trails
        "Compliment her.":
            b   "You don't meet many fish who like to read."
            b   "You must be very cultured!"
            show gloria happy with dissolve
            g   "You really mean it? That's so kind."
            jump happygloria0
label happygloria0:
    g   "You have such a way with words!"
    g   "It reminds me of my favourite author: Sharkespeare!"
    g   "So, what brings you to the park?"
    menu:
        "Little white lie...":
            b   "I just wanted to admire me some natural beauty!"
            g   "That's wonderful. Well, don't let me keep you."
            g   "But you should come back and visit me soon!"
            menu:
                "Leave. (She seems to like you a lot!)":
                    $   gloria_mood = 2
                    jump trails
        "Honesty is the best policy!":
            b   "Actually, I noticed your pheromones and followed the trail here."
            b   "I'm looking to settle down."
            g   "Oh..."
            show gloria neutral with dissolve
            g   "I don't think I know you well enough for that."
            g   "I need some time to think."
            menu:
                "Leave. (She seems to like you a bit!)":
                    $   gloria_mood = 1
                    jump trails
    
    
label gloria1:
    $gloria_level = 2
    scene bg ocean gloria with fade
    show barry neutral with dissolve
    if gloria_mood is 2:
        jump gloriahappy1
    show gloria neutral with dissolve    
    "Gloria is staring at the steam put out by the thermal vents with a content look on her face..."
    b   "(I think she liked me...)"
    b   "(I should try to get to know her better!)"
    b   "Hi Gloria!"
    g   "Oh hey Barry!"
    menu:
        "So tell me more about yourself.":
            g   "You're really that interested in me?"
            b   "(Hell yeah I am!)"
            g   "Well I like to read..."
            b   "(Yes... I know...)"
            g   "I also like to garden..."
            g   "And take moonlit swims..."
            show barry smirk with dissolve
            b   "(Now we're getting somewhere!)"
            g   "Sorry, did you say something?"
            show barry panic with dissolve
            b   "!"
            b   "(I better say something good, and quickly!)"
            jump gloriacompliment1
        "We talked about you a bit last time, so why don't I tell you a little bit about myself?":
            b   "Well my dad was an angler fish..."
            b   "So was my mom..."
            b   "We lived in the ocean for a few years..."
            b   "But then they both got eaten by a shark..."
            b   "So I moved here to the deep ocean to try to start a new life..."
            b   "..."
            b   "Well... what do you think?"
            g   "........."
            g   "......zzzz"
            show barry sad with dissolve
            b   "...Gloria?"
            g   "zzzzz-wha?"
            g   "Oh! Sorry!"
            b   "(I didn't think I was that boring...)"
            g   "I'm so sorry, that was so rude."
            show barry neutral with dissolve
            b   "It's okay!"
            b   "I wanted to tell you something..."
            g   "Yes Barry?"
            jump gloriacompliment1
            
label gloriacompliment1:
    menu:
        "Sweet compliment.":
            b   "The glow of your light warms my heart."
            show gloria happy with dissolve
            g   "(swoon)"
            g   "You know, I think I like you a lot more than I though I would."
            g   "It's getting late though, you should meet me back here again tomorrow night!"
            show barry smirk with dissolve
            $   gloria_mood = 2
            menu:
                "Leave (She seems to really like you!)":
                    jump trails
        "Spicy compliment.":
            show barry smirk with dissolve
            b   "You're like a prize winning fish..."
            b   "I don't know if I should eat you or mount you!"
            show gloria mad with dissolve
            g   "Ugh!"
            g   "And here I was thinking you were better than that!"
            g   "I'm looking for a nice fish, not a pig!"
            show barry sad with dissolve
            g   "I'm leaving, don't ever try to talk to me again..."
            $   gloria_gone = True
            menu:
                "Leave (She hates your guts... Good job...)":
                    jump trails
                    
label gloriahappy1:
    show gloria book with dissolve
    "Gloria is reading. She's moved on to a different book."
    "This one is much thicker - it looks like she's concentrating."
    menu:
        "Approach her.":
            jump gloriagreeting1
        "Let her read.":
            "..."
            "......"
            "........."
            menu:
                "Approach her.":
                    jump gloriagreeting1
                "Leave":
                    $   gloria_level = 1
                    jump trails
label gloriagreeting1:
    b   "(I better try to be a gentleman...)"
    b   "Good evening, Gloria. I see you've switched books."
    g   "I have! I wanted something more challenging."
    b   "Actually, I wanted to tell you that you inspired me to pick up a book this afternoon!"
    b   "I read a passage that reminded me of you."
    b   "Would you like to hear it?"
    g   "Would I ever!"
    menu:
        "A-Sea/D-Sea":
            b   "You hooked me all night long!"
            show gloria mad with dissolve
            g   "How crass!"
            g   "I thought you were better than that..."
            g   "Saying something like that is bad enough without getting my hopes up!"
            g   "Good bye and good ridance!"
            menu:
                "Leave.":
                    $gloria_gone = True
                    jump trails
                    
        "Sharkspeare":
            b   "Sonnet parody."
            show gloria happy with dissolve
            g   "You remembered my favourite author?"
            g   "That's so sweet."
            g   "I've never met a fish who like Sharkspeare as much as I do."
            menu:
                "Of course I remembered!":
                    b   "It's important to you, so it's important to me."
                    g   "(swoons)"
                    b   "I'd never read him before, but you've opened my eyes to literature."
                    g   "Look at me, I'm all flustered."
                    g   "Let me compose myself.  But promise me you'll come back later, okay?"
                    show barry smirk with dissolve
                    menu:
                        "I promise!":
                            $gloria_mood = 3
                            jump trails
                        "Just kidding! I'm not interested in you!":
                            show gloria mad with dissolve
                            g   "I can't believe you!"
                            g   "(sobbing)"
                            g   "You're a monster!"
                            g   "(runs away)"
                            hide gloria neutral
                            menu:
                                "Leave (That was awkward...)":
                                    $gloria_gone = True
                                    jump trails
                "The things I do for love.":
                    b   "I had to remember."
                    g   "What do you mean?"
                    b   "Well, if I want to hook up with you then I have to remember these things."
                    show gloria mad with dissolve
                    g   "Hook up?!"
                    g   "Is that all you think of me?"
                    g   "I can't believe I was starting to like you!"
                    menu:
                        "Leave (What a jerk...)":
                            $gloria_gone = True
                            jump trails
                    
        "Chumford and Sons":
            b   "I will bait, I will bait for you."
            g   "..."
            b   "...what?"
            show barry sad with dissolve
            b   "I thought you liked Chumford and Sons."
            g   "No..."
            g   "I like Sharkspeare..."
            g   "I'm not sure how you mixed those up."
            show barry neutral with dissolve
            b   "(Whoops...)"
            g   "But, I guess you at least tried to show me something I liked."
            g   "Look, I have to go meet my sister and her new husband for dinner."
            g   "But maybe I'll see you later?"
            menu:
                "Goodbye! (That was awkward...)":
                    $gloria_mood = 2
                    jump trails
                    
label gloria2:
    $gloria_level = 3
    scene bg ocean gloria with fade
    show barry neutral with dissolve
    show gloria neutral with dissolve
    if gloria_mood is 3:
        jump gloriahappy2
        
    "Gloria looks pensive."
    "She smiles and waves when she notices you."
    "Now is your chance!"
    b   "Gloria! You're looking as beautiful as ever."
    g   "Thank you Barry!"
    g   "You always say the sweetest things."
    g   "Actually, that reminds me of something I wanted to talk to you about..."
    show barry panic with dissolve
    g   "So... am I right in thinking that you're interested in me as more than a friend?"
    menu:
        "Honesty is the best policy...":
            show barry neutral with dissolve
            b   "You caught me!"
            b   "I would love to attach myself to your side and live with you forever!"
            g   "That's so romantic Barry, but..."
            g   "Tell me: have you been looking at ladyfish other than me?"
            menu:
                "You're the only one for me.":
                    b   "Yeah, I talked to other ladies..."
                    show barry smirk with dissolve
                    b   "But none of them are like you!"
                    b   "You're the only ladyfish for me Gloria!"
                    show gloria happy with dissolve
                    g   "Oh Barry!"
                    jump gloriavictory
                "You're the best fish in the sea!":
                    b   "Yeah..."
                    b   "I may have talked to other ladyfish..."
                    b   "But you're so clearly the best lady in this town!"
                    g   "..."
                    b   "(That pobably wasn't the best thing to say...)"
                    g   "Barry I don't think you get me."
                    show barry sad with dissolve
                    g   "Maybe we should just be friends."
                    menu:
                        "Ok, lets hang out later though!":
                            jump trails
        "Maybe...":
            b   "I wasn't sure how you felt about me..."
            b   "I felt like you were giving me mixed signals..."
            b   "So I felt kind of mixed about you..."
            g   "Oh... so how do you feel about me now?"
            menu:
                "Be a bit cautious...":
                    b   "Well..."
                    b   "I really like you..."
                    g   "Are you sure? I mean, you said you were mixed..."
                    menu:
                        "I really do mean it, you're the only one for me!":
                            b   "I'm sure!"
                            show barry smirk with dissolve
                            b   "I've never been so sure about anything in my life!"
                            show gloria happy with dissolve
                            g   "Wow! Such passion!"
                            jump gloriavictory
                        "I still don't know what I want...":
                            b   "Even still you're giving me mixed signals!"
                            b   "I don't know what you want from me."
                            g   "Did you ever stop to think whether it was a test Barry?"
                            show gloria mad with dissolve
                            g   "And I'm sorry, but you failed it."
                            g   "I think we should just be friends."
                            show barry sad with dissolve
                            menu:
                                "Ok.":
                                    jump trails
                "Go for it!":
                    show barry smirk with dissolve
                    b   "I really like you and would like to fuse my face to your side."
                    g   "..."
                    g   "I'm just not attracted to you that way."
                    g   "You're a really good person though."
                    b   "(Oh no!)"
                    show barry sad with dissolve
                    b   "(It looks like I've just crossed over, into...)"
                    menu:
                        "The Friend Zone!":
                            jump trails
        "I was...":
            b   "I was, but you keep playing hard to get."
            b   "It makes a guy feel like you're not interested!"
            show gloria mad with dissolve
            g   "Me? Playing hard to get? What are you talking about!?"
            b   "You totally were... Mixed signals, the whole shebang."
            g   "If you really loved me you would've kept on going..."
            b   "Well I guess I don't love you then."
            g   "Fine."
            b   "Fine."
            g   "I'm going home."
            menu:
                "Fine.":
                    jump trails
                    
label gloriahappy2:
    "Gloria is swimming in circles."
    "She looks nervous."
    b   "(Maybe she's been anxiously waiting for me!)"
    b   "Hello, my cultured pearl."
    g   "Oh Barry!"
    g   "You're so suave."
    b   "Only because I have such a good reason to be."
    g   "(swoons)"
    g   "So... I think we've gotten pretty close..."
    g   "And I was wondering..."
    g   "Would you maybe want..."
    b   "(Want what!?!?)"
    g   "...to be my boyfriend?"
    menu:
        "Sweet response":
            b   "I would be honoured to be your boyfriend."
            show gloria happy with dissolve
            b   "I would be the luckiest fish in the sea!"
            g   "I'm so glad you said yes!"
            show barry smirk with dissolve
            jump gloriavictory
        "Maybe we should go on a date to see if we're compatible?":
            g   "I thought we were pretty compatible!"
            g   "But that sounds like a good idea."
            g   "We should go to a concert!"
            menu:
                "Let's go to the Orcastra!":
                    show gloria happy with dissolve
                    g   "I love the Orcastra!"
                    g   "What a great idea."
                    g   "You really get me!"
                    jump gloriavictory
                "Ziggy Starfish is playing soon!":
                    g   "Oh..."
                    show gloria mad with dissolve
                    g   "I don't really like Ziggy Starfish..."
                    g   "Barry, I don't think you get me."
                    g   "Maybe we should just be friends."
                    show barry sad with dissolve
                    "Good going dude..."
                    "The only thing worse than a creeping dead zone..."
                    menu:
                        "Is the friend zone...":
                            jump trails
        "It's about time!":
            show barry smirk with dissolve
            b   "Finally!"
            g   "Excuse me?"
            b   "It took you long enough!"
            b   "I had to put up with Sharkspeare..."
            b   "I mean, what a pain!"
            show gloria mad with dissolve
            g   "I can't believe you!"
            g   "After all that, you're really just so shallow!"
            g   "I would never date someone like you."
            show barry sad with dissolve
            g   "Goodbye!"
            menu:
                "Um... Goodbye":
                    $gloria_gone = True
                    jump trails
                
            
label gloria3:
    scene bg ocean gloria with fade
    show barry neutral with dissolve
    show gloria book with dissolve
    
    "Gloria is reading her book again."
    "She smiles when she notices you and beckons you over."
    g   "Hi Barry!"
    g   "I was just reading some Sharkspeare."
    g   "Would you like to join me?"
    menu:
        "Join her.":
            b   "I'd love to."
            "You read Sharkspeare together."
            show barry sad with dissolve
            "Your head starts to hurt after a while so you politely excuse yourself."
            menu:
                "Leave (I'm so sick of Sharkspeare...)":
                    jump trails
        "Try your luck.":
            show barry smirk with dissolve
            b   "Actually, I was wondering if I could speare your shark... If you know what I mean..."
            g   "!"
            show gloria mad with dissolve
            g   "Seriously Barry?"
            g   "After all this time?"
            g   "You're disguisting..."
            hide gloria neutral with dissolve
            b   "(Well that didn't go very well...)"
            menu:
                "Leave (how did that line not work!?)":
                    $gloria_gone = True
                    jump trails
                    
label gloriagone:
        scene bg ocean gloria with fade
        show barry neutral with dissolve
        
        "The park is empty."
        show barry sad with dissolve
        b       "(I wonder where Gloria is...)"
        
        menu:
            "Leave.":
                jump trails
    
label gloriavictory:
    g   "Oh Barry, you really do care about me!"
    g   "I'm the luckiest ladyfish in the world!"
    b   "I love you Gloria!"
    g   "I love you Barry!"
    show barry smirk:
        ease 3.0 truecenter
    show gloria happy:
        ease 3.0 truecenter
    pause 1.0
    show heart with dissolve:
        zoom 1.3
    pause 5.0
    hide barry
    hide gloria
    hide heart
    show gloria win with dissolve
    pause 3.0
    "Congratulations!"
    "You found true love!"
    menu:
        "End Game.":
            return
    
    
    
label peggyintro:
    $   peggy_level = 1
    
    scene bg ocean peggy with fade
    show barry neutral with dissolve
    
    "As you enter the local bar, you are met with the sounds of sleazy jazz music, and are overwhelmed with the scents of many fertile females."
    "The crowd parts and reveals a stunning fish, with a body that sends your reproductive instincts into overdrive."
    
    show peggy neutral with dissolve
    
    
    label peggyintro1:
    menu:
        "Flirty introduction.":
            b   "It might be the sea-beers talking, but I've never seen an angelfish in the deep ocean before."
            p   "Oh you are too funny, how have I not met you before?"
            b   "You were probably too busy fending off your schools of suitors to notice me."
            p   "You are too kind."
            p   "Well my name is Peggy."
            jump afterpeggyintro
            
        "Romantic introduction.":
            b   "Shall I compare thee to the deep dark sea?"
            b   "Thou art more luminous and more inviting"
            b   "Rough currents do stir the bright anemones"
            b   "And the seas cold depths can be so biting."
            p   "..."
            b   "..."
            p   "..."
            b   "..."
            p   "Do you want to buy me a drink?"
            b   "Um, yes thats basically what I meant..."
            b   "(Goes to the bar and buys a round of sea-beers for the two of them.)"
            p   "Thanks, so my name is Peggy."
            jump afterpeggyintro
            
        "Loiter nearby and hope she starts a conversation with you.":
            "You awkwardly wait beside her for a few minutes."
            "She is constantly being hit on by other fish..."
            "She doesnt even notice you..."
            "(Lets try that again...)"
            jump peggyintro1
            
label afterpeggyintro:

    p   "What is your name?"
    b   "My name is Barry."
    
    menu:
        "So you come here often?":
            p   "Really?"
            p   "Thats the line you're going with?"
            p   "Honey, I practically own this place, and don't take this the wrong way but you should probably step up your game."
            p   "I have to go now, but come talk to me later."
            p   "I'll give you a second chance..."
            p   "Only because you're cute..."
            menu:
                "Leave (It sounds like you have a chance!)":
                    $   peggy_mood = 1
                    jump trails
            
        "So tell me about yourself.":
            p   "What is there to say that you can't already see."
            p   "Clearly I am a fish that posseses certain desirable... assets..."
            p   "And I certainly expect my suitors to be of the same quality as myself."
            b   "How do I measure up so far?"
            p   "That remains to be seen."
            p   "You do have a nice set of fins on you though."
            menu:
                "Thanks, yours are pretty nice as well!":
                    p   "Oh I know hon, I don't need you to tell me that."
                    p   "Listen, I gotta run, how about you meet me back here later, and we can continue where we left off."
                    menu:
                        "Sounds good to me!":
                            menu:
                                "Leave (She seems very interested in you!)":
                                    $peggy_mood = 2
                                    jump trails
                            
                        "How do I know you aren't trying to avoid me!?":
                            p   "If you keep acting like that, I won't need to try..."
                            b   "Ok, I'll see you then..."
                            menu:
                                "Leave (She seems to be interested in you!)":
                                    $peggy_mood = 1
                                    jump trails
                    
                "It's not how they look, but how I use them... If you know what I mean...":
                    show peggy happy
                    p   "Oh you are too much!"
                    p   "I'm sorry but I need to go meet a friend for lunch, how about we meet back here in about an hour?"
                    b   "Yes ma'am!"
                    $   peggy_mood = 2
                    jump trails
                "Hey!  Don't objectify my like that!":
                    p   "Oh I want to do more than 'objectify' you... If you know what I mean..."
                    b   "(gulp!)"
                    b   "Sorry I don't know what you mean..."
                    p   "I've got to run, but how about you meet me back here in about an hour to find out..."
                    menu:
                        "Sounds good to me!":
                            menu:
                                "Leave (She seems very interested in you!)":
                                    $peggy_mood = 2
                                    jump trails
                            
                        "How do I know you aren't trying to avoid me!?":
                            p   "If you keep acting like that, I won't need to try..."
                            b   "Ok, I'll see you then..."
                            menu:
                                "Leave (She seems to be interested in you!)":
                                    $peggy_mood = 1
                                    jump trails
                                    
        "So I am looking for a mate...":
            p   "You and every other fish in the sea!"
            p   "But I like your style, I hate a fish that doesn't know what he wants."
            p   "Listen, I told a friend of mine I'd meet her for lunch."
            p   "How about you meet me back here in a little bit and we continue this conversation then?"
            menu:
                "Sounds good to me!":
                    menu:
                        "Leave (She seems very interested in you!)":
                            $peggy_mood = 2
                            jump trails
                            
                "How do I know you aren't trying to avoid me!?":
                    show peggy negative
                    p   "Honey, if you keep acting like that, I won't need to try..."
                    b   "Ok, I'll see you then..."
                    menu:
                        "Leave (She seems to be interested in you!)":
                            $peggy_mood = 1
                            jump trails
            
label peggy1:
    scene bg ocean peggy with fade
    show barry neutral with dissolve
    "As you enter the bar you look around for Peggy, she said she would be here by now!"
    "After a few minutes you begin to worry that she has forgotten about you..."
    menu:
        "Keep waiting for her.":
            "You wait a few more minutes and eventually you see her entering the bar."
            if peggy_mood is 1:
                jump peggyneutral1
            if peggy_mood is 2:
                jump peggyhappy1
        "Give up and go home.":
            b   "(She was out of my league anyways...)"
            jump trails
        "Find other fish to hit on.":
            "You quickly scan the bar and find a fairly attractive fish that you are interested in."
            menu:
                "Approach this new fish.":
                    "You walk up to this new fish, brimming with confidence, and give her your best line:"
                    b   "Did you hear about Obama and the Sea Cucumb..."
                    "(you feel a tap on your shoulder)"
                    show peggy neutral with dissolve
                    p   "Not exactly the most patient fish are you!"
                    jump peggyhappy1
                "Go back to waiting for Peggy.":
                    "You wait a few more minutes and eventually you see her entering the bar"
                    if peggy_mood is 1:
                        jump peggyneutral1
                    if peggy_mood is 2:
                        "She spots you as soon as she comes inside and waves you down."
                        p       "Hey Barry!  Let me buy you a drink!"
                        jump peggyhappy1
                "Give up and go home.":
                    b   "(She was out of my league anyways...)"
                    jump trails
label peggyneutral1:
    show peggy neutral with dissolve
    b   "(waves at Peggy)"
    p   "Oh hey! Barney was it?"
    menu:
        "Yup thats me!":
            p   "Really? I could've sworn it was something else.."
            b   "(Uh oh...)"
            b   "No, no, it's Barney!"
            b   "Like in How I Met Your Mother!"
            b   "And the Purple Dinosaur!"
            p   "..."
            b   "..."
            p   "Wasn't it Barry?"
            menu:
                "Yeah sorry, it's actually Barry...":
                    p   "Oh sorry about that, let me buy you a drink to make it up to you."
                    jump peggybeer1
                "Nope!  Definitely Barney!":
                    p   "..."
                    b   "..."
                    p   "I'm pretty sure you're lying to me, and I don't really appreciate it..."
                    b   "NOPE MY NAME IS DEFINITELY BARNEY."
                    p   "I'm going to go now..."
                    p   "I don't know how I didn't see this side of you before..."
                    menu:
                        "Leave (Well that was dumb...)":
                            $   peggy_gone = True
                            jump trails
        "Close, but it's actually Barry!":
            p   "Oh sorry about that, let me buy you a drink to make it up to you."
            jump peggybeer1
            
label peggybeer1:
    b   "(Sweet!)"
    b   "(Free beer!)"
    p   "You'll have to excuse me. I meet all sorts of guys here."
    p   "Sometimes I can't even keep my boys straight!"
    b   "No kidding..."
    b   "(Poor guys...)"
    p   "So what do you think of the beer?"
    menu:
        "It's great!":
            b   "Driftwood beer is my favourite kind!"
            p   "Well you're my favourite kind..."
            b   "(She's coming on strong!)"
            jump peggyskip
        "Actually...":
            b   "It's... not bad..."
            p   "..."
            b   "It just tastes kind of cheap."
            show peggy negative with dissolve
            p   "Are you serious?"
            show barry panic with dissolve
            p   "I don't need another ungrateful hanger-on in my life!"
            menu:      
                "Apologize.":
                    b   "I'm sorry. I really appreciate you buying me a beer."
                    show barry neutral with dissolve
                    p   "Damn right you do."
                    show peggy neutral with dissolve
                    b   "(It really is gross...)"
                    "You slam back the beer so you don't have to taste it."
                    p   "You were thirsty!"
                    p   "How about you get the next round?"
                "Don't apologize.":
                    b   "First you forget my name and then you buy me crappy beer?"
                    b   "You've got no class."
                    p   "!"
                    p   "Well if I'm not good enough for you then why don't you just swim away."
                    show barry sad with dissolve
                    "You see other fish glaring at you. Evidently Peggy is well liked in this bar."
                    "Maybe it's best to make a hasty retreat..."
                    p   "That's right!"
                    p   "Just keep swimming!"
                    p   "Swimming!"
                    "You glance over your shoulder."
                    p   "Out!"
                    menu:
                        "Leave (Well done! Now they all hate you...)":
                            $       peggy_gone = True
                            jump trails
                    
label peggybeer2:
    b   "Sure! I'll show you my favourite beer."
    b   "(And not have to drink that swill that she likes...)"
    p   "Sounds good!"
    "You buy a round for you two."
    "She looks a little tipsy after finishing hers."
    p   "You know Barry..."
    p   "You're really cute."
    p   "Just the sort of fish I need right now."
    p   "All of my other men are so boring and they don't talk they way you do."
    p   "I like a man who knows what he wants."
    b   "(This is sounding good...)"
    p   "So tell me, Barney..."
    b   "...Barry..."
    p   "Right!"
    p   "Tell me, Barry, what do you want?"
    "It's the moment of truth!"
    menu:
        "Go for it!":
            b   "I want to find out wither you're an angelfish or a devilfish... If you know what I mean..."
            p   "I'm pretty sure I do..."
            jump kissthegirl
        "Hold up...":
            b   "I'm sorry, but I'm not sure."
            p   "What?!"
            p   "After all that?"
            b   "I'm sorry. I need time to think."
            $   peggy_level = 3
            menu:
                "Leave (Better make up your mind...)":
                    jump trails
    
label peggyhappy1:
    show peggy neutral with dissolve
    "Peggy swims up to the bar and buys a round of drinks for the two of you."
    label peggyskip:
    p   "I'm glad you came back, I was thinking about you the whole time I was gone."
    p   "And the thing I want to do to you..."
    show barry smirk with dissolve
    b   "!"
    b   "Oh yeah...?"
    p   "Do you want to come back to my place after this and see what I have in mind?"
    b   "(She sure is coming on strong...)"
    menu:
        "Let's go to your place.":
            show peggy happy with dissolve
            g   "Tee hee!"
            g   "I was kidding."
            g   "Maybe later though."
            "She winks at you."
            "You're a bit of a shmuck aren't you?"
            jump happybeer1
        "Let's go to my place.":
            show peggy happy with dissolve
            g   "Ooh! Bold!"
            g   "I was only kidding."
            g   "Let's hang around here for a while!"
            jump happybeer1
        "Slow down lady!":
            g   "Calm down! I was only joking."
            g   "What kind of fish do you think I am?"
            b   "(The kind that has three other guys hanging off her...)"
            g   "Did you say something?"
            show barry panic with dissolve
            b   "Nope! Nothing at all!"
            b   "(This is awkward...)"
            b   "(Better change the subject...)"
            menu:
                "So how about that local sports team...":
                    p   "..."
                    b   "I... Hear they're doing well in their respective categories..."
                    p   "Oh honey."
                    p   "Oh honey, no."
                    show barry sad with dissolve
                    jump sadbeer1
                "Order another round.":
                    b   "I'm sorry. You make me nervous sometimes!"
                    p   "Is that a good thing?"
                    menu:
                        "Yes!":
                            b   "You make me lose my cool."
                            p   "Well..."
                            p   "Maybe I want to heat things up..."
                            jump kissthegirl
                        "No!":
                            b   "You're just too much woman to handle..."
                            menu:
                                "Leave (Seriously dude?)":
                                    $   peggy_level = 3
                                    jump trails
            
label happybeer1:
    p   "In all seriousness, I wouldn't mind going back to my place later..."
    b   "(Score!)"
    b   "Oh yeah?"
    b   "I think I could be into that..."
    jump peggyvictory

label kissthegirl:
    menu:
        "Kiss her!":
            jump peggyvictory
        "Abort! Abort!":
            b   "Uh, actually I have a thing I have to do."
            p   "What? What sort of thing?"
            b   "A very important thing. Gotta run!"
            menu:
                "Leave (Smooth...)":
                     $       peggy_level = 3
                     jump trails
                
label sadbeer1:
    b "I’m sorry."
    b "You just make me so nervous sometimes!"
    b "Plus, I don’t usually think of dating as a spectator sport…"
    p "Oh, don’t mind them. They don’t care."
    b "(I’m not so sure about that…)"
    "The males attached to her stare at you with sadness in their eyes."
    "It’s really creepy."
    b   "Right…"
    p   "So…"
    "This is getting awkward really fast…"
    "You should probably do something…"
    jump kissthegirl 
        
label peggy3:
    
    scene bg ocean peggy with fade
    show barry neutral with dissolve
    show peggy neutral with dissolve
    "Peggy is sitting at the bar, drinking a double martini..."
    "She's stirring it with the sea grape pick..."
    menu:
        "Approach":
            p   "Well hi, stranger."
            p   "Wasn't sure if I'd see you around these parts again."
            b   "Yeah..."
            menu:
                "Are you still interested?":
                    p   "..."
                    p   "You sure don't pull your punches."
                    p   "Eh, why not?"
                    jump peggyvictory
                "Actually I should go...":
                    p   "I'm sorry to hear that..."
                    show peggy negative with dissolve
                    $   peggy_gone = True
                    jump trails
        "Leave":
            $   peggy_gone = True
            jump trails
            
label peggygone:
    
    scene bg ocean peggy with fade
    show barry neutral with dissolve
    
    "The bar seems emptier than usual."
    "Peggy is nowhere to be seen."
    "There is an open seat at the bar."
    menu:
        "Take a seat at the bar.":
            show bartender with dissolve
            "The bartender asks what you would like to drink."
            menu:
                "Driftwood Beer":
                    b   "Why does no one love me..."
                    b   "Another drink please!"
                    menu:
                        "Driftwood Beer":
                            b   "I'm not ugly right? Am I ugly!?"
                            b   "I need another drink..."
                            menu:
                                "Driftwood Beer":
                                    show barry drunk1 with dissolve
                                    b   "Girlsh are shtupid... Who needsh them anywaysh..."
                                    b   "Bartender, why is my drink empshty!"
                                    menu:
                                        "Whisky":
                                            b   "Why am I not able to picksh my own drinksh!"
                                            b   "Thish game *hic* world is shtupid anywaysh..."
                                            menu:      
                                                "Whisky":
                                                    show barry drunk2 with dissolve
                                                    b   "Why Anglerfishsh? What a shtupid idea!"
                                                    b   "Whatever I'm shick of this game *hic* world..."
                                                    menu:
                                                        "Whisky":
                                                            b   "I WILL BAIT I WILL BAIT FOR YOUUUU"
                                                            b   "NO ONE LOVESH ME..."
                                                            b   "(sobbing)"
                                                            menu:
                                                                "Whisky":
                                                                    jump barrydead
        "Leave":
            jump trails
            
label barrydead:
    show barry dead with dissolve
    "Well good for you..."
    "You drank yourself to death..."
    "Maybe if you treated those ladies better, you wouldn't have died sad and alone..."
    "Well at least you had fun striking out with Anglerfish right!"
    "Right?"
    menu:
        "End Game.":
            return
            
label peggyvictory:
    g   "Oh Barry, you saucy devil you!"
    g   "I'm going to show what a real ladyfish is made of!"
    b   "Oh Peggy!"
    g   "Oh Barry!"
    show barry smirk:
        ease 3.0 truecenter
    show peggy happy:
        ease 3.0 truecenter
    pause 1.0
    show heart with dissolve:
        zoom 1.3
    pause 5.0
    hide barry
    hide gloria
    hide heart
    show peggy win with dissolve
    pause 3.0
    "Well you found yourself a lady!"
    "Hope she makes you happy!"
    menu:
        "End Game.":
            return
    return
