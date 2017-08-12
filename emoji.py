import sys
import os

#========== vars
svg = 'emoji.svg'
html = 'emoji.html'

#========== functions
def curve(v):
    outer = 135 - v * 20
    inner = 135 + v * 20
    outer = int(outer)
    inner = int(inner)
    return str(outer), str(inner)

def color(v):
    if v == 1:
        col = "0,255,0"
    elif v == -1:
        col = "255,0,0"
    elif v > 0:
        val = 255 - (v*240)
        val = int(val)
        col = str(val) + ",255,0"
    elif v < 0:
        val = 255 + (v*240)
        val = int(val)
        col = "255," + str(val) + ",0"
    else:
        col = "255,255,0"
    return col

def writeSVG(outer, inner, col):
    with open( svg, 'w+' ) as s:
        fil = ('''<svg height="200" width="400">
  <defs>
    <linearGradient id="color">
      <stop style="stop-color:rgb(''' + col + ''')" />
    </linearGradient>
  </defs>
  <circle cx="100" cy="100" r="80" stroke="black" stroke-width="5" fill="url(#color)" />;
  <circle cx="130" cy="80" r="6" stroke="black" stroke-width="5" fill="url(#color)" />;
  <circle cx="70" cy="80" r="6" stroke="black" stroke-width="5" fill="url(#color)" />;

  <!-- path -->
  <path d="M 60,''' + outer + ''' C80,''' + inner + ''' 120,'''+ inner + ''' 140,''' + outer + '''" stroke="black" stroke-width="5" fill="none" />

  <!-- happy range
  <path d="M 60,115 C80,155 120,155 140,115" stroke="black" stroke-width="5" fill="none" /> -->

  <!-- unhappy range
  <path d="M 60,155 C80,115 120,115 140,155" stroke="black" stroke-width="5" fill="none" /> -->
</svg>''')
        s.write(fil)
        s.close()


def writeHtml():
    head = writeHead()
    body = writeBody()
    tail = writeTail()

def writeHead():
    with open( html, 'w+' ) as h:
        h.write('''<!DOCTYPE html>
<html>
<body>
''')
        h.close()

def writeBody():
    with open( svg, 'r') as s:
        data=s.read().replace('\n', '')
        with open( html, 'a' ) as b:
            b.write(data)
        b.close()

def writeTail():
    with open( html, 'a' ) as t:
        t.write('''</body>
</html>
''')
        t.close()

#=========== start main
if __name__ == '__main__':

    v = sys.argv[1]
    v = float(v)

    if (v > 1) or (v < -1):
        print("Numerical value out of bounds, need value -1 to 1")
        exit
    else:
        print("Writing SVG with value = " + str(v))

    # This code writes the SVG:
    outer, inner = curve(v)
    col = color(v)
    svgout = writeSVG(outer, inner, col)

    # Uncomment write HTML wrapper on svg
    htmlout = writeHtml()

