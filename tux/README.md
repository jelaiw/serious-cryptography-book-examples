Not a code example from the book, but JP Aumasson's mention did inspire me to encrypt Tux at some point.

Python code should be self-explanatory. A big TY to Imagemagick for converting PNG to RGBA and back again.

```sh
$ wget https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/1200px-Tux.svg.png
--2025-03-29 14:54:44--  https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/1200px-Tux.svg.png
Resolving upload.wikimedia.org (upload.wikimedia.org)... 208.80.154.240, 2620:0:861:ed1a::2:b
Connecting to upload.wikimedia.org (upload.wikimedia.org)|208.80.154.240|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 304220 (297K) [image/png]
Saving to: ‘1200px-Tux.svg.png’

1200px-Tux.svg.png                                     100%[===========================================================================================================================>] 297.09K  --.-KB/s    in 0.02s   

2025-03-29 14:54:44 (15.3 MB/s) - ‘1200px-Tux.svg.png’ saved [304220/304220]

$ file 1200px-Tux.svg.png 
1200px-Tux.svg.png: PNG image data, 1200 x 1422, 8-bit/color RGBA, non-interlaced
$ convert -depth 32 1200px-Tux.svg.png out.rgba
$ file out.rgba 
out.rgba: data
$ identify -format '%wx%h' 1200px-Tux.svg.png 
1200x1422$ convert -size 1200x1422 -depth 32 ecb_tux.rgba ecb_tux.png
$
```

Did not bother to save intermediate working material (RGBA files).
