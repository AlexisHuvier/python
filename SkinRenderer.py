import sys
import os
from PIL import Image

if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        print("Usage : python", sys.argv[0], "<skin file> [<is four pixel skin>]")
    elif not os.path.exists(sys.argv[1]):
        print("Unknown skin file")
    else:
        im = Image.open(sys.argv[1]).convert("RGBA")
        output = Image.new("RGBA", (16, 32), (255, 255, 255, 0))  
        output.paste(im.crop((8, 8, 16, 16)), (4, 0, 12, 8)) # HEAD
        output.alpha_composite(im.crop((40, 8, 48, 16)), (4, 0)) # HEAD OVERLAY
        output.paste(im.crop((20, 20, 28, 32)), (4, 8, 12, 20)) # CHEST
        output.alpha_composite(im.crop((20, 36, 28, 48)), (4, 8)) # CHEST OVERLAY  
        output.paste(im.crop((20, 52, 24, 64)), (8, 20, 12, 32)) # LEFT LEG
        output.alpha_composite(im.crop((4, 52, 8, 64)), (8, 20)) # LEFT LEG OVERLAY
        output.paste(im.crop((4, 20, 8, 32)), (4, 20, 8, 32)) # RIGHT LEG
        output.alpha_composite(im.crop((4, 36, 8, 48)), (4, 20)) # RIGHT LEG OVERLAY    
        if len(sys.argv) < 3 or sys.argv[2] == False:
            output.paste(im.crop((36, 52, 40, 64)), (12, 8, 16, 20)) # LEFT ARM
            output.alpha_composite(im.crop((52, 52, 56, 64)), (12, 8)) # LEFT ARM OVERLAY
            output.paste(im.crop((44, 20, 48, 32)), (0, 8, 4, 20)) # RIGHT ARM
            output.alpha_composite(im.crop((44, 36, 48, 48)), (0, 8)) # RIGHT ARM OVERLAY
        else:
            output.paste(im.crop((36, 52, 39, 64)), (12, 8, 15, 20)) # LEFT ARM
            output.alpha_composite(im.crop((52, 52, 55, 64)), (12, 8)) # LEFT ARM OVERLAY
            output.paste(im.crop((44, 20, 47, 32)), (1, 8, 4, 20)) # RIGHT ARM
            output.alpha_composite(im.crop((44, 36, 47, 48)), (1, 8)) # RIGHT ARM OVERLAY
        output = output.resize((150, 300), Image.NEAREST)
        output.save(sys.argv[1], "PNG")
        output.show()
