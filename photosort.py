#!/usr/bin/python

import sys
import os
from PIL import Image

def get_exif(img):
	img = Image.open('img.jpg')
	return img._getexit()

def main(args):
	if len(args) != 3:
		print "Usage: photosort INPUT_DIRECTORY OUTPUT_DIRECTORY"
		sys.exit(1)

	input_dir = args[1]
	output_dir = args[2]

	#TODO: Everything
		

main(sys.argv)