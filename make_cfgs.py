from biomes import biomes
from creatures import creatures, spawn

# yes, yes this is procedural and could be easier done functionally... but for such a narrow purpose... yeah

zones = {}

# recompile easy-to-read list of biome assignments into Mo'C-ready structure

for clime in biomes:
    for terrain in biomes[clime]:
        for mod in biomes[clime][terrain]:
            if biomes[clime][terrain][mod]:
                ct = '%s%s' % (clime, terrain)
                if ct not in zones:
                    zones[ct] = []
                for biome in biomes[clime][terrain][mod]:
                    if biome not in zones[ct]:
                        zones[ct].append('%s|%s' % (mod, biome))

# cycle through new construct and push to configuration file

MoCBiomeGroups = open('MoCBiomeGroups.cfg','w')
MoCBiomeGroups.write('# Configuration file\n')
for ct in zones:
    MoCBiomeGroups.write('\n####################\n# %s\n####################\n' % ct.lower())
    MoCBiomeGroups.write('%s {\n    S:%s <%s>\n}\n\n' % (ct.lower(), ct, ":".join(zones[ct])))
MoCBiomeGroups.close()

# now cycle through the creature construct and push out individual configs for each mod
# this relies on creatures.py having correctly named/cased mod names at the top of the hierarchy

BiomeSettings = "\n\n####################\n# entity-biome-settings\n####################\n\nentity-biome-settings {\n%s\n}"
SpawnSettings = "\n\n####################\n# entity-spawn-settings\n####################\n\nentity-spawn-settings {\n%s\n}\n"

for mod in creatures:
    CreaturesCFG = open('%s.cfg' % mod, 'w')
    ebs = []
    ess = []
    for btype in creatures[mod]:
        for beast in creatures[mod][btype]:
            ((rarity, behavior), categories) = creatures[mod][btype][beast]
            ebs.append('    S:%s <%s>' % (beast, ":".join(categories)))
            ess.append('    S:%s <%s:%d:%s>' % (beast, btype, spawn[rarity], spawn[behavior]))
            biomelist = []
    CreaturesCFG.write('# Configuration File')
    CreaturesCFG.write(BiomeSettings % "\n".join(ebs))
    CreaturesCFG.write(SpawnSettings % "\n".join(ess))
    CreaturesCFG.close()
