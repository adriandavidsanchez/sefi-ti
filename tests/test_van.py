import pytest

from motor.dominio import EntradaInvalidaError, calcular_van, dictamen_van, evaluar_inversion


def test_van_positivo_calculado_a_mano():
    # -1000 + 600/1.1 + 600/1.21 = 41.3223...
    assert calcular_van(0.10, [-1000, 600, 600]) == pytest.approx(41.3223, abs=1e-3)


def test_van_negativo():
    assert calcular_van(0.10, [-1000, 300, 300]) < 0


def test_van_con_tasa_cero_es_la_suma_simple():
    assert calcular_van(0.0, [-1000, 500, 500]) == pytest.approx(0)


def test_van_solo_inversion_inicial():
    assert calcular_van(0.10, [-500]) == pytest.approx(-500)


def test_flujo_vacio_lanza_error():
    with pytest.raises(EntradaInvalidaError):
        calcular_van(0.10, [])


@pytest.mark.parametrize("tasa", [-1, -1.5])
def test_tasa_invalida_lanza_error(tasa):
    with pytest.raises(EntradaInvalidaError):
        calcular_van(tasa, [-100, 200])


@pytest.mark.parametrize(
    "van, esperado",
    [(41.32, "Viable"), (-5.0, "No viable"), (0.0, "Indiferente"), (1e-9, "Indiferente")],
)
def test_dictamen(van, esperado):
    assert dictamen_van(van) == esperado


def test_evaluar_inversion_devuelve_van_y_dictamen():
    van, dictamen = evaluar_inversion(0.10, [-1000, 600, 600])
    assert van == pytest.approx(41.3223, abs=1e-3)
    assert dictamen == "Viable"
