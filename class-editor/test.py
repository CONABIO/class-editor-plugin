
'''
Created on Oct 11, 2017

@author: agutierrez
'''

def get_class_dic():
    
    level_1 = ['TIERRAS FORESTALES', 'PRADERAS', 'HUMEDAL', 'TIERRAS DE USO AGRICOLA', 'CUERPO DE AGUA', 'ASENTAMIENTOS', 'OTROS', 'INDEFINIDO']
    level_2 = {
               'TIERRAS FORESTALES':['BOSQUE DE CONIFERAS',
                                     'BOSQUE DE ENCINO',
                                     'BOSQUE MEZCLADO',
                                     'SELVAS HUMEDAS Y SUBHUMEDAS Y BOSQUE MESOFILO',
                                     'SELVAS SECAS',
                                     'MATORRAL XEROFILO SUBARBOREO',
                                     'MATORRAL XEROFILO ARBUSTIVO'],
               'PRADERAS':['PASTIZALES'],
               'HUMEDAL':['VEGETACION HIDROFILA'],
               'TIERRAS DE USO AGRICOLA':['AGRICULTURA'],
               'CUERPO DE AGUA':['CUERPO DE AGUA'],
               'ASENTAMIENTOS':['URBANO Y CONSTRUIDO'],
               'OTROS':['SUELO DESNUDO', 'NIEVE Y HIELO'],
               'INDEFINIDO':['INDEFINIDO']
               }
    level_3 = {
                'BOSQUE DE CONIFERAS':['BOSQUE DE AYARIN', 'BOSQUE DE CEDRO', 'BOSQUE DE OYAMEL', 'BOSQUE DE PINO', 'BOSQUE DE TASCATE'],
                'BOSQUE DE ENCINO':['BOSQUE DE ENCINO'],
                'BOSQUE MEZCLADO':['BOSQUE DE ENCINO-PINO', 'BOSQUE DE PINO-ENCINO', 'BOSQUE CULTIVADO', 'BOSQUE INDUCIDO'],
                'SELVAS HUMEDAS Y SUBHUMEDAS Y BOSQUE MESOFILO':['BOSQUE MESOFILO DE MONTANA', 'SELVA ALTA PERENNIFOLIA', 'SELVA BAJA PERENNIFOLIA', 'SELVA MEDIANA PERENNIFOLIA', 'PALMAR NATURAL', 'PETEN', 'SELVA DE GALERIA', 'SELVA ALTA SUBPERENNIFOLIA', 'SELVA MEDIANA SUBPERENNIFOLIA', 'SELVA BAJA ESPINOSA SUBPERENNIFOLIA', 'BOSQUE DE GALERIA', 'PALMAR', 'PALMAR INDUCIDO', 'VEGETACION DE PETEN', 'MANGLAR'],
                'SELVAS SECAS':['SELVA BAJA CADUCIFOLIA', 'SELVA MEDIANA CADUCIFOLIA', 'SELVA BAJA ESPINOSA CADUCIFOLIA', 'SELVA BAJA SUBCADUCIFOLIA', 'SELVA BAJA ESPINOSA', 'SELVA MEDIANA SUBCADUCIFOLIA'],
                'MATORRAL XEROFILO SUBARBOREO':['MATORRAL SUBTROPICAL', 'MATORRAL SUBMONTANO', 'MATORRAL ESPINOSO TAMAULIPECO', 'MATORRAL CRASICAULE', 'CHAPARRAL', 'MEZQUITAL DESERTICO', 'MEZQUITAL', 'MEZQUITAL TROPICAL', 'BOSQUE DE MEZQUITE', 'MATORRAL DE CONIFERAS'],
                'MATORRAL XEROFILO ARBUSTIVO':['MATORRAL DESERTICO MICROFILO', 'MATORRAL DESERTICO ROSETOFILO', 'MATORRAL ROSETOFILO COSTERO', 'MATORRAL SARCO-CRASICAULE', 'MATORRAL SARCO-CRASICAULE DE NEBLINA', 'MATORRAL SARCOCAULE', 'VEGETACION DE DESIERTOS ARENOSOS', 'VEGETACION GIPSOFILA', 'VEGETACION HALOFILA XEROFILA', 'VEGETACION HALOFILA', 'VEGETACION DE GALERIA'],
                'PASTIZALES':['PASTIZAL GIPSOFILO', 'PASTIZAL HALOFILO', 'PASTIZAL NATURAL', 'PRADERA DE ALTA MONTANA', 'SABANA', 'DUNAS COSTERAS', 'PASTIZAL INDUCIDO', 'VEGETACION DE DUNAS COSTERAS', 'SABANOIDE', 'PASTIZAL CULTIVADO'],
                'VEGETACION HIDROFILA':['POPAL', 'TULAR', 'VEGETACION HALOFILA HIDROFILA'],
                'AGRICULTURA':['AGRICULTURA DE HUMEDAD', 'AGRICULTURA DE RIEGO', 'AGRICULTURA DE TEMPORAL'],
                'CUERPO DE AGUA':['ACUICOLA', 'AGUA'],
                'URBANO Y CONSTRUIDO':['ASENTAMIENTOS HUMANOS', 'ZONA URBANA'],
                'SUELO DESNUDO':['SIN VEGETACION APARENTE', 'DESPROVISTO DE VEGETACION'],
                'NIEVE Y HIELO':['NIEVE', 'HIELO'],
                'INDEFINIDO':['INDEFINIDO']
               }
    level_4 = {
                'BOSQUE DE CONIFERAS':['ARBUSTIVO', 'ARBOREO', 'HERBACEO', 'NO APLICABLE', 'QUEMADO'],
                'BOSQUE DE ENCINO':['ARBUSTIVO', 'ARBOREO', 'HERBACEO', 'NO APLICABLE', 'QUEMADO'],
                'BOSQUE MEZCLADO':['ARBUSTIVO', 'ARBOREO', 'HERBACEO', 'NO APLICABLE', 'QUEMADO'],
                'SELVAS HUMEDAS Y SUBHUMEDAS Y BOSQUE MESOFILO':['ARBUSTIVO', 'ARBOREO', 'HERBACEO', 'NO APLICABLE', 'QUEMADO'],
                'SELVAS SECAS':['ARBUSTIVO', 'ARBOREO', 'HERBACEO', 'NO APLICABLE', 'QUEMADO'],
                'MATORRAL XEROFILO SUBARBOREO':['ARBUSTIVO', 'ARBOREO', 'HERBACEO', 'NO APLICABLE', 'QUEMADO'],
                'MATORRAL XEROFILO ARBUSTIVO':['ARBUSTIVO', 'ARBOREO', 'HERBACEO', 'NO APLICABLE', 'QUEMADO'],
                'PASTIZALES':['ARBUSTIVO', 'ARBOREO', 'HERBACEO', 'NO APLICABLE', 'QUEMADO'],
                'VEGETACION HIDROFILA':['ARBUSTIVO', 'ARBOREO', 'HERBACEO', 'NO APLICABLE', 'QUEMADO'],
                'AGRICULTURA':['NO APLICABLE', 'QUEMADO'],
                'CUERPO DE AGUA':['NO APLICABLE'],
                'URBANO Y CONSTRUIDO':['NO APLICABLE'],
                'SUELO DESNUDO':['NO APLICABLE', 'QUEMADO'],
                'NIEVE Y HIELO':['NO APLICABLE'],
                'INDEFINIDO':['INDEFINIDO', 'SOMBRA', 'NUBE', 'QUEMADO']
               }    
    
  
    return [level_1, level_2, level_3, level_4]


def class_dictionary(word):
    translate = {'BOSQUE DE AYARIN':'Douglas-fir and spruce forest',
                 'BOSQUE DE CEDRO':'Cedar forest',
                 'BOSQUE DE ENCINO':'Oak forest',
                 'BOSQUE DE ENCINO-PINO':'Oak-pine mixed forest',
                 'BOSQUE DE GALERIA':'Riparian forest',
                 'BOSQUE DE MEZQUITE':'Mesquite forest',
                 'BOSQUE DE OYAMEL':'Fir forest',
                 'BOSQUE DE PINO':'Pine forest',
                 'BOSQUE DE PINO-ENCINO':'Pine-oak mixed forest',
                 'BOSQUE DE TASCATE':'Juniper forest',
                 'BOSQUE INDUCIDO':'Induced forest',
                 'BOSQUE MESOFILO DE MONTANA':'Cloud forest',
                 'CHAPARRAL':'Chaparral',
                 'MANGLAR':'Mangrove',
                 'MATORRAL CRASICAULE':'Casicaulous shrubland',
                 'MATORRAL DE CONIFERAS':'Conifers shrubland',
                 'MATORRAL DESERTICO MICROFILO':'Microphyll desert scrub',
                 'MATORRAL DESERTICO ROSETOFILO':'Rosetophilous desert scrub',
                 'MATORRAL ESPINOSO TAMAULIPECO':'Tamaulipan thornscrub',
                 'MATORRAL ROSETOFILO COSTERO':'Coastal rosetophilous scrub',
                 'MATORRAL SARCOCAULE':'Sarcocaulous shrubland',
                 'MATORRAL SARCO-CRASICAULE':'Sarco-crasicaulous shrubland',
                 'MATORRAL SARCO-CRASICAULE DE NEBLINA':'Mist sarco-crasicaulous shrubland',
                 'MATORRAL SUBMONTANO':'Submontane shrubland',
                 'MATORRAL SUBTROPICAL':'Subtropical shrubland',
                 'MEZQUITAL':'Mesquite woodland',
                 'MEZQUITAL DESERTICO':'Semidesert Mesquite woodland',
                 'MEZQUITAL TROPICAL':'Tropical mesquite woodland',
                 'PALMAR INDUCIDO':'Induced palm groove',
                 'PALMAR NATURAL':'Natural palm groove',
                 'PASTIZAL GIPSOFILO':'Gypsophile grassland',
                 'PASTIZAL HALOFILO':'Halophile grassland',
                 'PASTIZAL INDUCIDO':'Induced grassland',
                 'PASTIZAL NATURAL':'Natural grassland',
                 'POPAL':'Popoay marsh or floodplain',
                 'PRADERA DE ALTA MONTANA':'High elevation alpine prairie',
                 'SABANA':'Savanna',
                 'SABANOIDE':'Induced savannah',
                 'SELVA ALTA PERENNIFOLIA':'High evergreen tropical rain forest',
                 'SELVA ALTA SUBPERENNIFOLIA':'High semi-evergreen tropical rain forest',
                 'SELVA BAJA CADUCIFOLIA':'Deciduous tropical dry forest',
                 'SELVA BAJA ESPINOSA CADUCIFOLIA':'Deciduous tropical thorn forest',
                 'SELVA BAJA ESPINOSA SUBPERENNIFOLIA':'Semi-evergreen tropical thorn forest',
                 'SELVA BAJA PERENNIFOLIA':'Low evergreen tropical forest',
                 'SELVA BAJA SUBCADUCIFOLIA':'Semi-deciduous Tropical dry forest',
                 'SELVA BAJA SUBPERENNIFOLIA':'Semi-evergreen Tropical dry forest',
                 'SELVA DE GALERIA':'Riparian tropical forest',
                 'SELVA MEDIANA CADUCIFOLIA':'Middle deciduous tropical forest',
                 'SELVA MEDIANA PERENNIFOLIA':'Middle evergreen tropical rain forest',
                 'SELVA MEDIANA SUBCADUCIFOLIA':'Middle semi-deciduous tropical rain forest',
                 'SELVA MEDIANA SUBPERENNIFOLIA':'Middle semi-evergreen tropical rain forest',
                 'SIN VEGETACION APARENTE':'Apparent unvegetated',
                 'TULAR':'Cat-tail marsh or flodplain',
                 'VEGETACION DE DESIERTOS ARENOSOS':'Sandy desert vegetation',
                 'VEGETACION DE DUNAS COSTERAS':'Coastal dune vegetation',
                 'VEGETACION DE GALERIA':'Riparian vegetation',
                 'VEGETACION DE PETEN':'Peten vegetation',
                 'VEGETACION GIPSOFILA':'Gypsophile vegetation',
                 'VEGETACION HALOFILA':'Halophile vegetation',
                 'VEGETACION HALOFILA HIDROFILA':'Halophile hydrophile vegetation',
                 'VEGETACION HALOFILA XEROFILA':'Halophile xerophilous vegetation',
                 'USO AGRICOLA':'Agricultural usage',
                 'AGRICULTURA DE TEMPORAL':'Rainfed agriculture',
                 'BOSQUE CULTIVADO':'Cultivated forest',
                 'AGRICULTURA DE RIEGO':'Irrigated agriculture',
                 'PASTIZAL CULTIVADO':'Cultivated pasture',
                 'ACUICOLA':'Aquaculture',
                 'AGRICULTURA DE HUMEDAD':'Moist soil agriculture',
                 'OTRAS':'Others',
                 'ZONA URBANA':'Urban area',
                 'ASENTAMIENTOS HUMANOS':'Human settlements',
                 'NO APLICABLE':'No applicable',
                 'DESPROVISTO DE VEGETACION':'Devoid of vegetation',
                 'CUERPO DE AGUA':'Water body',
                 'AGUA':'Water',
                 'NUBE':'Cloud',
                 'OTROS':'Others',
                 'ASENTAMIENTOS':'Settlements',
                 'HIELO':'Ice',
                 'NIEVE':'Snow',
                 'NIEVE Y HIELO':'Snow and Ice',
                 'AGRICULTURA':'Agriculture',
                 'TIERRAS FORESTALES':'Forest lands',
                 'PRADERAS':'Grasslands',
                 'HUMEDAL':'Wetland',
                 'TIERRAS DE USO AGRICOLA':'Land for agricultural use',
                 'INDEFINIDO':'Undefined',
                 'BOSQUE DE CONIFERAS':'Conifer Forest',
                 'BOSQUE MEZCLADO':'Mixed forest',
                 'SELVAS HUMEDAS Y SUBHUMEDAS Y BOSQUE MESOFILO':'Humid and subhumid tropical rain and cloud forests',
                 'SELVAS SECAS':'Tropical dry forest',
                 'MATORRAL XEROFILO SUBARBOREO':'Subarborous xerophyl shrubland',
                 'MATORRAL XEROFILO ARBUSTIVO':'Xerophyl shrubland',
                 'VEGETACION HIDROFILA':'Hidrophilous vegetation',
                 'URBANO Y CONSTRUIDO':'Urban and built',
                 'PASTIZALES':'Pastures',
                 'SUELO DESNUDO':'Bare land',
                 'SELVA BAJA ESPINOSA':'Tropical thorn forest',
                 'PETEN':'Peten',
                 'PALMAR':'Palm grove',
                 'DUNAS COSTERAS':'Coastal Dunes',
                 'ARBUSTIVO':'Shrubby',
                 'ARBOREO':'Arboreal',
                 'HERBACEO':'Herbaceous',
                 'QUEMADO':'Burnt'
                 }                        

    return translate.get(word, "Notfound:%s" %word)

if __name__ == '__main__':
    my_dict = get_class_dic()
    a = set()
    print 'level_1 = ['
    for word in my_dict[0]:
        print "'%s'," % class_dictionary(word)    
    print ']'
    print 'level_2 = {'
    for word in my_dict[1].keys():
        inside = my_dict[1].get(word)
        print "'%s':[" % class_dictionary(word)
        for other in inside:
            print "'%s'," % class_dictionary(other)
        print '],'
    print '}'
    print 'level_3 = {'
    for word in my_dict[2].keys():
        inside = my_dict[2].get(word)
        print "'%s':[" % class_dictionary(word)
        for other in inside:
            print "'%s'," % class_dictionary(other)
        print '],'
    print '}'
    print 'level_4 = {'
    for word in my_dict[3].keys():
        inside = my_dict[3].get(word)
        print "'%s':[" % class_dictionary(word)
        for other in inside:
            print "'%s'," % class_dictionary(other)
        print '],'
    print '}'
