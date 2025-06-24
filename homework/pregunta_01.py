"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"
    """
    import pandas as pd
    import os

    os.makedirs("files/output", exist_ok=True)

    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";")

    df.dropna(inplace=True)

    str_cols = ["sexo", "tipo_de_emprendimiento", "idea_negocio", "barrio", "línea_credito"]
    df[str_cols] = df[str_cols].apply(lambda col: col.str.lower().str.replace("_", " ", regex=False).str.replace("-", " ", regex=False))

    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(
        lambda x: "/".join(reversed(str(x).split("/"))) if pd.notnull(x) and len(str(x).split("/")[0]) == 4 else x
    )

    df["monto_del_credito"] = df["monto_del_credito"].str.replace("[$ ,]", "", regex=True).astype(float)

    columnas_clave = [
        "sexo", "tipo_de_emprendimiento", "idea_negocio", "barrio",
        "estrato", "comuna_ciudadano", "fecha_de_beneficio",
        "monto_del_credito", "línea_credito"
    ]
    df = df.drop_duplicates(subset=columnas_clave).dropna()

    df.to_csv("files/output/solicitudes_de_credito.csv", sep=";", index=False)

pregunta_01()
