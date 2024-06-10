import RPIO
from RPIO import PWM
import time, random

button_pin = 2
led_pin = 17

RPIO.setup(button_pin, RPIO.IN, pull_up_down=RPIO.PUD_UP)
RPIO.setup(led_pin, RPIO.OUT)

rodadas = int(input("Quantas rodadas você quer jogar? "))

for i in range(rodadas):
    print("Quando o LED acender, aperte o botão o mais rápido possível")
    time.sleep(0.5)
    print("Espere .......")
    time.sleep(random.randint(2, 6))

    RPIO.output(led_pin, True)
    timer_start = time.time()

    print("##### AGORA #####")
    RPIO.wait_for_edge(button_pin, RPIO.FALLING)

    RPIO.output(led_pin, False)
    timer_end = time.time()

    tempo_final = abs(timer_end - timer_start)

    print(f"Seu tempo foi = {'{:.3f}'.format(tempo_final)}s")

    if i < rodadas - 1:
        print("--- Próxima rodada ---")
        time.sleep(1)

RPIO.cleanup()