import re
def chage_date_format(dt):
    return re.sub(r'(\d{4})-(\d{2})-(\d{2})', '\\3-\\2-\\1', dt)
dt1 = "2026-01-02"
print(dt1)
print(chage_date_format(dt1))
