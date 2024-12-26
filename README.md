# Script para Buscar Transcritos en un Archivo GTF

## Descripción

Este script permite buscar transcritos específicos en un archivo GTF. Utiliza múltiples núcleos para acelerar el proceso de búsqueda y extrae información relevante sobre los transcritos, como el tipo de gen y el nombre del gen.

## Autor

- **Nombre:** Allan Javier Peñaloza Otárola
- **Contacto:** allan.penaloza@ug.uchile.cl
- **Fecha:** 10/10/2024

## Requisitos

- Python 3.x
- Módulos: `argparse`, `multiprocessing`, `re`

## Uso

### Parámetros

- `-i`, `--input`: Ruta al archivo GTF.
- `-q`, `--query`: Ruta al archivo de texto plano con la lista de transcritos a consultar.
- `-c`, `--cores`: Número de núcleos a utilizar (opcional, por defecto es 1).

### Ejemplo de Uso

```bash
python script.py -i path/to/file.gtf -q path/to/query.txt -c 4
```

## Funciones

### `parse_gtf(file_path, query_transcripts)`

Lee el archivo GTF y busca los transcritos especificados en `query_transcripts`. Devuelve una lista con los resultados encontrados.

### `load_query_transcripts(query_file)`

Carga la lista de transcritos a consultar desde un archivo de texto plano.

### `main()`

Función principal que maneja los argumentos de línea de comandos y coordina la ejecución del script utilizando múltiples núcleos.

## Notas

- Asegúrate de que el archivo GTF y el archivo de consulta estén en el formato correcto.
- El script utiliza expresiones regulares para extraer información del archivo GTF.e sea útil. ¿Hay algo más en lo que pueda ayudarte?
