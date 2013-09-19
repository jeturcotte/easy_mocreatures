easy_mocreatures
================

This is just a stupid-cheesy procedural python project to turn easier-to-read minecraft creature configs
into mo'creatures .cfg files that then must, by hand, be placed in the correct locations

MoCBiomeGrouns.cfg is placed in /config/MoCreatures/
and the rest are palced in /config/MoCreatures/Creatures/

The python code itself is stupid straight forward and could probably do well with lots of refactoring and upgrades...
but it does what it was initially intended to do.

biomes.py defines which biomes are in which groupnames
creatures.py defines creature spawn behavior names as well as which groupnames creatures are assigned to

both are intended to be easier to read and fiddle with than MoCreature's own configs, essentially.

That's it.
