from bs4 import BeautifulSoup
from IPython import embed


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
        </html>
    """

def main():
    html_doc = generate_html()
    embed()

    # soup = BeautifulSoup(html_doc, "html.parser")
    # a_elements = soup.find_all("a", href=True)

    # for a_element in a_elements:
    #     print(a_element['href'])

    # [a_element['href'] for a_element in BeautifulSoup(html_doc, "html.parser").find_all("a", href=True)]


if __name__ == "__main__":
    main()