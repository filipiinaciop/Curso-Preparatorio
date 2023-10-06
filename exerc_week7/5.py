from time import sleep

def tempo(min, segs):
    ts = min * 60 + segs

    for c in range(ts, -1, -1):
        min_rest = c // 60
        segs_rest = c % 60
        if c <= 10:
            print(f'\033[91m{min_rest:02d}:{segs_rest:02d}\033[0m')
        else:
            print(f'{min_rest:02d}:{segs_rest:02d} ')
        sleep(1)

segs = 0
def main():
    min = int(input('Qual o minuto inicial? ')) 
    if min != 0:
        segs = int(input('Quantos segundos? '))

    if min == 0:
        segs = int(input('Quantos segundos então? '))
    
    tempo(min, segs)

if __name__ == "__main__":
    main()
print('FIM')