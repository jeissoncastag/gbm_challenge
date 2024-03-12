def calcula_puntuacion(resultados, sistema_puntuacion):
    puntuaciones = [0] * len(resultados[0])
    for i, puntos in enumerate(sistema_puntuacion):
        puntuaciones[i] = puntos

    puntuacion_final = [0] * len(resultados[0])
    for carrera in resultados:
        for i, posicion in enumerate(carrera):
            puntuacion_final[i] += puntuaciones[posicion - 1]
    return puntuacion_final

def define_campeon(resultados, sistemas_puntuacion):
    campeones = set()
    max_puntuacion = -1

    for sistema in sistemas_puntuacion:
        puntuacion_final = calcula_puntuacion(resultados, sistema)
        max_puntuacion_actual = max(puntuacion_final)
        if max_puntuacion_actual > max_puntuacion:
            max_puntuacion = max_puntuacion_actual
            campeones = {i + 1 for i, p in enumerate(puntuacion_final) if p == max_puntuacion}
        elif max_puntuacion_actual == max_puntuacion:
            campeones |= {i + 1 for i, p in enumerate(puntuacion_final) if p == max_puntuacion}
    return sorted(campeones)

def main():
    G, P = map(int, input().split())
    resultados = []
    for _ in range(G):
        resultados.append(list(map(int, input().split())))
    
    S = int(input())
    sistemas_puntuacion = []
    for _ in range(S):
        sistema = list(map(int, input().split()))
        sistemas_puntuacion.append(sistema[1:])

    campeones = define_campeon(resultados, sistemas_puntuacion)
    print(*campeones)

if __name__ == "__main__":
    main()