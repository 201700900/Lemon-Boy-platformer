from cx_Freeze import setup,Executable


executables = [ Executable("lemon_boy.py",
                base = "Win32GUI",
                icon = "lemon.ico")]

build_exe_options ={"Packages": ["pygame","pytmx","pytweening","script","os.path","math","sys"],
                    "incluide_files": [ 
        "Pixel Digivolve.otf",
        "map/map1.tmx",
        "map/map2.tmx",
        "map/map3.tmx",
        "map/map4.tmx",
        "map/map5.tmx",
        "map/map6.tmx",
        "sound/arrow_sound.wav",
        "sound/blip.wav",
        "sound/dead.wav",
        "sound/Jumpa.wav",
        "Pickup_Coin.wav",
        "image/door1.png",
        "image/door2.png",
        "image/door3.png",
        "image/door4.png",
        "image/fire_cannon.png",
        "image/spikes.png",
        "image/key.png",
        "image/lemon.png",
        "image/pasto.png",
        "image/plataform.png",
        "image/trampoline.png",
        "image/ball.png",
        "image/ball2.png",
        "image/ball3.png",
        "image/dead.png",
        "image/heart1.png",
        "image/sprites/apple1.png",
        "image/sprites/apple2.png",
        "image/sprites/apple3.png",
        "image/sprites/apple4.png",
        "image/sprites/hug/hug0.png",
        "image/sprites/hug/hug1.png",
        "image/sprites/hug/hug2.png",
        "image/sprites/hug/hug3.png",
        "image/sprites/hug/hug4.png",
        "image/sprites/hug/hug5.png",
        "image/sprites/hug/hug6.png",
        "image/sprites/hug/hug7.png",
        "image/sprites/hug/hug8.png",
        "image/sprites/hug/hug9.png",
        "image/sprites/hug/arrow.png",
        "image/sprites/hug/paty.png",
        "lemon.ico",
                            ]}

setup(
    name = "Lemon Boy",
    version = "1.0",
    description = "Platformer",
    options = {"build.exe":build_exe_options},
    executables = executables
)
