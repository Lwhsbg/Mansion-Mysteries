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
