# Render this document with DrawBot3: http://www.drawbot.com/

# Import modules:
import math


# Basic variables  (width, height, margin):
W, H, M = 1920, 1080, 128
headlineXPos = M+10
headlineYPos = -M-46
headlineLineHeight = 80
headlineFontSize = 72


def grid(W, H, M):  # (width, height, margin)
    fill(None)
    gridWidth = W-(M*2)
    gridHeight = (H-(M*2))-40
    print("grid width =", gridWidth)
    print("grid Height =", gridHeight)

    stpY = 0  # Step in sequence on x axis
    stroke(0.4)  # Set grid line color RED
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
    stroke(0.4)  # Set grid line color RED
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


# Title Page #####################################################
newPage(W, H)
fill(1)
stroke(None)       
# rect(-10, -10, W+10, H+10)  # Draw the background
font("fonts/Epistle-Regular.ttf")  # Set the font

# Image
image("images/mf-a.png", (W/1.7, 0), alpha=1)

# Text
headlineTxt = FormattedString()
headlineTxt.append("The History and Future of Free Software Font Editors", \
    font="fonts/Epistle-Regular.ttf", \
    fontSize=headlineFontSize , \
    fill=(0), \
    lineHeight=headlineLineHeight\
)

headlineSub = FormattedString()
headlineSub.append("@eliheuer—OSDNYC—July, 2018 ", \
    font="fonts/Epistle-Regular.ttf", \
    fontSize=headlineFontSize/2 , \
    fill=(0), \
    lineHeight=headlineLineHeight/2\
)

textBox(headlineTxt, (headlineXPos, headlineYPos, \
    W/2, H), align="left"
)
textBox(headlineSub, (headlineXPos, headlineYPos-710, \
    W/2, H), align="left"
)


# grid(W, H, 140)        # Draw the grid


# MetaFont #############################################
newPage(W, H)

# image
# image("images/metafont-a.jpg", (0, 0), alpha=0.5)

# Headline
headlineTxt = FormattedString()
headlineTxt.append("METAFONT", \
    font="fonts/Epistle-Regular.ttf", \
    fontSize=headlineFontSize, \
    fill=(0), \
    lineHeight=headlineLineHeight)
textBox(headlineTxt, (headlineXPos, headlineYPos, W/2, H), align="left")

knuthQuote1 = FormattedString()
knuthQuote1.append('“A mathematical formula should never be “owned”\n  by anybody!\n\n  Mathematics belong to God.”\n\n  — Donald Knuth', \
    font="fonts/Epistle-Regular.ttf", \
    fontSize=60, \
    fill=(0), \
    lineHeight=80, \
    firstLineIndent=-25)
textBox(knuthQuote1, (984, -97, 780, 1000), align="left")

# grid(W, H, 140)        # Draw the grid

#art
artX = M
artY = M+30
step = 0
stroke(0)
fontSize(100)     
font("Helvetica-Bold")  # Set the font
for i in range(24):
    artX += 7
    artY += 7
    step += 0.1
    rotate(step)
    fill(artX/250)
    text("METAFONT", (artX+M, artY))


# Emigre #############################
newPage(W, H)

# image
image("images/fontastic.jpg", (W/2, 0), alpha=1)
image("images/zuzana.png", ((W/2)-450, -70), alpha=1)

# Headline
headlineTxt = FormattedString()
headlineTxt.append("Emigre", \
    font="fonts/Epistle-Regular.ttf", 
    fontSize=headlineFontSize, \
    fill=(0), \
    lineHeight=headlineLineHeight)
textBox(headlineTxt, (headlineXPos, headlineYPos, W/2, H), align="left")

#art
artX = M
artY = M+30
step = 0
stroke(0)
fontSize(160)     
font("fonts/Toren-Rotalic.otf")  # Set the font
for i in range(24):
    artX += 1
    artY += 1
    step += 0.05
    rotate(step)
    fill(artX/150)
    text("Emigre", (artX, artY))

# grid(W, H, 140)        # Draw the grid


# GNU+Linux ############################
newPage(W, H)

image("images/raspberry-pi.png", (M-100, M-400), alpha=0.5)

# Headline
headlineTxt = FormattedString()
headlineTxt.append("GNU+Linux", \
    font="fonts/Epistle-Regular.ttf", \
    fontSize=headlineFontSize, \
    fill=(0), \
    lineHeight=headlineLineHeight)
textBox(headlineTxt, (headlineXPos, headlineYPos, W/2, H), align="left")


#art
artX = 0
artY = M+200
step = 0
stroke(0)
fontSize(160)     
font("fonts/Toren-Mono.otf")  # Set the font
for i in range(10):
    artX += 7
    artY += 7
    step += 0.1
    fill(step)
    text("GNU+Linux", (artX, artY))

rmsQuote1 = FormattedString()
rmsQuote1.append('“In the long run, making programs free is a step toward a postscarcity world, where nobody will have to work very hard just to make a living... There will be no need to be able to make a living from programming.”\n\n  — Richard Stallman', \
    font="fonts/Epistle-Regular.ttf", \
    fontSize=60, \
    fill=(0), \
    lineHeight=80, \
    firstLineIndent=-25)
textBox(rmsQuote1, (984, -97, 780, 1000), align="left")



# grid(W, H, 140)        # Draw the grid


# simple ≠ easy ############################
newPage(W, H)

# image("images/fontastic.jpg", (W/2, 0), alpha=1)

# Headline
headlineTxt = FormattedString()
headlineTxt.append("Simple ≠ Easy", \
    font="fonts/Epistle-Regular.ttf", \
    fontSize=headlineFontSize, \
    fill=(0), \
    lineHeight=headlineLineHeight)
textBox(headlineTxt, (headlineXPos, headlineYPos, W/2, H), align="left")

#art
artX = M+600
artY = M+30
step = 0
stroke(0)
fontSize(150)     
font("Helvetica-Bold")  # Set the font
for i in range(24):
    artX += 7
    artY += 7
    step += 0.1
    rotate(step**2)
    fill(step)
    text("Simple ≠ Easy", (artX, artY))

grid(W, H, 140)        # Draw the grid

# FontForge ############################
newPage(W, H)

image("images/fontforge-chip.jpg", (W/2, 0), alpha=1)
image("images/mmcharview.png", (W/3, 407), alpha=1)

# Headline
headlineTxt = FormattedString()
headlineTxt.append("FontForge", \
    font="fonts/Epistle-Regular.ttf", \
    fontSize=headlineFontSize, \
    fill=(0), \
    lineHeight=headlineLineHeight)
textBox(headlineTxt, (headlineXPos, headlineYPos, W/2, H), align="left")

#art
artX = M-60
artY = M
stroke(0)
fontSize(200)     
font("fonts/Toren-Rotalic.otf")  # Set the font
for i in range(16):
    artX += 7
    artY += 7
    fill(artX/250)
    text("FontForge", (artX, artY))

# grid(W, H, 140)        # Draw the grid


# TruFont ############################
newPage(W, H)

image("images/TruFont.png", (W/2, 156), alpha=1)

# Headline
headlineTxt = FormattedString()
headlineTxt.append("TruFont", \
    font="fonts/Epistle-Regular.ttf", \
    fontSize=headlineFontSize, \
    fill=(0), \
    lineHeight=headlineLineHeight)
textBox(headlineTxt, (headlineXPos, headlineYPos, W/2, H), align="left")

    
#art
artX = M-20
artY = M
step = 0
stroke(0)
fontSize(100)     
font("fonts/Toren-Proportional.otf")  # Set the font
for i in range(18):
    artX += 3
    artY += 5
    step += 0.1
    fontSize(50+artX*1.5)
    fill(step)
    text("TruFont", (artX, artY))

# grid(W, H, 140)        # Draw the grid


# EditFonts ############################
newPage(W, H)

image("images/sugar_pi_01.png", (W/3, 0), alpha=1)

# Headline
headlineTxt = FormattedString()
headlineTxt.append("EditFonts", \
    font="fonts/Epistle-Regular.ttf", \
    fontSize=headlineFontSize, \
    fill=(0), \
    lineHeight=headlineLineHeight)
textBox(headlineTxt, (headlineXPos, headlineYPos, W/2, H), align="left")

    
#art
artX = M-60
artY = M
stroke(0)
fontSize(200)     
font("fonts/Toren-Rotalic.otf")  # Set the font
for i in range(16):
    artX += 7
    artY += 7
    fontSize(artX)
    fill(artX/250)
    text("EditFonts", (artX, artY))

# grid(W, H, 140)        # Draw the grid


# TurtleFont ############################
newPage(W, H)

image("images/tf-01.png", (W/3, 0), alpha=1)
# image("images/tf-02.png", (, 0), alpha=1)

# Headline
headlineTxt = FormattedString()
headlineTxt.append("TurtleFont", \
    font="fonts/Epistle-Regular.ttf", \
    fontSize=headlineFontSize, \
    fill=(0), \
    lineHeight=headlineLineHeight)
textBox(headlineTxt, (headlineXPos, headlineYPos, W/2, H), align="left")

    
#art
artX = M-60
artY = M
stroke(0)
fontSize(200)     
font("fonts/Toren-Rotalic.otf")  # Set the font
for i in range(16):
    artX += 7
    artY += 7
    fill(artX/250)
    text("TurtleFont", (artX, artY))

# grid(W, H, 140)        # Draw the grid

# TFont ############################
newPage(W, H)

image("images/TruFont.png", (W/2, 50), alpha=1)
# image("images/mmcharview.png", (W/3, 286), alpha=1)

# Headline
headlineTxt = FormattedString()
headlineTxt.append("tfont", \
    font="fonts/Epistle-Regular.ttf", \
    fontSize=headlineFontSize, \
    fill=(0), \
    lineHeight=headlineLineHeight)
textBox(headlineTxt, (headlineXPos, headlineYPos, W/2, H), align="left")

    
#art
artX = M-60
artY = M
stroke(0)
fontSize(200)     
font("fonts/Toren-Rotalic.otf")  # Set the font
for i in range(16):
    artX += 7
    artY += 7
    fill(artX/250)
    text("tfont", (artX, artY))

# grid(W, H, 140)        # Draw the grid


# Toki #############################################
newPage(W, H)

# image
# image("images/metafont-a.jpg", (0, 0), alpha=0.5)

# Headline
headlineTxt = FormattedString()
headlineTxt.append("toki pona", \
    font="fonts/lp.otf", \
    fontSize=headlineFontSize, \
    fill=(0), \
    lineHeight=headlineLineHeight)
textBox(headlineTxt, (headlineXPos, headlineYPos, W/2, H), align="left")

tokiQuote1 = FormattedString()
tokiQuote1.append('sina sona ala sona e toki pona', \
    font="fonts/lp.otf", \
    fontSize=60, \
    fill=(0), \
    lineHeight=80, \
    firstLineIndent=-25)
textBox(tokiQuote1, (984, -97, 780, 1000), align="left")

# grid(W, H, 140)        # Draw the grid

#art
artX = M
artY = M+30
step = 0
stroke(0)
fontSize(100)     
font("fonts/lp.otf")  # Set the font
for i in range(24):
    artX += 7
    artY += 7
    step += 0.1
    rotate(step)
    fill(artX/250)
    text("sina sona ala sona e toki pona", (artX+M, artY))


saveImage("~/Type/the-history-and-future-of-free-software-font-editors/slides.pdf")
