import pytest
import leccion2_programa_bpp

def test_resta():
    x = 5
    resultado = 5-(5-1) 
    assert resultado == leccion2_programa_bpp.resta(x)

def test_suma():
    x = 5
    resultado = 5+5+1
    assert resultado == leccion2_programa_bpp.suma(x)

def test_menorque100():
    x = 5
    resultado = True
    assert resultado == leccion2_programa_bpp.menorque100(x) 

def test_numeroprimo():
    x = 5
    resultado = True
    assert resultado == leccion2_programa_bpp.numeroprimo(x) 

def test_parimpar():
    x = 5
    resultado = 'impar'
    assert resultado == leccion2_programa_bpp.parimpar(x) 

