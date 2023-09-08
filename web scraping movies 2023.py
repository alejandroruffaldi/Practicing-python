import pandas as pd
import bs4 as soup
import requests
import sqlite3

def extract_movie_data(url):
    info = requests.get(url)
    data = soup.BeautifulSoup(info.text, 'html.parser')

    titles = [i.text for i in data.find_all('h2')]

    fecha_estreno_tags = data.find_all('p', class_='css-aeyldl et3p2gv0')
    fechas_de_estreno = []
    for tag in fecha_estreno_tags:
        fecha_text = tag.get_text(strip=True)
        if "Fecha de estreno:" in fecha_text:
            fecha = fecha_text.replace("Fecha de estreno:", "").strip()
            fechas_de_estreno.append(fecha)

    min_length = min(len(titles), len(fechas_de_estreno))

    df = pd.DataFrame({'Titles': titles[:min_length], 'Release date': fechas_de_estreno[:min_length]})

    return df

url = 'https://www.fotogramas.es/noticias-cine/g40497441/mejores-peliculas-2023/'
df = extract_movie_data(url)

# Create a SQLite database and store the DataFrame in it
peliculasestrenos2023 = sqlite3.connect('Peliculas2023.db')
df.to_sql('MOVIES2023', peliculasestrenos2023, if_exists='replace', index=False)
peliculasestrenos2023.commit()

c = peliculasestrenos2023.cursor()
c.execute('SELECT * FROM MOVIES2023')

for row in c.fetchall():
    print(row)
peliculasestrenos2023.close()




