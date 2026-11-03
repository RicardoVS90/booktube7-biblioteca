#!/usr/bin/env python3
"""BookTube7 — publicar una versión nueva de un libro (por Ricardo Vera).

Uso:
  python3 publicar.py                      -> recalcula tamaño y huella de todos los libros
  python3 publicar.py daniel-profecia-y-cumplimiento   -> además sube la versión de ese libro

Pasos para actualizar un libro:
  1. Reemplaza el archivo en libros/<id>/ (mismo nombre).
  2. Ejecuta: python3 publicar.py <id>
  3. git add -A && git commit -m "Daniel v2" && git push
Los lectores lo reciben al tocar "Actualizar biblioteca".
"""
import json, hashlib, os, sys, datetime
aqui = os.path.dirname(os.path.abspath(__file__))
ruta = os.path.join(aqui, 'index.json')
idx = json.load(open(ruta, encoding='utf-8'))
subir = sys.argv[1:]
for l in idx['libros']:
    datos = open(os.path.join(aqui, l['archivo']), 'rb').read()
    l['tamano'] = len(datos)
    nueva = hashlib.sha256(datos).hexdigest()
    if l['id'] in subir:
        l['version'] += 1
        print(f"{l['titulo']}: versión {l['version']}")
    elif nueva != l.get('sha256'):
        print(f"Aviso: «{l['titulo']}» cambió pero no subiste su versión; los lectores no lo recibirán.")
    l['sha256'] = nueva
idx['actualizado'] = datetime.date.today().isoformat()
json.dump(idx, open(ruta, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('index.json listo')
