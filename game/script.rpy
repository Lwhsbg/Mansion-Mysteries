image bg_man_son = Transform("images/bg man_son.jpg", xysize=(1920, 1080))
image bg_kitchen_room = Transform("images/bg kitchen_room.jpg", xysize=(1920, 1080))
image bg_lab_room = Transform("images/bg lab_room.jpg", xysize=(1920, 1080))
image bg_library_room = Transform("images/bg library_room_.jpg", xysize=(1920, 1080))
image bg_living_room = Transform("images/bg living_room.jpg", xysize=(1920, 1080))
image bg_bedroom_image = Transform("images/bg bedroom_image.jpg", xysize=(1920, 1080))
default wolf_symbol_found = False
default kitchen_key_found = False
default clues_found = set()
default entity_suspicion = 0
default stag_symbol_found = False
default cabinet_key_found = False
default shelf_code_found = False
default owl_symbol_found = False
default moth_symbol_found = False
default mirror_seen = False
default lock_correct = False

define fade_black = Fade(0.5, 0.3, 1.2, color="#000000")
define slow_fade  = Fade(1.0, 0.5, 2.0, color="#000000")

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
    scene bg_man_son
    with dissolve
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
    return

label go_in:
    "{i}Your intrusive thoughts takes over you and you decide to head in.{/i}"
    "{i}Once you go inside, you come upon a huge sitting room with great airflow.{/i}"
    scene bg_living_room
    with dissolve
    with hpunch
    "{i}The place gives off a mysterious and creepy vibe, with it's dark interiors shining.{/i}"
    "{i}Suddenly, you feel like something is watching you, closely from the back.You turn around, to see nothing.{/i}"
    m "Was that just my imagination? I think I have had a bit too much to drink."
    m "Should I head back?"
    menu:
        m "Should I head back?"
        "Head back.":
            jump Head_back
        "Go on.":
            jump go_on

label Head_back:
    m "I should probably head back."
    "{i}As you turned away to go back, there was nothing. Just a black wall. The front door had disappeared leaving you in utter shock.{/i}"
    scene black
    "{i}You then hear a sound in a distance.{/i}"
    e "grrrrrrrrrrrrrrrrrrrrr..."
    m "Am I dreaming??"
    jump room_start

label go_on:
    m "Hell, I will go on."
    "{i}As you start to walk inside, you hear a creepy whistle behind you.{/i}"
    e "grrrrrrrrrrrrrrrrrrrrrrrrrr..."
    "{i}In complete shock, you quickly turn around, just to see nothing but a dark black wall in place of the door that you had come in from.{/i}"
    scene black
    m "Am I dreaming?"
    jump room_start

label room_start:
    "{i}Terrified of what you just witnessed, you fall into your knees and start calmly collect whatever thoughts you had.{/i}"
    scene bg_living_room
    with dissolve
    with hpunch
    m "{i}Okay, this is not a dream. I should think of this rationally. If not the front door, I can see the back door at the far end of the hallway.{/i}"
    m "I should go check it out."
    "{i}You head out to the backyard exit but see it locked with a pin, asking for four animals.{/i}"
    "{i}Then you look around to observe around and find out that there are 4 total rooms in the wide mansion.{/i}"
    "{i}You find it weird that there were only 4 excluding the living room in such a big mansion, but paid no mind because you had bigger fish to fry.{/i}"
    m "I have no other options but to do this now..."
    m "Let's see, there seems to be 4 rooms."
    m "A Kitchen, a Laboratory, a Bedroom and a Library"
    jump mansion_hub

label mansion_hub:
    "{i}You find yourself standing in the living room before 4 doors.{/i}"
    menu:
        m "Which one should I go?"
        "Kitchen":
            jump kitchen_room
        "Laboratory":
            jump lab_clue
        "Bedroom":
            jump bedroom_clue
        "Library":
            jump library_clue
        "Try the back door." if len(clues_found) >= 4:
            jump backdoor_lock

# ============================================================
#  KITCHEN
# ============================================================
label kitchen_room:
    scene bg_kitchen_room
    with dissolve
    with hpunch
    "{i}You see a wide kitchen with a big table readily set for six, although the dust tells that it hasnt been touched in years.{/i}"
    "{i}Food that hasnt been touched in years hang around from the kitchen balcony, almost as if staring at you.{/i}"
    jump kitchen_menu

label kitchen_menu:
    "{i}You head towards the table{/i}"
    menu:
        "What do you want to check?"
        "Examine the table.":
            jump kitchen_table
        "Check the knives and the cutting board.":
            jump kitchen_knives
        "Check the cellar door." if kitchen_key_found:
            jump kitchen_cellar
        "Check the cellar door." if not kitchen_key_found:
            "It is bolted with a heavy lock. You may need to find a key."
            jump kitchen_menu
        "Leave the Kitchen.":
            jump mansion_hub

label kitchen_table:
    "{i}You go towards the table where you find six plates.{/i}"
    "{i}Five of them are chipped, rusty and old. The sixth is a bit finer china plate, and suprisingly spotless.{/i}"
    menu:
        "What do you want to do?"
        "Lift the sixth plate.":
            "{i}After lifting the sixth plate, a brass key is beneath it. Can it be used for something?{/i}"
            $ kitchen_key_found = True
            $ clues_found.add("kitchen_key")
            m "Someone left this here for me to find it."
            $ entity_suspicion += 1
            jump kitchen_menu
        "Leave it alone.":
            m "{i}Something feels wrong about touching it. You step back.{/i}"
            jump kitchen_menu

label kitchen_knives:
    "{i}Carved into the cutting board, was a wolf's head half worn out, with it's jaws open.{/i}"
    if not wolf_symbol_found:
        $ wolf_symbol_found = True
        $ clues_found.add("wolf_symbol")
        m "So the wolf is the first clue to the exit."
        jump kitchen_menu
    else:
        m "The wolf again. I should look for other things."
        jump kitchen_menu

label kitchen_cellar:
    "{i}The key turns easily. Too easily. Cold air flows from the passage below.{/i}"
    menu:
        "{i}Do you choose to go down?{/i}"
        "Go down.":
            scene black with fade_black
            "{i}You walk down to the bottom of the cell.{/i}"
            "{i}At the pitch darkness of the cell, where you can't see clearly, you feel an old scrap of paper.{/i}"
            "{i}Then suddenly, you hear a rustle and a whisper-like voice in your spine.{/i}"
            e "Ohh~~ I wasnt expecting you to be this brave..."
            $ entity_suspicion += 2
            "{i}You immediately rush upwards as soon as you hear that, without looking back.{/i}"
            scene bg_kitchen_room
            with dissolve
            with hpunch
            "{i}You shake off the dust from the paper and start reading it.{/i}"
            $ clues_found.add("cellar_note")
            "{i}There were four names, with the letter forgive written over and over again.{/i}"
            m "I wonder what this is about."
            jump kitchen_menu
        "Stay at the top.":
            m "I better not go to that sketchy place."
            jump kitchen_menu

# ============================================================
#  LABORATORY
# ============================================================
label lab_clue:
    jump laboratory_room

label laboratory_room:
    scene bg_lab_room
    with dissolve
    with hpunch
    "{i}The air around the lab becomes sharper, tinged with a chemical smell that stings the back of your throat.{/i}"
    "{i}You can see a line of cracked beakers on the cabinets. A central chair sits loose in the middle with leather straps hanging from it.{/i}"
    m "{i}What was this room used for?{/i}"
    m "{i}I should look around for clues around the lab. There is probably a symbol for the lock somewhere.{/i}"
    jump lab_menu

label lab_menu:
    menu:
        "What do you want to check?"
        "Read the journal on the desk.":
            jump lab_journal
        "Check the mounted skull on the wall.":
            jump lab_skull
        "Try the locked cabinet." if cabinet_key_found:
            jump lab_cabinet
        "Try the locked cabinet." if not cabinet_key_found:
            "{i}It seems to be locked with a combination code which you do not know about yet.{/i}"
            "{i}Maybe you could find it somewhere.{/i}"
            jump lab_menu
        "Leave the laboratory.":
            jump mansion_hub

label lab_journal:
    "{i}You open the journal and check the pages.{/i}"
    "{i}The first few pages were normal. Reports on progress, dosage and hope.{/i}"
    "{i}Further in, the handwriting turns jagged, almost like the writer is getting frustrated overtime.{/i}"
    "{i}There are many torn out pages with jagged handwriting.{/i}"
    m "{i}Maybe the code has been torn out by whoever this is. The cabinet was not meant to be after all.{/i}"
    "{i}Just as you are losing hope on finding the combination, you approach the last page.{/i}"
    "{i}There, with a ruined handwriting laid a combination, what seemed like a three--one--four.{/i}"
    "{i}After that, written..'She is running out of time.'{/i}"
    $ cabinet_key_found = True
    $ clues_found.add("lab_journal")
    jump lab_menu

label lab_skull:
    "{i}Mounted above the cabinet is a stag's skull, antlers spread wide. Something is etched faintly into the bone.{/i}"
    if not stag_symbol_found:
        $ stag_symbol_found = True
        $ clues_found.add("stag_symbol")
        m "{i}So it is a stag this room. This is interestingly creepy.{/i}"
        $ entity_suspicion += 1
        "{i}As you step back from the skull, you feel eyes on you that aren't there.{/i}"
        jump lab_menu
    else:
        m "The stag again. I've already got this one."
        jump lab_menu

label lab_cabinet:
    "{i}You turn the dial of the lock. 3--1--4, and it opens up.{/i}"
    "{i}Inside, there is a torn photograph of what seems like a family photo wrapped in a muddy cloth.{/i}"
    m "Is this the family photo of the family which used to live here? I should wash it and look at it properly."
    $ clues_found.add("lab_photo")
    e "{i}...{/i}"
    "{i}You suddenly feel a cold gust of wind straight on your neck. But more than that, from a distance you can feel something staring you down.{/i}"
    "{i}You sense it getting closer and closer. In a hurry, you throw the photo away and then make a run for it outside the laboratory.{/i}"
    $ entity_suspicion += 2
    jump lab_menu

# ============================================================
#  LIBRARY
# ============================================================
label library_clue:
    jump library_room

label library_room:
    scene bg_library_room
    with dissolve
    with hpunch
    "{i}Tall shelves stretch up into shadow, packed with books that look untouched by anything but time.{/i}"
    "{i}The room is covered with dust, with seemingly a globe at the middle.{/i}"
    m "{i}If there are answers in this house, they're probably in here somewhere.{/i}"
    m "{i}There are many things that I can find here. I should definitely try searching around.{/i}"
    jump library_menu

label library_menu:
    menu:
        "What do you want to check?"
        "Look through the family ledger.":
            jump library_ledger
        "Examine the owl bookend by the globe around the middle.":
            jump library_owl
        "Search the shelves for a hidden book." if shelf_code_found:
            jump library_hidden_book
        "Search the shelves for a hidden book." if not shelf_code_found:
            "{i}The shelves are a mess, hundreds of spines all blurring together. You wouldn't know what to look for without some kind of order to search by.{/i}"
            jump library_menu
        "Leave the Library.":
            jump mansion_hub

label library_ledger:
    "{i}You open a ledger lying in the desk of the library. There were names, some minimal info.{/i}"
    "{i}But in the end of it all, there was a family tree drawn with fading ink.{/i}"
    "{i}Seems like this person was tracking the blood relation percentage.{/i}"
    "{i}There, just one name was scratched out.{/i}"
    m "{i}Looks like this person did not want anyone to figure out who this was.{/i}"
    "{i}On the last page, there was a slight bit of text at the bottom that read:{/i}"
    m "Shelf 3, row 1?"
    m "{i}That is oddly specific. Maybe that means something.{/i}"
    $ shelf_code_found = True
    $ clues_found.add("library_ledger")
    jump library_menu

label library_owl:
    if not owl_symbol_found:
        "{i}An owl made up of rare dark wood perches up on the table, with it's eyes hollowed out.{/i}"
        m "That is creepy. But an owl this time huh."
        $ owl_symbol_found = True
        $ clues_found.add("owl_symbol")
        $ entity_suspicion += 1
        "{i}For a moment, you'd swear the owl's head has turned slightly since you walked in.{/i}"
        jump library_menu
    else:
        m "The owl again. I've already got this one."
        jump library_menu

label library_hidden_book:
    "{i}You follow the note that you got from the ledger, shelf 3, row 1.{/i}"
    "{i}There, you find a singular old book.{/i}"
    m "Oh, what is it about this time..."
    "{i}Inside isn't a story. It's a diary, the handwriting small and childlike.{/i}"
    "{i}\"Grandmother's voice is still in the walls. Papa says it's the wind. I don't think Papa believes that either.\"{/i}"
    $ clues_found.add("library_diary")
    e "You're not supposed to read that."
    $ entity_suspicion += 2
    "{i}The book slips from your hands before you even feel yourself let go of it. It's gone by the time it hits the floor.{/i}"
    jump library_menu

# ============================================================
#  BEDROOM
# ============================================================
label bedroom_clue:
    jump bedroom_room

label bedroom_room:
    scene bg_bedroom_image
    with dissolve
    with hpunch
    "{i}Unlike the rest of the house, this room feels almost untouched by the decay outside its door.{/i}"
    "{i}A bed sits made, the sheets barely faded. A vanity mirror stands in the corner, and a wooden case rests on the dresser.{/i}"
    m "{i}This room feels... different. Like someone still lives here.{/i}"
    m "{i}I should look around properly. This might be the last room I need.{/i}"
    jump bedroom_menu

label bedroom_menu:
    menu:
        "What do you want to check?"
        "Look at the wooden case on the dresser.":
            jump bedroom_case
        "Look at the vanity mirror.":
            jump bedroom_mirror
        "Check under the floorboards." if mirror_seen:
            jump bedroom_floorboard
        "Check under the floorboards." if not mirror_seen:
            "{i}Nothing about the floor looks out of place to you right now.{/i}"
            jump bedroom_menu
        "Leave the Bedroom.":
            jump mansion_hub

label bedroom_case:
    "{i}Inside the case is a collection of moths, pinned neatly under glass, wings spread wide.{/i}"
    if not moth_symbol_found:
        m "{i}A moth this time. That should be the last one.{/i}"
        $ moth_symbol_found = True
        $ clues_found.add("moth_symbol")
        $ entity_suspicion += 1
        "{i}One of the moths, you swear, was not pinned down a moment ago.{/i}"
        jump bedroom_menu
    else:
        m "The moth again. I've already got this one."
        jump bedroom_menu

label bedroom_mirror:
    "{i}You step towards the vanity mirror, the glass fogged with age.{/i}"
    "{i}You wipe it clear with your sleeve, and for a second, your reflection is not quite your own.{/i}"
    "{i}Something stands behind you in the glass. Tall. Still. Watching.{/i}"
    m "{i}...{/i}"
    "{i}You spin around. Nothing is there. When you look back at the mirror, it's just you again.{/i}"
    e "You weren't supposed to see that yet."
    $ entity_suspicion += 2
    $ mirror_seen = True
    m "{i}Okay. Okay. That was real. That was actually real.{/i}"
    jump bedroom_menu

label bedroom_floorboard:
    "{i}Still shaken, you notice one floorboard sits slightly raised near the bed.{/i}"
    "{i}You pry it up. Underneath is a small folded letter, along with a strip of old fabric tied around it.{/i}"
    "{i}The letter has four names written on it, matching the ones from the cellar note.{/i}"
    "{i}Beside each name is drawn a small symbol: a wolf, a stag, an owl, a moth.{/i}"
    m "{i}That's it. That's the order.{/i}"
    $ clues_found.add("bedroom_letter")
    "{i}A weight settles over the room, heavier than before.{/i}"
    e "You found all of it."
    $ entity_suspicion += 2
    jump bedroom_menu

# ============================================================
#  BACK DOOR LOCK + ENDINGS
# ============================================================
label backdoor_lock:
    scene bg_living_room with dissolve
    "{i}You stand before the backyard door, with the four symbols memorized in your head.{/i}"
    "{i}Wolf. Stag. Owl. Moth. You think back to the letter, to the order the names were written in.{/i}"
    m "{i}I only get one real shot at this. I need to be sure.{/i}"
    menu:
        "Enter the order: Wolf, Stag, Owl, Moth.":
            $ lock_correct = True
            jump lock_result
        "Enter the order: Moth, Owl, Stag, Wolf.":
            $ lock_correct = False
            jump lock_result
        "Enter the order: Owl, Moth, Stag, Wolf.":
            $ lock_correct = False
            jump lock_result

label lock_result:
    if lock_correct:
        "{i}The four pins click into place, one after another. A heavy groan echoes from deep inside the door frame.{/i}"
        m "That is it. This is actually it."
        jump ending_router
    else:
        "{i}The pins jam halfway. Nothing happens. The lock does not react, it just waits, cold under your hand.{/i}"
        m "That is wrong. This has to be wrong."
        $ entity_suspicion += 3
        e "You are running out of chances."
        "{i}Something moves behind you in the dark, closer than it has ever been.{/i}"
        jump ending_caught

label ending_router:
    if entity_suspicion < 5:
        jump ending_clean_escape
    else:
        jump ending_haunted_escape

label ending_clean_escape:
    scene black with slow_fade
    "{i}The door swings open into the cold, wet, dark of the forest outside. Real air. Real rain.{/i}"
    "{i}You do not look back. You do not let yourself. You just run until the mansion is lost behind the trees, then nothing at all.{/i}"
    "{i}By morning, you are at the roadside, flagging down the car that first passes.{/i}"
    m "It is over. Whatever that was, it is over."
    "{i}You never go back for your car.{/i}"
    "THE END"
    return

label ending_haunted_escape:
    scene black with slow_fade
    "{i}The door gives way. You stumble out into the rain, gasping like you were just saved from drowning.{/i}"
    "{i}You make it to the road. You make it home. Weeks pass. Then months.{/i}"
    "{i}But the temperature in your house never quite sits right anymore. And one eerie rainy night, you hear it as you were just about to fall asleep...{/i}"
    e "Click."
    "{i}You never sleep with the lights off again.{/i}"
    "{i}THE END{/i}"
    return

label ending_caught:
    scene black with Pause(0.5)
    "{i}The air in the room grows impossibly thin. You claw at your own throat for a breath that won't come.{/i}"
    e "You were not the first. You will not be the last."
    "{i}The dark presses from every side at once, and the living room, the mansion, the world outside it - all of it goes quiet.{/i}"
    "{i}THE END{/i}"
    return