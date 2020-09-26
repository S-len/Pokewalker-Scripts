# Pokewalker Scripts
A collection of pokewalker-related scripts.

## Summary
* img_to_bin.py -- Converts a 64x48 or 64x96 image (2 images that animate) into the format used by the pokewalker
	* slice_image.py -- Slices up the image into the 2 shades and into a 64x8 chunks
	* img_to_txt.py -- Converts the image into a binary string
	* txt_to_bin.py -- Converts the binary string into raw sprite format used by the pokewalker
* bin_to_img.py -- Does the reverse
* sprite_dump.py -- Runs bin_to_img.py over a dumped a/2/5/6 package to get all the sprites.

## Required libararies
* Pillow -- For image processing (basically all of the image-related scripts)
* Ndspy -- For rom/narc traversal (scrape.py)

Just install them with pip.

## Guide
Getting custom sprites onto the pokewalker:
1. Get a 64x48 4 color image where the colors are #000000, #404040, #808080 and #FFFFFF
2. Run img_to_bin.py to convert it into a binary file.
3. Use Tinke to replace the desired sprite at a/2/5/6 (id is the pokedex id minus 1, so Bulbasaur is 0 for example)
4. Save your ROM and run it via TWiLightMenu while having a cart that has IR plugged into slot 1.
5. Send the Pokemon whose sprite you replaced to the walker.
6. Done.
Note: For problems with getting the IR to work with custom roms you should ask the
people that made it, I really can't help you with that.
You can try [this](https://github.com/DS-Homebrew/TWiLightMenu/issues/962) or [this](https://github.com/DS-Homebrew/nds-bootstrap/issues/431).
If you can, use a legit HGSS cart for the IR, since that's pretty much always going to work.

Dumping sprites from a/2/5/6:
1. Get your backup of HGSS.
2. Open it up in Tinke and navigate to a/2/5/6.
3. Extract the package.
4. Run sprite_dump.py over it.
