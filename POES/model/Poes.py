#Funcion POES

def poes(area, h, poro, swi, boi):
    """

    Parameters
    ----------
    area: Area in ft2
    h: Thickness in ft
    poro: Porosity (dimensionless)
    swi: water saturation (dimensionless)
    boi: oil bubble factor (bbl / stb)

    Returns
    -------
    poes: Petroleum original in situ (bbl)

    """
    poes = (7758*area*h*poro*(1-swi))/boi

    return poes
