import csv


def show_menu():
    print('*** MENU PRINCIPAL ***')
    print('1. Cargar archivo')
    print('2. Exportar cantidad de mesas por región')
    print('3. Exportar recuento general')
    print('4. Exportar resultados en local')
    print('0. Salir')


def import_data():
    filename = input('Ingresa el nombre del archivo de datos: ')
    file_data = []
    file = open(filename)
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for line in reader:
        registry = {
            'nro_region': int(line[0]),
            'region': line[1],
            'provincia': line[2],
            'circunscripcion_senatorial': int(line[3]),
            'distrito': int(line[4]),
            'comuna': line[5],
            'circunscripcion_electoral': line[6],
            'local': line[7],
            'nro_mesa': int(line[8]),
            'tipo_mesa': line[9],
            'mesas_fusionadas': line[10],
            'electores': int(line[11]),
            'nro_en_voto': int(line[12]),
            'candidato': line[13],
            'votos_tricel': int(line[14])
        }
        file_data.append(registry)
    file.close()
    return file_data


def export_tables_by_region(data, filename):
    tables_by_region = {}
    for table in data:
        if table['region'] in tables_by_region:
            tables_by_region[table['region']] += 1
        else:
            tables_by_region[table['region']] = 1
    regions = list(tables_by_region.keys())
    file = open(filename, 'w')
    for region in regions:
        file.write(f'{region};{tables_by_region[region]}\n')
    file.close()


def export_general_results(data, filename):
    count = {}
    for table in data:
        if table['candidato'] not in count:
            count[table['candidato']] = 1
        else:
            count[table['candidato']] += table['votos_tricel']
    candidates = list(count.keys())
    file = open(filename, 'w')
    for candidate in candidates:
        file.write(f'{candidate};{count[candidate]}\n')
    file.close()


def export_count_by_local(data, filename):
    local = input(
        'Ingresa el nombre del local a graficar (debe estar igual que en el archivo): ')
    tables_in_local = [x for x in data if x['local'] == local]
    count = {}
    for table in tables_in_local:
        if table['candidato'] not in count:
            count[table['candidato']] = 1
        else:
            count[table['candidato']] += table['votos_tricel']
    print(count)
    candidates = list(count.keys())
    file = open(filename, 'w')
    for candidate in candidates:
        file.write(f'{candidate};{count[candidate]}\n')
    file.close()


if __name__ == '__main__':
    data = []
    while True:
        show_menu()
        opcion = int(input('Selecciona una opción: '))
        if opcion == 0:
            exit(0)
        elif opcion == 1:
            data = import_data()
        elif opcion == 2:
            filename = input('Ingresa el nombre del archivo de salida: ')
            export_tables_by_region(data, filename)
        elif opcion == 3:
            filename = input('Ingresa el nombre del archivo de salida: ')
            export_general_results(data, filename)
        elif opcion == 4:
            filename = input('Ingresa el nombre del archivo de salida: ')
            export_count_by_local(data, filename)
