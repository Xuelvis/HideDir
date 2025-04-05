import requests
import argparse
import threading

def scan_subdomain(url, word):
    full_url = f"http://{word}.{url}"
    try:
        res = requests.get(full_url, timeout=3)
        if res.status_code < 400:
            print(f"[+] Subdomain found: {full_url}")
    except:
        pass

def scan_directory(url, word):
    if not url.startswith("http"):
        url = "http://" + url
    full_url = f"{url}/{word}"
    try:
        res = requests.get(full_url, timeout=3)
        if res.status_code < 400:
            print(f"[+] Directory found: {full_url}")
    except:
        pass

def main():
    parser = argparse.ArgumentParser(
        prog="hidedir",
        description="Ferramenta para encontrar subdomínios e diretórios ocultos. Criado por Xuelv1s.",
        epilog="Exemplos:\n  hidedir -url site.com\n  hidedir -url site.com --dirs\n  hidedir -url site.com --wordlist minha.txt --dirs",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("-url", required=True, help="Alvo da varredura (ex: site.com)")
    parser.add_argument("--wordlist", help="Wordlist personalizada (opcional)")
    parser.add_argument("--dirs", action="store_true", help="Ativa a busca por diretórios em vez de subdomínios")
    
    args = parser.parse_args()

    # Define a wordlist padrão caso nenhuma seja fornecida
    wordlist = args.wordlist if args.wordlist else "default_wordlist.txt"

    try:
        with open(wordlist, "r") as file:
            words = [line.strip() for line in file.readlines()]
    except:
        print("[!] Wordlist não encontrada!")
        return

    tipo_busca = "diretórios" if args.dirs else "subdomínios"
    print(f"\n[!] Iniciando busca por {tipo_busca} em {args.url}...\n")

    threads = []

    for word in words:
        if args.dirs:
            t = threading.Thread(target=scan_directory, args=(args.url, word))
        else:
            t = threading.Thread(target=scan_subdomain, args=(args.url, word))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    print(r"""
  _    _ _     _      _____  _      
 | |  | (_)   | |    |  __ \(_)     
 | |__| |_  __| | ___| |  | |_ _ __ 
 |  __  | |/ _` |/ _ \ |  | | | '__|
 | |  | | | (_| |  __/ |__| | | |   
 |_|  |_|_|\__,_|\___|_____/|_|_|   

   hidedir - subdomain & dir finder
          by Xuelv1s
    """)
    main()

