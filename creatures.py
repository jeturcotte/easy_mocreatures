# [min spawn, max spawn, per cluster(?)]

spawn = {
    'solitary': '1:1:1',
    'pair': '2:2:2',
    'pack': '2:5:5',
    'swarm': '4:8:8',
    'herd': '10:10:20',
    'chaotic': '1:10:10',
    'ubiquitous': 20,
    'common': 10,
    'uncommon': 6,
    'evasive': 4,
    'rare': 2,
    'unique': 1
}

# { mod: { type: { name: ([rarity, behavior],[list of biome categories]) } } }

creatures = {
    'BiomesOPlenty': {
        'AMBIENT': {},
        'CREATURE': {
            'Rosester': (['rare','pack'],['ODDWOOD','ODDPLAIN'])
        },
        'WATERCREATURE': {},
        'MONSTER': {
            'Glob': (['rare','pack'],['WARMSHORE','HUMIDSHORE','ODDSHORE','DEADSHORE']),
            'JungleSpider': (['unique','solitary'],['HUMIDWOOD','HUMIDHILL'])
        },
        'UNDEFINED': {}
    },
    'MoCreatures': {
        'AMBIENT': {
            'Ant': (['uncommon','swarm'],['COOLPLAIN','WARMPLAIN','ARIDPLAIN','WARMHILL','ARIDHILL','HUMIDPLAIN','HUMIDHILL']),
            'Bee': (['uncommon','swarm'],['COOLPLAIN','COOLHILL','COOLWOOD','WARMPLAIN','WARMHILL','WARMWOOD']),
            'ButterFly': (['common','solitary'],['COOLPLAIN','COOLHILL','WARMPLAIN','WARMHILL','HUMIDPLAIN','HUMIDHILL','COOLPEAK','WARMPEAK']),
            'Crab': (['uncommon','chaotic'],['COOLSHORE','WARMSHORE','HUMIDSHORE','ARIDSHORE','ODDSHORE']),
            'Cricket': (['common','solitary'],['COOLPLAIN','COOLWOOD','COOLHILL','COOLPEAK','WARMPLAIN','WARMWOOD','WARMHILL','WARMPEAK','HUMIDPLAIN','HUMIDWOOD','HUMIDHILL','HUMIDPEAK','ARIDWOOD','ARIDSHORE']),
            'DragonFly': (['evasive','solitary'],['COOLSHORE','WARMSHORE','HUMIDSHORE','ARIDSHORE','HUMIDWOOD','HUMIDPLAIN']),
            'FireFly': (['evasive','solitary'],['COOLPLAIN','COOLWOOD','WARMPLAIN','WARMWOOD']),
            'Fly': (['ubiquitous','solitary'],['COOLPLAIN','COOLSHORE','COOLWOOD','WARMPLAIN','WARMSHORE','WARMWOOD','ARIDSHORE','ARIDWOOD','HUMIDSHORE','HUMIDPLAIN','HUMIDWOOD','HUMIDHILL','HUMIDPEAK']),
            'Maggot': (['evasive','pack'],['WARMWOOD','HUMIDWOOD']),
            'Roach': (['rare','swarm'],['COOLWOOD','WARMWOOD','ARIDWOOD','ARIDSHORE','HUMIDWOOD']),
            'Snail': (['evasive','solitary'],['COOLWOOD','COOLSHORE','WARMWOOD','WARMSHORE','HUMIDWOOD','HUMIDSHORE','HUMIDPLAIN','HUMIDHILL'])
        },
        'CREATURE': {
            'Bear': (['evasive','solitary'],['FROZENSHORE','FROZENPLAIN','FROZENWOOD','FROZENHILL','COOLPLAIN','COOLWOOD','COOLHILL','WARMWOOD','WARMHILL']),
            'BigCat': (['evasive','solitary'],['COOLSHORE','COOLPLAIN','COOLWOOD','WARMWOOD','WARMPLAIN','WARMHILL','ARIDSHORE','ARIDWOOD','HUMIDWOOD','HUMIDHILL']),
            'Bird': (['ubiquitous','chaotic'],['COOLWOOD','COOLHILL','COOLPLAIN','WARMWOOD','WARMPLAIN','WARMHILL','WARMPEAK','ARIDSHORE','ARIDWOOD','HUMIDSEA','HUMIDSHORE','HUMIDPLAIN','HUMIDWOOD','HUMIDHILL','HUMIDPEAK']),
            'Boar': (['uncommon','swarm'],['COOLWOOD','COOLPLAIN','WARMWOOD','WARMPLAIN','ARIDWOOD','HUMIDPLAIN']),
            'Bunny': (['uncommon','pair'],['FROZENPLAIN','FROZENWOOD','COOLPLAIN','COOLWOOD','WARMWOOD','WARMPLAIN']),
            'Crocodile': (['rare','chaotic'],['ARIDSHORE','HUMIDSHORE','HUMIDSEA']),
            'Deer': (['evasive','chaotic'],['COOLPLAIN','COOLWOOD','COOLHILL','WARMPLAIN','WARMWOOD','WARMPLAIN']),
            'Duck': (['common','pair'],['COOLSHORE','WARMSHORE','ARIDSHORE','HUMIDSHORE']),
            'Elephant': (['uncommon','pack'],['FROZENPLAIN','COOLPLAIN','ARIDSHORE','HUMIDPLAIN']),
            'Fox': (['evasive','pair'],['FROZENPLAIN','FROZENWOOD','FROZENHILL','COOLSHORE','COOLWOOD','COOLPLAIN','ARIDSHORE']),
            'Goat': (['common','pack'],['FROZENPEAK','FROZENHILL','COOLPEAK','COOLHILL','WARMPEAK','HUMIDPEAK']),
            'Kitty': (['uncommon','solitary'],['ARIDSHORE','WARMSHORE']),
            'KomodoDragon': (['rare','solitary'],['ARIDSHORE','HUMIDSHORE']),
            'Mouse': (['common','swarm'],['COOLPLAIN','WARMPLAIN','ARIDSHORE','ARIDWOOD','WARMWOOD','COOLWOOD']),
            'Ostrich': (['uncommon','pair'],['ARIDWOOD','ARIDPLAIN']),
            'PetScorpion': (['rare','solitary'],['ARIDPLAIN','ARIDHILL','ARIDWOOD']),
            'Raccoon': (['evasive','pair'],['COOLWOOD','WARMWOOD']),
            'Snake': (['rare','solitary'],['WARMPLAIN','WARMWOOD','ARIDPLAIN','ARIDWOOD','ARIDSHORE','HUMIDPLAIN','HUMIDWOOD','HUMIDSHORE','HUMIDSEA','HUMIDHILL']),
            'Turkey': (['uncommon','swarm'],['COOLPLAIN','COOLHILL','WARMPLAIN','WARMHILL']),
            'Turtle': (['uncommon','solitary'],['WARMSHORE','ARIDSHORE','HUMIDSHORE','WARMWOOD','WARMHILL','HUMIDHILL']),
            'WildHorse': (['uncommon','herd'],['COOLPLAIN','WARMPLAIN','ARIDSHORE']),
            'Wyvern': (['unique','pair'],['ODDPEAK','ARIDPEAK','HUMIDPEAK'])
        },
        'WATERCREATURE': {
            'Dolphin': (['uncommon','pack'],['COOLSEA','WARMSEA','ARIDSEA','HUMIDSEA']),
            'Fishy': (['common','chaotic'],['FROZENSEA','FROZENSHORE','COOLSEA','COOLSHORE','WARMSEA','WARMSHORE','ARIDSEA','ARIDSHORE']),
            'JellyFish': (['uncommon','chaotic'],['COOLSEA','COOLSHORE','WARMSEA','WARMSHORE','ARIDSEA','ARIDSHORE','DEADSHORE']),
            'MediumFish': (['common','swarm'],['FROZENSEA','COOLSEA','WARMSEA','HUMIDSEA','ARIDSEA','HUMIDSHORE']),
            'Piranha': (['rare','swarm'],['HUMIDSHORE','EVILSHORE']),
            'Ray': (['uncommon','pack'],['WARMSEA','WARMSHORE','HUMIDSEA','HUMIDSHORE','ARIDSEA','ARIDSHORE']),
            'Shark': (['uncommon','solitary'],['FROZENSEA','COOLSEA','WARMSEA','HUMIDSEA','ARIDSEA','HUMIDSHORE']),
            'SmallFish': (['ubiquitous','herd'],['FROZENSEA','FROZENSHORE','COOLSEA','COOLSHORE','WARMSEA','WARMSHORE','ARIDSEA','ARIDSHORE'])
        },
        'MONSTER': {
            'BigGolem': (['unique','solitary'],['EVILHILL','EVILPEAK']),
            'FlameWraith': (['rare','pair'],['DEADWOOD','FIRYWOOD']),
            'HellRat': (['rare','pair'],['FIRYPLAIN','FIRYWOOD','FIRYPEAK','FIRYHILL','EVILPLAIN','EVILHILL','EVILPEAK']),
            'HorseHob': (['evasive','solitary'],['DEADPLAIN']),
            'MiniGolem': (['rare','solitary'],['EVILHILL','EVILPLAIN']),
            'Ogre': (['rare','solitary'],['EVILHILL','EVILPEAK','EVILWOOD']),
            'Rat': (['uncommon','swarm'],['WARMWOOD','HUMIDWOOD','EVILSHORE','EVILWOOD','EVILHILL']),
            'Scorpion': (['uncommon','solitary'],['ARIDPLAIN','EVILPLAIN','EVILHILL']),
            'SilverSkeleton': (['rare','pair'],['DEADPLAIN','DEADHILL','DEADWOOD']),
            'WWolf': (['evasive','pack'],['EVILWOOD','EVILPLAIN']),
            'Werewolf': (['rare','solitary'],['EVILPLAIN','EVILHILL','EVILWOOD','EVILSHORE']),
            'Wraith': (['uncommon','solitary'],['DEADPLAIN','DEADWOOD','DEADHILL','DEADPEAK'])
        },
        'UNDEFINED': {}
    },
    'Vanilla': {
        'AMBIENT': {
            'Bat': (['uncommon','solitary'],['COOLHILL','WARMHILL','HUMIDHILL','ARIDHILL','COOLPEAK','WARMPEAK','ARIDPEAK','HUMIDPEAK'])
        },
        'CREATURE': {
            'Chicken': (['common','pack'],['WARMPLAIN','WARMWOOD','HUMIDPLAIN','HUMIDHILL','HUMIDWOOD','ARIDSHORE']),
            'Cow': (['uncommon','herd'],['COOLPLAIN','WARMPLAIN','ARIDSHORE','HUMIDPLAIN']),
            'EntityHorse': (['uncommon','pack'],['COOLPLAIN','WARMPLAIN','ARIDSHORE','HUMIDPLAIN']),
            'MushroomCow': (['rare','herd'],['ODDPLAIN','ODDWOOD','ODDHILL']),
            'Ozelot': (['uncommon','solitary'],['ARIDSHORE','HUMIDWOOD','HUMIDHILL']),
            'Pig': (['common','pack'],['COOLWOOD','WARMWOOD','ARIDWOOD','HUMIDWOOD']),
            'Sheep': (['common','herd'],['COOLPLAIN','COOLHILL','WARMPLAIN','WARMHILL','ARIDSHORE']),
            'Wolf': (['uncommon','pack'],['COOLPLAIN','COOLWOOD','WARMWOOD'])
        },
        'WATERCREATURE': {
            'Squid': (['rare','swarm'],['COOLSEA','WARMSEA','ARIDSEA','HUMIDSEA','HUMIDSHORE'])
        },
        'MONSTER': {
            'Blaze': (['rare','pair'],['FIRYSHORE','FIRYPLAIN','FIRYWOOD','FIRYHILL','FIRYPEAK']),
            'CaveSpider': (['rare','solitary'],['EVILWOOD']),
            'Creeper': (['rare','solitary'],['EVILPLAIN','EVILWOOD','EVILHILL']),
            'EnderDragon': (['unique','solitary'],[]),
            'Enderman': (['rare','pair'],['EVILSHORE','EVILPLAIN','EVILWOOD','EVILHILL','EVILPEAK','EVILSEA']),
            'Ghast': (['rare','solitary'],['FIRYPLAIN','FIRYHILL','FIRYPEAK','EVILPEAK']),
            'Giant': (['rare','solitary'],['EVILPLAIN','EVILHILL']),
            'LavaSlime': (['evasive','pair'],['FIRYSHORE','FIRYPLAIN','FIRYHILL']),
            'PigZombie': (['common','pack'],['DEADHILL','DEADPLAIN','FIRYPLAIN','FIRYWOOD']),
            'Silverfish': (['unique','solitary'],['EVILPEAK']),
            'Skeleton': (['common','solitary'],['DEADPLAIN','DEADSHORE','DEADWOOD','DEADSEA','DEADWOOD']),
            'Slime': (['uncommon','pair'],['HUMIDSEA','HUMIDSHORE','WARMSHORE','EVILSHORE']),
            'SnowMan': (['unique','chaotic'],['FROZENPEAK']),
            'Spider': (['uncommon','solitary'],['HUMIDWOOD','EVILWOOD','ODDWOOD']),
            'Witch': (['rare','solitary'],[]),
            'WitherBoss': (['rare','solitary'],[]),
            'Zombie': (['common','chaotic'],['DEADPLAIN','DEADWOOD','DEADHILL'])
        },
        'UNDEFINED': {
            'Villager': (['uncommon','pair'],[]),
            'VillagerGolem': (['uncommon','solitary'],[])
        }
    }
}
