import json

SITE_DATA = {
    "url": "https://intl-ssl-hth.com",
    "keywords": ["hth", "sports", "entertainment", "live", "casino"],
    "tags": ["hth", "betting", "online", "platform"],
    "description": "hth is an international online sports and casino platform providing diverse entertainment options."
}

def load_site_data():
    return SITE_DATA

def extract_keywords(data):
    return data.get("keywords", [])

def extract_url(data):
    return data.get("url", "")

def extract_tags(data):
    return data.get("tags", [])

def extract_description(data):
    return data.get("description", "")

def format_summary(data):
    url = extract_url(data)
    keywords = extract_keywords(data)
    tags = extract_tags(data)
    description = extract_description(data)

    lines = []
    lines.append("Site Summary")
    lines.append("=" * 40)
    lines.append(f"URL: {url}")
    lines.append(f"Keywords: {', '.join(keywords)}")
    lines.append(f"Tags: {', '.join(tags)}")
    lines.append(f"Description: {description}")
    lines.append("=" * 40)
    return "\n".join(lines)

def generate_structured_summary(data):
    return {
        "url": extract_url(data),
        "keyword_list": extract_keywords(data),
        "tag_list": extract_tags(data),
        "description": extract_description(data)
    }

def print_structured_summary(structured):
    print(json.dumps(structured, indent=2, ensure_ascii=False))

def main():
    site_data = load_site_data()
    summary_text = format_summary(site_data)
    print(summary_text)
    print()
    structured = generate_structured_summary(site_data)
    print("Structured JSON:")
    print_structured_summary(structured)

if __name__ == "__main__":
    main()