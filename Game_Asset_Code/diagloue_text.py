def level_1_dialogue(player_icon,abyss_icon):
    test_level_1_dialogue=[
            ("",player_icon,""),
            ("We have been waiting for your arrivial with great anticipation. Your powers far exceed the rest!",abyss_icon,"The Abyss"),
            ("Are you sure its me, who alone has to do all this?",player_icon,"You"),
            ("There are no errors in this judgement. Go south east to find directions to Worlocks Vassal. ",abyss_icon,"The Abyss"),
            ("Worlocks Vassal!? Are you crazy? I don't have such powers to deal with that beast",player_icon,"You"),
            ("This is the first step to defeat Anes... It's you or no one, to ensure our safety.",abyss_icon,"The Abyss"),
        ]

    test_level_2_dialogue=[
            ("The Sun is very bright like it was never ever this bright yesterday \n did you know that. I also had a tuna sandwhich yesterday which was very good.",player_icon,"You"),
            ("Ok what I am supposed to do with that information. I have better  \n things to do.",abyss_icon,"The Abyss"),
            ("work",player_icon,"You"),
            ("Nice ",abyss_icon,"The Abyss"),
            ("Nices work",player_icon,"You")
        ]

    test_level_3_dialogue=[
            ("",player_icon,""),
            ("Intresting, this reads 'Worlocks Vassal located in the North-Optomind District Section A12 is heavily guarded and fortified. Those who have dealt with Worlock have noted his intial strength and power. Though overtime he seems to tire out but with measurable strength. It is unclear how to defeat him. One may try to tire him out as a attempt.'",player_icon,"You"),
            ("I will have to tire him out if I want to see another day.....",player_icon,"You"),

        ]
    return test_level_1_dialogue,test_level_2_dialogue,test_level_3_dialogue

def level_1_dialogue_walk_up(player_icon,elder_icon):
    test_level_1_dialogue=[
        ("Your time to ensure the safety of your people has arrived. You must defeat Anes.",elder_icon,"Wizard"),
        ("He is to powerful for me to fight on my own! I cant do this......",player_icon,"You"),
        ("You musnt'n doubt yourself. That will be your defeat. Go straight ahead \n and meet the Abyss. They will guide you further",elder_icon,"Wizard"),
        ("It isn't safe beyond these borders. His men are everywhere.",player_icon,"You"),
        ("ENOUGH!!.....Your power exceeds theres.....Now go!.",elder_icon,"Wizard"),
        ]
    return test_level_1_dialogue
       
