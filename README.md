
# hidedir 🕵️‍♂️

**hidedir** é uma ferramenta de busca por subdomínios e diretórios ocultos desenvolvida em Python, voltada para pentesters, CTF players e entusiastas de segurança. Rápida, simples e eficiente, ela permite encontrar rotas escondidas em sites que podem ser exploradas.

## 🚀 Funcionalidades

- Busca automática por subdomínios e diretórios usando uma wordlist padrão.
- Suporte a wordlists personalizadas.
- Saída colorida para facilitar a visualização.
- Totalmente executável por terminal.
- Argumento `--help` com instruções.

## 🛠️ Como usar

```bash
python3 hidedir.py -url <https://example.com> [--wordlist <caminho/para/sua/wordlist.txt>]
```

Se nenhuma wordlist for informada, será usada a interna com mais de 50 termos.

### 📘 Exemplo:

```bash
python3 hidedir.py -url https://sitealvo.com
```

```bash
python3 hidedir.py -url https://sitealvo.com --wordlist minhas_palavras.txt
```

## 📁 Estrutura

```
hidedir/
├── hidedir.py
├── default_wordlist.txt
```

## 📦 Compilação para .exe

Para gerar a versão `.exe`:
```bash
pyinstaller --onefile hidedir.py
```

O executável será gerado na pasta `dist/`.

## 👤 Autor

Ferramenta criada por **Xuelv1s** 🧠💻  
Siga para mais conteúdos sobre hacking, pentest e segurança da informação.

---

Ferramenta criada apenas para fins educacionais e legais.

