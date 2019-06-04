#!/bin/bash

# This script will detect newly created and
# staged image files (*.png) and add a 3-pixel
# gray boder to each image.

echo "Adding borders to images..."

git diff --cached --name-status | while read st file; do
        if [ "$st" != 'A' ]; then continue; fi
        if [[ $file == *.png ]]; then
		echo "Adding border to ${file}..."
		convert $file -bordercolor gray -border 3 $file
        fi
done

echo "Finished"
