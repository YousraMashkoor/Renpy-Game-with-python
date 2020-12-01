# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


image saya= "images/saya.png"
image saya_normal ="images/saya_normal.png"
image saya_shock ="images/saya_shock.png"
image saya_pain ="images/saya_pain.png"
image saya_pain2 ="images/saya_pain2.png"
image saya_sad ="images/saya_sad.png"
image saya_smile ="images/saya_smile3.png"
image news = "images/newspaper.png"

image memory_frame= "images/memory2.png"
image memory_letter= "images/memory1.jpg"
image memory3= "images/memory3.jpg"
image memory4= "images/memory4.jpg"
image memory5= "images/memory5.jpg"
image black ="images/black.png"

image street ="images/street.png"
image room_girl ="images/room_girl.png"
image room_girl_cat ="images/room_girl_cat.png"
image dead ="images/dead.png"

image room = "images/room.jpg"
image room2 = "images/room2.jpg"
image kitchen = "images/kitchen.jpg"
image kitchen_cat = "images/kitchen_cat.jpg"
image butterfly = "images/butterfly.png"

image spark2:
    "images/gif/spark/1.png"
    0.1
    "images/gif/spark/2.png"
    0.1
    "images/gif/spark/3.png"
    0.1
    "images/gif/spark/4.png"
    0.1
    repeat
    
image sparkt:
    "images/gif/sparkt/1.png"
    0.1
    "images/gif/sparkt/2.png"
    0.1
    "images/gif/sparkt/3.png"
    0.1
    "images/gif/sparkt/4.png"
    0.1
    "images/gif/sparkt/5.png"
    0.1
    "images/gif/sparkt/6.png"
    0.1
    "images/gif/sparkt/7.png"
    0.1
    "images/gif/sparkt/8.png"
    0.1
    "images/gif/sparkt/9.png"
    0.1
    "images/gif/sparkt/10.png"
    0.1
    repeat

define s = Character("Saya")
define m = Character("Mom")
define j = Character("Jia")
define d = Character("Director")

transform bounce:
    xalign 0.5 yalign 0.0
    linear 5.0 yalign 0.3
    linear 5.0 yalign 0.0
    repeat


# The game starts here.

label start:
    $ dep=0
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.
    scene butterfly:
        zoom 1.5
        parallel:
            ease 5.0 zoom 1.0 #zoom out
        parallel:
            yalign 0.0
            linear 5.0 yalign 0.5 #or whatever fit.
    show sparkt at bounce
    show spark2 at bounce
    $renpy.music.set_volume(0.2, 1.5, 'music')
    $renpy.music.set_volume(5.5, 0, 'sound')
    play sound "audio/intro.wav"
    "Our memory is a more perfect world then the Universe."
    "It gives back lives to those who no longer exists."
    $renpy.music.set_volume(1.0, 1.5, 'music')
    stop sound
    ""
    $renpy.music.set_volume(0.2, 1.5, 'music')
    play sound "audio/intro2.wav"
    "But.."
    "What if they no longer persists?"
    stop sound
    $renpy.music.set_volume(1.0, 1.5, 'music')
    "..."
    $renpy.music.set_volume(1.0, 0, 'sound')
    stop music fadeout 1.0
    
    
    
    scene room with dissolve
    show saya at right with dissolve
    play music "audio/bg2.mp3" fadein 1.0
    s "I've been staring out of this window, for I don't know how long. "

    s "I don't know this place and I don't know why I'm here."
    
    hide saya
    show saya_normal at right
    menu:
        "Am I kidnapped?":
            s "I must be hit on the head, cuz I can't recall a thing"
        "OMG! That's scary":
            s "I believe so."
        "Bruh! I just started playing, idk.":
            s "hmm..."
    
    hide saya_normal
    show saya at right
    s "Lately I've been having troubled sleeping pattern."
    hide saya
    show saya_normal at right
    menu:
        "It's nothing new":
            $ dep = dep+2
        "No way yo! I'm normal":
            s "Lucky."
        "maybe sometimes":
            $ dep = dep +1
            
    hide saya_normal
    show saya at right
    s "The pleasure of remembering had been taken away from me."
    s "My name? My Family? The memories I should have valued the most, are all lost."
    s "Why can't I concentrate!"
    hide saya
    show saya_normal at right
    menu:
        "That's so me":
            $ dep = dep+2
        "Meh! You're on your own":
            s "Lucky."
        "Yeah! happens sometimes, It's fine!":
            $ dep = dep +1
    s "No one has entered this room, and I'm scared to go outside."
    
    
    hide saya
    show saya_normal at right
    menu:
        "Go out anyways":
            play sound "<from 0 to 1.5>audio/sfx/walk.wav"
            hide saya_normal
            "*Heads to the Kitchen*"
        "Aight! Im'ma sleep":
            s "Yeah! I'll just shut my eyes. This is what first comes to my mind, but my curiosity is takng over my fear."
            play sound "<from 0 to 1.5>audio/sfx/walk.wav"
            hide saya_normal
            "*Heads to the Kitchen*"
        
    hide saya_normal
    scene kitchen with dissolve
    show saya at right
    s "Why? Why does it have to be empty?"
    s " I hate how this house is devoid of people."
    s "Just like how my mind is devoid of any memory."
    
    hide saya
    show saya_normal at right
    menu:
        "Maybe everyone's out for grocery":
            s "Yeah! I should wait for them to get back"
        "I probably used to live alone":
            s "Did I really used to live alone?"
        "Yo who cares! let's just sleep":
            s "I guess I'll sleep after I'll look around a bit"
    hide saya_normal
    show saya at right
    s "Agh! I don't know why but my heart aches! as if before loosing my conciousness, I was in extremem despair."
    s " Like I never wanted to regain my conciousness... or... mayebe I wasn't meant to...?"
    
    "As I look around my eerie environment, something caught my eye"
    "..."
    
    $ mem_used=0
    $ curr_mem=0
    $ survive = False
    hide saya
    show saya_normal at right
    menu objects:
    
        "Pick up the letter" if not mem_used == 1: #m=1 c=1
            jump letter
        "{s}Pick up the letter{/s}" if (mem_used == 1 or curr_mem>1): 
            jump objects
            
        "Pick up the frame" if not mem_used == 2: # m=2 c=2
            jump picframe
        "{s}Pick up the frame{/s}" if (mem_used == 2 or curr_mem>1):
            jump objects
            
    label picframe:
        if curr_mem>1:
            return
        scene memory_frame with dissolve:
            zoom 1.5 xalign 1.0 yalign 1.0
        show saya_shock at left with vpunch
        play sound "<from 0.2>audio/sfx/shock.wav"
        s "Wait! is this..."
        s "I do!"
        s "I do have a family. This picture seems to have been taken in this house."
        s "But where are they?"
        menu: 
            "I'd rather stay alone":
                $ dep=dep+2
                s "Uh! okay but..."
            "OMG! are they okay?":
                s "I hope so.."
            "Socializing is a chore":
                $ dep =dep +1
                s "Uh! okay but..."
        hide saya_shocked
        show saya_pain at left
        s "Ugh!"
        
        show saya_pain at left
        scene memory_frame:
            zoom 1.5 xalign 1.0 yalign 1.0
            ease 1.5 zoom 1.0
        
        play sound "audio/sfx/recall.wav"
        "Mom! Dad!"
        "I remember them now. But why aren't they here?"
        "..."
        $ mem_used = 2
        $ curr_mem = curr_mem + 1
        if not curr_mem==2:
            scene kitchen with dissolve
            jump objects
        else:
            jump cat_appears
        
    label letter:
        scene memory_letter with dissolve:
            zoom 1.5 xalign 1.0 yalign 1.0
        show saya_normal at left with dissolve
        s "So I applied for medschool and got selected"
        hide saya_normal
        show saya_sad at left
        s "How odd! I became a doctor yet I don't posses a thing that would indicate that I was one."
        s "This means I never went to medschool, despite clearing my admission."
        scene memory_letter:
            zoom 1.5 xalign 1.0 yalign 1.0
            ease 4 zoom 1.0
        s "..."
        s "No wait!"
        s "I did go to medschool!!"
        s "..."
        $ mem_used = 1
        $ curr_mem = curr_mem + 1
        if not curr_mem==2:
            scene kitchen with dissolve
            jump objects
        else:
            jump cat_appears
            
    label cat_appears:
        scene kitchen_cat with dissolve:
            zoom 2.0 xalign 0.6 yalign 0.7
        play sound "audio/sfx/cat.wav"
        $renpy.music.set_volume(5.0, 0, 'sound')
        "*Rumaging sound*"
        "A cat?.... Aah! It's eating the only can of food I got!"
    menu:
        "Shoo Kitty Kat":
            jump close_window
        "Let her eat! I don't feel hungry anymore anyways":
            $ survive = True
        "Hit her!":
            s "You're the worst!"
            jump close_window
        "Sell her and get money for food":
            s "...just stay there...I\'m gonna put you in a niiiice little cage..."
            s "Aah! how dare you scratch me... pfft! whatever"
            jump close_window
    label close_window:
        scene kitchen_cat with dissolve:
            zoom 2.0 xalign 0.6 yalign 0.7
            ease 4 xalign 0.3
        if not survive:
            s "I'll just close this window, just in case she finds her way in again."
        s "..."
    show news with dissolve:
        zoom 1.0
        ease 2 zoom 0.5 yalign 0.5 xalign 0.5
    s "Is that a news paper?"
    s "\"A father shot his family dead\""
    stop music fadeout 1.0
    play sound "<from 0 to 8>audio/sfx/beat.wav"
    s "wha.. agh!"
    s "..."
    jump story
    
    label story:
        stop sound
        scene memory3 at bounce with dissolve:
            zoom 2.0
            parallel:
                xalign 0.8 yalign 0.2
                linear 9.0 yalign 0.7
                parallel:
                    linear 5.0 yalign 0.4
                parallel:
                    linear 9.0 xalign 0.1
                    ease 4 zoom 1.0
        play music "audio/theme.mp3" fadein 4.0
        "The weather that day was exteremely humid, and my father... was practically pronounced dead.\nHe had been a living corpse after a horrible accident happen almost 3 years ago."
        "My mom refused to give up on him."
        
        "Even if it meant giving up on her own childeren \n"
        m "This is all my fault! This is all my fault! I\'m sorry Girls... Forgive me! Please forgive me"
        "Eventually it was way too much for her to take in."
        j "Mommy?"
        m "I'm sorry! I'm sorry! I'll fix this.. I'm sorry!"
        "Untill one day.."
        scene memory4 at bounce with dissolve:
            zoom 2.0
            parallel:
                xalign 0.8 yalign 0.2
                linear 9.0 yalign 0.7
                parallel:
                    linear 5.0 yalign 0.4
                parallel:
                    linear 9.0 xalign 0.1
                    ease 4 zoom 1.0
        d "Students like you are the reasons of proud for us!"
        d "So our school has decided to fully fund your academic."
        d "Congratulations Miss Saya!"
        s "Yess! Yes! I got into the medschool!!"
        s "All our problems are gonna end now! \nWe don't need to live in poverty anymore! " 
        s "Mom's gonna be sooo happy \n"
        menu:
            "Wanna hear my success story?":
                s "Uhh! no"
            "Gosh! Why am I so lazy":
                $ dep = dep+1
            "Welp I'm still a failure":
                $ dep =dep+2
        play sound "audio/sfx/door.wav"
        "*Step step*"
        s "MOM! MOM! Guess what!\n I have a surprise for you."
        s "You would have never guess this in a million years"
        scene memory5:
            zoom 1.5 xalign 1.0 yalign 1.0
            ease 4 zoom 1.0
        s "Mom?"
        s "Jia?"
        show saya_pain2 with dissolve
        s "..."
        "She left me with the cruelty of this world... and took with her everything that was dear to me"
        scene room_girl with dissolve:
                zoom 2.0 yalign 1.0 xalign 0.5
                ease 4 zoom 1.0
        s "What's the point now anymore!"
        s "I don't see why....I should live! I'm better of dead"

        menu:
            "Let's do it together!":
                $ dep = dep+2
            "No Gurl! Watcha taking 'bout":
                s "Lucky."
            "... Let me ask my mom":
                $ dep = dep +1
        if survive:
            jump live
        jump die
        
        label live:
            s "I'll just take this all"
            play sound "audio/sfx/cat.wav"
            "Meow"
            scene room_girl_cat with dissolve
            s "You're still here..."
            s "I guess you can live here after me"
            s "This place won't have anyone anyway... It never did"
            "Meow"
            s "This? this is for me."
            s "Hey!! wait... no"
            s "Hey?"
            s "Hey! Are you..."
            "..."
            s "Hah!"
            s "Hahaha"
            s "HAHAHAHA"
            s "Everyone around me ends up the same"
            s "You too now"
            s "I must be cursed!"
            
            #goes to dump the cat
            scene street with dissolve:
                zoom 1.0 xalign 0.0 yalign 0.5
                linear 9.0 yalign 0.7
            "..."
            s "I suppose this is our farewell"
            "..."
            play sound "audio/sfx/cat.wav"
            
            "*Meow*"
            scene street with dissolve:
                zoom 1.0 xalign 1.0 yalign 1.0
                linear 5.0 xalign 0.5
                ease 4 zoom 0.46
            "..."
            "These kittens... so she had kittens!"
            menu:
                "Pick them up":
                    s "I suppose I can"
                "Aww!Pet them and give them food":
                    s "I won't let you starve like me"
                "Knit them a sweater":
                    s "Wait!...I don't know how to knit"
                    
            s "So she left you just like my mom!"
            play sound "audio/sfx/cat.wav"
            "Meow"
            s "You're just like me. There was no one for me when she left\nI was alone just like you"
            scene room2 with dissolve
            s "Sigh*"
            s "I suppose that's how it is!"
            s "In this cruel world with it's cruel people.\nI would live."
            s "For those who can't live for themselves."
            show saya_smile at right
            s "Like me, Like YOU!"
            play sound "audio/sfx/cat.wav"
            "*Meow*"
            s "...And yes you too!"
            s "I want to be hope"
            s "I want to treasure these memories"
            s "Life brings tears, smiles, and memories"
            s "But the only thing that can travel through time... is memory"
            jump end
            
            
        label die:
            label final_choice:
                menu:
                    "End it":
                        scene dead with dissolve
                        s "I suppose this is how it ends."
                        jump end
                    "{s}Live on{/s}":
                        jump final_choice
        
        label end:
            scene black
            $ per = (dep/10.0)*100.0
            $ _game_menu_screen = None
            show text ("{size=40}Through out this play you've shown [per]% depression. \nPlease refer to PHQ-9 Questionnaire for more accurate results.") with dissolve
            with Pause(2.5)
            show text ("{size=40}Please don't click the screen or it'll crash(>-<)") with dissolve
            with Pause(2.5)
            show text ("{size=40}Depression is a common mental disorder. \nGlobally, more than 264 million people of all ages suffer from depression!") with dissolve
            with Pause(5.5)
            show text ("{size=40}Severe depression often leads to have suicidal and self-harm thoughts.") with dissolve
            with Pause(3.5)
            show text ("{size=40}While according to WHO Suicide is the third leading cause of death in 15-19-year-olds.") with dissolve
            with Pause(3.5)
            show text ("{size=40}Globally 800,000 people die from suicide every year.") with dissolve
            with Pause(3.5)
            show text ("{size=40}Don't stay quiet to someone suffering from depression.") with dissolve
            with Pause(2.5)
            show text ("{size=40}Let's spread HOPE together!") with dissolve
            with Pause(2.5)
            $ _game_menu_screen = "save"
            jump credits


        label credits:
            $ _game_menu_screen = None
            show text ("{size=80}Credits\n\n{size=40}Special thanks to Khaya Ahmed for making this project possible\n\n{size=40}{size=40}Title Screens and Designing by\n{size=60}Kiran Mashkoor\n\n{size=40}written by\n{size=60}Yousra Mashkoor\nKiran Mashkoor\n\n{size=40}Developed and Directed by\n{size=60}Yousra Mashkoor\n\n{size=40}Song Artist and Musician:\n\n{size=30}Isolated by\n {size=30}Lucas King \n and Promoted by MrSnooze\n\n{size=30}Ancient by\n{size=30}CryFrom Album: Ethnic Sadness\nByComposer: Russ Landau (ASCAP){size=60}\n\n{size=40}Resources\n\n{size=30}Characters by Sutemo\n{size=30}Background by unclemugen and onlyyouqj\n\n{size=20}This work is a piece of fiction. Any semblance to people, places, religions or incidents – real or otherwise – is probably unintentional.{size=40}\n\n\nTime Travelers Production\n") at Move((0.5, 3.5), (0.5, 0.0), 75.0, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
            with Pause(75.0)
            show text ("{size=80}Thank you for playing!") with dissolve
            with Pause(3.5)
            $ _game_menu_screen = "save"
            
    # This ends the game.

    return
    