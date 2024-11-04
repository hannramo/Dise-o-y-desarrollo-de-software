
#Importamos las librerias de los archivos que necesitamos
import json
import xml.etree.ElementTree as ET
import yaml

# Obtener datos del usuario o empleado
def obtener_datos_persona():
    nombre = input("Ingresa tu nombre: ")
    N_empleado = input("Ingrese su Numero de Empleado: ")
    carrera = input("Ingresa su Especialidad o Carrera: ")
    return {
        "nombre": nombre,
        # Convertimos el dato a entero
        "N_empleado": int(N_empleado),  
        "carrera": carrera
    }

#Convertimos los datos del usuario
persona = obtener_datos_persona()

#Convertimos los resultados a formato JSON
json_output = json.dumps(persona, indent=4)

#Convertimos los resultados a formato XML
def dict_to_xml(tag, d):
    element = ET.Element(tag)
    for key, val in d.items():
        child = ET.SubElement(element, key)
        child.text = str(val)
    return element

xml_element = dict_to_xml("persona", persona)
xml_output = ET.tostring(xml_element, encoding="unicode")

#Convertimos los resultados a formato YAML
yaml_output = yaml.dump(persona, default_flow_style=False)

# Imprimir resultados
print(" ")
print("Formato JSON:\n", json_output)
print(" ")
print("\nFormato XML:\n", xml_output)
print(" ")
print("\nFormato YAML:\n", yaml_output)