# SEFI-TI · Urban Style Barber Shop

Motor financiero (VAN, dictamen de viabilidad y, próximamente, TIR) con arquitectura hexagonal.

## Ejecutar pruebas
```bash
pip install -r requirements.txt
pytest          # falla si la cobertura de ramas es menor a 90 %
```

## Git Flow
- `main`: código estable, protegido (Pull Request + 1 aprobación + CI en verde).
- `develop`: integración del trabajo del equipo.
- `feature/<nombre>`: una rama por historia o funcionalidad, sale de `develop`.

Flujo: `feature/*` → PR a `develop` → al cerrar el Sprint, PR de `develop` a `main`.

## Convención de commits
`tipo: descripción corta` con tipo en `feat`, `fix`, `test`, `ci`, `docs`, `refactor`.
Ejemplo: `test: agregar pruebas del VAN con casos calculados a mano`.
