def main():
    """
    Obtener la temperatura máxima y mínima para la ciudad que proporcione el usuario
    """
    import requests
    import os

    while True:
        print('Inserte la ciudad de la cual desea conocer el tiempo:')
        city = input().capitalize()
        req = requests.get(
            url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=es&appid={os.environ["API_KEY_openWeather"]}')
        json = req.json()
        temp = json['main']['temp']
        temp_max = json['main']['temp_max']
        temp_min = json['main']['temp_min']
        name = json['name']
        print(f'Ahora en {name}:')
        print(f'Temperatura: {round(temp)} °C')
        print(f'Temperatura máxima: {round(temp_max)} °C')
        print(f'Temperatura mínima: {round(temp_min)} °C')
        print('========================================')

        cond = input('¿Desea realizar una consulta mas? [y]/[n]\n')
        if cond == 'y':
            continue
        elif cond == 'n':
            break
        else:
            print('Ingrese una condición válida')

if __name__ == '__main__':
    print('Bienvenido a CutreWeather')
    main()
