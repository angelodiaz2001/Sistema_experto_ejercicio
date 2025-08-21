def sistema_experto_auto_basico():
    print("=== Sistema Experto de Diagnóstico de Automóviles ===")

    arranca = input("¿El automóvil arranca? (si/no): ").strip().lower().replace('í', 'i')
    luces_tablero = input("¿Las luces del tablero están encendidas? (si/no): ").strip().lower().replace('í', 'i')
    se_apaga_acelerar = input("¿El automóvil se apaga al acelerar? (si/no): ").strip().lower().replace('í', 'i')
    humo_negro = input("¿Sale humo negro por el escape? (si/no): ").strip().lower().replace('í', 'i')
    humo_blanco = input("¿Sale humo blanco constante por el escape? (si/no): ").strip().lower().replace('í', 'i')

    diagnostico = None
    
    if arranca == "no" and luces_tablero == "no":
        diagnostico = "Batería descargada"
    elif arranca == "no" and luces_tablero == "si":
        diagnostico = "Fallo en el motor de arranque"
    elif arranca == "si" and se_apaga_acelerar == "si":
        diagnostico = "Problema en el suministro de combustible"

    if diagnostico is None:
        if humo_negro == "si":
            diagnostico = "Mezcla rica de combustible"
        elif humo_blanco == "si":
            diagnostico = "Falla en la junta de culata"

    if diagnostico:
        print("\nPosible diagnóstico:", diagnostico)
    else:
        print("\nNo hay datos suficientes para definir la causa con los síntomas dados.")


if __name__ == "__main__":
    sistema_experto_auto_basico()
