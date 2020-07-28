import pandas as pd

# verilerimizin bulunduğu csv dosyamızı okuduk
df = pd.read_csv('dataset/youtube-ing.csv')

# 1- İlk kayıt:
result = df.head(10)

# 2- İkinci 10 kayıt:
result = df[10:20].head(10)

# 3- Dataset' de bulunan kolan isimlerini ve sayıları:
result = df.columns
result = len(df.columns)

# 4- Aşağıda verilen kolanları silmek ve kalan kolonları:
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
df.drop(['thumbnail_link', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed', 'description',
         'trending_date'], axis=1, inplace=True)
result = df

# 5- Like ve Dislike sayılarının ortalaması:
result = df['likes'].mean()
result = df['dislikes'].mean()

# 6- İlk 100 videonun like ve dislike kolonları:
result = df.head(100)[['title', 'likes', 'dislikes']]

# 7- En çok görüntülenen video:
result = df[df['views'].max() == df['views']]['title'].iloc[0]

# 8- En az görüntülenen video:
result = df[df['views'].min() == df['views']]['title'].iloc[0]

# 9- En çok görüntülenen ilk 10 video:
result = df.sort_values('views', ascending=False)[['title', 'views']].head(10)

# 10- Kategorilere göre beğeni ortalamalarının sıralı hali:
result = df.groupby('category_id').mean().sort_values('likes')['likes']

# 11- Kategoriye göre yorum sayılarını yukarıdan aşağı sıralı hali:
result = df.groupby('category_id').mean().sort_values('comment_count', ascending=False)['comment_count']

# 12- Kategorilerde ki video sayıları:
result = df.groupby('category_id')['video_id'].count()
# ikinci bir yol
result = df['category_id'].value_counts()

# 13- Her videonun başlıklarının uzunluklarını yeni bir kolona yazmak için:
df['title_len'] = df['title'].apply(len)
result = df

# 14- Her bir videoda kullananılan tag sayılarını yeni kolona yazmak için:
df['tag_count'] = df['tags'].apply(lambda x: len(x.split('|')))


# ikinci bir yol
def tagCount(tag):
    return len(tag.split('|'))


df['tag_count'] = df['tags'].apply(tagCount)


# 15- En popüler videolar (like/dislike)

def likedislikeOran(dataset):
    likesList = list(dataset['likes'])  # like sayılarını aldık
    dislikesList = list(dataset['dislikes'])  # dislike sayılarını aldık

    liste = list(zip(likesList, dislikesList))  # (like,dislike), (like,dislike)

    oranListe = []

    for like, dislike in liste:
        if (like + dislike) == 0: # video like ve dislike almamşışsa 0 atandı
            oranListe.append(0)
        else:
            oranListe.append(like / (like + dislike)) # oran hesaplandı

    return oranListe


df['like_rate'] = likedislikeOran(df) # oranın gösterileceği kolon açıldı ve veriler gönderildi
print(df.sort_values('like_rate', ascending=False)[['title','likes','dislikes','like_rate']])

print(result)
