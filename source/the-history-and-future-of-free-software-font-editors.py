# Render this specimen with DrawBot3: http://www.drawbot.com/

# Import modules:
import math

#Import pages
# import

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

# Page loop
varWght = 400
stepUp = 0
stepDown = 0
for frame in range(4):
    newPage(W, H)
    fill(0)           # Background color
    rect(0, 0, W, H)  # Draw the background

    # Draw the grid
    # grid(32)
    font("fonts/amiri/Amiri-Bold.ttf")
    # Basic Style
    stroke(None)
    fill(1)
    fontSize(160)
    # Draw specimen
    # lineHeight(32*4)
    lh = 32*5
    text("The History and Future", (M, (H-(88))-(1*lh)), align="left")
    text("of Free Software", (M, (H-(88))-(2*lh)), align="left")
    text("Font Editors", (M, (H-(88))-(3*lh)), align="left")
    # text("Font Editors", (W/2, (896)-(4*lh)), align="center")
    
    fill(1,0,0)
    oval(W-(M*2), M, M, M)

# Save PDF
#saveImage("the-history-and-future-of-free-software-font-editors.pdf")