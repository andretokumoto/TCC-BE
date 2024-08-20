def to_pdf(dados):
    ...
    
def to_tex(dados):
    
    document_type = dados.get('document_type')
    
    #verifica o tipo de documento requerido
    if document_type == 'oficio':
        template_path = 'FormataiBE_API//tampletes/oficio.tex'  #template
        output_path = 'FormataiBE_API/tampletes/arquivo_gerado.tex'   #arquivo gerado

    with open(template_path, 'r') as template_file:#le os dados do template e salva na variavel template
        template = template_file.read()    
    
    #substitui os dados do template pelo do requerimento
    oficio = template.replace('__OFICIO_NUMERO__', dados.get('oficio_numero', ''))   
    
    '''
    template_path = 'FormataiBE_API/template.tex'  #template
    output_path = 'FormataiBE_API/resultado.tex'   #arquivo gerado

    with open(template_path, 'r') as template_file:
        template = template_file.read()
        '''