import time, random
from timeit import default_timer as timer

rodadas = int(input("quantas rodadas você quer jogar? "))

for i in range(rodadas):
    print("quando o aviso aparecer aperte ENTER o mais rapido possivel")
    time.sleep(0.5)
    print("espere .......")
    time.sleep(random.randint(2, 6))
    
    timer_start = timer()
    
    input("******* AGORA ********")
    
    timer_end = timer()
    
    tempo_final = (timer_start - timer_end)
    
    print(f"seu tempo foi de = {'{:.3f}'.format(abs(tempo_final))}s")
    
    if i < rodadas - 1:
        print("---proxima rodada---")
        time.sleep(1.5)
