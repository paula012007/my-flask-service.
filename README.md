# Mi Servicio Flask

## Construcción de la imagen Docker

```bash
docker build -t mi-servicio .
```

## Ejecutar contenedor

```bash
docker-compose up
```

## Requisitos

- Docker instalado
- Docker Compose instalado
- Python 3.10

## Configuración

Puerto:

5000

## Solución de errores comunes

Si falla:

```bash
docker-compose down
docker-compose up --build
```

## Detener contenedor

```bash
docker-compose down
```
