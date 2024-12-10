from bs4 import BeautifulSoup


def clean_html(html_string: str) -> str:
    def remove_malicious_tags_and_attributes(html: str) -> str:
        soup = BeautifulSoup(html, "html.parser")
        for tag in soup(["script", "iframe", "embed", "object", "link", "meta", "style"]):
            tag.decompose()

        for tag in soup.find_all(True):
            for attribute in ["onerror", "onclick", "onload", "style", "srcdoc", "href", "src"]:
                if attribute in tag.attrs:
                    del tag.attrs[attribute]

        return str(soup)

    cleaned_html = html_string
    previous_html = ""

    # Повторяем очистку до стабилизации
    while cleaned_html != previous_html:
        previous_html = cleaned_html
        cleaned_html = remove_malicious_tags_and_attributes(cleaned_html)
    return cleaned_html


example_html = input()

cleaned_html = clean_html(example_html)
print(cleaned_html)
