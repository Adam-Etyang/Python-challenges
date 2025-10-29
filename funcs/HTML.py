def tag(name, *content, class_=None, **attrs):
    """Generste one or more HTML tags"""
    if class_ is not None:
        attrs["class"] = class_
    attr_pairs = (f' {attr}="{value}"' for attr, value in sorted(attrs.items()))
    attr_str = "".join(attr_pairs)
    if content:
        elements = (f"<{name}{attr_str}>{c}</{name}>" for c in content)
        return "\n".join(elements)
    else:
        return f"<{name}{attr_str}/>"


if __name__ == "__main__":
    print(tag("br"))
    print(tag("p", "hello world", id=33))
    my_tag = {
        "name": "img",
        "title": "Sunset Boulevard",
        "src": "sunset.jpg",
        "class": "framed",
    }
    print(tag(**my_tag))
