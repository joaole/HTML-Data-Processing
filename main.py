from get_html_information import html_to_dataframe
from hmtl_c import html_c
from remove_special_characters import remove_special_characters
import pandas as pd 
from keywords import keywords
from save_to_excel import save_to_excel

def keywords_filter(df, keywords):
    pattern = '|'.join(keywords)
    return df[df['Descrição'].str.contains(pattern, case=False, na=False)]

df_bruta = html_to_dataframe(html_content=html_c)

df_bruta = df_bruta.map(remove_special_characters)
df_tratada = keywords_filter(df_bruta, keywords)

save_to_excel(df_bruta, 'Licitações_completas.xlsx')
save_to_excel(df_tratada, 'Licitações_filtradas.xlsx')
