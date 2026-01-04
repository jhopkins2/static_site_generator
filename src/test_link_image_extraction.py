import unittest
from inline_functions import extract_markdown_links, extract_markdown_images

class TestExtraction(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
                "This is text with an ![image](https://www.boot.dev/boots.jpg)"
                )
        self.assertEqual([("image","https://www.boot.dev/boots.jpg")], matches)

    def test_extract_multiple_markdown_images(self):
        matches = extract_markdown_images(
                "This is text with an ![image](https://www.boot.dev/boots.jpg) and ![blarg](test.jpg)"
                )
        self.assertEqual([("image","https://www.boot.dev/boots.jpg"), ("blarg", "test.jpg")], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
                "This is text with a link [i'm a link](https://www.boot.dev)"
                )
        self.assertEqual([("i'm a link", "https://www.boot.dev")], matches)

    def test_extract_multiple_markdown_links(self):
        matches = extract_markdown_links(
                "This is text with a link [i'm a link](https://www.boot.dev) and [blarg](http://8.8.8.8)"
                )
        self.assertEqual([("i'm a link", "https://www.boot.dev"), ("blarg", "http://8.8.8.8")], matches)

    def test_extract_markdown_link_with_images(self):
        matches = extract_markdown_links(
                "This is text with a link [i'm a link](https://www.boot.dev) and ![image](https://www.boot.dev/boots.jpg)"
                )
        self.assertEqual([("i'm a link", "https://www.boot.dev")], matches)

    def test_extract_markdown_images_with_links(self):
        matches = extract_markdown_images(
                "This is text with an ![image](https://www.boot.dev/boots.jpg) and [blarg](test.jpg)"
                )
        self.assertEqual([("image","https://www.boot.dev/boots.jpg")], matches)


if __name__ == "__main__":
    unittest.main()
