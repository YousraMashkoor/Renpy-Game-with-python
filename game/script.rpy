# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image saya= "images/saya.png"


define s = Character("Saya")
define m = Character("Mom")
define j = Character("Jia")
define d = Character("Director")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.
    "Our memory is a more perfect world then the Universe."
    "It gives back lives to those who no longer exists"
    
    show saya
    s "I've been staring out of this window, for I don't know how long. "

    s "I don't know this place and I don't know why I'm here."
    menu:
        "Am I kidnapped?":
            s "I must be hit on the head, cuz I can't recall a thing"
        "OMG! That's scary":
            s "I believe so."
        "Bruh! I just started playing, idk.":
            s "hmm..."
        
    show saya
    s "The pleasure of remembering had ben taken away from me."
    s "M name? My Family? The memories I should have valued the most, are all lost."
    s "No one has entered this room, and I'm acred to go outside."
    
    menu:
        "Go out anyways":
            "Heads to the Kitchen"
        "Alright! Im'ma sleep":
            s "Yeah! I'll just shut my eyes. This is what first comes to my mind, but my curiosity is takng over my fear."
            "Heads to the Kitchen"
    s "Why? Why does it have to be empty?"
    s " I hate how this house is devoid of people."
    s "Just like how my mind is devoid of any memory."
    
    menu:
        "Maybe everyone's out for gracery":
            s "Yeah! I should wait for them to get back"
        "I probably used to live alone":
            s "Did I really used to live alone?"
        "Yo who cares! let's just sleep":
            s "I guess I'll sleep after I'll look around a bit"
    s "Agh! I don't know why but my heart aches! as if before loosing my conciousness, I was in extremem despair."
    s " Like I never wanted to regain my conciousness... or... mayebe I wasn't meant to...?"
    
    "As I look around my eerie environment, something caught my eye"
    "..."
    
    $ mem_used=0
    $ curr_mem=0
    $ survive = False
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
        s "Wait! is this..."
        s "I do!"
        s "I do have a family. This picture seems to have been taken in this house."
        s "But where are they?"
        s "Ugh!"
        s "Mom! Dad!"
        s "I remember them now. But why aren't they here?"
        $ mem_used = 2
        $ curr_mem +=1
        if not curr_mem>1:
            jump objects 
        
    label letter:
        s "So I applied for medschool and got selected"
        s "How odd! I became a doctor yet I don't posses a thin that would indicate that I was one."
        s "This means I never went to medschool, despite clearing my admission."
        s "..."
        $ mem_used = 1
        $ curr_mem +=1
        if not curr_mem>1:
            jump objects
            
    "*Rumaging sound*"
    "A cat?.... Aah! It's eating the only can of food I got!"
    menu:
        "Shoo Kitty Kat":
            jump close_window
        "Let her eat! I don't feel hungry anymore anyway":
            $ survive = True
        "Hit her!":
            s "You're the worst!"
            jump close_window
        "Sell her and get money for food":
            s "...just stay there...I\'m gonna put you in a niiiice little cage..."
            s "Aah! how dare you scratch me... pfft! whatever"
            jump close_window
    label close_window:
        s "I'll just close this window, just in case she finds her way in again."
    
    s "Is that a news paper?"
    s "\"A father shot his family dead\""
    s "wha.. agh!"
    s "..."
    jump story
    
    label story:
        "The weather that day was exteremely humid, and my father... was practically pronounced dead.\nHe had been a living corpse after a horrible accident happen almost 3 years ago."
        "My mom refused to give up on him,even if it meant giving up on her own childeren \n"
        m "This is all my fault! This is all my fault! I\'m sorry Girls... Forgive me! Please forgive me"
        "Eventually it was way too much for her to take in."
        j "Mommy?"
        m "I'm sorry! I'm sorry! I'll fix this.. I'm sorry!"
        "Untill one day.."
        d "Students like you are the reasons of proud for us!"
        d "So our school has decided to fully fund your academic."
        d "Congratulations Miss Saya!"
        s "Yess! Yes! I got into the medschool!!"
        s "All our problems gonna end now! \nWe don't need to live in poverty anymore! " 
        s "Mom's gonna be sooo happy \n"
        "*Step step*"
        s "MOM! MOM! Guess what!\n I have a surprise for you."
        s "You would have never guess this in a million years"
        s "Mom?"
        s "Jia?"
        s "..."
        "She left me with the cruelty of this world... and took with her everything that was dear to me"
        s "What's the point now anymore?"
        s "I don't see any purpose anymore"
        if survive:
            jump live
        jump die
        
        label live:
            s "I'll just take this all"
            "Meow"
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
            "..."
            "*Meow*"
            "..."
            "These kittens... so she had kittens!"
            menu:
                "Pick them up":
                "Pet them and give them food":
                "Knit them a sweater":
                    
            s "So she left you just like my mom!"
            "Meow"
            s "You're just like me. There was no one for me when she left\nI was alone just like you"
            s "In this cruel world with it's cruel people.\n I want to live."
            s "For those who can't live for themselves."
            s "Like me, Like you!"
            s "I want to be hope"
            
            
            
            
        label die:
            s "I suppose this is how it ends."
            
            
            
            
        
        
    # This ends the game.

    return
