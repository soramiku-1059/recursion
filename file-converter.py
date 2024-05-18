import markdown
import sys

if len(sys.argv) == 4:
    if sys.argv[1] == "markdown":
        with open(sys.argv[2]) as f:
            md = f.read()      
        html = markdown.markdown(md)

        with open(sys.argv[3],'w') as f:
            f.write(html)


        

