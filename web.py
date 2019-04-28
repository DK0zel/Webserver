from flask import Flask

app = Flask(__name__)

k = False
mech = False

@app.route('/')
def index():
    return '''<<!DOCTYPE html>
    <html>
     <head>
      <meta charset="utf-8">
      <title>Переключатели</title>
     </head>
     <body>
    
       <p><b>Идя домой, вы случайно</b></p>
<p><b>Запнулись и упали в яму</b></p>
<div class = "video">
<iframe width="560" height="315" src="https://www.youtube.com/embed/kWTwbLyRgng?start=22" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
       </div>
             <form action="start">
        <p><input type="submit" value="">Начать лабиринт</p>
      </form> 
                   <form action="music">
        <p><input type="submit" value="">музыка для игры</p>
      </form> 
     </body>
    </html>''' 
@app.route('/music')
def music():
    return '''<<!DOCTYPE html>
        <html>
         <head>
          <meta charset="utf-8">
          <title>Переключатели</title>
         </head>
         <body>
 <div class = "audio">
            <iframe frameborder="0" style="border:none;width:600px;height:100px;" 
            width="600" height="100" 
            src="https://music.yandex.ru/iframe/#track/481532/70353/">
            Слушайте <a href='https://music.yandex.ru/album/70353/track/481532'>
            I Got 5 On It (Feat. Michael Marshall)</a> — <a href='https://music.yandex.ru/artist/36706'>
            Luniz</a> на Яндекс.Музыке</iframe>
        </div>
         </body>
        </html>'''     
@app.route('/start')
def start():
    return '''<<!DOCTYPE html>
    <html>
     <head>
      <meta charset="utf-8">
      <title>Переключатели</title>
     </head>
     <body>
      <form action="at1">
       <p><b>ВЫ ПРОСНУЛИСЬ В НЕПОНЯТНОМ МЕСТЕ.
ВЫ ВИДИТЕ ТАБЛИЧКУ "ВЫ В ЛАБИРИНТЕ.
ДВЕ ДВЕРИ НЕ ПРОПУСТЯТ ОДНОГО ЧЕЛОВЕКА,
ЛИШЬ ОДНА ДВЕРЬ НЕ ОПАСНА.
КАКУЮ ДВЕРЬ ВЫ ВЫБИРЕТЕ:ПЕРВУЮ ИЛИ ВТОРУЮ? (1/2)</b></p>
        <p><input type="submit" value="">Первая</p>
      </form> 
      <form action="at2">
        <p><input type="submit" value="">Вторая</p>
      </form> 
     </body>
    </html>'''


@app.route('/at1')


def at1():
    return '''<<!DOCTYPE html>
    <html>
     <head>
      <meta charset="utf-8">
      <title>Переключатели</title>
     </head>
     <body>
      <form action="at11">
       <p><b>ТЫ ПРОИГРАЛ, ТЫ НЕ СМОГ, ТЫ НЕ ВЫЙДЕШЬ ОТСЮДА
(на вас выскочил демон).
Вы пробуете уклонится от удара демона (прыжки с помощью < или >)</b></p>
        <p><input type="submit" value="<"></p>
      </form> 
            <form action="at101">
            <p><input type="submit" value=">"></p>
      </form> 
     </body>
    </html>'''  


@app.route('/at11')
def at11():
    return '''<<!DOCTYPE html>
    <html>
     <head>
      <meta charset="utf-8">
      <title>Переключатели</title>
     </head>
     <body>
      <form action="at101">
       <p><b>ВЫ смогли увернутся.
ДЕМОН жадно смотрит за вами</b></p>
        <p><input type="submit" value="<"></p>
      </form> 
            <form action="at12">
            <p><input type="submit" value=">"></p>
      </form> 
     </body>
    </html>'''


@app.route('/at12')
def at12():
    return '''<<!DOCTYPE html>
    <html>
     <head>
      <meta charset="utf-8">
      <title>Переключатели</title>
     </head>
     <body>
      <form action="at101">
       <p><b>ВЫ смогли увернутся.
ДЕМОН жадно смотрит за вами</b></p>
        <p><input type="submit" value="<"></p>
      </form> 
            <form action="at13">
            <p><input type="submit" value=">"></p>
      </form> 
     </body>
    </html>'''  

@app.route('/at13')
def at13():
    return '''<<!DOCTYPE html>
    <html>
     <head>
      <meta charset="utf-8">
      <title>Переключатели</title>
     </head>
     <body>
      <form action="at111">
       <p><b>ВЫ смогли увернутся.
Вы бьете демона и он рассыпается в прах, зачем его нужно было бояться?
ВЫ ВИДЕЛИ КАК ЧТО-ТО БЛЕСНУЛО В ПРАХЕ.
ОБЫСКАТЬ ПРАХ? (да/нет)</b></p>
        <p><input type="submit" value="ДА"></p>
      </form> 
            <form action="at121">
            <p><input type="submit" value="НЕТ"></p>
      </form> 
     </body>
    </html>''' 
@app.route('/at101')
def at101():
    return '''<<!DOCTYPE html>
    <html>
     <head>
      <meta charset="utf-8">
      <title>Переключатели</title>
     </head>
     <body>
       <p><b>Вы Проиграли :(
       Утешительный приз: </b></p>
             <div class = "video">
       <iframe width="560" height="315" src="https://www.youtube.com/embed/umDr0mPuyQc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
       </div>
     </body>
    </html>'''
@app.route('/at102')
def at102():
    return '''<<!DOCTYPE html>
    <html>
     <head>
      <meta charset="utf-8">
      <title>Переключатели</title>
     </head>
     <body>
       <p><b>Вы Проиграли :( Вам воткнули когти в спину
       Утешительный приз: </b></p>
                    <div class = "video">
       <iframe width="560" height="315" src="https://www.youtube.com/embed/umDr0mPuyQc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
       </div>
     </body>
    </html>''' 
@app.route('/at111')
def at111():
    global k
    k = True
    return '''<<!DOCTYPE html>
     <html>
      <head>
       <meta charset="utf-8">
       <title>Переключатели</title>
      </head>
      <body>
       <form action="at14">
        <p><b>ВЫ ПОДОБРАЛИ КРЕСТИК</b></p>
<p><b>идем дальше?(да/нет)</b></p>
         <p><input type="submit" value="ДА"></p>
       </form> 
             <form action="start">
             <p><input type="submit" value="НЕТ"></p>
       </form> 
      </body>
     </html>'''
@app.route('/at121')
def at121():
    return '''<<!DOCTYPE html>
     <html>
      <head>
       <meta charset="utf-8">
       <title>Переключатели</title>
      </head>
      <body>
       <form action="at14">
<p><b>идем дальше?(да/нет)</b></p>
         <p><input type="submit" value="ДА"></p>
       </form> 
             <form action="start">
             <p><input type="submit" value="НЕТ"></p>
       </form> 
      </body>
     </html>'''  

@app.route('/at14')
def at14():
    return '''<<!DOCTYPE html>
     <html>
      <head>
       <meta charset="utf-8">
       <title>Переключатели</title>
      </head>
      <body>
       <form action="at15">
<p><b>ВЫ ЧУВСВУЕТЕ КАК ВЫ ПРОХОДИТЕ СКВОЗЬ САМО ВРЕМЯ ВО ТЬМЕ, ВОЗДУХ НЕ ДВИГАЕТСЯ,
ВДРУГ ВЫ ЧУВСТВУЕТЕ КАК "ЧТО-ТО" ОХОТИТСЯ ЗА ВАМИ.
ПЕРЕД ВАМИ ДВА ВЫБОРА:ИДТИ ТИХО ИЛИ ПОБЕЖАТЬ СО ВСЕХ НОГ? (бежать/идти)</b></p>
         <p><input type="submit" value="бежать"></p>
       </form> 
             <form action="at102">
             <p><input type="submit" value="идти"></p>
       </form> 
      </body>
     </html>''' 
@app.route('/at15')
def at15():
    return '''<<!DOCTYPE html>
     <html>
      <head>
       <meta charset="utf-8">
       <title>Переключатели</title>
      </head>
      <body>
       <form action="at16">
<p><b>ВЫ ПОБЕЖАЛИ, СУЩЕСТВО ОТСТАЛО ОТ ВАС.
ПЕРЕД ВАМИ МЕЧ В КАМНЕ.ПОПРОБОВАТЬ ЕГО ДОСТАТЬ?(да/нет)</b></p>
         <p><input type="submit" value="да"></p>
       </form> 
             <form action="start">
             <p><input type="submit" value="нет"></p>
       </form> 
      </body>
     </html>'''
@app.route('/at16')
def at16():
    return '''<<!DOCTYPE html>
     <html>
      <head>
       <meta charset="utf-8">
       <title>Переключатели</title>
      </head>
      <body>
       <form action="mech">
<p><b>ВАС ТЯНЕТ В ДРУГОЕ ИЗМЕРЕНИЕ.ОСТАТЬСЯ? (да/нет)</b></p>
         <p><input type="submit" value="да"></p>
       </form> 
             <form action="at17">
                 <p><input type="submit" value="нет"></p>
       </form> 
      </body>
     </html>'''
@app.route('/at17')
def at17():
    return '''<<!DOCTYPE html>
     <html>
      <head>
       <meta charset="utf-8">
       <title>Переключатели</title>
      </head>
      <body>
       <form action="kon1">
<p><b>ВЫ ВЫТЯНУЛИ МЕЧ, МИР ВОКРУГ МЕНЯЕТСЯ....
ВЫ ОКАЗАЛИСЬ В СРЕДНЕВЕКОВОМ ГОРОДЕ,
НА ВАС БЕГУТ ЛЮДИ БЕЗ ОРУЖИЯ. ЗАЩИЩАТЬСЯ?(да/нет)</b></p>
         <p><input type="submit" value="да"></p>
       </form> 
             <form action="kon2">
                 <p><input type="submit" value="нет"></p>
       </form> 
      </body>
     </html>'''
@app.route('/kon1')
def kon1():
    return '''<<!DOCTYPE html>
     <html>
      <head>
       <meta charset="utf-8">
       <title>Переключатели</title>
      </head>
      <body>
<p><b> ВЫ УБИЛИ МИРНЫХ ЛЮДЕЙ.
ВЫ ВЫИГРАЛИ, НО ВАШЕ ИМЯ БУДЕТ ПОКРЫТО КРОВЬЮ ВО ВЕКИ ВЕКОВ</b></p>
       </form> 
      </body>
     </html>'''
@app.route('/kon2')
def kon2():
    return '''<<!DOCTYPE html>
     <html>
      <head>
       <meta charset="utf-8">
       <title>Переключатели</title>
      </head>
      <body>
<p><b> ВЫ СТАЛИ КОРОЛЕМ
ВЫ ВЫИГРАЛИ, ВЫ БУДЕТЕ ПРАВИТЬ ЭТИМИ МИРНЫМИ ЛЮДЬМИ,
НЕ ЗНАЯ ИХ ЯЗЫКА</b></p><div class = "video">

       </form>
       <div class = "video">
       <iframe width="560" height="315" src="https://www.youtube.com/embed/n-DUQ--5wF4?start=188" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
       </div>
      </body>
     </html>'''
@app.route('/mech')
def mech():
    global mech
    mech = True
    return '''<<!DOCTYPE html>
    <html>
     <head>
      <meta charset="utf-8">
      <title>Переключатели</title>
     </head>
     <body>
      <form action="at1">
       <p><b>ВЫ ПРОСНУЛИСЬ В НЕПОНЯТНОМ МЕСТЕ.
ВЫ ВИДИТЕ ТАБЛИЧКУ "ВЫ В ЛАБИРИНТЕ.
ДВЕ ДВЕРИ НЕ ПРОПУСТЯТ ОДНОГО ЧЕЛОВЕКА,
ЛИШЬ ОДНА ДВЕРЬ НЕ ОПАСНА.
КАКУЮ ДВЕРЬ ВЫ ВЫБИРЕТЕ:ПЕРВУЮ ИЛИ ВТОРУЮ? 
МЕЧ ОСТАЛСЯ У ВАС В РУКАХ(1/2)</b></p>
<p><input type="submit" value="">Первая</p>
      </form> 
      <form action="at2">
        <p><input type="submit" value="">Вторая</p>
      </form> 
     </body>
    </html>'''
@app.route('/at2')
def at2():
    return '''<<!DOCTYPE html>
    <html>
     <head>
      <meta charset="utf-8">
      <title>Переключатели</title>
     </head>
     <body>
      <form action="at21">
       <p><b>ДВЕРЬ С ГРОХОТОМ ЗАХЛАПЫВАЕТСЯ ЗА ВАМИ.
ВЫ ВИДЕТЕ ДВА МОСТА.
ДВЕ СУДЬБЫ: ЖИЗНЬ И СМЕРТЬ.
ПРАВАЯ ИЛИ ЛЕВАЯ? (</>)</b></p>
        <p><input type="submit" value="<"></p>
      </form> 
            <form action="at2001">
        <p><input type="submit" value=">"></p>
      </form> 
     </body>
    </html>''' 
@app.route('/at21')
def at21():
    return '''<<!DOCTYPE html>
    <html>
     <head>
      <meta charset="utf-8">
      <title>Переключатели</title>
     </head>
     <body>
      <form action="at51">
       <p><b>МОСТ ТРЕЩИТ, НО ВЫ ПРОХОДИТЕ НА ДРУГУЮ СТОРОНУ.
ПЕРЕД ВАМИ ДВЕ ЯМЫ: ИЗ ОДНОЙ ПАХНЕТ ТАБАКОМ (левая)
Левая или правая? или пойдем назад? (</>/назад)</b></p>
        <p><input type="submit" value="<"></p>
      </form> 
            <form action="at52">
        <p><input type="submit" value=">"></p>
      </form> 
                  <form action="at53">
        <p><input type="submit" value="">назад</p>
      </form> 
     </body>
    </html>'''     
@app.route('/at53')
def at53():
    return '''<<!DOCTYPE html>
    <html>
     <head>
      <meta charset="utf-8">
      <title>Переключатели</title>
     </head>
     <body>
    
       <p><b>Вы упали в трубу.Вас сьел Гумба</b></p>
     </body>
    </html>'''
@app.route('/at52')
def at52():
    return '''<<!DOCTYPE html>
    <html>
     <head>
      <meta charset="utf-8">
      <title>Переключатели</title>
     </head>
     <body>
    
       <p><b>Вы победили, вас вывел Агасфер из лабиринта Агасфер</b></p>
       <p><b>Вы проснулись на кровати у себя дома</b></p>
                    <div class = "video">
       <iframe width="560" height="315" src="https://www.youtube.com/embed/2JzF07PPUYg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
       </div>
     </body>
    </html>''' 
@app.route('/at51')
def at51():
    return '''<<!DOCTYPE html>
    <html>
     <head>
      <meta charset="utf-8">
      <title>Переключатели</title>
     </head>
     <body>
    
       <p><b>Вы нашли золото, но на нем спит дракон</b></p>
       <p><b>Вы боитесь его тронуть и уходите.</b></p>
       <p><b>Скоро обновление</b></p>
       <div class = "video">
       <iframe width="560" height="315" src="https://www.youtube.com/embed/2JzF07PPUYg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
       </div>
     </body>
    </html>''' 
@app.route('/at2001')
def at2001():
    return '''<<!DOCTYPE html>
    <html>
     <head>
      <meta charset="utf-8">
      <title>Переключатели</title>
     </head>
     <body>
      <form action="at34">
       <p><b>Но каким то неведомым образом вас относит в начальную комнату.
и снова таже табличка "ВЫ В ЛАБИРИНТЕ.
ДВЕ ДВЕРИ НЕ ПРОПУСТЯТ ОДНОГО ЧЕЛОВЕКА,
ЛИШЬ ОДНА ДВЕРЬ НЕ ОПАСНА.
КАКУЮ ДВЕРЬ ВЫ ВЫБИРЕТЕ:ПЕРВУЮ ИЛИ ВТОРУЮ?
КУДА ВЫ ПОЙДЕТЕ:В ПЕРВУЮ, ВО ВТОРУЮ ИЛИ В ТРЕТЬЮ ДВЕРЬ??? (1/2/3)</b></p>
        <p><input type="submit" value="">1</p>
      </form> 
            <form action="at33">
        <p><input type="submit" value="">2</p>
      </form> 
                  <form action="at32">
        <p><input type="submit" value="">3</p>
      </form> 
     </body>
    </html>''' 
@app.route('/at32')
def at32():
    return '''<<!DOCTYPE html>
    <html>
     <head>
      <meta charset="utf-8">
      <title>Переключатели</title>
     </head>
     <body>
    
       <p><b>ЗА ДВЕРЬЮ ВАС ЖДАЛА СМЕРТЬ...
НО ЧУДЕСНЫМ ОБРАЗОМ (И РАССТВОРЕНИЕМ КРЕСТИКА) ВЫ ПРОХОДИТЕ СКВОЗЬ КОЛОДЕЦ С ШИПАМИ.
В СЛЕДУЩЕЙ КОМНАТЕ ВАС ЖДЕТ ЛИШЬ ПОГИБЕЛЬ (НАДПИСЬ НА ТАБЛИЧКЕ).
ИДЕМ ДАЛЬШЕ! (ПОДУМАЛИ ВЫ И ШАГНУЛИ ВО ТЬМУ).
ВЫ ОЧНУЛИСЬ В КОМНАТЕ СИДЯ НА КРАСНОМ КОЖАНОМ КРЕСЛЕ, ПЕРЕД ВАМИ СИДИТ ЧЕЛОВЕК В ЧЕРНЫХ ОЧКАХ.
ОН ПРЕДЛАГАЕТ ВАМ ДВЕ ТАБЛЕТКИ:
СИНИЮ И КРАСНУЮ
КАКУЮ ВЫ ВЫБЕРЕТЕ? В следующем обновлении</b></p>
<div class = "video">
            <iframe width="560" height="315" src="https://www.youtube.com/embed/o6AqKthOuC0?start=23" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
     </body>
    </html>''' 
@app.route('/at33')
def at33():
    return '''<<!DOCTYPE html>
    <html>
     <head>
      <meta charset="utf-8">
      <title>Переключатели</title>
     </head>
     <body>
    
       <p><b>Вы попали в червоточину и вас выкинуло обратно в реальный мир</b></p>
<p><b>Вы очнулись возле компьютера...</b></p>
<p><b>Нужно больше спать по ночам, а не отсыпаться перед компом.</b></p>
<div class = "video">
       <iframe width="560" height="315" src="https://www.youtube.com/embed/2JzF07PPUYg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
       </div>
     </body>
    </html>''' 
@app.route('/at34')
def at34():
    return '''<<!DOCTYPE html>
    <html>
     <head>
      <meta charset="utf-8">
      <title>Переключатели</title>
     </head>
     <body>
    
       <p><b>Вы вспомнили реальный мир, но вернуться невозможно</b></p>
              <div class = "video">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/umDr0mPuyQc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
       </div>
     </body>
    </html>''' 
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')