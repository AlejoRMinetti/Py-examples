"""
Checkea existencia de archivo
"""

def existFile(Path, fileName):
    try:
        with open(Path + fileName) as f:
            f.close()
            return True
            # Do something with the file
    except IOError:
        return False


if __name__ == '__main__':
    # Arguments:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path2file', type=str, 
                    default=r"C:\Users\alejo\AppData\Roaming\MetaQuotes\Tester\FBF1B8542F2BB5E0DC137458AD2FCF28\Agent-127.0.0.1-3000\MQL5\Files/",
                    help='Mismo path de ubicacion de AquiEstamos.txt generado en Tester por fileRecibidor.mq5')
    parser.add_argument('-f', '--fileName', type=str, 
                    default="AquiEstamos.txt",
                    help='Mismo path de ubicacion de AquiEstamos.txt generado en Tester por fileRecibidor.mq5')
    args = parser.parse_args()

    print("Buscando el archivo "+args.fileName+" en "+ args.path2file)
    if existFile(args.path2file,args.fileName):
        print("Existe ese archivo! ")
    else:
        print("No existe ese archivo en esa path")