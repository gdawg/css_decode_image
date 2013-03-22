import sys
import argparse
import cssutils
import logging
import base64

arg_parser = argparse.ArgumentParser(description='extract images from css')
arg_parser.add_argument("-i","--input",help="input css file",required=True)  

args = arg_parser.parse_args()

cssutils.log.setLevel(logging.FATAL) # <-- he's a bit chatty
sheet = cssutils.parseString(open(args.input).read())

output_num = 0
output_prefix = "IMG"

print "parsed..."
for rule in sheet.cssRules:

	try:
		val = str(rule.style.background)

		details = val[(val.find("data:")+5):val.rfind(")")]
		parts = details.split(',')

		out_suffix = ""

		if parts[0].startswith('image/png'):
			out_suffix = "png"
		if parts[0].startswith('image/gif'):
			out_suffix = "gif"
		if parts[0].startswith('image/jpg'):
			out_suffix = "jpg"

		if out_suffix != "":
			out_file_name = "{0}{1:03d}.{2}".format(output_prefix,output_num,out_suffix)
			output_num = output_num + 1

			print " saving",out_file_name
			open(out_file_name,'w').write(base64.b64decode(parts[1]))


	except AttributeError, e:
		print " skipped rule (",e,")"

print "done"
print ""