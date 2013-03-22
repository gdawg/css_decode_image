CSS Decode Image
================

Python scripts to extract stored image data from css files.

ok, so maybe there's currently only one script, but it'll pull stored base64 encoded JPG,GIF,PNG files from css.

## Usage

    usage: cssdecodeimg.py [-h] -i INPUT
    cssdecodeimg.py: error: argument -i/--input is required

Assuming you have a css file containing a base64 encoded image, stored as a background like so

    .div-with-img {
    	background:url("data:image/png;base64,iVBORw0KGgoAA  ...
	}	

run

    python cssdecodeimg.py -i input.css

## Sample output

    teh_dawgz@poota ~/rad_dir/css_decode_image $ python cssdecodeimg.py -i input.css
    parsed...
     saving IMG000.png
     saving IMG001.png
     skipped rule ( 'CSSMediaRule' object has no attribute 'style' )
     saving IMG024.png
     saving IMG025.png
     saving IMG035.png
    done
    
