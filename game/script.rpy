# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

## Canadian Characters
define can_main   = Character("You")
define camila   = Character("Camila")
define teacher   = Character("Teacher")
define Principal   = Character("Principal")
define can_mom   = Character("Mom")
define guidance_counselor   = Character("Guidance Counselor")
define therapist   = Character("Therapist")

## Japan Characters
define yuuki = Character("Ohno Yuuki")
define ayako = Character("Sato Ayako")
define jap_mom   = Character("Mom")
define jap_dad   = Character("Dad")

## Pakistan Characters
define aasim   = Character("Aasim")
define brother   = Character("Brother")
define pak_main   = Character("You")




# The game starts here.

# story_a = set in Canada
# story_b = set in Japan
# story_c = set in Pakistan

# TODO: Add BGM for each of the routes


label start:
    scene selection_v2
    "Where would you like travel to?"

    menu:
        "Canada":
            jump story_a_define
        "Japan":
            jump story_b_define
        "Pakistan":
            jump story_c_define


label story_a_define:
    scene black with fade
    jump story_a

label story_b_define:
    scene black with fade
    jump story_b

label story_c_define:
    scene black with fade
    "Glossary - if you need to refer to any of these definitions during gameplay, click the ‘History’ tab in the bottom of the screen and scroll to the top.\n
    Chai - spiced milk tea\n
    Hajj - an annual pilgrimage to Mecca that takes place in the last month of the year that all Muslims are expected to make at least once in their lifetime\n
    insha’Allah = ‘God willing’\n
    Pendu - colloquially used to refer to someone or something that reminds you of village life\n
    Salwar Kameez - a traditional South Asian outfit with a long tunic and loose, pleated trousers\n
    Rupees - the national currency of Pakistan\n
    Guru - literally ‘teacher;’ in the context of transgender communities, it refers to the matriarch of the adoptive family structures that often form. ‘Gurus’ are often compared to Western pimps.\n
    Mamu - literally ‘mother’s brother;’ colloquially used to refer to police officers\n
    Marvia Malik - Pakistan’s first transgender news anchor; she works for Kohenoon News based in Lahore, Pakistan\n
    Saas - literally ‘mother-in-law’\n
    Bahu - literally ‘daughter-in-law’\n
    Chalo - literally ‘let’s go;’ often used as a transition in conversation\n"
    jump story_c

label end:
    scene main_menu
    "Play Again?"

    menu:
        "Yes ... Return to Menu":
            jump start

        "Maybe another time":
            return


###################### Canada Story Start

label story_a:
    scene ca_morning
    can_main "Ugh it's morning…"
    menu:
        "Go to school":
            jump story_a_to_school
        "Fake being sick":
            jump story_a_fake_sick


label story_a_to_school:
    scene ca_camila
    can_main "Oh, hey, Camila."
    camila "Hey, girl! Why so glum?"
    can_main "It’s nothing… just not feeling it today."
    camila "Ahhh it's probably just transition stuff. It’s still fairly new for you, right?"
    can_main "Yeah, but I don’t think it’s that. It feels like it’s different."
    camila "Eh, I wouldn’t worry about it. I mean you're soooooo much luckier than people in other countries. It's just sad. You know Canada is one of the most progressive countries and we..."
    can_main "Well thanks that definitely helped me feel better…"
    camila "You know what I mean. Just be grateful! I’m sure you’ll feel better, soon or something."
    "*Bell Rings*"
    camila "Oh, I got to get to class! See you later?"
    menu:
        "Brush it off":
            jump story_a_brush_off
        "Get frustrated":
            jump story_a_frustrated

label story_a_frustrated:
    scene ca_lockers

    can_main "YOU DON’T GET IT! *slam fist into lockers* "
    camila "*yelps*"
    can_main "{i} oh no I didn’t mean it… I--{\i}"
    teacher "Stop right there, young lady! You’re going to the principal’s office"
    menu:
        "Go to principal’s office":
            jump story_a_principal

label story_a_brush_off:
    can_main "Maybe…"
    jump story_a_class

label story_a_fake_sick:
    scene ca_morning
    show ca_mom_bedroom
    "*Mom comes in the room worried*"
    can_mom "Hi honey, why aren’t you getting ready for school?"
    can_main "I’m not feeling well. I think I’m gonna stay home today"
    can_mom "You sure? I think you look fine. How about you start getting ready and see how you feel? I’m sure you’ll feel better. It’s not good for you to miss this much school."
    menu:
        "Go to school":
            jump story_a_to_school
        "Stay in bed":
            jump story_a_stay_bed

label story_a_stay_bed:
    scene ca_morning
    can_main "{i}This is never gonna get any better, why would I even bother? Ughhhhh I’m going back to sleep…{/i}"
    jump end

label story_a_principal:
    scene ca_principal
    Principal "We do not allow violence at this school young lady. Please take a seat while I call your parents."
    can_main "*under her breath* 'You mean parent…'"
    menu:
        "Leave the office and ditch school":
            jump story_a_ditch_school

label story_a_class:
    scene ca_teacher
    "*Bell rings again*"
    teacher "Excuse me, I need to talk to you. Can you please stay after class?"
    teacher "Your last test score is very low. You told me you were getting treatment and that everything was under control. I have been very lenient with you, but it seems like you are not improving."
    can_main "I don’t have everything under control."
    teacher "Maybe you should see the guidance counselor, he can provide more help."
    can_main "He hasn’t really helped me in the past. I think this is a different problem ..."
    teacher "Well you have to do something because you’re not going to be able to pass if you keep this up."
    menu:
        "Ditch school":
            jump story_a_ditch_school
        "Go to guidance counselor":
            jump story_a_gc

label story_a_gc:
    scene ca_guidance
    guidance_counselor "So, what’s going on? It’s been a while since I last saw you."
    can_main "It’s nothing really."
    guidance_counselor "Well there must be some reason why you’re here."
    can_main "I was told to come here because I’m still not doing well in class. I don’t think I need to be here."
    guidance_counselor "Okay, well I can only help you if you want to be helped. Here are some pamphlets that might be useful for you."
    can_main "Wow thanks… I don’t think it’s related to my transition though."
    guidance_counselor "It probably is, it may just not seem like it. Give the pamphlets a try. You never know."
    can_main "Sure."
    menu:
        "Ditch school":
            jump story_a_ditch_school
        "Go home to worried mom":
            jump story_a_home

label story_a_home:
    scene black
    show ca_kitchen
    can_mom "Honey, what happened? The school called and told me you were having some trouble. Is there anything I can do to help?"
    can_main "I’m fine."
    can_mom "You know you can talk to me about anything. I love you."
    can_main "I don’t need your help, thank you… Maybe you should focus on yourself…"
    can_mom "What does that mean?!?!"
    can_main "Nothing. I gotta go."
    menu:
        "Go to therapy":
            jump story_a_therapy

label story_a_therapy:
    therapist "Good afternoon! How have you been?"
    can_main "Mostly good…"
    therapist "Well that’s good to hear! Is there anything that you want to talk about?"
    can_main "Actually... it’s not good. I haven’t been feeling right for a while now, but everyone keeps telling me that it probably has to do with my transition. I don’t think it does though… I can just tell."
    therapist "Hmmmm. It’s completely possible to have other issues, you’re only human. Let’s talk this out and see what we can do…"
    jump end


label story_a_ditch_school:
    scene ca_ditching
    can_main "{i}thinking I can’t do this anymore I need to go somewhere {\i}"
    menu:
        "Go home":
            jump story_a_home
        "Go to the town (coffee shop)":
            jump story_a_coffee

label story_a_coffee:
    scene ca_coffee
    can_main "{i} *Sigh* I love this place… Maybe I should order something that will calm me down.{\i}"
    menu:
        "Order a cool espresso drink":
            jump story_a_coffee_shop_next
        "Order a black coffee":
            jump story_a_coffee_shop_next


label story_a_coffee_shop_next:
    scene ca_coffee
    can_main "{i} *Sighing* Ahhh that’s kind of better… Ugh I don’t know what to do. I’m so all over the place, I need to organize my thoughts.{\i}"
    menu:
        "Listen to music and reflect":
            jump story_a_music
        "Write in journal":
            jump story_a_journal

label story_a_music:
    scene ca_coffee
    can_main "{i} This isn’t working…{\i}"
    menu:
        "Write in journal":
            jump story_a_journal


label story_a_journal:
    scene ca_journal
    can_main "{i} Well she told me to keep a journal months ago and I’ve just been carrying this empty one around in my bag… time to use it. I don’t really see how it could help but there’s no harm in trying I guess…{\i}"
    "(writes) Dear Diary (scratch out)"
    "..."
    "{i}No that’s not my style…{/i}"
    "*writing* I don’t really know what has been going on with me, but I guess that’s why I’m writing this…"
    jump end



###################### Canada Story End





###################### Japan Story Start
label story_b:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "jp bg room.png" or "jp bg room.jpg") to the
    # images directory to show it.

    scene jp bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    show ca_home_t

    jap_mom "You decided to spend your prime in Tokyo and you're telling me that you can't find any halfway decent eligible bachelors?"

    "I'm having my weekly lunch break phone call with my parents, who live (and raised me in) the countryside."

    "It's been several months since I'd started at my schoolteacher position in Tokyo. My parents haven't gotten over that their 'daughter' is in The Big City, in 'her' twenties, and yet, obstinately single. They mean well, but... sometimes their advice is a tad misguided."

    "For one thing, although I live in an overcrowded city, it's not exactly easy for me to find 'halfway decent eligible' guys interested in me because, well, I'm a guy too."

    jap_mom "Your father and I are only getting older. We only have so many years left to see our grandchildren before we make our exit."

    "It's funny she'd say that, because I'd been thinking of getting sterilized... I don't know that I never want biological children, but Japanese law won't recognize my gender identity unless I become 'unable to reproduce'."

    jap_mom "Yuuki-chan, are you listening? Tell your parents they won't die before seeing their grandchildren."

    scene jp bg room

    menu:
        "How do I respond?"

        "Tell Mom and Dad you'll try your best.":
            jump story_b_reassure

        "Tell Mom and Dad you'd rather not lie to them.":
            jump story_b_not_lie

        "Say you weren't listening.":
            jump story_b_werent_listening

label story_b_reassure:
    yuuki "{a=http://lang-8.com/725244/journals/199182171541683591437838792131877435706}{i}Ganbarimasu.{/i}{/a}"

    jap_mom "That's our Yuuki!"

    yuuki "The thing is—"

    jump story_b_end_of_call

label story_b_not_lie:
    yuuki "I'd rather not lie to you..."

    jap_mom "Then find a boyfriend sooner rather than later!"

    yuuki "It's really not that easy..."

    jump story_b_end_of_call

label story_b_werent_listening:
    yuuki "Sorry, I'm a bit out of it."

    jap_mom "What're we going to do with you? Your parents are going to die of a broken heart."

    jump story_b_end_of_call

label story_b_end_of_call:
    # Play sound of classroom bell

    yuuki "Ah, sorry. It seems like the lunch break is over. We'll talk again next week, yeah?"

    jap_dad "Yeah."

    jap_mom "We're always missing you around. Love you!"

    yuuki "Love you."

    # Play sound of call disconnecting

    hide ca_home_t

    "I sigh in mild relief. Another uneventful conversation with my parents, another day I remain in their good graces as their only and darling daughter. I keep telling myself that one day, one of these days, I'll tell them about my gender troubles and happenings, but there's never seems like a 'right' time."

    "Students shuffle into the classroom, as lethargic as you'd expect high schoolers to be on a Monday afternoon."

    yuuki "Alright, everyone. Let's settle in and start our review session for the test later this week."

    "At the reminder of the upcoming test, the students straighten themselves in their seats a little and put effort into being (or seeming?) alert and attentive."

    "At the start of the school year, during the first couple days of my teaching career, I was a little taken aback that I, someone who'd only so recently been on the other side of the classroom, was being heralded as an 'authority'."

    "Now, though, I found myself teasing with my power when I could. The atmosphere change in the classroom at the mention of a test hasn't gotten old, yet."

    # chalkboard sounds

    "{i}PRODUCT RULE and QUOTIENT RULE{/i}, I write out on the chalkboard."

    yuuki "To differentiate products and quotients we have the Product Rule and the Quotient Rule."

    yuuki "If the two functions f(x) and g(x) are differentiable (i.e. the derivative exist) then the product is differentiable and {font=fonts/Inconsolata-Regular.ttf}(fg)' = f'g + fg'{/font}."

    "My body becomes more relaxed as I continue writing on the chalkboard and reading my own handwriting aloud."

    "Math's always comforted me, with its no-nonsense language and problems. In contrast to having to figure out how to conversations with my parents that didn't leave me feeling like I'd somehow betrayed them, calculus problems were a pleasure."

    # more chalkboard sounds

    "A couple of hours pass like this, and then I've found myself dismissing my last class of the day."

    show jp bg hallway with dissolve

    "As a new faculty member, I haven't yet been asked to sponsor any after-school club, so I go home a little earlier than other teachers."

    "I make my way through the school hallways, idly trying to recall if I have any unexpired food left in the fridge."

    "I pass by Sato Ayako-sensei's classroom, where I find her hunched over at her desk, looking somewhat deep in thought. Sato-sensei is interesting—she's kept trying to make acquaintances with me, despite my reserved nature. Well, 'my reserved nature' isn't quite right..."

    "I wouldn't think of myself as reserved, but, ever since I started transitioning, I found myself unsure of where I fit into society and how to proceed with developing new interpersonal relationships."

    "I look cisgender enough that I don't have to worry about confused stares, but I worry about becoming 'exposed' if I were to let those unfamiliar with my history get close to me. There's no way of knowing how they'd react."

    "Still, it'd be nice to have a friend in an unfamiliar city..."

    menu:
        "What should I do?"

        "Poke my head in the door and say hi to Sato-sensei.":
            $ convo_with_sato = True
            jump story_b_head_poke

        "Continue home.":
            $ convo_with_sato = False
            jump story_b_continue_home

label story_b_head_poke:

    "I decide it can't hurt to say hi to Sato-sensei, so I poke my head in the door to do so."

    yuuki "Sato-sensei! How are you?"

    show jp ayako happy

    ayako "I'm well. How are you, Ohno-sensei?"

    menu:
        "How do I respond?"

        "Tell her I'm also well.":
            jump story_b_do_well

        "Tell her about my troubles with my parents.":
            jump story_b_troubles_with_parents

label story_b_do_well:
    yuuki "I'm doing well. You seem deep in thought—what're you working on?"

    ayako "Ah, it's nothing big. It's just that I'm realizing that I'll be spending the holidays alone."

    "I wonder if she's telling me this as a subtle hint to invite her out for the holidays. I wouldn't mind hanging out with Sato-sensei, but it's hard to feel 'right' hanging out with anyone while being a very closeted trans man. I worry about giving off the wrong messages and getting into an uncomfortable situation."

    yuuki "Well, getting some well-deserved peace and quiet to yourself sounds like an excellent vacation."

    "Sato-sensei smiled, but doesn't seem convinced."

    ayako "I'll try to remind myself of that."

    "She turns her attention from me to some papers on her desk."

    ayako "I have some paperwork to fill out, so we should catch up later."

    "I nod and walk back into the hallway."

    jump story_b_continue_home

label story_b_troubles_with_parents:
    yuuki "I'm mostly doing well, the most complicated thing in my life is that I'm having some drama with my parents."

    ayako "Oh no! What's going on?"

    yuuki "It's nothing big! They just keep pushing me to get a girlfriend; they don't like how much of a loner I seem to be."

    "I cringe slightly at my use of 'girlfriend', when my parents would probably faint if they'd heard I had one."

    ayako "You {i}are{/i} a bit of a loner. Maybe a girlfriend would get you to go out more!"

    yuuki "Yeah, maybe."

    "I wonder if I'd be able to find a partner who'd push me out of the protective shell I've formed for myself—I sure hope I do."

    "Sato-sensei averts her glance from me to her desk."

    ayako "Actually, I have no holiday plans right now, aside from that I need to do some shopping for my family members."

    "Without meaning to, I tense my body."

    ayako "Would you like to come along with me?"

    "Sato-sensei is a nice person, and I'm sure I'd have a great time with her but without thinking I immediately respond:"

    yuuki "Sorry, I've already done my holiday shopping and my upcoming schedule is a bit hectic, right now."

    "Sato-sensei immediately puts her hands up, palms toward me, signalling for me not to feel bad about my rejection."

    ayako "I completely understand. I have some paperwork to fill out, so we should catch up more later."

    "I nod and walk back into the hallway."

    jump story_b_continue_home

label story_b_continue_home:
    show jp bg train with dissolve

    # moving train sounds

    if convo_with_sato:
        "I'm on the train home, leaning against the window and thinking back to my conversations with my parents and with Sato-sensei."

    else:
        "I'm on the train home, leaning against the window and thinking back to my conversation with my parents."

    "I've been thinking about this a lot: I'm happier than I've ever been, living my life as a man rather than as a woman. However, I'm also more isolated than I've ever been. It's hard to figure out what face to put on toward different people in my life."

    "I look through my Twitter feed, hoping to find some meme or another that'll make me laugh."

    "Instead, I come across a tweet from Ebina City Council member Tsuruhashi Masumi, in response to Asahi Shimbun's report on an attitude survey regarding same sex marriage:"

    "'If abnormal people increase, human beings will become extinct. … Homosexuality is abnormal. Media should be more responsible than to report abnormal activities.'"

    "'{a=https://www.tofugu.com/japan/conformity-in-japan/}The nail that sticks out gets hammered down{\a},' as the saying goes."

    "Would I be regarded as a 'homosexual' in Tsuruhashi-san's eyes, when I identify as a man and am interested in women? Probably, I think, resolving not to further dwell on the subject."

    "I look out the window and watch the city pass by. I let myself fall asleep, telling myself to be content with what I have. As long as I don't make too much of a splash around me, I'll be fine."

    hide jp bg train with dissolve

    # This ends the game.

    jump end
###################### Japan Story End

###################### Pakistan Story Start
label story_c:
    scene pk bedroom with dissolve
    "*wake up*"

    menu:
        "Stay in bed a little longer":
            jump story_c_in_bed
        "Brush teeth":
            jump story_c_morning_routine

label story_c_in_bed:
    scene pk bedroom with dissolve
    "*grab your phone*"

    menu:
        "News":
            jump story_c_news
        "Tinder!":
            jump story_c_binder

label story_c_morning_routine:
    scene pk bedroom with dissolve
    "*rustling*"
    "*Aasim wakes up*"

    "You kiss him on the cheek and roll out of bed. You pick up the ring from the bedside table"

    pak_main "Can I get you chai?"

    aasim "I'm okay"

    "You look at the time. You're late!!"

    jump story_c_late

label story_c_news:
    scene black
    show pk news with dissolve
    "Once ostracized now Pakistani Transgender people are running for Parliament"

    "{i}Hmmm.... maybe I should vote this year. When are Elections again?{/i}"

    "*Opens Calendar App*"

    #Calendar App Opening screen switch
    scene black
    show pk calendar1 with dissolve
    "Today's Date: July 13th, 2018"
    "Election Day: July 25th, 2018"
    "Dr. Rahman comes for shots: July 28th, 2018"

    menu:
        "Keep looking at your calendar":
            jump story_c_calendar
        "Tinder!":
            jump story_c_binder

label story_c_calendar:
    scene black
    show pk calendar2 with dissolve
    "Right ... Hajj ... "

    "{i}Hopefully things will change in the Saudi Government soon, insha'Allah{/i}"

    "You look over at the clock for the time. You're late!!"

    jump story_c_late

label story_c_binder:
    scene black
    show pk tinder with dissolve
    "Left, Left, Lef....oooo...."

    "{i}nope. jk. He's too pendu{/i}"

    "{i}nothing good today{/i}"

    menu:
        "Keep Swiping":
            jump story_c_binder_repeating
        "News!":
            jump story_c_news

label story_c_binder_repeating:
    scene black
    show pk tinder2 with dissolve
    "Left, Left, Left"

    "{i}Still nothing good today{/i}"

    jump story_c_your_late


label story_c_your_late:
    "You look at the time. You're late!"

    jump story_c_late



label story_c_late:
    scene pk makeup with dissolve
    "You run to the bathroom and start putting on your make up"

    "You wear the salwar kameez that you bought last weekend and head out. You wave hello to the chowkidar and head down the road"

    menu:
        "Take the back roads. Less people means less stares":
            jump story_c_back_road
        "There's safety in being in public":
            jump story_c_main_road

label story_c_back_road:
    scene pk backroad with dissolve
    "You walk through some alleys. On your way, you say hello to some children, give 100 rupees to the woman on the street corner (even though you know it goes straight to the guru - 100 rupees for a blessing isnt too bad of a deal), and skip over some puddles"
    "{i}Nothing too out of the ordinary{/i}"
    jump story_c_arrived

label story_c_main_road:
    scene pk mainroad with dissolve
    "'Hey! Beautiful gay!'"
    "You look at the standing mamu"
    "He turns away"
    pak_main "'Family always has your back,' you say sarcastically under your breath"
    "{i}Hmm... maybe you should call your brother today. Although it is his responsiblity{/i}"
    jump story_c_arrived

label story_c_arrived:
    scene pk office with dissolve
    " 'Government of Pakistan' ... You're here"
    "You hand the security guard your I.D. He looks you up and down and looks like he’s about to raise an eyebrow. But he doesn’t. You’re let in without exchanging a word"
    "Normal day at work. Paper pushing, phone checking, some staring"
    "{i}Who actually cares about other people’s taxes{/i}"

    scene pk clock3pm with dissolve
    "The clock hits 3pm. Time to check out. You're feeling lazy"
    menu:
        "Rikshaw":
            jump story_c_rikshaw
        "Uber":
            jump story_c_uber

label story_c_rikshaw:
    scene pk rickshaw with dissolve
    "You walk to the street corner and flag one down. He takes you home and you pay him 20 rupees. He says 'thank you'"
    "No words other than that"
    jump story_c_home

label story_c_uber:
    scene pk uber with dissolve
    "You walk outside and she picks you up. You say 'thank you' and get out"
    "No words other than that"
    jump story_c_home

label story_c_home:
    scene pk home
    "You stroll into your home and take a seat on the couch"

    menu:
        "Turn on the T.V.":
            jump story_c_tv
        "Call your brother":
            jump story_c_brother

label story_c_tv:
    scene pk marvia with dissolve
    "Its Marvia Malik on Kohenoon News. She's talking about a village gang that killed two men {i}suspected{/i} of being gay"

    menu:
        "Switch to Drama Network":
            jump story_c_tv_drama
        "Uhhh... you should definitely call your brother":
            jump story_c_brother

label story_c_tv_drama:
    scene pk drama with dissolve
    "{i}Finally, not another saas-bahu drama {/i}"
    "You enjoy your lazy day. You watch T.V. till it's time to prep dinner. You wash your dishes, do your night prayers, and head to bed."
    #Story is finished

    jump end

label story_c_brother:
    scene black
    show pk bhai with dissolve
    pak_main "It's been a week! Don't you don't have to check up on your little sister?"
    brother "I'm sorry"
    pak_main "Fine. I guess I should be the one checking up on you. You're okay?"
    brother "Yeah, fine"
    pak_main "How's Kareem?"
    brother "We broke up"
    pak_main "Oh ... Are you okay? Do you want to talk about it?"
    brother "I'm fine, but I don't feel like talking"
    pak_main "He wont tell anyone, will he?"
    brother "He's not tryna to kill me"
    pak_main "Okay. Okay. What can I do?"
    brother "Nothing right now. ... I'm fine ... Chalo, I'll call you this weekend. I'm a little busy right now"
    pak_main "Bye"
    #Screen change

    "'How did I get it better than him?' You think to yourself"
    "Might as well watch some TV"
    jump story_c_tv_drama
###################### Pakistan Story End







### End of Code
