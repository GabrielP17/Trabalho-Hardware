import time, random
from timeit import default_timer as timer

rodadas = int(input("quantas rodadas você quer jogar? "))

for i in range(rodadas):
    print("quando o led acender aperte o botão o mais rapido possivel")
    time.sleep(0.5)
    print("espere .......")
    time.sleep(random.randint(2, 6))
    
    timer_start = timer()
    
    input("aperte o botão")
    
    timer_end = timer()
    
    tempo_final = (timer_start - timer_end)
    
    print(f"tempo = {'{:.3f}'.format(abs(tempo_final))}s")
    
    if i < rodadas - 1:
        print("---proxima rodada---")
        time.sleep(1)