import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


import os

ARQUIVO = Path(os.environ.get(
    "FACTORY_SDF",
    Path(__file__).resolve().parents[1] / "worlds/factory_cell.sdf"
))


class TestFactoryGeometry(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.raiz = ET.parse(ARQUIVO).getroot()

    def test_modelos_obrigatorios(self):
        nomes = {
            modelo.get("name")
            for modelo in self.raiz.findall("./world/model")
        }
        self.assertTrue(
            {"factory_floor", "conveyor", "peca_01"}.issubset(nomes)
        )

    def test_dimensoes_esteira(self):
        esteira = self.raiz.find("./world/model[@name='conveyor']")
        visual = esteira.findtext(
            "./link/visual/geometry/box/size"
        )
        colisao = esteira.findtext(
            "./link/collision/geometry/box/size"
        )

        self.assertEqual(visual, "6 1.2 0.2")
        self.assertEqual(visual, colisao)

    def test_peca_dinamica(self):
        peca = self.raiz.find("./world/model[@name='peca_01']")
        self.assertEqual(peca.findtext("static"), "false")
        self.assertEqual(
            peca.findtext("pose"), "0 0 1.5 0 0 0"
        )


if __name__ == "__main__":
    unittest.main()
