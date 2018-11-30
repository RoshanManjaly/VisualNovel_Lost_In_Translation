# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define yuuki = Character("Yuuki")
define jap_mom   = Character("Mom")
define jap_dad   = Character("Dad")


# The game starts here.

# story_a = set in Argentina
# story_b = set in Japan
# story_c = set in Pakistan



label start:
    "Where would you like travel to?"

    menu:
        "Argentina":
            jump story_a

        "Japan":
            jump story_b

        "Pakistan":
            jump story_c





label story_a:
        "Argentina Story in Progress"

        menu:
            "Return to Selection Menu":
                jump start


label story_c:
        "Pakistan Story in Progress"

        menu:
            "Return to Selection Menu":
                jump start

label story_b:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    show okaasan happy at left
    show otousan happy at right

    jap_mom "You decided to spend your prime in Tokyo and you're telling me that you can't find any halfway decent eligible bachelors?"

    "It's been several months since I'd started at my schoolteacher position in Tokyo. My parents haven't gotten over that their 'daughter' is in The Big City, in 'her' twenties, and yet, obstinately single. They mean well, but... sometimes their advice is a tad misguided."

    "For one thing, although I live in an overcrowded city, it's not exactly easy for me to find 'halfway decent eligible' guys interested in me because, well, I'm a guy too."

    jap_mom "Your father and I are only getting older. We only have so many years left to see our grandchildren before we make our exit."

    "It's funny she'd say that, because I'd been thinking of getting sterilized... I don't know that I never want biological children, but Japanese law won't recognize my gender identity unless I become 'unable to reproduce'."

    jap_mom "Yuuki-chan, are you listening? Tell your parents they won't die before seeing their grandchildren."

    scene bg room

    menu:
        "Tell Mom and Dad you'll try your best.":
            jump reassure

        "Tell Mom and Dad you'd rather not lie to them.":
            jump not_lie

        "Say you weren't listening.":
            jump werent_listening

label reassure:
    yuuki "{i}Ganbarimasu.{/i}"

    jap_mom "That's our Yuuki!"

    yuuki "The thing is--"

    jump end_of_call

label not_lie:
    yuuki "I'd rather not lie to you..."

    jap_mom "Then find a boyfriend sooner rather than later!"

    yuuki "It's really not that easy..."

    jump end_of_call

label werent_listening:
    yuuki "Sorry, I'm a bit out of it."

    jap_mom "What're we going to do with you? Your parents are going to die of a broken heart."

    jump end_of_call

label end_of_call:
    # Play sound of classroom bell

    yuuki "Ah, sorry. It seems like the lunch break is over. We'll talk again next week, yeah?"

    jap_dad "Yeah."

    jap_mom "We're always missing you around. Love you!"

    yuuki "Love you."

    # Play sound of call disconnecting

    hide okaasan
    hide otousan

    "I sigh in mild relief. Another conversation with my parents, another day I remain in their good graces as their only and darling daughter. I keep telling myself that one day, one of these days, I'll tell them about my gender troubles and happenings, but there's never seems like a 'right' time."

    "Students shuffle into the classroom, as lethargic as you'd expect high schoolers to be on a Monday afternoon."

    yuuki "Alright, everyone. Let's settle in and start our review session for the test later this week."

    "At the reminder of the upcoming test, the students straighten themselves in their seats a little and put effort into being (or seeming?) alert and attentive."

    "At the start of the school year, during the first couple days of my teaching career, I was a little taken aback that I, someone who'd only so recently been on the other side of the classroom, was being heralded as an 'authority'."

    "Now, though, I found myself teasing with my power when I could. The atmosphere change in the classroom at the mention of a test hasn't gotten old, yet."

    # chalkboard sounds

    "{i}PRODUCT RULE and QUOTIENT RULE{/i}, I write out on the chalkboard."

    yuuki "To differentiate products and quotients we have the Product Rule and the Quotient Rule."

    yuuki "If the two functions f(x) and g(x) are differentiable (i.e. the derivative exist) then the product is differentiable and {font=fonts/Inconsolata-Regular.ttf}(fg)' = f'g + fg'{/font}."



    # This ends the game.

    return
