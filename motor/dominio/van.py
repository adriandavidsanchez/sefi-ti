"""Motor financiero: VAN y dictamen de viabilidad (US-01).

Capa de dominio: funciones puras, sin entrada/salida ni dependencias externas.
"""
from motor.dominio.errores import EntradaInvalidaError

TOLERANCIA = 1e-6


def calcular_van(tasa: float, flujos: list[float]) -> float:
    """VAN = sum(F_t / (1 + tasa)^t), con F_0 como inversión inicial (negativa)."""
    if not flujos:
        raise EntradaInvalidaError("El flujo de caja no puede estar vacío.")
    if tasa <= -1:
        raise EntradaInvalidaError("La tasa de descuento debe ser mayor que -100 %.")
    return sum(f / (1 + tasa) ** t for t, f in enumerate(flujos))


def dictamen_van(van: float) -> str:
    """Clasifica el VAN: Viable (> 0), Indiferente (= 0) o No viable (< 0)."""
    if van > TOLERANCIA:
        return "Viable"
    if van < -TOLERANCIA:
        return "No viable"
    return "Indiferente"


def evaluar_inversion(tasa: float, flujos: list[float]) -> tuple[float, str]:
    """Devuelve (VAN, dictamen) para una inversión."""
    van = calcular_van(tasa, flujos)
    return van, dictamen_van(van)
