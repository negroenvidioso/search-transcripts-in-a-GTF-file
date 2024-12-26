###################################################################################
#                                                                                 #
#                         Script para Buscar Transcritos en un Archivo GTF        #
#                                                                                 #
# Autor: Allan Javier Peñaloza Otárola                                            #
# Contacto: allan.penaloza@ug.uchile.cl                                           #
# Fecha: 12/10/2024                                                               #
#                                                                                 #
###################################################################################

import argparse
import multiprocessing as mp
import re

def parse_gtf(file_path, query_transcripts):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    results = []
    for line in lines:
        if "ensembl	transcript" in line:
            transcript_id_match = re.search(r'transcript_id "([^"]+)"', line)
            gene_biotype_match = re.search(r'gene_biotype "([^"]+)"', line)
            gene_name_match = re.search(r'gene_name "([^"]+)"', line)

            if transcript_id_match:
                transcript_id = transcript_id_match.group(1)
                if transcript_id in query_transcripts:
                    gene_biotype = gene_biotype_match.group(1) if gene_biotype_match else "N/A"
                    gene_name = gene_name_match.group(1) if gene_name_match else "N/A"
                    results.append(f"{transcript_id}\t{gene_biotype}\t{gene_name}")

    return results

def load_query_transcripts(query_file):
    with open(query_file, 'r') as file:
        query_transcripts = [line.strip() for line in file.readlines()]
    return query_transcripts

def main():
    parser = argparse.ArgumentParser(description="Script para buscar transcritos en un archivo GTF.")
    parser.add_argument('-i', '--input', required=True, help="Ruta al archivo GTF.")
    parser.add_argument('-q', '--query', required=True, help="Ruta al archivo de texto plano con la lista de transcritos a consultar.")
    parser.add_argument('-c', '--cores', type=int, default=1, help="Número de núcleos a utilizar.")
    args = parser.parse_args()

    query_transcripts = load_query_transcripts(args.query)

    with mp.Pool(args.cores) as pool:
        results = pool.apply(parse_gtf, (args.input, query_transcripts))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
