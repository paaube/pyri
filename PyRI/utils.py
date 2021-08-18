from PyRI.Directories import *
from PyRI.ExpData import ExpData
from PyRI.Sellmeier import Sellmeier
import os, json


def DataBank():
    """Returns the materials for which the experimental data is available
    and the materials for which Sellmeier's formula is available
    """

    with open(os.path.join(DataPath, 'meta_expdata.json'), "r") as f:
        expdata = json.load(f)
        material_expdata = []
        for material_e in expdata["local_data"]:
            material_expdata.append(material_e)


    with open(os.path.join(DataPath, 'meta_sellmeier.json'), "r") as f:
        sellmeier = json.load(f)
        material_sellmeier = []
        for material_s in sellmeier["sellmeier_formula"]:
            material_sellmeier.append(material_s)
    print(f"Material with experimental data: {material_expdata}")
    print(f"Material with Sellmeier's formula: {material_sellmeier}")
