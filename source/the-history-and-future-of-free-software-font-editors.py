# Render this document with DrawBot3: http://www.drawbot.com/

# Import modules:
import math

# Basic variables  (width, height, margin):
W, H, M = 1920, 1080, 128

def grid(W, H, M):  # (width, height, margin)
    fill(None)
    gridWidth = W-(M*2)
    gridHeight = (H-(M*2))-40
    print("grid width =", gridWidth)
    print("grid Height =", gridHeight)
    
    stpY = 0  # Step in sequence on x axis    
    stroke(0, 0, 1)  # Set grid line color RED
    gridUnitY = 40
    for y in range(20):
        polygon((M, (M+20)+stpY), (W-M, (M+20)+stpY))
        stpY += gridUnitY  # Set position for next gridline 

    # stpX = 0  # Step in sequence on x axis    
    # stroke(0, 0, 1)  # Set grid line color RED
    # gridUnitX = 40
    # for x in range(42):
    #     polygon((M+stpX, H-(M+20)), ((M)+stpX, (M+20)))
    #     stpX += gridUnitX  # Set position for next gridline 
   
    stpXY = 0
    stroke(0.5,0.5,0.5)  # Set grid line color RED
    for xx in range(4):
        stpX = 0  # Step in sequence on x axis    
        for x in range(8):
            rect(M+stpX, (M+20)+stpXY, 40*4, 40*4)
            stpX += 211  # Set position for next gridline
    
        stpXY += 200

   
    # Draw margin
    stroke(1,0,0)
    fill(None)
    rect(M, M+20, gridWidth, gridHeight)
    
def newSlide():
    newPage(W, H)
    font("fonts/Epistle-Regular.ttf")  # Set the font
    #font("fonts/amiri/Amiri-Bold.ttf")


# Title Page #####################################################
newSlide()
fill(0)
stroke(10)           # Set the background color
rect(0-10, 0-10, W+10, H+10)  # Draw the background
# grid(W, H, 140)        # Draw the grid

# Basic Style
stroke(None)
# image("images/metafont-a-dark.jpg", (W/2.4, -64), alpha=0.3)
# image("images/mmcharview.png", (M, M), alpha=1)

headlineTxt = FormattedString()
headlineTxt.append("The History and Future of Free Software Font Editors", font="fonts/Epistle-Regular.ttf", fontSize=124 , fill=(1), lineHeight=120)
textBox(headlineTxt, (M+10, 350, W/1.2, H/2), align="left")



# text("The History and Future", (M+10, startPoint-(lineHeight*0)), align="left")
# text("of Free Software", (M+10 , startPoint-(lineHeight*1)) , align="left")
# text("Font Editors", (M+10, startPoint-(lineHeight*2)), align="left")


# MetaFont #####################################################
newSlide()
# grid(W, H, 140)        # Draw the grid

# Headline

# image("images/metafont-a.jpg", (W/2.4, -64), alpha=0.3)
# image("images/mmcharview.png", (M, M), alpha=1)

headlineTxt = FormattedString()
headlineTxt.append("Egalitarian Computing", font="fonts/Epistle-Regular.ttf", fontSize=96, fill=(0), lineHeight=80)
textBox(headlineTxt, (M+10, 360, W/1, H/2), align="left")



# MetaFont #############################################
newSlide()
# grid(W, H, 140)        # Draw the grid

# image
image("images/metafont-a.jpg", (0, 0), alpha=0.3)

# Headline
headlineTxt = FormattedString()
headlineTxt.append("METAFONT", font="fonts/Epistle-Regular.ttf", fontSize=96, fill=(0), lineHeight=80)
textBox(headlineTxt, (M+10, 354, W/2, H/2), align="left")

knuthQuote1 = FormattedString()
knuthQuote1.append('“A mathematical formula should never be “owned”\n  by anybody!\n\n Mathematics belong to God.”\n\n — Donald Knuth', font="fonts/Epistle-Regular.ttf", fontSize=60, fill=(0), lineHeight=80, firstLineIndent=-25)
textBox(knuthQuote1, (980, -95, 760, 1000), align="left")


# Emigre and the Macintosh #############################################
newSlide()
# grid(W, H, 140)        # Draw the grid

# image
image("images/fontastic.jpg", (W/2, 0), alpha=1)

# Headline
headlineTxt = FormattedString()
headlineTxt.append("Emigre", font="fonts/Epistle-Regular.ttf", fontSize=96, fill=(0), lineHeight=96)
textBox(headlineTxt, (M+10, 354, W/2, H/2), align="left")

# GNU+Linux #####################################################
newSlide()
grid(W, H, 140)        # Draw the grid

# Headline

# image("images/metafont-a.jpg", (W/2.4, -64), alpha=0.3)
# image("images/mmcharview.png", (M, M), alpha=1)

headlineTxt = FormattedString()
headlineTxt.append("GNU+Linux", font="fonts/Epistle-Regular.ttf", fontSize=96, fill=(0), lineHeight=80)
textBox(headlineTxt, (M+10, 354, W/2, H/2), align="left")

image("images/raspberry-pi.png", (M-100, M-400), alpha=0.3)

knuthQuote1 = FormattedString()
knuthQuote1.append('"In the long run, making programs free is a step toward a postscarcity world, where nobody will have to work very hard just to make a living. People will be free to devote themselves to activities that are fun, such as programming, after spending the necessary ten hours a week on required tasks such as legislation, family counseling, robot repair and asteroid prospecting. There will be no need to be able to make a living from programming." -- RMS', font="fonts/Epistle-Regular.ttf", fontSize=48, fill=(0), lineHeight=64)
textBox(knuthQuote1, (800, -100, 1000, 1000), align="left")



# MetaFont #####################################################
newSlide()
# grid(W, H, 140)        # Draw the grid

# Headline

# image("images/metafont-a.jpg", (W/2.4, -64), alpha=0.3)
# image("images/mmcharview.png", (M, M), alpha=1)

headlineTxt = FormattedString()
headlineTxt.append("METAFONT", font="fonts/Epistle-Regular.ttf", fontSize=96, fill=(0), lineHeight=80)
textBox(headlineTxt, (M+10, 360, W/2, H/2), align="left")

knuthQuote1 = FormattedString()
knuthQuote1.append('"A mathematical formula should never be "owned" by anybody! Mathematics belong to God." -- Knuth', font="fonts/Epistle-Regular.ttf", fontSize=72, fill=(0), lineHeight=72)
textBox(knuthQuote1, ((W/1.5)+25, -200, 600, 1000), align="left")


# I still believe that most typefaces are designed for commercial reasons, just to make money or for identity purposes. In reality the number of good typefaces is rather limited and most of the new ones are elaborations on pre-existing faces. --massimo

# beyond eurocentric design
#  

# The Parable of the Frog

saveImage("slides.pdf")