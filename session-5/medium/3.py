from bs4 import BeautifulSoup
from IPython import embed
import re


def generate_html():
    return """
        <html>
            <head></head>
            <body>
                <a href="/a.html">A</a>
                <a href="/b.html">B</a>
                <a href="/c.html">C</a>
                <a href="/d.html">D</a>
            </body>

            <script>
                var hello = "yoh";
                var one = 1;
                alert(hello);
            </script>

            <script>
                var two = 2.0;
                var three = "tatlo";
            </script>
        </html>
    """

def main():
    html_doc = generate_html()

    soup = BeautifulSoup(html_doc, "html.parser")
    scripts = soup.find_all("script")
    pattern = "var (.*?) = (.*?);"

    output = {}
    for script in scripts:
        vars = re.findall(pattern, script.get_text())

        for var in vars:
            output[var[0]] = var[1]
    
    print(output)



if __name__ == "__main__":
    main()