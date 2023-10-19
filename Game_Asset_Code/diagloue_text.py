def level_1_dialogue(player_icon,abyss_icon):
    test_level_1_dialogue=[
            ("This is a test of the dialogue system",player_icon,"You"),
            ("This shoul work and it if does it will be autoamted",abyss_icon,"The Abyss"),
        ]

    test_level_2_dialogue=[
            ("The Sun is very bright like it was never ever this bright yesterday \n did you know that. I also had a tuna sandwhich yesterday which was very good.",player_icon,"You"),
            ("Ok what I am supposed to do with that information. I have better  \n things to do.",abyss_icon,"The Abyss"),
            ("work",player_icon,"You"),
            ("Nice ",abyss_icon,"The Abyss"),
            ("Nices work",player_icon,"You")
        ]

    test_level_3_dialogue=[
            ("The part three diaglue of lebel 1",player_icon,"You"),
            ("What what what yes yes yes.",abyss_icon,"The Abyss"),
            ("this is working as indedned",player_icon,"You"),

        ]
    return test_level_1_dialogue,test_level_2_dialogue,test_level_3_dialogue

def level_1_dialogue_walk_up(player_icon,elder_icon):
    test_level_1_dialogue=[
        ("Your time to ensure the safety of \n your people has arrived.",elder_icon,"Wizard"),
        ("He is to powerful for me to fight on my own! I cant do this...",player_icon,"You"),
        ("You musnt'n doubt yourself. That will be your defeat. Go straight ahead \n and meet the Abyss.",elder_icon,"Wizard"),
        ("It isn't safe beyond these borders. His men are everywhere.",player_icon,"You"),
        ("Your power exceeds theres.....Now go!.",elder_icon,"Wizard"),
        ]
    return test_level_1_dialogue
       
