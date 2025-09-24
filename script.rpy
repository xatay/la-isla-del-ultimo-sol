define n = Character("Nikki", image="nikki")
define eg = Character("El General")
define j = Character("Juancho")
define c = Character("Claus")
define p = Character("Pancho")
define t = Character("Tina")
define tf = Character("Teniente Felipe")
define preg = Character("???")
define tb = Character("Toby")
define f = Character("Flor")
define b = Character("Betty")
define pb = Character("Pablo")
define tr = Character("Teniente Rosa")

image black = "solid colors/black.png"
image home1 = "maps/1.png"
image home1_hover = "maps/1_hover.png"
image mesa1 = "maps/2.png"
image campa1 = "maps/3.png"
image campa1_hover = "maps/3_hover.png"
image campb1 = "maps/4.png"
image campb1_hover = "maps/4_hover.png"

image side nikki = "characters/nikki.png"
image el general = "characters/el general.png"
image juancho = "characters/juancho.png"
image claus = "characters/claus.png"
image pancho = "characters/pancho.png"
image tina = "characters/tina.png"
image teniente felipe = "characters/teniente felipe.png"
image flor = "characters/flor.png"
image betty = "characters/betty.png"
image pablo = "characters/pablo.png"
image teniente rosa = "characters/teniente rosa.png"

image bgcampa1 = "backgrounds/3.png"
image bgcampb1 = "backgrounds/4.png"

image animation_sol:
    "animations/eclipse/sol1.png"
    pause 0.15
    "animations/eclipse/sol2.png"
    pause 0.15
    "animations/eclipse/sol3.png"
    pause 0.15
    "animations/eclipse/sol4.png"
    pause 0.15
    repeat

image animation_luna:
    "animations/eclipse/luna1.png"
    pause 0.15
    "animations/eclipse/luna2.png"
    pause 0.15
    "animations/eclipse/luna3.png"
    pause 0.15
    "animations/eclipse/luna4.png"
    pause 0.15
    repeat

transform move_across:
    xpos 0.4
    linear 7.0 xpos 0.0 
    repeat False

init python:
    renpy.music.register_channel("bgs", "sfx", True)

init python:
    bgs_started = False
    def play_bgs_once(sound_file, volume=1.0):
        global bgs_started
        if not bgs_started:
            renpy.music.play(sound_file, channel="bgs", loop=True)
            bgs_started = True
            renpy.music.set_volume(volume, channel="bgs")

screen home1: 
    on "show" action Function(play_bgs_once, "audio/bgs/campa.ogg", 0.3),
    imagemap:
        ground "home1"
        hover "home1_hover"
        
        hotspot (53, 519, 588, 562) clicked Jump("mesa1")
        hotspot (934, 0, 399, 614) clicked Jump("campa1") hovered Play("sound", "audio/sfx/cierre.ogg")

screen campa1:
    on "show" action Function(play_bgs_once, "audio/bgs/campa.ogg", 1.0)
    imagemap:
        ground "campa1"
        hover "campa1_hover"
        
        hotspot (63, 439, 269, 426) clicked Jump("home1") hovered Play("sound", "audio/sfx/cierre.ogg")
        hotspot (336, 460, 509, 618) clicked Jump("tinapancho1")
        hotspot (850, 378, 330, 320) clicked Jump("bosquesoleado1") hovered Play("sound", "audio/sfx/pasos 1.ogg")
        hotspot (1292, 365, 350, 560) clicked Jump("clausjuancho1")
        hotspot (1668, 562, 247, 153) clicked Jump("campb1") hovered Play("sound", "audio/sfx/pasos 2.ogg")

screen campb1:
    on "show" action Function(play_bgs_once, "audio/bgs/campa.ogg", 1.0)
    imagemap:
        ground "campb1"
        hover "campb1_hover"
        
        hotspot (0, 793, 290, 252) clicked Jump("campa1") hovered Play("sound", "audio/sfx/pasos 1.ogg")
        hotspot (305, 634, 400, 413) clicked Jump("florbetty1")
        hotspot (1069, 625, 222, 372) clicked Jump("pablo1")
        hotspot (1530, 817, 388, 197) clicked Jump("campc1") hovered Play("sound", "audio/sfx/pasos 2.ogg")




screen bosquesoleado:
    imagemap:
        ground "bosque soleado.png"
        hover "bosque soleado hover.png"
        
        hotspot (837, 225, 140, 145) clicked Jump("bosquesombreado")

screen bosquesombreadoct:
    imagemap:
        ground "bosque sombreado con toby muerto.png"
        hover "bosque sombreado con toby muerto hover.png"
        
        hotspot (35, 480, 145, 145) clicked Jump("playa")

screen bosquesombreadost:
    imagemap:
        ground "bosque sombreado sin toby muerto.png"
        hover "bosque sombreado sin toby muerto hover.png"
        
        hotspot (35, 480, 145, 145) clicked Jump("playa")




label start:
    $ items = [] 
    $ evento1 = False
    $ evento2 = False
    $ felipeOrden = True
    $ pedirElBalde = False
    $ tobyNombre = False
    $ tobyMuerto = False

    scene black
    window hide
    show text "{font=Birthlong.ttf}{size=50}Hace tres meses que estoy en esta isla...{/size}{/font}" at truecenter with fade
    $ renpy.pause() 

    # Fade out text
    hide text with fade

    show animation_sol zorder 5
    with dissolve
    show animation_luna at move_across zorder 10
    with dissolve

    show text "{font=Birthlong.ttf}{size=100}{vspace=750}La Isla del Ultimo Sol{/size}{/font}"
    $ renpy.pause() 

    hide animation_sol with dissolve
    hide animation_luna with dissolve
    hide text with dissolve

    play movie "video/1.webm"
    jump home1

label mesa1:
    scene mesa1
    $ renpy.pause()
    jump home1

label home1:
    call screen home1

label campa1:
    if felipeOrden:
        scene campa1
        show teniente felipe with dissolve
        tf "Estabas durmiendo, soldado?"
        n "No, señor, estaba ordenando mis cosas"
        tf "El General quiere verte en su carpa"
        $ felipeOrden = False
        jump iroexplorar
    call screen campa1

menu iroexplorar:
    "Bueno dale":
        n "Bueno dale"
        hide teniente felipe with dissolve
        jump campc1

    "Ahora voy en breve":
        n "Ahora voy en breve"
        hide teniente felipe with dissolve
        jump campa1

label campb1:
    call screen campb1

label campc1:
    scene carpa del general

    if not evento1:
        show el general with dissolve
        n "General, me dijeron que quería verme"
        eg "Soldado, le voy a dar una tarea muy importante. Acérquese, por favor."
        eg "Seguro habra escuchado en el campamento que los suministros de alimento que trajimos resultaron pocos para la duración de esta misión."
        eg "Estamos esperando la llegada de un paquete muy importante pero mientras tanto, todos debemos colaborar."
        n "Señor?"
        eg "Anda a pescar a la playa, pibe."
        $ evento1 = True
        hide el general with dissolve
    else:
        show el general with dissolve
        eg "Todavia no fuiste a pescar?"
        hide el general with dissolve

    jump campb1

label tinapancho1:
    scene bgcampa1

    if evento1:
        show tina at left with dissolve
        show pancho at right with dissolve
        t "Te mandaron a pescar solo? Podria haber zorros en la zona, porque no vas con alguien?"
        p "No me mires a mi, yo ya estoy hasta las manos"
        hide tina with dissolve
        hide pancho with dissolve
    else: 
        show tina at left with dissolve
        show pancho at right with dissolve
        p "Ya te despertaste, vago?"
        n "Que estan haciendo?"
        t "Andamos con Pancho moviendo los pocos suministros que tenemos..."
        t "Aunque basicamente lo estoy moviendo todo yo."
        p "Te estoy ayudando, no digas que no!"
        t "Agarraste la caja mas chiquita!"
        
        hide tina with dissolve
        hide pancho with dissolve

    jump campa1

label clausjuancho1:
    scene bgcampa1

    if evento1:
        show juancho at left with dissolve
        show claus at right with dissolve

        c "Asi que te mandaron a pescar, por fin te mandaron a hacer algo"
        j "Uuh, que bueno! Hoy les voy a preparar una rica sopa de pescado!"
        c "Agarra la pala, Nikki!"
        hide juancho with dissolve
        hide claus with dissolve
    else: 
        show juancho at left with dissolve
        show claus at right with dissolve
        
        j "Hoy me toco acomodar la carpa, la verdad preferiria cocinar..."
        c "No te quejes, gordo! Yo ando remendando los uniformes."
        hide juancho with dissolve
        hide claus with dissolve

    jump campa1

label florbetty1:
    scene bgcampb1

    if evento1:
        show flor with dissolve
        f "El General te mando a pescar? Vas a necesitar la caña y el balde. Betty fue la ultima en ir a pescar."
        show flor at left
        show betty at right with dissolve
        b "Te doy la caña pero el balde se lo preste a Pablo, vas a tener que pedirselo."
        if "caña" not in items:
            $ items.append("caña")
        $ pedirElBalde = True
        hide flor with dissolve
        hide betty with dissolve
    else: 
        show flor with dissolve
        f "Nicki! No ves que estoy ocupada?"
        hide flor with dissolve
        show betty with dissolve
        n "Que estan haciendo?"
        b "Hola, Nikki, estoy abriendo los suministros."
        n "Y Flor?"
        b "Esta supervisando a todos, tiene que asegurarse de que todo este."
        b "Pero en realidad esta nerviosa porque faltan 5 latas de tomate."
        n "Quien se robaria tanto tomate? Y para que?"
        b "Supongo que nunca lo sabremos..."
        hide betty with dissolve
    jump campb1

label pablo1:
    scene bgcampb1

    if evento1:
        if not pedirElBalde:
            show pablo with dissolve
            pb "El General me da miedo a veces... casi siempre."
            hide pablo with dissolve
        else:
            show pablo with dissolve
            pb "El balde? Si, yo se lo habia pedido a Betty"
            pb "Estaba usandolo en el bosque para juntar frutas pero despues escuche un ruido"
            pb "Y me dio miedo porque pense que era un zorro asi que me volvi y deje el balde"
            hide pablo with dissolve
        jump campb1
    else: 
        show pablo with dissolve
        if "conejito de mimbre" not in items:
            n "En que andas?"
            pb "Ando haciendo unos conejitos de mimbre para la suerte"
            pb "Queres uno?"
            jump conejitodemimbre
        else:
            pb "Amo hacer conejitos de mimbre."
            jump campb1

menu conejitodemimbre:
    "Aceptar":
        n "Me gustaria"
        "Recibis un coleccionable: Conejito de Mimbre"
        $ items.append("conejito de mimbre")

        pb "Disfrutalo!"
        hide pablo with dissolve
        jump campb1

    "Denegar":
        n "Quizas mas tarde"
        pb "Bueno... quizas mas tarde no haya otro"
        hide pablo with dissolve
        jump campb1

label bosquesoleado1:
    if not evento1:
        show teniente rosa with dissolve
        tr "No podes ir al bosque todavia porque tenes que hablar con el General"
        hide teniente rosa with dissolve
        jump campa1
    else:
        jump bosquesoleado
    
label bosquesoleado:
    call screen bosquesoleado

label bosquesombreado:
    if evento2:
        if tobyMuerto:
            call screen bosquesombreadoct

        else:
            call screen bosquesombreadost
    
    else: 
        scene bosque sombreado
        show toby with dissolve

        preg "Por... favor... Ayuda.. me..."
        "Es un zorro herido!"
        "*saca cuchillo*"
        preg "No me mates..."
        "Un zorro enemigo... pero esta herido..."
        "Debería matarlo, pero quizas el sepa donde se esconden los demás zorros..."
        jump preguntasatoby

menu preguntasatoby:
    "Que haces en nuestro territorio?":
        jump pat1

    "Quien sos? Y de donde venis?":
        jump pat2

    "Quien te envio?":
        jump pat3

    "Por que debería perdonarte la vida?":
        jump pat4

label pat1:
    n "Que haces en nuestro territorio?"
    n "Este lugar esta rodeado de soldados conejos, te matarían en un instante."
    preg "No, por favor! Yo solo me quiero escapar de esta isla!"
    preg "Quiero volver a casa, quiero ver a mi novia, esta embarazada!"
    preg "Mira, esta es ella"
    $ tobyNombre = True
    tb "Su nombre es Maria, y yo me llamo Toby. Nos íbamos a casar cuando vuelva"

    jump bosquesombreado2

label pat2:
    n "Quien sos? Y de donde venis?"
    $ tobyNombre = True
    tb "Me llamo Toby, me trajeron aca para pelear pero yo no tengo intenciones de seguir. Me escape."
    n "Un zorro desertor? Que patetico"
    tb "Por favor perdóname la vida y te doy un mapa"

    jump bosquesombreado2

label pat3:
    n "Quien te envio?"
    preg "Nadie!"
    n "Mentira! Estas buscando invadir nuestro campamento!"
    preg "No! No es verdad! Solo quiero irme de esta isla!"
    n "Mostrame alguna prueba"
    preg "En mi bolsillo tengo un mapa que dibuje"

    jump bosquesombreado2

label pat4:
    n "Por que debería perdonarte la vida?"
    preg "Porque yo solo soy un pibe, como vos. Yo no quiero morir en esta guerra."
    n "Vos sos un zorro! No sos nada como yo!"
    preg "Si, nací zorro, pero yo no elegí venir aca o pelear contra ustedes."
    $ tobyNombre = True
    tb "Me llamo Toby y tengo 20 años. Hace semanas que estoy planeando escapar."
    n "Un zorro desertor? Que patetico"
    tb "Por favor perdóname la vida y te doy un mapa"

    jump bosquesombreado2

label bosquesombreado2:
    $ items.append("mapa")

    if tobyNombre:
        "Toby te da un mapa que tiene una carta escrita del otro lado"

    else:
        "El zorro te da un mapa con una carta del otro lado. Podemos confiar en el?"

    n "Esta chica... Es una coneja"

    if tobyNombre:
        tb "Si, es mi chica. Yo nunca quise matar conejos, yo no tengo ningún problema con ustedes."

    else:
        preg "Si, es mi chica. Yo nunca quise matar conejos, yo no tengo ningún problema con ustedes."

    "Sera que esta diciendo la verdad? Se puede confiar en un zorro?"
    "Si lo dejo con vida podrían descubrir nuestra base"
    jump decisiontoby

menu decisiontoby:
    "MATAR AL ZORRO CON UN TIRO":
        $ carta = 'torre'
        jump mataratoby

    "QUITAR SU PIERNA DE LA TRAMPA":
        $ carta = 'muerte'
        jump liberaratoby

    "AYUDARLO A CURAR SU HERIDA":
        $ carta = 'carro'
        jump ayudaratoby

    "HERIRLO PARA SACARLE INFORMACION":
        $ carta = 'diablo'
        jump heriratoby

label mataratoby:
    n "Perdón, pero sos un zorro y no puedo confiar en vos."
    
    if tobyNombre:
        tb "Noo, por favor!"

    else:
        preg "Noo, por favor!"

    "*le pega un tiro*"
    hide toby

    "Era lo mejor para todos, rápido y sin dolor."
    $ evento2 = True
    $ tobyMuerto = True

    jump bosquesombreado

label liberaratoby:
    n "Esta bien, te voy a dejar ir. Pero no quiero verte de vuelta por estas partes."
    "*le saca la pierna de la trampa*"
    
    if tobyNombre:
        tb "Muchas gracias, soldado! No lo olvidare!"

    else:
        preg "Muchas gracias, soldado! No lo olvidare!"

    n "Escapate antes que te vean mis compañeros."
    hide toby
    $ evento2 = True

    jump bosquesombreado

label ayudaratoby:
    n "Te voy a ayudar porque yo tampoco elegí pelear en esta guerra."
    n "Me llamo Nikki y tengo 24 años."

    "*le saca la pierna de la trampa*"
    
    if tobyNombre:
        tb "Muchas gracias, Nikki! No lo olvidare!"

    else:
        tb "Yo me llamo Toby y tengo 20"
        tb "Muchas gracias, Nikki! No lo olvidare!"

    "*lo cura*"
    n "Podes caminar?"
    tb "Si, masomenos."
    n "Bien, escapate antes que te vean mis compañeros."
    hide toby
    $ evento2 = True

    jump bosquesombreado

label heriratoby:
    n "No puedo dejarte ir hasta que me digas donde esta el campamento de los zorros."
    
    if tobyNombre:
        tb "No puedo decirte eso, pondría en peligro a los demás."

    else:
        preg "YNo puedo decirte eso, pondría en peligro a los demás."

    "*lo hiere*"

    if tobyNombre:
        tb "No, por favor! No lo hagas!"

    else:
        preg "No, por favor! No lo hagas!"

    n "Decime donde esta el campamento!"
    "*lo hiere*"
    n "Si no me decís te voy a llevar a nuestra base y ellos son peores que yo."

    if tobyNombre:
        tb "No te voy a decir nada!"

    else:
        preg "No te voy a decir nada!"

    n "Entonces no me dejas opción..."

    hide toby
    show black with dissolve

    $ renpy.pause() 

    show bosque sombreado con toby muerto
    n "Para ser desertor era bastante leal."

    $ evento2 = True
    $ tobyMuerto = True

    jump bosquesombreado
    # Finaliza el juego:

label playa:
    scene playa
    "*vas a la playa*"

    return

    
    # This ends the game.
    return