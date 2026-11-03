# BookTube7 — biblioteca en línea

Servidor de libros de **BookTube7** (por Ricardo Vera), publicado con GitHub Pages en
`https://ricardovs90.github.io/booktube7-biblioteca/`.

## Primera vez
1. Crea en GitHub el repositorio **booktube7-biblioteca** (público) en la cuenta RicardoVS90.
2. Sube el contenido de esta carpeta.
3. En el repositorio: *Settings → Pages → Source: Deploy from a branch → main / (root)*.
4. En unos minutos `https://ricardovs90.github.io/booktube7-biblioteca/index.json` debe abrir en el navegador.

## Agregar o actualizar un libro
- **Actualizar:** reemplaza el archivo en `libros/<id>/`, ejecuta `python3 publicar.py <id>` y sube los cambios.
- **Libro nuevo:** crea `libros/<id-nuevo>/` con el archivo y una `portada.jpg`, copia una entrada en
  `index.json` cambiando `id`, `titulo`, `lomo` (texto corto del lomo), `formato` (`pdf` o `epub`) y rutas,
  con `"version": 1`. Luego `python3 publicar.py` y sube los cambios.

La app solo descarga un libro cuando su `version` en `index.json` es mayor que la que tiene el lector.
GitHub admite archivos de hasta 100 MB.

## Radio y canal de YouTube
En `index.json`:
- `radio.stream`: lista de direcciones del audio (HLS .m3u8) de Nuevo Tiempo Paraguay; se prueban en orden. Si está vacía o ninguna responde,
  la radio de la sala abre la página `radio.pagina` en el navegador. Cuando la completes y subas,
  la radio sonará dentro de la app (después de tocar ⟳ Actualizar).
- `youtube.url`: canal que abre la computadora de la sala (en la app de YouTube si está instalada).
