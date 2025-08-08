with open('txt.txt', 'r', encoding='utf-8') as file:
    f = [i.replace('\n', '') for i in file.readlines() if int(i.replace('\n', '')[-7:-3]) < 2024]
    with open('nesovM.txt', 'a', encoding='utf-8') as nesovM:
        with open('nesovW.txt', 'a', encoding='utf-8') as nesovW:
            with open('sovM.txt', 'a', encoding='utf-8') as sovM:
                with open('sovW.txt', 'a', encoding='utf-8') as sovW:
                    for i in f:
                        sp = i.split()
                        mou = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля' ,'августа', 'сентября', 'октября', 'ноября', 'декабря']
                        if 2024 - int(i[-7:-3]) >= 18:
                            if sp[3] == 'м':
                                mouth = mou.index(sp[5])+1
                                sovM.write(f'{sp[0]} {(sp[1])[0]}. {(sp[2])[0]}. {sp[4] if int(sp[4])>10 else "0"+sp[4]}.{mouth if int(mouth)>10 else "0"+ str(mouth)}.{sp[6][-2:]} {sp[7]} \n')
                            else:
                                mouth = mou.index(sp[5])+1
                                sovW.write(f'{sp[0]} {(sp[1])[0]}. {(sp[2])[0]}. {sp[4] if int(sp[4])>10 else "0"+sp[4]}.{mouth if int(mouth)>10 else "0"+ str(mouth)}.{sp[6][-2:]} {sp[7]} \n')

                        else:
                            if sp[3] == 'м':
                                mouth = mou.index(sp[5])+1
                                nesovM.write(f'{sp[0]} {(sp[1])[0]}. {(sp[2])[0]}. {sp[4] if int(sp[4])>10 else "0"+sp[4]}.{mouth if int(mouth)>10 else "0"+ str(mouth)}.{sp[6][-2:]} {sp[7]} \n')
                            else:
                                mouth = mou.index(sp[5])+1
                                nesovW.write(f'{sp[0]} {(sp[1])[0]}. {(sp[2])[0]}. {sp[4] if int(sp[4])>10 else "0"+sp[4]}.{mouth if int(mouth)>10 else "0"+ str(mouth)}.{sp[6][-2:]} {sp[7]} \n')
