# Render this specimen with DrawBot3: http://www.drawbot.com/

# Import modules:
import math

#Import pages
import pages.page001

# Basic variables  (width, height, ):
W, H, M, F = 1920, 1080, 128, 32

# Load font and print font info:
# print(installedFonts(supportsCharacters=None))
font("fonts/amiri/Amiri-Bold.ttf")


# Draw a grid from a given increment:
def grid(inc):

    stpX, stpY = 0, 0  # Step in sequence on x axis
    incX, incY = inc, inc  # Grid increment
    
    stroke(0.6, 0, 0)  # Set grid line color RED
    for x in range(int(((W-(M*2))/inc+1 ))):
        polygon((M+stpX, M), (M+stpX, H-(M-8)))
        stpX += incX  # Set position for next gridline

    stroke(0, 0, 0.6)  # Set grid line color BLUE      
    for y in range(int(((H-(M*2))/inc)+2)):
        polygon((M, M+stpY), (W-M, M+stpY))
        stpY += incY  # Set position for next gridline


# Title Page #####################################################
newPage(W, H)
fill(0)           # Set the background color
rect(0, 0, W, H)  # Draw the background
# grid(32)        # Draw the grid
font("fonts/Epistle-Regular.ttf")  # Set the font

# Basic Style
stroke(None)
fill(1)
fontSize(150)
lh = 32*5

# Headline
text("The History and Future", (M, (H-(88))-(1*lh)), align="left")
text("of Free Software", (M, (H-(88))-(2*lh)), align="left")
text("Font Editors", (M, (H-(88))-(3*lh)), align="left")

# Shapes
fill(1,0,0)
polygon((W-(M*4), M), (W-(M*3), M), (W-(M*3.5), M*2), close=True)
fill(1,1,0)
rect(W-(M*3), M, M, M)
fill(0,0,1)
oval(W-(M*2), M-8, M+16, M+16)

# fontForge Page ######################################################### 
newPage(W, H)
fill(0)           # Set the background color
rect(0, 0, W, H)  # Draw the background
grid(32)        # Draw the grid
font("fonts/Epistle-Regular.ttf")  # Set the font

# Basic Style
stroke(None)
fill(1)
fontSize(150)
lh = 32*5

# Headline
text("FontForge", (M, (H-(88))-(1*lh)), align="left")

# FontForge Page ######################################################### 
newPage(W, H)
fill(0)           # Set the background color
rect(0, 0, W, H)  # Draw the background
# grid(32)        # Draw the grid
font("fonts/Epistle-Regular.ttf")  # Set the font

# Basic Style
stroke(None)
fill(1)
fontSize(150)
lh = 32*5

# Headline
text("FontForge", (M, (H-(88))-(1*lh)), align="left")


# FontForge Page ######################################################### 
newPage(W, H)
fill(0)           # Set the background color
rect(0, 0, W, H)  # Draw the background
# grid(32)        # Draw the grid
font("fonts/Epistle-Regular.ttf")  # Set the font

# Basic Style
stroke(None)
fill(1)
fontSize(150)
lh = 32*5

# Headline
text("TruFont", (M, (H-(88))-(1*lh)), align="left")

# TurtleFont Page ######################################################### 
newPage(W, H)
fill(0)           # Set the background color
rect(0, 0, W, H)  # Draw the background
# grid(32)        # Draw the grid
font("fonts/Epistle-Regular.ttf")  # Set the font

# Basic Style
stroke(None)
fill(1)
fontSize(150)
lh = 32*5

# Headline
text("TurtleFont", (M, (H-(88))-(1*lh)), align="left")


# Save PDF
saveImage("the-history-and-future-of-free-software-font-editors.pdf")
