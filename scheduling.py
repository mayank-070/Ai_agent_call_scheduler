import spacy
import re
from datetime import datetime
import dateparser

nlp = spacy.load("en_core_web_sm")


def extract_datetime(text):
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "DATE":  
            date_text = ent.text

            parsed_date = dateparser.parse(date_text)
            
            if parsed_date:
              
                month = parsed_date.strftime("%B")
                day = parsed_date.day
                time = parsed_date.strftime("%H:%M") if parsed_date.hour or parsed_date.minute else None
                return {"month": month, "day": day, "time": time, "raw_date": parsed_date}
    
    print("No valid date parsed.")  
