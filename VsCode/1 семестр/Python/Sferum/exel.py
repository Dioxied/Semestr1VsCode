import pandas as pd

                # new_data = (f'{sp[0]} {(sp[1])[0]}. {(sp[2])[0]}. {sp[4] if int(sp[4])>10 else "0"+sp[4]}.{mouth if int(mouth)>10 else "0"+ str(mouth)}.{sp[6][-2:]} {sp[7]} \n')
outsovm, outsovw, outnesowm, outnesoww = 'outsovm.xlsx', 'outsovw.xlsx', 'outnesovm.xlsx', 'outnesovw.xlsx'
with open('txt.txt', 'r', encoding='utf-8') as file:
    f = [i.replace('\n', '') for i in file.readlines() if int(i.replace('\n', '')[-7:-3]) < 2024]
    for i in f:
        sp = i.split()
        mou = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля' ,'августа', 'сентября', 'октября', 'ноября', 'декабря']
        if 2024 - int(i[-7:-3]) >= 18:
            if sp[3] == 'м':
                mouth = mou.index(sp[5])+1
                new_data = {'Name': [f"{sp[0]} {(sp[1])[0]}. {(sp[2])[0]}"], 'Age': [f"{sp[4] if int(sp[4])>10 else '0'+sp[4]}.{mouth if int(mouth)>10 else '0'+ str(mouth)}.{sp[6][-2:]} {sp[7]}"]}
                df_new = pd.DataFrame(new_data)
                df_existing = pd.read_excel(outsovm)
                df_combined = df_existing.concat(df_new, ignore_index=True)
                df_combined.to_excel(outsovm, index=False)
            else:
                mouth = mou.index(sp[5])+1
                new_data = {'Name': [f"{sp[0]} {(sp[1])[0]}. {(sp[2])[0]}"], 'Age': [f"{sp[4] if int(sp[4])>10 else '0'+sp[4]}.{mouth if int(mouth)>10 else '0'+ str(mouth)}.{sp[6][-2:]} {sp[7]}"]}
                df_new = pd.DataFrame(new_data)
                df_existing = pd.read_excel(outsovw)
                df_combined = df_existing.concat(df_new, ignore_index=True)
                df_combined.to_excel(outsovw, index=False)
        else:
            if sp[3] == 'м':
                mouth = mou.index(sp[5])+1
                new_data = {'Name': [f"{sp[0]} {(sp[1])[0]}. {(sp[2])[0]}"], 'Age': [f"{sp[4] if int(sp[4])>10 else '0'+sp[4]}.{mouth if int(mouth)>10 else '0'+ str(mouth)}.{sp[6][-2:]} {sp[7]}"]}
                df_new = pd.DataFrame(new_data)
                df_existing = pd.read_excel(outnesowm)
                df_combined = df_existing.concat(df_new, ignore_index=True)
                df_combined.to_excel(outnesowm, index=False)
            else:
                mouth = mou.index(sp[5])+1
                new_data = {'Name': [f"{sp[0]} {(sp[1])[0]}. {(sp[2])[0]}"], 'Age': [f"{sp[4] if int(sp[4])>10 else '0'+sp[4]}.{mouth if int(mouth)>10 else '0'+ str(mouth)}.{sp[6][-2:]} {sp[7]}"]}
                df_new = pd.DataFrame(new_data)
                df_existing = pd.read_excel(outnesoww)
                df_combined = df_existing.concat(df_new, igore_index=True)
                df_combined.to_excel(outnesoww, index=False)
