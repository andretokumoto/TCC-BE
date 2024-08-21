def open_template(template_path):
    #le os dados do template e salva na variavel template
    with open(template_path, 'r') as template_file:
      template = template_file.read()  
    return template

def salva_arquivo(output_path,doc_gerado):
    with open(output_path, 'w') as output_file:#abre o arquivo de entrada para edição
        template = output_file.write(doc_gerado)  

def to_pdf(dados):
    ...
    
def to_tex(dados):
    
    document_type = dados.get('document_type')#verifica o tipo de documento requerido
    output_path = 'FormataiBE_API/tampletes/arquivo_gerado.tex'   #arquivo gerado
    
    #verifica o tipo de documento requerido
    
    '''----- OFICIO ------------------------'''
    doc_gerado = None
    
    if document_type == 'oficio':
        template_path = 'FormataiBE_API/tampletes/oficio.tex'  #template oficio
        template = open_template(template_path)#le os dados do template
        
        #substitui os dados do template pelo do requerimento
        doc_gerado = template.replace('__OFICIO_NUMERO__', dados.get('oficio_numero', ''))
        doc_gerado = template.replace('__DESTINATARIO__', dados.get('destinatario', ''))
        doc_gerado = template.replace('__ENDERECO_DESTINATARIO__', dados.get('endereco_destinatario', ''))
        doc_gerado = template.replace('__CIDADE_ESTADO__', dados.get('cidadeEstado_destinatario', ''))
        doc_gerado = template.replace('__CEP__', dados.get('cep_destinatario', ''))
        doc_gerado = template.replace('__TEXTO_SOLICITACAO__', dados.get('corpo_mensagem', ''))
        doc_gerado = template.replace('__NOME_REMETENTE__', dados.get('nome_remetente', ''))
        doc_gerado = template.replace('__CARGO_REMETENTE__', dados.get('cargo_remetente', ''))
        doc_gerado = template.replace('__ORGANIZACAO_REMETENTE__', dados.get('organizacao_remetente', ''))
        
        salva_arquivo(output_path,doc_gerado)


    return output_path
'''------------------------------------------------------------------------------------------------------------------------------------------------'''
   


    
