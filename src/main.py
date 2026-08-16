from textnode import TextNode, TextType


def main():
    test_obj = TextNode(text="This is some test anchor text",text_type=TextType.LINK,url="https://www.boot.dev")
    print(test_obj)

main()