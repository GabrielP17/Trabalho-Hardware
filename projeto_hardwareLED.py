import RPi.GPIO as GPIO
import time
import random
 
button_pin = 2
led_pin = 17
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)
 
rodadas = int(input("Quantas rodadas você quer jogar? "))
 
for i in range(rodadas):
    print("Quando o LED acender, aperte o botão o mais rápido possível")
    time.sleep(0.5)
    print("Espere .......")
    time.sleep(random.randint(2, 6))
 
    GPIO.output(led_pin, True)
    timer_start = time.time()
 
    print("#####AGORA##### ")
    while GPIO.input(button_pin) == GPIO.HIGH:
        pass
 
    GPIO.output(led_pin, False)
    timer_end = time.time()
 
    tempo_final = abs(timer_end - timer_start)
 
    print(f"Seu tempo foi = {'{:.3f}'.format(tempo_final)}s")
 
    if i < rodadas - 1:
        print("--- Próxima rodada ---")
        time.sleep(1)
 
GPIO.cleanup()
 
