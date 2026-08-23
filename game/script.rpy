label start:
    $ player_name = renpy.input("Please enter your name:")
    $ player_name = player_name.strip()

    if not player_name:
        $ player_name = "Sulek"

    label real_start:
        scene black 
        "{i}You find yourself in your car returning from a highschool reunion party in another city.{/i}"
        "{i}It was already 12 am in the morning and in a deep, dark forest connecting the two cities.{/i}"
        m "{i}This silence is eerie. I should play some music.{/i}"
        "{i}All of a sudden, you feel an alarming presence in a distance, and then a huge sound in the back.{/i}"
        "{i}You had crashed into a tree, with your tires busted and no means to call for help.{/i}"
        "{i}If that was not bad enough, the upset sky that could pour any minute had started doing it's job.{/i}"
        "{i}You panic on what to do, and while searching for nearby huge trees, you spot a dim fade of light in a distance.{/i}"
        m "What is that? Maybe that is a sign for help.."
        "{i}You walk towarsa the light expecting shelter.{/i}"
        "{i}In almost a surreal fashion, a big mansion stands in front of you.{/i}"
        scene man_son 
        with Dissolve
        with hpunch
        m "Huh? Why is this in the middle of a forest?"
        m "Must have been abandoned in the past."
        "{i}You had no more time for any more questions. You were soaked by the rain and the visibility was decreasing every second.{/i}"
        "{i}You slowly walk towards the mansion. You see some shade where the rain ws not getting right outside the door.{/i}"
        m "I guess i will stay there for tonight and ask for help in the day."
        "{i}You head there and lay down in the ground to rest.{/i}"
        "{i}After a while, you decide to look around what there is.{/i}"
        "{i}You can see the huge doors leading inside, a garden with long withered flowers, a table outside which seemed to be used for morning teas, and big windows.{/i}"
        m "Looks like this used to be a residence of a very wealthy family."
        m "Makes me curious to see what lies inside... Maybe expensive antiques which can make me rich."
        m "I doubt anybody is living inside, and in this state i can quietly walk away with whatever treasures i can find."
        menu:
            "Should I take a look inside?"
            "Go inside":
                jump go_in
            "Do not go inside":
                jump dont_go
label dont_go:
    "You decide not to go."
    "{i}You fall asleep and wake up 5 hours later in the morning.{/i}"
    scene black 
    "{i}You suprisingly feel light in the morning although you feel like you forgot something important.{/i}"
    "{i}You carry on to the road where your broken down car is.{/i}"
    "{i}You wait for a vehicle to pass by and eventually, you make it out of there.{/i}"
    return:
label go_in:
    "{i}Your intrusive thoughts takes over you and you decide to head in.{/i}"
    "{i}Once you go inside, you come upon a huge sitting room with great airflow.{/i}"
    scene living_room with dissolve with hpunch
    "{i}The place gives off a mysterious and creepy vibe, with it's dark interiors shining.{/i}"
    "{i}Suddenly, you feel like something is watching you, closely from the back.You turn around, to see nothing.{/i}"
    m "Was that just my imagination? I think I have had a bit too much to drink."
    m "Should I head back?"
    menu:
        m "Should I head back?"
        "Head back.":
            jump to Head_back
        "Go on.":
            jump to go_on
    label Head_back:
        m "I should probably head back."
        "{i}As you turned away to go back, there was nothing. Just a black wall. The front door had disappeared leaving you in utter shock.{/i}"
        scene black
        "{i}You then hear a sound in a distance.{/i}"
        e "grrrrrrrrrrrrrrrrrrrrr..."
        m "Am I dreaming??"
        jump to room_start
    label go_on:
        m "Hell, I will go on."
        "{i}As you start to walk inside, you hear a creepy whistle behind you.{/i}"
        e "grrrrrrrrrrrrrrrrrrrrrrrrrr..."
        "{i}In complete shock, you quickly turn around, just to see nothing but a dark black wall in place of the door that you had come in from.{/i}"
        scene black
        m "Am I dreaming?"
        jump to room_start
    label room_start:
        "{i}Terrified of what you just witnessed, you fall into your knees and start calmly collect whatever thoughts you had.{/i}"
        scene living_room with dissolve with hpunch
        m "{i}Okay, this is not a dream. I should think of this rationally. If not the ront door, I can see the back door at the far end of the hallway.{/i}"
        m "I should go check it out."
        "{i}You head out to the backyard exit but see it locked with a pin, asking for four animals.{/i}"
        "{i}Then you look around to observe around and find out that there are 4 total rooms in the wide mansion.{/i}"
        "{i}You find it weird that there were only 4 excluding the living room in such a big mansion, but paid no mind because you had bigger fish to fry.{/i}"
        m "I have no other options but to do this now..."
        m "Let's see, there seems to be 4 rooms."
        m "A Kitchen, a Laboratory, a Bedroom and a Library"
        menu:
            m "Which one should I go to first?"
            "Kitchen":
                jump to Kitchen_clue
                
            

            

