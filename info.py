import re
def func(text):
    name_pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
    money_pattern = r'\b\d+(?:,\d{3})*(?:\.\d+)?\s*(rupees|USD|EUR|INR|€|$)\b'
    need_keywords = ['service','consultation','assistance','help','project management','tasks','support']
    names = re.findall(name_pattern,text)
    amounts_paid = re.findall(money_pattern,text)
    needs = []
    for keyword in need_keywords:
        if keyword in text.lower():
            needs.append(f"Need for {keyword}")
    return {
        "Names":" ".join(names),
        "Amounts Paid":" ".join(amounts_paid),
        "Needs":"\n".join(needs)
    }



 
