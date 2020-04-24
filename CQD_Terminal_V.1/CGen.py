# Where the magic happens#

import random

def charater_gen():
    species_list = ['Human', 'Elf', 'Dwarf', 'Halfling', 'Dragonborn', 'Gnome', 'Half-Elf', 'Half-Ork', 'Tiefling']
    class_list = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Wizard']
    gender_list = ['Male', 'Female']
    background_list = ['Spy/Criminal', 'Folk Hero', 'Acolyte', 'Noble', 'Sage', 'Soldier']

    species_result = random.choice(species_list)
    class_result = random.choice(class_list)     # To be implemented?#
    background_result = random.choice(background_list)      # To be implemented?#

    print("""
    """)
    print("Species: ", species_result)
    print("Class: ", class_result)
    print("Background: ", random.choice(background_list))
    print("Gender: ", random.choice(gender_list))
    print("-----------------------------")
    print("Str: ", random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))
    print("Dex: ", random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))
    print("Con: ", random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))
    print("Int: ", random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))
    print("Wis: ", random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))
    print("Cha: ", random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))
    print("-----------------------------")

    if species_result == 'Human':
        print("""
        Human Traits:
        >Ability Score Increase: Ability scores each increase +1
        >Alignment Advice: Humans tend toward no particular 
        alignment. The best and the worst are found among them.
        >Size: Humans vary widely in height and build, from 
        barely 5 feet to well over 6 feet tall. Regardless 
        of your position in that range, your size is Medium.
        >Speed: Base walking speed is 30 feet.
        >Languages: They can speak, read, and write Common 
        and one extra language of your choice.
        
        Variant Human Traits:
        If your campaign uses the optional feat rules from the 
        Player’s Handbook, your Dungeon Master might allow 
        these variant traits.
        >Ability Score Increase: Two different ability scores 
        of your choice increase by 1.
        >Skills: You gain proficiency in one skill of your choice.
        >Feat: You gain one feat of your choice.
        """)
    elif species_result == 'Elf':
        print("""
        Elf Traits:
        >Ability Score Increase: Dexterity score increases by 2
        >Alignment Advice: Elves love freedom, variety, and 
        self-expression, so they lean strongly toward the gentler 
        aspects of chaos. They value and protect others’ freedom 
        as well as their own, and they are more often good than 
        not. The drow are an exception; their exile into the 
        Underdark has made them vicious and dangerous.
        >Size: Elves range from under 5 to over 6 feet tall and 
        have slender builds. Your size is Medium.
        >Speed: Base walking speed is 30 feet.
        >Languages: They can speak, read, and write Common and Elvish
        >Darkvision: They can see in dim light within 60 feet of 
        them, but can’t discern color in the dark, only shades of gray.
        >Keen Senses: They have proficiency in the Perception skill.
        >Fey Ancestry: They have advantage on saving throws against 
        being charmed, and magic can’t put them to sleep
        >Trance: Elves don’t need to sleep. Instead, they meditate deeply, 
        remaining semiconscious, for 4 hours a day. After resting in 
        this way, they gain the same benefit that a human does from 
        8 hours of sleep
        
        Known Variants: Eladrin, High Elf, Wood Elf 
        """)
    elif species_result == 'Dwarf':
        print("""
        Dwarf Traits:
        >Ability Score Increase: Constitution score increases by 2.
        >Alignment Advice: Most dwarves are lawful, believing firmly 
        in the benefits of a well-ordered society. They tend toward 
        good as well, with a strong sense of fair play and a belief 
        that everyone deserves to share in the benefits of a just 
        order.
        >Size: Dwarves stand between 4 and 5 feet tall and average 
        about 150 pounds. Your size is Medium.
        >Speed: there base walking speed is 25 feet. Your speed is 
        not reduced by wearing heavy armor.
        >Languages: They can speak, read, and write Common and Dwarvish.
        >Darkvision: They can see in dim light within 60 feet of 
        them, but can’t discern color in the dark, only shades of gray.
        >Dwarven Resilience: They have advantage on saving throws 
        against poison, and have resistance against poison damage.
        >Dwarven Combat Training: They  have proficiency with the 
        battleaxe, handaxe, light hammer, and warhammer.
        >Tool Proficiency: They gain proficiency with the artisan’s
        tools of their choice: smith’s tools, brewer’s supplies, 
        or mason’s tools.
        >Stonecunning: Whenever they make an Intelligence (History) 
        check related to the origin of stonework, they are considered 
        proficient in the History skill and add double their proficiency
        bonus to the check, instead of the normal proficiency bonus.
        
        Known Variants: Hill Dwarf, Mountain Dwarf
        """)
    elif species_result == 'Halfling':
        print("""
        Halfling Traits:
        >Ability Score Increase: Dexterity score increases by 2.
        >Alignment Advice: Most halflings are lawful good. As a rule, 
        they are good-hearted and kind, hate to see others in pain, 
        and have no tolerance for oppression. They are also very 
        orderly and traditional, leaning heavily on the support of their 
        community and the comfort of their old ways.
        >Size: Halflings average about 3 feet tall and weigh about 40 
        pounds. Your size is Small.
        >Speed: There base walking speed is 25 feet.
        >Languages: They can speak, read, and write Common and Halfling.
        >Lucky: When they roll a 1 on the d20 for an attack roll, ability 
        check, or saving throw, they can reroll the die and must use the 
        new roll.
        >Brave: They have advantage on saving throws against being frightened.
        >Halfling Nimbleness: They can move through the space of any creature 
        that is of a size larger than them.
        
        Known Variants: Lightfoot Halfling, Stout Halfling
        """)
    elif species_result == 'Dragonborn':
        print("""
        Dragonborn Traits:
        >Ability Score Increase: Strength score increases by 2, and Charisma 
        score increases by 1.
        >Alignment Advice: Dragonborn tend to extremes, making a conscious 
        choice for one side or the other in the cosmic war between good and evil 
        (represented by Bahamut and Tiamat, respectively). Most dragonborn are 
        good, but those who side with Tiamat can be terrible villains.
        >Size: Dragonborn are taller and heavier than humans, standing well over 
        6 feet tall and averaging almost 250 pounds. Your size is Medium.
        >Speed: There base walking speed is 30 feet.
        >Languages: They can speak, read, and write Common and Draconic.
        >Draconic Ancestry: They have draconic ancestry. Choose one type of 
        dragon from the Draconic Ancestry table.
        >Breath Weapon: They can use there action to exhale destructive energy. 
        There draconic ancestry determines the size, shape, and damage type 
        of the exhalation.
        >Damage Resistance: They have resistance to the damage type associated 
        with there draconic ancestry.
        """)
    elif species_result == 'Gnome':
        print("""
        Gnome Traits:
        >Ability Score Increase: Intelligence score increases by 2.
        >Alignment Advice: Gnomes are most often good. Those who tend toward 
        law are sages, engineers, researchers, scholars, investigators, or 
        inventors. Those who tend toward chaos are minstrels, tricksters, 
        wanderers, or fanciful jewelers. Gnomes are good-hearted, and even 
        the tricksters among them are more playful than vicious.
        >Size: Gnomes are between 3 and 4 feet tall and average about 40 pounds. 
        There size is Small.
        >Speed: There base walking speed is 25 feet.
        >Languages: They can speak, read, and write Common and Gnomish.
        >Darkvision: They can see in dim light within 60 feet of 
        them, but can’t discern color in the dark, only shades of gray.
        >Gnome Cunning: They have advantage on all Intelligence, Wisdom, and 
        Charisma saving throws against magic.
        Known Variants: Deep Gnome, Rock Gnome
        """)
    elif species_result == 'Half-Elf':
        print("""
        Half-Elf Traits:
        >Ability Score Increase: Charisma score increases by 2, and two other 
        ability scores of choice increase by 1.
        >Alignment Advice: Half-elves share the chaotic bent of their elven 
        heritage. They value both personal freedom and creative expression, 
        demonstrating neither love of leaders nor desire for followers. They 
        chafe at rules, resent others’ demands, and sometimes prove unreliable, 
        or at least unpredictable.
        >Size: Half-elves are about the same size as humans, ranging from 5 to 6 
        feet tall. There size is Medium.
        >Speed: There base walking speed is 30 feet.
        >Languages: They can speak, read, and write Common, Elvish, and one extra 
        language.
        >Darkvision: They can see in dim light within 60 feet of 
        them, but can’t discern color in the dark, only shades of gray.
        >Fey Ancestry: They have advantage on saving throws against being charmed, 
        and magic can’t put them to sleep.
        >Skill Versatility: They gain proficiency in two skills of there choice
        """)
    elif species_result == 'Half-Ork':
        print("""
        Half_Ork Traits:
        >Ability Score Increase: Strength score increases by 2, and Constitution 
        score increases by 1.
        >Alignment Advice: Half-orcs inherit a tendency toward chaos from their orc 
        parents and are not strongly inclined toward good. Half-orcs raised among 
        orcs and willing to live out their lives among them are usually evil.
        >Size: Half-orcs are somewhat larger and bulkier than humans, and they range 
        from 5 to well over 6 feet tall. There size is Medium.
        >Speed: There base walking speed is 30 feet.
        >Languages: They can speak, read, and write Common and Orc. 
        >Darkvision: They can see in dim light within 60 feet of 
        them, but can’t discern color in the dark, only shades of gray.
        >Menacing: They gain proficiency in the Intimidation skill.
        >Relentless Endurance: When they are reduced to 0 hit points but not killed 
        outright, they can drop to 1 hit point instead. they can’t use this feature 
        again until you finish a long rest.
        >Savage Attacks: When they score a critical hit with a melee weapon attack, 
        they can roll one of the weapon’s damage dice one additional time and add it 
        to the extra damage of the critical hit.
        """)
    elif species_result == 'Tiefling':
        print("""
        Tiefling Traits:
        >Ability Score Increase: Intelligence score increases by 1, and Charisma 
        score increases by 2.
        >Alignment Advice: Tieflings might not have an innate tendency toward 
        evil, but many of them end up there. Evil or not, an independent nature 
        inclines many tieflings toward a chaotic alignment.
        >Size: Tieflings are about the same size and build as humans. 
        There size is Medium.
        >Speed: There base walking speed is 30 feet.
        >Languages: They can speak, read, and write Common and Infernal.
        >Darkvision: They can see in dim light within 60 feet of 
        them, but can’t discern color in the dark, only shades of gray.
        >Hellish Resistance: They have resistance to fire damage.
        >Infernal Legacy: They know the thaumaturgy cantrip. When they reach 3rd 
        level, they can cast the hellish rebuke spell as a 2nd-level spell once 
        with this trait and regain the ability to do so when they finish a long rest. 
        When they reach 5th level, they can cast the darkness spell once with this 
        trait and regain the ability to do so when they finish a long rest. 
        Charisma is there spellcasting ability for these spells.
        """)
    else:
        print("Whoops! A mistake was made")

    print("-----------------------------")
    print("""
    
    Press 1 to roll again
    Press 2 to quit
    """)
    cgen_number = input("Please select a number: ")
    try:
        cgen_int = int(cgen_number)
    except ValueError:
        print(" Invalid Selection! ")
        charater_gen()

    if cgen_int == 1:
        charater_gen()
    elif cgen_int == 2:
        exit()
    else:
        print("Invalid Selection! Please try again")
        charater_gen()



