from biomes import biomes
from creatures import creatures

# yes, yes this is procedural and could be easier done functionally... but for such a narrow purpose... yeah

zones = {}

# recompile easy-to-read list of biome assignments into Mo'C-ready structure

print '# Configuration file \n\nbiomegroup-defaults {'
for cmod in creatures:
    for cname in creatures[cmod]:
        found_in_biomes = []
        for bmod in biomes:
            for bname in biomes[bmod]:
                each_req_satisfied = True
                if not creatures[cmod][cname]:
                    continue
                for reqs in creatures[cmod][cname]:
                    at_least_one_requirement = False
                    for this_req in reqs:
                        if this_req in biomes[bmod][bname]:
                            at_least_one_requirement = True
                    if not at_least_one_requirement:
                        each_req_satisfied = False
                if each_req_satisfied:
                    found_in_biomes.append('%s|%s' % (bmod, bname))
        print '\tS:%s_%s_DEFAULT:<%s>' % (
            cmod.upper(), cname.upper(), ':'.join(found_in_biomes)
        )
print '}'

