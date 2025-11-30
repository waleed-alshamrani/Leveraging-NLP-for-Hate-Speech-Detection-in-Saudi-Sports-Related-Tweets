import pandas as pd
from pyarabic.araby import strip_tashkeel, tokenize

# تحميل البيانات
df = pd.read_csv("Dataset_F.csv")

# الكلمات التي نرغب بترشيحها
#keywords = ['كرة', 'كورة', 'مباراة', 'الرياضة', 'اللاعب', 'المنتخب', 'دوري', 'نادي', 'هدف', 'الشوط',"الهلال","فقراوي","طحلبي","خدمي","طاقيه","طاقيه","روشن","كاس","كأس"]
keywords = ["الهلال","فقراوي","طحلبي","خدمي","طاقيه","طاقيه","روشن","نصراوي","اتحادي","هلالي","اهلاوي","الشباب","اتحاد","الاهلي","النصر"]

# دالة مساعدة لترشيح النص: تطبيع + بحث
def contains_keyword_ar(text, keywords):
    if not isinstance(text, str):
        return False
    # حذف التشكيل مثلاً
    norm = strip_tashkeel(text)
    norm = norm.lower()
    for kw in keywords:
        if kw in norm:
            return True
    return False

# تطبيق الترشيح
mask = df['Tweet'].apply(lambda x: contains_keyword_ar(x, keywords))
filtered = df[mask]

# حفظ الناتج
filtered.to_csv("A6.csv", index=False)
