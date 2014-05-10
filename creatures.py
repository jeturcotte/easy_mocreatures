# mod: { beast: [[this, or, that], 'and' [this, or, that]], etc }
creatures = {
    'BOP': {
        'bird': [],
        'glob': [['hot','molten'], ['wet','soaked'], ['dangerous']],
        'junglespider': [['hot','warm'], ['wet','soaked'], ['tangled'],['dangerous']],
        'phantom': [['evil']],
        'pixie': [['magical']],
        'rosester': [['magical'], ['brush','thickets']],
        'wasp': [['warm','hot'], ['dangerous'], ['dry'], ['hilly','mountainous']]
    },
    'MOC': {
        'ant': [['cool','warm','hot'], ['arid','dry','balanced','wet'], ['calm','wild','dangerous']],
        'bear': [['icy','cool','warm'], ['dry','balanced','wet'], ['hilly','mountainous'], ['brush','thicket','forested'], ['wild','dangerous']],
        'bee': [['cool','warm','hot'], ['arid','dry','balanced','wet'], ['calm','wild','dangerous']],
        'bigcat': [['icy','cool','warm'], ['dry','balanced','wet'], ['brush','thicket','forested']],
        'biggolem': [['evil','magical'], ['deserted','brush']],
        'bird': [['cool','warm','hot'], ['dry','balanced','wet','soaked'], ['magical', 'calm', 'wild']],
        'boar': [['cool','warm','hot'], ['dry','balanced'], ['wild','dangerous'], ['brush','thickets','forested','tangled']],
        'bunny': [['icy','cool','warm'], ['dry','balanced'], ['magical','calm']],
        'butterfly': [['cool','warm','hot'], ['arid','dry','balanced','wet'], ['calm','wild','dangerous']],
        'crab': [['soaked','water'], ['icy','cool','warm','hot']],
        'cricket': [['cool','warm','hot'], ['arid','dry','balanced','wet'], ['calm','wild','dangerous']],
        'crocodile': [['warm','hot'], ['shore', 'soaked'], ['wild','dangerous']],
        'deer': [['cool','warm'], ['brush','thickets','forested'], ['calm', 'wild']],
        'dolphin': [['submerged']],
        'dragonfly': [['cool','warm','hot'], ['arid','dry','balanced','wet'], ['calm','wild','dangerous']],
        'duck': [['cool','warm','hot'], ['soaked','wet','balanced'], ['calm','wild']],
        'egg': [],
        'elephant': [['icy','cool','warm','hot'], ['dry','balanced'], ['brush','thickets'], ['wild','dangerous']],
        'ent': [['cool','warm','hot'], ['magical'], ['thickets','forested','tangled']],
        'firefly': [['cool','warm','hot'], ['arid','dry','balanced','wet'], ['calm','wild','dangerous']],
        'fishbowl': [],
        'fishy': [['submerged','soaked','wet','balanced']],
        'fly': [['cool','warm','hot'], ['arid','dry','balanced','wet'], ['calm','wild','dangerous']],
        'fox': [['flat','shelved','hilly','mountainous'], ['calm','wild','dangerous']],
        'goat': [['cool','warm','hot'], ['flat','shelved','hilly','mountainous'], ['calm','wild']],
        'hellrat': [['hot','molten'], ['evil']],
        'horsemob': [['evil']],
        'jellyfish': [['submerged']],
        'kitty': [],
        'kittybed': [],
        'komododragon': [['hot'], ['dangerous']],
        'litterbox': [],
        'maggot': [['cool','warm','hot'], ['arid','dry','balanced','wet'], ['calm','wild','dangerous']],
        'mediumfish': [['submerged','soaked','wet','balanced']],
        'minigolem': [['evil','magical'], ['deserted','brush']],
        'mole': [['cool','warm','hot'], ['flat','hilly','mountainous','shelved'], ['brush', 'thickets', 'deserted'], ['calm','wild']],
        'mouse': [['cool','warm','hot'], ['flat','hilly','mountainous','shelved'], ['calm','wild']],
        'ogre': [['mountainous', 'jagged'], ['dangerous','evil']],
        'ostrich': [['warm','hot'], ['arid','dry','balanced'], ['deserted', 'brush']],
        'petscorpion': [],
        'piranha': [['hot'], ['dangerous'], ['submerged','soaked','wet','balanced']],
        'raccoon': [['cool','warm'], ['flat','hilly','mountainous','shelved'], ['calm','wild']],
        'rat': [['cool','warm','hot'], ['flat','hilly','mountainous','shelved'], ['dangerous','evil','wild']],
        'ray': [['submerged']],
        'roach': [['cool','warm','hot'], ['arid','dry','balanced','wet'], ['calm','wild','dangerous']],
        'scorpion': [['warm','hot'], ['arid','dry'], ['evil','dangerous'], ['deserted','brush','thickets']],
        'shark': [['submerged'], ['wild','dangerous']],
        'silverskeleton': [['evil']],
        'smallfish': [['submerged','soaked','wet','balanced']],
        'smail': [['cool','warm','hot'], ['soaked','wet']],
        'snake': [['warm','hot'], ['arid','dry','balanced','wet'], ['wild','dangerous','evil']],
        'turkey': [['cool'], ['calm','wild'], ['brush','thickets','forested']],
        'turtle': [['cool','warm','hot'], ['shore','flat','shelved'], ['deserted','brush'], ['magical','calm','wild']],
        'werewolf': [['evil']],
        'wildhorse': [['cool','warm','hot'], ['brush'], ['calm','wild'], ['dry','balanced']],
        'wwolf': [['cool','warm','hot'], ['dangerous','evil'], ['flat','shelved','hilly','mountainous'], ['brush','thickets','forested','tangled']],
        'wyvern': [],
    },
    'MC': {
        'bat': [['cool','warm','hot'], ['arid','dry','balanced','wet'], ['calm','wild','dangerous']],
        'blaze': [['molten'], ['evil']],
        'cavespider': [['hot'],['wet','soaked'], ['dangerous','evil']],
        'chicken': [['cool','warm','hot'], ['dry','balanced','wet'], ['thickets','forested','tangled'], ['calm','wild']],
        'cow': [['cool','warm'], ['dry','balanced','wet'], ['brush','thickets'], ['calm','wild']],
        'creeper': [['warm','hot'], ['wet','soaked'], ['forested','tangled'], ['wild','dangerous','evil']],
        'enderdragon': [],
        'enderman': [['magical','evil']],
        'entityhorse': [['cool','warm','hot'], ['brush'], ['calm','wild'], ['dry','balanced']],
        'ghast': [['molten'], ['evil']],
        'giant': [['evil']],
        'lavaslime': [['hot','molten'],['deserted'],['magical','evil','dangerous'],['arid','dry']],
        'mushroomcow': [['fungal']],
        'ozelot': [['warm','hot'], ['hilly','mountainous'], ['forested','tangled'], ['balanced','wet']],
        'pig': [['cool','warm','hot'], ['balanced','wet'], ['calm','wild'], ['brush','thickets']],
        'pigzombie': [['evil']],
        'sheep': [['cool','warm'], ['brush','thickets'], ['calm','wild']],
        'silverfish': [],
        'skeleton': [['evil']],
        'slime': [['warm','hot'],['soaked'],['magical','wild','dangerous','evil']],
        'snowman': [],
        'spider': [['cool','warm','hot'], ['arid','dry','balanced','wet'], ['dangerous','evil']],
        'squid': [['submerged','shore','soaked']],
        'villager': [],
        'villagergolem': [],
        'witch': [['cool','warm','hot'], ['evil']],
        'witherboss': [],
        'wolf': [['icy','cool','warm'], ['wild','dangerous'], ['flat','shelved','hilly','mountainous'], ['brush','thickets','forested']],
        'zombie': [['evil']]
    }
}