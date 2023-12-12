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
            ("Intresting, this reads 'Worlock Vassal located in the North-Optomind District Section A12 is heavily guarded and fortified. Those who have dealt with Worlock have noted his intial strength and power. Though overtime he seems to tire out but with measurable strength. It is unclear how to defeat him. One may try to tire him out as a attempt.'",player_icon,"You"),
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

def level_2_dialogue(player_icon):
    level_2_dialogue_1=[
        ("Anes's fortress should be nearby. This place is eerliy quite, wait who's that?",player_icon,"You")
    ]
    return level_2_dialogue_1

def level_2_dialogue_walk_up(player_icon,guard_icon,brute_icon,frost_icon):
    level_2_dialouge_2=[
        ("What are you doing here? You know Worlock is nearby right.",player_icon,"You"),
        ("Long story, but I would rather not get into it....",guard_icon,"???"),
        ("You can tell me, I can help you!.",player_icon,"You"),
        ("Help me with what? I've been through more than you could dream of.",guard_icon,"???"),
        ("Do you know, or heard of the Wizard by chance? I was sent here to defeat Worlock...",player_icon,"You"),
        ("If I tell you will you leave me alone?",guard_icon,"???"),
        ("Sure......",player_icon,"You"),
        ("I was trying to loot Worlock's chamber with my buddies. Heard he has alot of gold in it. Unfortunetely though, he got the best of us and im the only one standing. Name is Knave by the way.",guard_icon,"Knave"),
        ("Do you have any idea on how to beat him? ",player_icon,"You"),
        ("I've heard you must tire him out. Didn't seem like that worked. Though, we only lasted a few seconds.",guard_icon,"Knave"),
        ("Hmmm. Any other tips?",player_icon,"You"),
        ("Oh yeah, their are alot of his goons South-East of here. It would be best to take them out beforehand.",guard_icon,"Knave"),
        ("Thank you!",player_icon,"You"),
        ("Now will you leave me alone?",guard_icon,"Knave"),
        ("Whatever, sounds good.....",player_icon,"You"),
    ]
    level_2_dialouge_3=[
        ("GeT hIM !!!!!!!!!",brute_icon,"Brute"),
        ("Oh no......",player_icon,"You")

    ]
    level_2_dialogue_4=[
        ("WHO GOES THERE",frost_icon,"Anes"),
        ("You've hurt our people enough! I ask you to stop immedietely or face severe consequences!",player_icon,"You"),
        ("HAHAHHA. WHO ARE YOU ANYWAYS! YOU WILL DIE NOW!!!!!",frost_icon,"Worlock"),
        ("Why did I say that.....",player_icon,"You")
    ]
    return level_2_dialouge_2,level_2_dialouge_3,level_2_dialogue_4

def level_3_dialogue(player_icon,arrow_enemy_icon):
    level_3_dialogue_1=[
        ("There has to be something nearby.... I'll keep looking around.",player_icon,"You")
    ]
    level_3_dialogue_2=[
        ("There must be some sort of clue to where Anes is.....",player_icon,"You")
    ]
    level_3_dialogue_3=[
        ("HE FELL FOR IT, GET HIM!!",arrow_enemy_icon,"Archer"),
        ("I need to get out of here!",player_icon,"You")
    ]
    return level_3_dialogue_1,level_3_dialogue_2,level_3_dialogue_3

       
